# gross.py
from app.recovery_plane.models import *
from app.recovery_plane.exceptions import *

class GrossManager:
    def process(self, data: dict):
        return {"status": "ok", "module": "gross"}
