# windows implementation for temporal plane
from app.temporal_plane.models import *
from app.temporal_plane.enums import *
from app.temporal_plane.exceptions import *

class WindowsManager:
    def __init__(self):
        pass
    def evaluate(self, ref: TemporalObjectRef) -> dict:
        return {"status": "ok"}
