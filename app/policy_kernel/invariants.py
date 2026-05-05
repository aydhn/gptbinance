class ActivationInvariants:
    @staticmethod
    def check_invariants(activation_state: dict):
        if not activation_state.get("board_decision_ref"):
            raise ValueError("No activation without final board decision ref")
        if activation_state.get("automatic_expansion", False):
            raise ValueError("No automatic expansion after probation")
