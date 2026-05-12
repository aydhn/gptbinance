class ActivationHistory:
    def __init__(self):
        self.stage_progressions = []

    def log_progression(self, stage: str, diagnostic_refs: list = None):
        self.stage_progressions.append({"stage": stage, "diagnostic_refs": diagnostic_refs})
