from app.resilience.models import (
    ExperimentScope,
    ExperimentDefinition,
    ExperimentGateReport,
)
from app.resilience.enums import GateVerdict
import logging

logger = logging.getLogger(__name__)


class SafetyGate:
    def evaluate(
        self, definition: ExperimentDefinition, scope: ExperimentScope
    ) -> ExperimentGateReport:
        if scope.is_live_mainnet:
            return ExperimentGateReport(
                verdict=GateVerdict.BLOCK,
                reason="Chaos/Fault injection on mainnet live is strictly prohibited.",
                blocked_by="MainnetBlocker",
            )

        if scope.safe_scope not in definition.allowed_scopes:
            return ExperimentGateReport(
                verdict=GateVerdict.BLOCK,
                reason=f"Scope {scope.safe_scope} is not in allowed scopes {definition.allowed_scopes}",
                blocked_by="ScopeValidator",
            )

        return ExperimentGateReport(
            verdict=GateVerdict.ALLOW, reason="All safety gates passed."
        )
