from app.governance.models import CandidateBundle, ActivationReadinessReport
from app.governance.enums import BundleStage


class ActivationManager:
    def simulate_handoff(
        self, bundle: CandidateBundle, target_mode: str
    ) -> ActivationReadinessReport:
        checks = {
            "is_approved": bundle.stage_state.stage
            in [
                BundleStage.APPROVED_FOR_SHADOW,
                BundleStage.APPROVED_FOR_PAPER,
                BundleStage.APPROVED_FOR_TESTNET_EXEC,
                BundleStage.APPROVED_FOR_LIVE_CAUTION,
            ],
            "has_rollback": bundle.rollback_ref is not None,
        }

        is_ready = all(checks.values())
        warnings = []
        if not is_ready:
            warnings.append("Activation simulation failed checks.")

        return ActivationReadinessReport(
            bundle_id=bundle.bundle_id,
            target_mode=target_mode,
            is_ready=is_ready,
            checks=checks,
            warnings=warnings,
        )
