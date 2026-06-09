class ViabilityLinkage:
    def __init__(self):
        self.notes = []

    def link_investigation(self, investigation_id: str, details: dict):
        self.notes.append(details)
        return {"status": "linked", "investigation_id": investigation_id, "caution": "explicit caution: investigation posture required"}
