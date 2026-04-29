from app.execution.live_runtime.models import LiveRollbackPlan
from app.execution.live_runtime.enums import RollbackSeverity
from typing import Dict, Any
import logging

logger = logging.getLogger(__name__)


class LiveRollbackController:
    def __init__(self, flatten_controller: Any):
        self.flatten_controller = flatten_controller

    def initiate_rollback(
        self,
        run_id: str,
        severity: RollbackSeverity,
        reason: str,
        context: Dict[str, Any],
    ) -> LiveRollbackPlan:
        logger.error(
            f"Initiating rollback for {run_id}. Severity: {severity.value}. Reason: {reason}"
        )

        # Disarm Mainnet execution
        if "mainnet_armed" in context:
            context["mainnet_armed"] = False
            logger.info("Mainnet execution explicitly disarmed via rollback.")

        trigger_flatten = severity == RollbackSeverity.HARD

        plan = LiveRollbackPlan(
            run_id=run_id,
            severity=severity,
            reason=reason,
            disarm_mainnet=True,
            trigger_flatten=trigger_flatten,
        )

        return plan
