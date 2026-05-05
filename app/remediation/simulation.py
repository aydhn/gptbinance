from app.remediation.models import RemediationPack, SimulationResult
from app.remediation.enums import RemediationClass


class DryRunEngine:
    def simulate(self, pack: RemediationPack) -> SimulationResult:
        deltas = []
        if pack.recipe.safety_class == RemediationClass.READ_ONLY:
            deltas.append("Local state will sync with venue.")
        elif pack.recipe.safety_class == RemediationClass.VENUE_AFFECTING:
            deltas.append(
                "A review request will be generated for venue order cancellation."
            )

        return SimulationResult(
            is_safe=True,
            expected_deltas=deltas,
            verification_expectations=[
                "Finding should disappear from active drift reports."
            ],
            no_op_detected=False,
        )
