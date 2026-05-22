class PolicyContext:
    def __init__(self):
        self.precedent_posture = None
        self.active_conflicts = []
        self.stale_analogies = []


class PrecedentContext:
    def __init__(self):
        self.precedent_posture = None
        self.active_conflicts = []
        self.stale_analogies = []
        self.exception_inflation = False
        self.rationale_coverage = []
