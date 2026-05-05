from typing import Dict
from app.experiments.models import CandidateReference


class CandidateRegistry:
    def __init__(self):
        self._candidates: Dict[str, CandidateReference] = {}

    def register(self, candidate: CandidateReference) -> str:
        self._candidates[candidate.candidate_id] = candidate
        return candidate.candidate_id

    def get(self, candidate_id: str) -> CandidateReference:
        return self._candidates.get(candidate_id)

    def list_by_hypothesis(self, hypothesis_id: str) -> list[CandidateReference]:
        return [
            c for c in self._candidates.values() if c.hypothesis_id == hypothesis_id
        ]
