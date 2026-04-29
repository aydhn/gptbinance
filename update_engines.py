import re

# Update app/backtest/models.py
with open("app/backtest/models.py", "r") as f:
    models_content = f.read()

if "risk_rejection_rationale: str" not in models_content:
    models_content = models_content.replace(
        "class SimulatedOrderIntent(BaseModel):",
        "class SimulatedOrderIntent(BaseModel):\n    risk_rejection_rationale: str = \"\"\n    is_risk_approved: bool = False"
    )
    with open("app/backtest/models.py", "w") as f:
        f.write(models_content)

# Update app/backtest/engine.py
with open("app/backtest/engine.py", "r") as f:
    engine_content = f.read()

if "from app.risk.engine import RiskEngine" not in engine_content:
    imports = """from app.risk.engine import RiskEngine
from app.risk.models import RiskConfig, RiskEvaluationRequest, RiskContext, ExposureSnapshot, DrawdownStateModel
from app.risk.state import RiskStateManager
from app.risk.repository import RiskRepository
from app.risk.storage import RiskStorage
from app.risk.exposure import ExposureCalculator
from app.risk.enums import RiskVerdict
"""
    engine_content = imports + engine_content

    init_patch = """
        self.strategy_engine = StrategyEngine()

        # Risk Engine Setup
        self.risk_config = RiskConfig() # default config
        self.risk_state_manager = RiskStateManager()
        self.risk_engine = RiskEngine(self.risk_config, self.risk_state_manager)
        self.risk_storage = RiskStorage()
        self.risk_repository = RiskRepository(self.risk_storage)
        self.exposure_calculator = ExposureCalculator()
"""
    engine_content = engine_content.replace(
        "self.strategy_engine = StrategyEngine()", init_patch
    )

    eval_patch = """
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
                        self.config.allow_long and sim_intent.side.name == "BUY"
                        or self.config.allow_short and sim_intent.side.name == "SELL"
                    ):
                        raw_intents.append(sim_intent)

            # 5. Route through Risk Engine
            if raw_intents:
                # Build context
                exposure_snap = self.exposure_calculator.calculate(
                    [self.position_manager.state], self.equity_tracker.cash, step_context.timestamp
                )

                # Update drawdown state in risk manager
                dd_model = DrawdownStateModel(
                     peak_equity=self.equity_tracker.drawdown_tracker.peak_equity,
                     current_equity=self.equity_tracker.cash,
                     drawdown_pct=self.equity_tracker.drawdown_tracker.current_drawdown_pct,
                     last_updated=step_context.timestamp
                )
                self.risk_state_manager.update_drawdown(dd_model)

                risk_context = RiskContext(
                    timestamp=step_context.timestamp,
                    drawdown_state=dd_model,
                    exposure_snapshot=exposure_snap,
                    volatility_multiplier=1.0 # Mock or extract from features
                )

                for ri in raw_intents:
                    req = RiskEvaluationRequest(
                        intent=ri,
                        context=risk_context,
                        available_capital=self.equity_tracker.cash
                    )

                    bundle = self.risk_engine.evaluate_intent(req)
                    self.risk_repository.store_decision(self.run.run_id, bundle)

                    if bundle.decision.verdict in (RiskVerdict.APPROVE, RiskVerdict.REDUCE):
                        approved = bundle.decision.approved_intent
                        approved.is_risk_approved = True
                        pending_intents.append(approved)
                    else:
                        pass # Rejected by risk
"""
    # Find the old section to replace
    start_idx = engine_content.find("# 4. Generate Order Intents for NEXT bar")
    end_idx = engine_content.find("# Force close open position at end", start_idx)

    if start_idx != -1 and end_idx != -1:
        engine_content = engine_content[:start_idx] + eval_patch + "\n        " + engine_content[end_idx:]

    with open("app/backtest/engine.py", "w") as f:
        f.write(engine_content)
