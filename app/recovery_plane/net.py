# net.py
from app.recovery_plane.models import *
from app.recovery_plane.exceptions import *

class NetManager:
    def process(self, data: dict):
        return {"status": "ok", "module": "net"}
