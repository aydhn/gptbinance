from app.cost_plane.models import CostForecastReport, SpendRecord
from app.cost_plane.base import ForecastEvaluatorBase
import uuid

class ForecastManager(ForecastEvaluatorBase):
    def __init__(self):
        self._reports: list[CostForecastReport] = []

    def evaluate(self, spend_history: list[SpendRecord]) -> CostForecastReport:
        if not spend_history:
            return CostForecastReport(
                report_id=str(uuid.uuid4()),
                cost_id="unknown",
                forecast_amount=0.0,
                currency="USD",
                uncertainty_class="high"
            )

        cost_id = spend_history[0].cost_id
        currency = spend_history[0].currency
        total = sum([s.amount for s in spend_history])
        avg = total / len(spend_history)
        forecast_amount = avg * 1.1 # 10% trend assumed

        report = CostForecastReport(
            report_id=str(uuid.uuid4()),
            cost_id=cost_id,
            forecast_amount=forecast_amount,
            currency=currency,
            uncertainty_class="medium"
        )
        self._reports.append(report)
        return report

    def list_reports(self) -> list[CostForecastReport]:
        return self._reports
