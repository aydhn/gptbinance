# Example facade to hook everything together
from app.assurance_plane.registry import AssuranceRegistry
from app.assurance_plane.repository import AssuranceRepository
from app.assurance_plane.trust import evaluate_trust

class AssurancePlaneFacade:
    def __init__(self):
        self.registry = AssuranceRegistry()
        self.repository = AssuranceRepository(self.registry)

    def get_trust_verdict(self, assurance_id: str):
        record = self.repository.get(assurance_id)
        if record:
            return evaluate_trust("verdict-1", record)
        return None
