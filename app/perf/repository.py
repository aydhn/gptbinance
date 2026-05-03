from typing import Optional, List
from app.perf.storage import PerfStorage
from app.perf.models import PerfRun, PerfRegressionReport, HostQualificationReport


class PerfRepository:
    def __init__(self, storage: PerfStorage):
        self.storage = storage

    def save_perf_run(self, run: PerfRun) -> None:
        self.storage.save_run(run)

    def get_perf_run(self, run_id: str) -> Optional[PerfRun]:
        return self.storage.load_run(run_id)

    def get_all_run_ids(self) -> List[str]:
        return self.storage.list_runs()

    def save_regression_report(self, report: PerfRegressionReport) -> None:
        self.storage.save_regression(report)

    def save_qualification_report(self, report: HostQualificationReport) -> None:
        self.storage.save_qualification(report)

    def get_qualification_report(
        self, host_class_value: str
    ) -> Optional[HostQualificationReport]:
        return self.storage.load_qualification(host_class_value)
