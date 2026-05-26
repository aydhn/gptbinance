# dispute.py
from app.recovery_plane.models import *
from app.recovery_plane.exceptions import *

class DisputeManager:
    def process(self, data: dict):
        return {"status": "ok", "module": "dispute"}
