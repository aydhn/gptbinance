from app.risk.engine import RiskEngine
from app.risk.models import (
    RiskConfig,
    RiskEvaluationRequest,
    RiskContext,
    ExposureSnapshot,
    DrawdownStateModel,
)
from app.risk.state import RiskStateManager
from app.risk.repository import RiskRepository
from app.risk.storage import RiskStorage
from app.risk.exposure import ExposureCalculator
from app.risk.enums import RiskVerdict
from typing import Optional, List, Dict, Any
import uuid
from datetime import datetime
from app.backtest.models import (
    BacktestConfig,
    BacktestRun,
    BacktestResult,
    SimulatedOrderIntent,
    BacktestArtifactManifest,
    BacktestStepContext,
)
from app.backtest.enums import PositionSide
from app.backtest.config import validate_backtest_config
from app.backtest.replay_driver import ReplayDriver
from app.backtest.position_state import PositionManager
from app.backtest.ledger import Ledger
from app.backtest.equity import EquityTracker
from app.backtest.performance import PerformanceCalculator
from app.backtest.fill_model import FillModel
from app.backtest.order_intents import OrderIntentMapper

from app.strategies.engine import StrategyEngine
from app.strategies.models import StrategySpec
from app.strategies.enums import StrategyType


class BacktestEngine:
    def __init__(self, config_dict: dict):
        self.config = validate_backtest_config(config_dict)
        self.run_id = str(uuid.uuid4())
        self.run = BacktestRun(
            run_id=self.run_id, config=self.config, started_at=datetime.now()
        )

        self.position_manager = PositionManager(self.config.symbol)
        self.ledger = Ledger()
        self.equity_tracker = EquityTracker(self.config.initial_capital)
        self.fill_model = FillModel(self.config.execution)

        self.strategy_engine = StrategyEngine()

        # Risk Engine Setup
        self.risk_config = RiskConfig()  # default config
        self.risk_state_manager = RiskStateManager()
        self.risk_engine = RiskEngine(self.risk_config, self.risk_state_manager)
        self.risk_storage = RiskStorage()
        self.risk_repository = RiskRepository(self.risk_storage)
        self.exposure_calculator = ExposureCalculator()

        # Load mock strategy just to test the flow

    def run_backtest(self) -> BacktestResult:
        driver = ReplayDriver(
            self.config.symbol,
            self.config.interval,
            self.config.start_time,
            self.config.end_time,
        )

        pending_intents: List[SimulatedOrderIntent] = []
        bar_count = 0

        for step_context in driver.generate_steps():
            bar_count += 1

            # 1. Update Unrealized PnL based on open
            self.position_manager.update_unrealized_pnl(step_context.bar_open)
            self.equity_tracker.snapshot(
                step_context.timestamp, self.position_manager.state.unrealized_pnl
            )

            # 2. Process pending intents from PREVIOUS bar
            for intent in pending_intents:
                position_side_before = self.position_manager.state.side

                # Check exposure limits simply
                if (
                    self.config.exposure_mode == "SINGLE_POSITION"
                    and position_side_before != PositionSide.FLAT
                    and not intent.is_reduce_only
                ):
                    continue  # Skip entry if already in position

                fill = self.fill_model.simulate_fill(intent, step_context)

                new_state, realized_pnl = self.position_manager.apply_fill(fill)

                self.ledger.record_fill(fill, position_side_before, new_state.side)
                self.equity_tracker.process_fill(fill.decision.fee_paid, realized_pnl)

            pending_intents.clear()

            # 3. Evaluate Strategy with current bar close features
            signal_batch = self.strategy_engine.evaluate(
                symbol=self.config.symbol,
                interval=self.config.interval,
                timestamp=step_context.timestamp,
                features=step_context.features,
            )

            # 4. Generate Order Intents for NEXT bar
            raw_intents = []
            if signal_batch.resolved_exit_intents:
                for exit_intent in signal_batch.resolved_exit_intents:
                    sim_intent = OrderIntentMapper.from_exit_intent(
                        exit_intent, self.position_manager.state
                    )
                    if sim_intent:
                        raw_intents.append(sim_intent)

            if signal_batch.resolved_entry_intent:
                sim_intent = OrderIntentMapper.from_entry_intent(
                    signal_batch.resolved_entry_intent,
                    self.position_manager.state,
                    self.equity_tracker.cash,
                    step_context.bar_close,
                )
                if sim_intent:
                    if (
                        self.config.allow_long
                        and sim_intent.side.name == "BUY"
                        or self.config.allow_short
                        and sim_intent.side.name == "SELL"
                    ):
                        raw_intents.append(sim_intent)

            # 5. Route through Risk Engine
            if raw_intents:
                # Build context
                exposure_snap = self.exposure_calculator.calculate(
                    [self.position_manager.state],
                    self.equity_tracker.cash,
                    step_context.timestamp,
                )

                # Update drawdown state in risk manager
                dd_model = DrawdownStateModel(
                    peak_equity=self.equity_tracker.drawdown_tracker.peak_equity,
                    current_equity=self.equity_tracker.cash,
                    drawdown_pct=self.equity_tracker.drawdown_tracker.current_drawdown_pct,
                    last_updated=step_context.timestamp,
                )
                self.risk_state_manager.update_drawdown(dd_model)

                risk_context = RiskContext(
                    timestamp=step_context.timestamp,
                    drawdown_state=dd_model,
                    exposure_snapshot=exposure_snap,
                    volatility_multiplier=1.0,  # Mock or extract from features
                )

                for ri in raw_intents:
                    req = RiskEvaluationRequest(
                        intent=ri,
                        context=risk_context,
                        available_capital=self.equity_tracker.cash,
                    )

                    bundle = self.risk_engine.evaluate_intent(req)
                    self.risk_repository.store_decision(self.run.run_id, bundle)

                    if bundle.decision.verdict in (
                        RiskVerdict.APPROVE,
                        RiskVerdict.REDUCE,
                    ):
                        approved = bundle.decision.approved_intent
                        approved.is_risk_approved = True
                        pending_intents.append(approved)
                    else:
                        pass  # Rejected by risk

        # Force close open position at end
        if self.position_manager.state.side != PositionSide.FLAT:
            # Create a mock exit
            from app.backtest.enums import OrderSide

            sim_intent = SimulatedOrderIntent(
                timestamp=self.config.end_time,
                symbol=self.config.symbol,
                side=(
                    OrderSide.SELL
                    if self.position_manager.state.side == PositionSide.LONG
                    else OrderSide.BUY
                ),
                quantity=self.position_manager.state.quantity,
                is_reduce_only=True,
                intent_source="End of Backtest",
                rationale="Forced close",
            )
            mock_context = BacktestStepContext(
                timestamp=self.config.end_time,
                bar_open=100.0,
                bar_high=100.0,
                bar_low=100.0,
                bar_close=100.0,
                bar_volume=0.0,  # dummy
            )
            fill = self.fill_model.simulate_fill(sim_intent, mock_context)
            pos_before = self.position_manager.state.side
            self.position_manager.apply_fill(fill)
            self.ledger.record_fill(fill, pos_before, PositionSide.FLAT)
            self.equity_tracker.process_fill(fill.decision.fee_paid, fill.realized_pnl)

        self.run.completed_at = datetime.now()

        summary = PerformanceCalculator.calculate(
            run_id=self.run.run_id,
            initial_capital=self.config.initial_capital,
            trades=self.ledger.get_completed_trades(),
            final_equity=self.equity_tracker.cash,  # All pos closed
            drawdown_summary=self.equity_tracker.get_drawdown_summary(),
            total_bars=bar_count,
        )

        return BacktestResult(run=self.run, summary=summary)
