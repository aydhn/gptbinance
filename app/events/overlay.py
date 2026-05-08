class EventRiskOverlay:
    def get_event_posture(self) -> dict:
        # Event window no-new-exposure / reduced-size semantics
        return {"no_new_exposure": False}
