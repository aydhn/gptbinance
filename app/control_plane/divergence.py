from app.control_plane.models import ControlDivergenceReport


class DivergenceEngine:
    def log_divergence(
        self, action_id: str, diff_type: str, severity: str, details: str
    ) -> ControlDivergenceReport:
        return ControlDivergenceReport(
            action_id=action_id,
            divergence_type=diff_type,
            severity=severity,
            details=details,
        )
