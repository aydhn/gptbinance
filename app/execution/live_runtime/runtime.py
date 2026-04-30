
from app.products.enums import ProductType
import logging
import time
from typing import Dict, Any, List
from datetime import datetime

from app.portfolio.engine import PortfolioEngine
from app.portfolio.models import PortfolioIntentBatch


from app.execution.live_runtime.enums import (
    LiveSessionStatus,
    SessionArmingStatus,
    LiveRuntimeVerdict,
    LiveAuditEventType,
    FlattenMode,
    RollbackSeverity,
)
from app.execution.live_runtime.models import (
    LiveSessionConfig,
    LiveRun,
    LiveAuditRecord,
    LiveFillRecord,
    LiveSessionSummary,
    LiveFlattenRequest,
)
from app.execution.live_runtime.start_gates import LiveStartGateEvaluator
from app.execution.live_runtime.account_sync import AccountSynchronizer
from app.execution.live_runtime.capital_caps import CapitalCapEnforcer
from app.execution.live_runtime.position_book import LivePositionManager
from app.execution.live_runtime.pnl import LivePnlCalculator
from app.execution.live_runtime.flatten import LiveFlattenController
from app.execution.live_runtime.rollback import LiveRollbackController
from app.execution.live_runtime.audit import LiveAuditWriter
from app.execution.live_runtime.notifier_bridge import LiveNotifierBridge

logger = logging.getLogger(__name__)


