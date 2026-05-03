class EvidencePack:
    def __init__(self):
        self.perf_summary_ref = None
        self.host_qualification_ref = None
        self.perf_regression_ref = None

    def add_perf_evidence(self, summary_id: str, qual_id: str, reg_id: str) -> None:
        self.perf_summary_ref = summary_id
        self.host_qualification_ref = qual_id
        self.perf_regression_ref = reg_id
