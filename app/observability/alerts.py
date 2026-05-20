class SemanticAlerting:
    def alert_on_conflict(self, conflict):
        print(f"[ALERT] Semantic Conflict Detected: {conflict.unresolved_notes}")

    def alert_on_dangerous_alias(self, term_name, alias_name):
        print(f"[ALERT] Dangerous Alias Detected: {alias_name} for term {term_name}")
