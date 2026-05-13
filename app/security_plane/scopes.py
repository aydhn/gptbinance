class ScopeManager:
    @staticmethod
    def is_scope_widening(old_scope: str, new_scope: str) -> bool:
        if old_scope == new_scope:
             return False
        if old_scope != "*" and new_scope == "*":
             return True
        return False
