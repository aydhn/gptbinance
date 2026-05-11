from app.policy_plane.models import PolicyDivergenceReport


def report_divergence(
    src: str, target: str, reason: str, severity: str
) -> PolicyDivergenceReport:
    return PolicyDivergenceReport(
        source_environment=src,
        target_environment=target,
        divergence_reason=reason,
        severity=severity,
    )
