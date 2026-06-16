from app.waterfall_plane.models import IntercreditorRecord

def register_intercreditor_rule(rule_id: str, description: str) -> IntercreditorRecord:
    return IntercreditorRecord(rule_id=rule_id, description=description)
