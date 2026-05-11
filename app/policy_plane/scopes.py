class ScopeCalculus:
    @staticmethod
    def is_within_scope(request_scope: dict, allowed_scope: dict) -> bool:
        for k, v in allowed_scope.items():
            if request_scope.get(k) != v:
                return False
        return True
