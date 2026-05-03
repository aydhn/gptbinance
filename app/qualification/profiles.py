class QualificationProfile:
    def __init__(self, mode: str):
        self.mode = mode
        self.min_perf_evidence_required: list[str] = []

    def set_requirements(self):
        if self.mode == "paper_ready":
            self.min_perf_evidence_required.append("latency_budget_pass")
        elif self.mode == "testnet_exec_ready":
            self.min_perf_evidence_required.extend(["latency_budget_pass", "cpu_budget_pass"])
