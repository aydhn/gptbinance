class DecisionQualityReporting:
    def log_funnel_friction(self, candidate_id: str, reject_reason: str):
        # Log events where a signal existed but allocation rejected it
        pass

class DecisionQualityExecutionReport:
    @staticmethod
    def add_friction_surface(reason: str):
        pass # records defer/reject events
