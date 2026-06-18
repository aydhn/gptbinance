class SubstantiationManager:
    def __init__(self):
        self.records = {}

    def add(self, entity_id: str, data: dict):
        self.records[entity_id] = data
        return data

    def get(self, entity_id: str):
        return self.records.get(entity_id)

    def list_all(self):
        return list(self.records.values())


def check_adjudication_proof_standard(finding_id: str, adjudication_id: str) -> dict:
    if not adjudication_id:
        return {"safe": False, "caution": "Explicit caution: substantiated finding treated dispositive without adjudication posture"}
    return {"safe": True, "finding_id": finding_id, "adjudication_id": adjudication_id}

# RELIANCE PLANE INTEGRATION
# Enforces safe-decision-use, explicit freshness limits, and contradiction avoidance for substantiation.py.

# Added for Phase 163 Clearing Plane Integration
from app.clearing_plane.integration import integrate_with_clearing_plane

def evaluate_clearing_integration_hook():
    integration = integrate_with_clearing_plane("app/investigation_plane/substantiation.py")
    return integration.evaluate_posture()
