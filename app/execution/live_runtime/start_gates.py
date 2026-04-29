from typing import Dict, Any, List
from app.execution.live_runtime.models import LiveStartGateReport, LiveSessionConfig
from app.execution.live_runtime.enums import LiveRolloutMode


class LiveStartGateEvaluator:
    def evaluate(
        self, config: LiveSessionConfig, context: Dict[str, Any]
    ) -> LiveStartGateReport:
        blockers = []
        warnings = []
        reasons = []
        recommended_actions = []

        is_armed = context.get("mainnet_armed", False)
        if not is_armed:
            blockers.append("Mainnet is not armed. Missing explicit arming.")

        has_active_maintenance = context.get("active_maintenance", False)
        if has_active_maintenance:
            blockers.append("Active maintenance window detected.")

        has_active_incident = context.get("active_incident", False)
        if has_active_incident:
            blockers.append("Active unresolved incident detected.")

        is_kill_switch_active = context.get("kill_switch_active", False)
        if is_kill_switch_active:
            blockers.append("Global kill switch is ACTIVE.")

        ops_ready = context.get("ops_readiness_pass", False)
        if not ops_ready:
            blockers.append("Ops readiness checks failed.")

        reconciliation_clean = context.get("reconciliation_clean", False)
        if not reconciliation_clean:
            blockers.append("Unresolved anomalies from past sessions exist.")

        if config.rollout_mode == LiveRolloutMode.FULL_LIVE_LOCKED:
            blockers.append("FULL_LIVE_LOCKED mode is strictly forbidden for now.")

        if len(config.capital_caps.allowlist) == 0 and config.rollout_mode in [
            LiveRolloutMode.CANARY_LIVE,
            LiveRolloutMode.CAPPED_LIVE,
        ]:
            blockers.append("Capital caps allowlist is empty for live rollout mode.")

        passed = len(blockers) == 0

        if passed:
            reasons.append(
                f"Successfully passed start gates for {config.rollout_mode.value}."
            )
        else:
            reasons.append("Start gates blocked session start.")
            recommended_actions.append(
                "Resolve all blockers before attempting to start."
            )

        return LiveStartGateReport(
            passed=passed,
            reasons=reasons,
            blockers=blockers,
            warnings=warnings,
            recommended_actions=recommended_actions,
            effective_rollout_mode=config.rollout_mode,
        )
