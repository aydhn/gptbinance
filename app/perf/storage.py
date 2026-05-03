import json
import os
from typing import Optional, List
from app.perf.models import PerfRun, PerfRegressionReport, HostQualificationReport


class PerfStorage:
    def __init__(self, base_path: str = "data/perf"):
        self.base_path = base_path
        os.makedirs(os.path.join(base_path, "runs"), exist_ok=True)
        os.makedirs(os.path.join(base_path, "regressions"), exist_ok=True)
        os.makedirs(os.path.join(base_path, "qualifications"), exist_ok=True)

    def save_run(self, run: PerfRun) -> None:
        path = os.path.join(self.base_path, "runs", f"{run.run_id}.json")
        with open(path, "w") as f:
            f.write(run.model_dump_json(indent=2))

    def load_run(self, run_id: str) -> Optional[PerfRun]:
        path = os.path.join(self.base_path, "runs", f"{run_id}.json")
        if not os.path.exists(path):
            return None
        with open(path, "r") as f:
            return PerfRun.model_validate_json(f.read())

    def list_runs(self) -> List[str]:
        path = os.path.join(self.base_path, "runs")
        return [f.replace(".json", "") for f in os.listdir(path) if f.endswith(".json")]

    def save_regression(self, report: PerfRegressionReport) -> None:
        filename = f"{report.baseline_run_id}_{report.target_run_id}.json"
        path = os.path.join(self.base_path, "regressions", filename)
        with open(path, "w") as f:
            f.write(report.model_dump_json(indent=2))

    def save_qualification(self, report: HostQualificationReport) -> None:
        filename = f"{report.host_class.value}.json"
        path = os.path.join(self.base_path, "qualifications", filename)
        with open(path, "w") as f:
            f.write(report.model_dump_json(indent=2))

    def load_qualification(
        self, host_class_value: str
    ) -> Optional[HostQualificationReport]:
        path = os.path.join(
            self.base_path, "qualifications", f"{host_class_value}.json"
        )
        if not os.path.exists(path):
            return None
        with open(path, "r") as f:
            return HostQualificationReport.model_validate_json(f.read())
