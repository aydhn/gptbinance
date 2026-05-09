from app.workflow_plane.models import WorkflowDivergenceReport

class DivergenceEvaluator:
    def __init__(self):
        self.reports = []

    def log_divergence(self, workflow_id: str, divergence_type: str, severity: str, description: str) -> WorkflowDivergenceReport:
        import uuid
        report = WorkflowDivergenceReport(
            report_id=f"div-{uuid.uuid4().hex[:8]}",
            workflow_id=workflow_id,
            divergence_type=divergence_type,
            severity=severity,
            blast_radius="isolated",
            description=description
        )
        self.reports.append(report)
        return report
