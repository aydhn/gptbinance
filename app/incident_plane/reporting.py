from app.incident_plane.models import IncidentManifest, RecoveryVerificationRecord

class IncidentReporter:
    def format_registry(self) -> str:
        from app.incident_plane.registry import CanonicalIncidentRegistry
        lines = ["CANONICAL INCIDENT REGISTRY"]
        lines.extend([f" - {fam}" for fam in CanonicalIncidentRegistry.FAMILIES])
        return "\n".join(lines)

    def format_manifest(self, manifest: IncidentManifest) -> str:
        if not manifest:
            return "Incident not found."
        lines = [
            f"INCIDENT MANIFEST [{manifest.incident_id}]",
            f"Family: {manifest.family}",
            f"Severity: {manifest.severity.value.upper()}",
            f"Urgency: {manifest.urgency.value.upper()}",
            f"Status: {manifest.current_status.value.upper()}",
            f"Owner: {manifest.primary_owner}",
            f"Blast Radius: {manifest.blast_radius}"
        ]
        return "\n".join(lines)

    def format_verification(self, verification: RecoveryVerificationRecord) -> str:
        if not verification:
            return "No verification record found."
        lines = [
            f"RECOVERY VERIFICATION [{verification.incident_id}]",
            f"Verdict: {verification.verdict.value.upper()}",
            f"Objective Checks Passed: {verification.objective_checks_passed}",
            f"No-Regression Passed: {verification.no_regression_checks_passed}",
            f"Quiet Period Met: {verification.quiet_period_met}",
            f"Proof Notes: {verification.proof_notes}"
        ]
        return "\n".join(lines)
