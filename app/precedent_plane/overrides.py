# Precedent Plane Module: overrides
from app.precedent_plane.models import *

class OverridesManager:
    def __init__(self):
        self.records = []

    def process(self, *args, **kwargs):
        # Implementation for overrides
        return True

class PrecedentOverride:
    def __init__(self):
        self.authority_plane_override_authority_refs = []
        self.scope_refs = []
        self.hierarchy_refs = []
