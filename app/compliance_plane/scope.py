from typing import Dict, Any


class ScopeManager:
    def check_scope_match(
        self, req_scope: Dict[str, Any], evidence_scope: Dict[str, Any]
    ) -> bool:
        # Simplistic check: all keys in req_scope must exist and match in evidence_scope
        for k, v in req_scope.items():
            if evidence_scope.get(k) != v:
                return False
        return True