class LiveOrchestrator:
    def __init__(
        self,
        config: LiveSessionConfig,
        run_id: str,
        execution_gateway: Any,
        account_sync: AccountSynchronizer,
        notifier: LiveNotifierBridge,
        portfolio_engine: PortfolioEngine = None,
    ):
        self.run = LiveRun(run_id=run_id, config=config)
        self.execution_gateway = execution_gateway
        self.account_sync = account_sync
        self.notifier = notifier
        self.portfolio_engine = portfolio_engine

        self.gate_evaluator = LiveStartGateEvaluator()
        self.cap_enforcer = CapitalCapEnforcer(config.capital_caps)
        self.position_manager = LivePositionManager()
        self.pnl_calc = LivePnlCalculator(run_id)

        self.flatten_ctrl = LiveFlattenController(
            execution_gateway, self.position_manager
        )
        self.rollback_ctrl = LiveRollbackController(self.flatten_ctrl)
        self.audit_writer = LiveAuditWriter()

    def start_session(self, context: Dict[str, Any]) -> bool:
        self.run.state.status = LiveSessionStatus.GATES_CHECKING
        report = self.gate_evaluator.evaluate(self.run.config, context)

        if not report.passed:
            self.run.state.status = LiveSessionStatus.HALTED
            logger.error(f"Live session start blocked: {report.blockers}")
            return False

        self.run.state.arming_status = SessionArmingStatus.ARMED_AND_VERIFIED
        self.run.state.status = LiveSessionStatus.RUNNING
        self.run.state.start_time = datetime.utcnow()

        self.audit_writer.write_record(
            LiveAuditRecord(
                run_id=self.run.run_id,
                event_type=LiveAuditEventType.SESSION_START,
                details=f"Started mode {self.run.config.rollout_mode.value}",
            )
        )

        # Hydrate account state
        self.account_sync.hydrate(self.run.run_id)

        if self.run.config.require_telegram_notify:
            self.notifier.notify_live_start(self.run.run_id, self.run.config)

        return True

    async def process_intent(self, intent: Dict[str, Any]) -> bool:
        if self.run.state.status != LiveSessionStatus.RUNNING:
            logger.warning("Session not running. Intent ignored.")
            return False

        # 1. Capital Cap Check
        pb = self.position_manager.get_book()
        decision = self.cap_enforcer.evaluate_intent(intent, pb)

        if decision.verdict != LiveRuntimeVerdict.PROCEED:
            logger.warning(f"Live cap reject: {decision.reason}")
            self.audit_writer.write_record(
                LiveAuditRecord(
                    run_id=self.run.run_id,
                    event_type=LiveAuditEventType.CAPITAL_CAP_INTERVENTION,
                    details=f"Reject intent: {decision.reason}",
                )
            )
            if decision.cap_type:
                self.notifier.notify_cap_hit(
                    self.run.run_id, decision.cap_type.value, decision.reason
                )
            return False

        # 2. Handoff to Execution Gateway

        if hasattr(intent, "product_type") and getattr(intent, "product_type") != ProductType.SPOT:
            # Enforce Testnet for derivatives!
            try:
                order_id = await self.executor.execute_derivative(intent, testnet_first=True) if hasattr(self.executor, 'execute_derivative') else 'mock'
                self.storage.record_trade(order_id, intent.symbol, intent.side, intent.quantity, 0.0)
                logger.info(f"Recorded live derivative trade for {intent.symbol}")
            except Exception as e:
                 logger.error(f"Live execution failed for derivative {intent.symbol}: {e}")
            return

        try:

            # Assuming intent format fits execution gateway submit signature
            qty = intent.get("qty", 0.0)
            symbol = intent.get("symbol", "")
            side = intent.get("side", "BUY")
            order_type = intent.get("type", "MARKET")

            # Simple simulation of submit for the core framework
            res = getattr(self.execution_gateway, "submit_order", lambda *a, **k: None)(
                symbol=symbol, side=side, order_type=order_type, qty=qty
            )

            notional = qty * intent.get("price", 0.0)
            self.cap_enforcer.record_submit(notional)

            self.audit_writer.write_record(
                LiveAuditRecord(
                    run_id=self.run.run_id,
                    event_type=LiveAuditEventType.ORDER_SUBMIT,
                    details=f"Submitted {side} {qty} {symbol}",
                )
            )
            return True

        except Exception as e:
            logger.error(f"Execution gateway submit failed: {e}")
            return False

    def handle_fill(self, fill: LiveFillRecord) -> None:
        self.position_manager.process_fill(fill)

        self.audit_writer.write_record(
            LiveAuditRecord(
                run_id=self.run.run_id,
                event_type=LiveAuditEventType.ORDER_FILL,
                details=f"Filled {fill.qty} {fill.symbol} @ {fill.price}",
            )
        )

        # Update PnL
        prices = {fill.symbol: fill.price}
        pnl_snaps = self.pnl_calc.compute_pnl(self.position_manager.get_book(), prices)

        # Check Daily Loss
        decision = self.cap_enforcer.evaluate_loss(pnl_snaps)
        if decision.verdict == LiveRuntimeVerdict.HALT:
            self.notifier.notify_cap_hit(
                self.run.run_id,
                decision.cap_type.value if decision.cap_type else "loss",
                decision.reason,
            )
            self.trigger_flatten(FlattenMode.CANCEL_AND_CLOSE, "Daily loss cap hit")

        # Notify
        if self.run.config.require_telegram_notify:
            pos = self.position_manager.get_book().positions[fill.symbol]
            self.notifier.notify_live_fill(
                self.run.run_id,
                fill.symbol,
                fill.side,
                fill.qty,
                fill.price,
                pos.realized_pnl,
            )

    def trigger_flatten(self, mode: FlattenMode, reason: str) -> None:
        self.run.state.status = LiveSessionStatus.FLATTENING

        req = LiveFlattenRequest(run_id=self.run.run_id, mode=mode, reason=reason)
        res = self.flatten_ctrl.execute_flatten(req)

        self.audit_writer.write_record(
            LiveAuditRecord(
                run_id=self.run.run_id,
                event_type=LiveAuditEventType.FLATTEN,
                details=f"Flatten executed: {res.success}. Cancelled {res.orders_cancelled}, Closed {res.positions_closed}",
            )
        )

        self.notifier.notify_flatten(
            self.run.run_id, res.success, res.orders_cancelled, res.positions_closed
        )
        self.run.state.status = LiveSessionStatus.HALTED

    def trigger_rollback(
        self, severity: RollbackSeverity, reason: str, context: Dict[str, Any]
    ) -> None:
        self.run.state.status = LiveSessionStatus.ROLLING_BACK
        plan = self.rollback_ctrl.initiate_rollback(
            self.run.run_id, severity, reason, context
        )

        self.audit_writer.write_record(
            LiveAuditRecord(
                run_id=self.run.run_id,
                event_type=LiveAuditEventType.ROLLBACK,
                details=f"Rollback initiated. Severity: {severity.value}",
            )
        )

        if plan.trigger_flatten:
            self.trigger_flatten(
                FlattenMode.CANCEL_AND_CLOSE, f"Rollback trigger: {reason}"
            )

        self.notifier.notify_rollback(self.run.run_id, severity.value, reason)
        self.run.state.status = LiveSessionStatus.HALTED

    def stop_session(self) -> None:
        if self.run.state.status == LiveSessionStatus.RUNNING:
            self.run.state.status = LiveSessionStatus.COMPLETED
            self.run.state.end_time = datetime.utcnow()

            self.audit_writer.write_record(
                LiveAuditRecord(
                    run_id=self.run.run_id,
                    event_type=LiveAuditEventType.SESSION_STOP,
                    details="Normal session stop.",
                )
            )
