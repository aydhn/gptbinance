# estate_scope.py
from typing import Dict, List, Optional
from app.insolvency_plane.models import EstateScopeRecord

class EstateScopeManager:
    def __init__(self):
        self.scopes: Dict[str, EstateScopeRecord] = {}

    def add_scope(self, scope: EstateScopeRecord):
        self.scopes[scope.scope_id] = scope

    def get_scope(self, scope_id: str) -> Optional[EstateScopeRecord]:
        return self.scopes.get(scope_id)

    def list_scopes(self) -> List[EstateScopeRecord]:
        return list(self.scopes.values())
