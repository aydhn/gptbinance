from app.cost_plane.models import CostDivergenceReport
import uuid

class DivergenceManager:
    def __init__(self):
        self._reports: list[CostDivergenceReport] = []

    def report_divergence(self, source_env: str, target_env: str, divergence_amount: float, currency: str, severity: str) -> CostDivergenceReport:
        report = CostDivergenceReport(
            report_id=str(uuid.uuid4()),
            source_env=source_env,
            target_env=target_env,
            divergence_amount=divergence_amount,
            currency=currency,
            severity=severity
        )
        self._reports.append(report)
        return report

    def list_reports(self) -> list[CostDivergenceReport]:
        return self._reports
