from datetime import datetime
from app.ops.models import RolloverSummary
from app.ops.repository import OpsRepository


class RolloverManager:
    def __init__(self, repository: OpsRepository):
        self.repository = repository

    def execute_rollover(self, run_id: str) -> RolloverSummary:
        summary = RolloverSummary(
            run_id=run_id,
            date=datetime.utcnow(),
            total_orders=0,
            incidents_count=len(self.repository.get_incidents(run_id)),
            status="completed",
        )
        return summary
