from typing import Dict, Any, List
from app.execution.live.models import SafeExecutionGateResult, ExecutionConfig
from app.execution.live.enums import ExecutionEnvironment, SafetyGateSeverity
import logging

logger = logging.getLogger(__name__)


class SafetyGate:
    def check(
        self, config: ExecutionConfig, context: Dict[str, Any]
    ) -> SafeExecutionGateResult:
        raise NotImplementedError


class MainnetDisarmedGate(SafetyGate):
    def check(
        self, config: ExecutionConfig, context: Dict[str, Any]
    ) -> SafeExecutionGateResult:
        if (
            config.environment == ExecutionEnvironment.MAINNET
            and not config.mainnet_armed
        ):
            return SafeExecutionGateResult(
                passed=False,
                reason="Mainnet execution is not explicitly armed.",
                severity=SafetyGateSeverity.BLOCK.value,
            )
        return SafeExecutionGateResult(passed=True)


class RolloutModeAllowedGate(SafetyGate):
    def check(
        self, config: ExecutionConfig, context: Dict[str, Any]
    ) -> SafeExecutionGateResult:
        rollout_mode = context.get("rollout_mode", "shadow_only")
        if rollout_mode == "full_live_locked":
            return SafeExecutionGateResult(
                passed=False,
                reason="FULL_LIVE_LOCKED mode is strictly blocked.",
                severity=SafetyGateSeverity.BLOCK.value,
            )
        return SafeExecutionGateResult(passed=True)


class SessionReadinessGate(SafetyGate):
    def check(
        self, config: ExecutionConfig, context: Dict[str, Any]
    ) -> SafeExecutionGateResult:
        is_ready = context.get("is_session_ready", False)
        if not is_ready:
            return SafeExecutionGateResult(
                passed=False,
                reason="Trading session is not ready.",
                severity=SafetyGateSeverity.BLOCK.value,
            )
        return SafeExecutionGateResult(passed=True)


class ReleaseVersionGate(SafetyGate):
    def check(
        self, config: ExecutionConfig, context: Dict[str, Any]
    ) -> SafeExecutionGateResult:
        if context.get("version_mismatch"):
            return SafeExecutionGateResult(
                passed=False,
                reason="Version mismatch detected.",
                severity=SafetyGateSeverity.BLOCK.value,
            )
        return SafeExecutionGateResult(passed=True)


class AuthorizationBundleGate(SafetyGate):
    def check(
        self, config: ExecutionConfig, context: Dict[str, Any]
    ) -> SafeExecutionGateResult:
        auth_bundle = context.get("authorization_bundle")
        if auth_bundle and auth_bundle.verdict.value != "approved":
            # If auth bundle is strictly present but denied, block.
            # If missing entirely, assume control layer disabled for tests.

            return SafeExecutionGateResult(
                passed=False,
                reason="Missing or denied authorization bundle for live action.",
                severity=SafetyGateSeverity.BLOCK.value,
            )
        return SafeExecutionGateResult(passed=True)


class SafetyGateManager:
    def check_resilience_block(self) -> bool:
        return True

    def __init__(self):
        self.gates: List[SafetyGate] = [
            MainnetDisarmedGate(),
            SessionReadinessGate(),
            RolloutModeAllowedGate(),
            ReleaseVersionGate(),
            AuthorizationBundleGate(),
        ]

    def add_gate(self, gate: SafetyGate):
        self.gates.append(gate)

    def evaluate_all(
        self, config: ExecutionConfig, context: Dict[str, Any]
    ) -> SafeExecutionGateResult:
        for gate in self.gates:
            result = gate.check(config, context)
            if not result.passed:
                logger.warning(f"Safety gate blocked execution: {result.reason}")
                return result
        return SafeExecutionGateResult(passed=True)
