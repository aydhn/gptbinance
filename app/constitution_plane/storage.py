from typing import Dict
from app.constitution_plane.models import FinalVerdictRecord, ConstitutionTrustVerdict

class ConstitutionStorage:
    def __init__(self):
        self._final_verdicts: Dict[str, FinalVerdictRecord] = {}
        self._trust_verdicts: Dict[str, ConstitutionTrustVerdict] = {}

    def save_final_verdict(self, record: FinalVerdictRecord):
        self._final_verdicts[record.object_id] = record

    def get_final_verdict(self, object_id: str) -> FinalVerdictRecord:
        return self._final_verdicts.get(object_id)

    def save_trust_verdict(self, object_id: str, verdict: ConstitutionTrustVerdict):
        self._trust_verdicts[object_id] = verdict
