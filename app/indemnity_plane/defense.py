from app.indemnity_plane.models import DefenseDutyRecord
def evaluate_defense(indemnity_id: str, defense_class: str) -> DefenseDutyRecord:
    return DefenseDutyRecord(indemnity_id=indemnity_id, defense_class=defense_class)
