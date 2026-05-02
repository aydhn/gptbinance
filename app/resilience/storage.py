from typing import Dict
from app.resilience.models import ExperimentSummary


class StorageLayer:
    def __init__(self):
        self.summaries: Dict[str, ExperimentSummary] = {}

    def save_summary(self, summary: ExperimentSummary):
        self.summaries[summary.run_id] = summary

    def get_summary(self, run_id: str) -> ExperimentSummary | None:
        return self.summaries.get(run_id)
