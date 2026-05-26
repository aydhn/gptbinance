# provisional.py
from app.recovery_plane.models import *
from app.recovery_plane.exceptions import *

class ProvisionalManager:
    def process(self, data: dict):
        return {"status": "ok", "module": "provisional"}
