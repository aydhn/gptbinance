from typing import Dict, Any, List
from app.commitment_plane.models import CommitmentObject, CommitmentTrustVerdictModel
from app.commitment_plane.enums import CommitmentTrustVerdict

class CommitmentRegistryBase:
    def register_commitment(self, commitment: CommitmentObject) -> str:
        raise NotImplementedError

    def get_commitment(self, commitment_id: str) -> CommitmentObject:
        raise NotImplementedError

class BreachEvaluatorBase:
    def evaluate(self, commitment: CommitmentObject) -> List[Dict[str, Any]]:
        raise NotImplementedError

class DischargeEvaluatorBase:
    def evaluate(self, commitment: CommitmentObject) -> bool:
        raise NotImplementedError

class TrustEvaluatorBase:
    def evaluate(self, commitment: CommitmentObject) -> CommitmentTrustVerdictModel:
        raise NotImplementedError
