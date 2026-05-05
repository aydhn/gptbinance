from app.remediation.models import RemediationPack, BlastRadiusReport
from app.remediation.enums import BlastRadiusSeverity, RemediationClass


class BlastRadiusAnalyzer:
    def analyze(self, pack: RemediationPack) -> BlastRadiusReport:
        impacted = []
        severity = BlastRadiusSeverity.LOW
        side_effects = []

        if pack.recipe.safety_class == RemediationClass.VENUE_AFFECTING:
            severity = BlastRadiusSeverity.CRITICAL
            impacted.extend(["venue", "order_lifecycle", "ledger"])
            side_effects.append("May alter live venue state and trigger fills.")
        elif pack.recipe.safety_class == RemediationClass.APPROVAL_BOUND_LOCAL:
            severity = BlastRadiusSeverity.MEDIUM
            impacted.extend(["crossbook", "qualification"])
            side_effects.append("May pause trading for symbol.")
        else:
            impacted.append("shadow_state")
            side_effects.append("Local cache refresh only.")

        return BlastRadiusReport(
            severity=severity,
            impacted_domains=impacted,
            side_effects=side_effects,
            conflict_warnings=[],
        )
