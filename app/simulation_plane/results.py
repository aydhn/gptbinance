class SimulationResult:
    def __init__(self, result_id: str, target_release_candidate_ref: str = None):
        self.result_id = result_id
        self.target_release_candidate_ref = target_release_candidate_ref

class SimulationEvidenceBuilder:
    def build_promotion_grade_evidence(self):
        # Tied to target release candidate refs
        pass

    def tie_compatibility_to_assumptions(self):
        # Release compatibility tied to simulation assumptions
        pass
