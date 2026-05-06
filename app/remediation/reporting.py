from app.remediation.models import (
    BlastRadiusReport,
    RemediationPack,
    SimulationResult,
)


class RemediationReporter:
    def format_pack_summary(self, pack: RemediationPack) -> str:
        return f"""
=== REMEDIATION PACK: {pack.pack_id} ===
Recipe: {pack.recipe.name} ({pack.recipe.safety_class.value})
Finding: {pack.finding_ref.finding_id} ({pack.finding_ref.source_domain})
Scope: {pack.scope.model_dump()}
Actions: {len(pack.actions)}
"""

    def format_blast_radius(self, report: BlastRadiusReport) -> str:
        return f"""
=== BLAST RADIUS ===
Severity: {report.severity.value}
Impacted: {', '.join(report.impacted_domains)}
Side Effects: {', '.join(report.side_effects)}
"""

    def format_simulation(self, res: SimulationResult) -> str:
        return f"""
=== SIMULATION ===
Safe: {res.is_safe}
Deltas: {res.expected_deltas}
Expectations: {res.verification_expectations}
"""


def generate_remediation_apply_review_request():
    pass


def generate_remediation_rollback_review_request():
    pass
