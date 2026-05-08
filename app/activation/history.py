class ActivationHistory:
    def log_allocation_diffs(self, diff_id: str):
        # Stage-to-stage allocation diffs lineage exported
        pass

class ExecutionActivationHistory:
    def __init__(self):
        self.stage_diffs = []

    def record_diff(self, stage_from: str, stage_to: str, diff_ref: str):
        self.stage_diffs.append({"from": stage_from, "to": stage_to, "diff_ref": diff_ref})
