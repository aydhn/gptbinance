# remedy.py
from app.recovery_plane.models import *
from app.recovery_plane.exceptions import *

class RemedyManager:
    def process(self, data: dict):
        return {"status": "ok", "module": "remedy"}
