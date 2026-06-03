# incidents.py
from app.resilience_plane.models import *

class IncidentsLinkage:
    def evaluate(self, resilience_id: str):
        return {"status": "linked", "resilience_id": resilience_id}
