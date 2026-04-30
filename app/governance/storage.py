from typing import Any


class GovernanceStorage:
    # In-memory mock for now
    def __init__(self):
        self.runs = {}
        self.bundles = {}
        self.decay_reports = {}

    def save_run(self, run: Any):
        self.runs[run.run_id] = run

    def save_bundle(self, bundle: Any):
        self.bundles[bundle.bundle_id] = bundle

    def save_decay_report(self, report: Any):
        self.decay_reports[report.report_id] = report
