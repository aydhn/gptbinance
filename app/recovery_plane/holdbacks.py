# holdbacks.py
from app.recovery_plane.models import *
from app.recovery_plane.exceptions import *

class HoldbacksManager:
    def process(self, data: dict):
        return {"status": "ok", "module": "holdbacks"}
