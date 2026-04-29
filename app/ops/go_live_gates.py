from app.ops.models import GoLiveGateReport
from app.ops.enums import GoLiveVerdict


class GoLiveGate:
    def evaluate(self, run_id: str) -> GoLiveGateReport:
        return GoLiveGateReport(
            verdict=GoLiveVerdict.FAIL,
            reasons=["Mainnet execution is explicitly disabled in this phase."],
            blockers=["Mainnet Live Default Block"],
            recommended_actions=[
                "Review control plane architecture before enabling mainnet."
            ],
        )
