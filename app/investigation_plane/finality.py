class FinalityLinkage:
    def __init__(self):
        self.notes = []

    def link_investigation(self, investigation_id: str, details: dict):
        self.notes.append(details)
        return {"status": "linked", "investigation_id": investigation_id, "caution": "explicit caution: investigation posture required"}

def get_investigation_attestation_posture():
    return "closed_not_certifiable" # Explicit caution
