from app.ops.models import GoLiveGateReport
from app.ops.enums import GoLiveVerdict


class GoLiveGate:
    def evaluate(
        self, run_id: str, rollout_mode: str = "shadow_only"
    ) -> GoLiveGateReport:
        if rollout_mode == "full_live_locked":
            return GoLiveGateReport(
                verdict=GoLiveVerdict.FAIL,
                reasons=["FULL_LIVE_LOCKED mode is strictly blocked in this phase."],
                blockers=["Mainnet Full Live Block"],
                recommended_actions=["Use canary_live or capped_live rollout modes."],
            )

        # If canary or capped, pass it up to LiveStartGateEvaluator to do the detailed check
        if rollout_mode in ["canary_live", "capped_live"]:
            return GoLiveGateReport(
                verdict=GoLiveVerdict.CAUTION,
                reasons=[
                    f"Proceeding cautiously with {rollout_mode}. Ensure LiveStartGates are evaluated."
                ],
                blockers=[],
                recommended_actions=[
                    "Ensure Capital Caps and execution hooks are active."
                ],
            )

        return GoLiveGateReport(
            verdict=GoLiveVerdict.FAIL,
            reasons=[
                "Mainnet execution is generally disabled unless explicitly routed to a capped mode."
            ],
            blockers=["Mainnet Live Default Block"],
            recommended_actions=[
                "Review control plane architecture before enabling mainnet."
            ],
        )
