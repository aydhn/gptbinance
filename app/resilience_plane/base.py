# base.py
from app.resilience_plane.models import *
from app.resilience_plane.exceptions import *

class BaseManager:
    def __init__(self):
        self.records = []

    def manage(self, **kwargs):
        pass
