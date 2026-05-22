# Precedent Plane Module: overrides
from app.precedent_plane.models import *

class OverridesManager:
    def __init__(self):
        self.records = []

    def process(self, *args, **kwargs):
        # Implementation for overrides
        return True
