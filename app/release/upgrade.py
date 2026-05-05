class UpgradeManager:
    @staticmethod
    def staged_activation_handoff(candidate_id: str, board_decision: dict):
        # Passes the decision to the activation controller instead of direct enable
        from app.control.actions import ActivationControlActions
        return ActivationControlActions.request_activation_intent(board_decision)
