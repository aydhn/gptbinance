class AllocationIntent:
    def require_decision_lineage(self, decision_id: str):
        pass
    def __init__(self, intent_id: str, active_release_context: str = None):
        self.intent_id = intent_id
        self.active_release_context = active_release_context

class AllocationEngine:
    def evaluate_release_drift(self):
        # Release drift acts as input to candidate comparability
        pass



# Cost plane evaluation integration
def assert_economic_denominator(has_economic_denominator: bool):
    if not has_economic_denominator:
        return "caution"
    return "ready"
