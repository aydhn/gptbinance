from typing import Dict, Optional
from app.stressrisk.models import StressRun


class StressStorage:
    def __init__(self):
        self.runs: Dict[str, StressRun] = {}

    def save_run(self, run: StressRun):
        self.runs[run.run_id] = run

    def get_run(self, run_id: str) -> Optional[StressRun]:
        return self.runs.get(run_id)
