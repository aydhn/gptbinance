# stay_scope.py
from typing import Dict, List, Optional
from app.insolvency_plane.models import StayScopeRecord

class StayScopeManager:
    def __init__(self):
        self.scopes: Dict[str, StayScopeRecord] = {}

    def add_scope(self, scope: StayScopeRecord):
        self.scopes[scope.scope_id] = scope

    def get_scope(self, scope_id: str) -> Optional[StayScopeRecord]:
        return self.scopes.get(scope_id)

    def list_scopes(self) -> List[StayScopeRecord]:
        return list(self.scopes.values())
