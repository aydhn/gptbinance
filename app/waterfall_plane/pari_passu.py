from app.waterfall_plane.models import PariPassuRecord
from typing import List

def register_pari_passu_rule(rule_id: str, members: List[str]) -> PariPassuRecord:
    return PariPassuRecord(rule_id=rule_id, members=members)
