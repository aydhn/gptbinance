from app.commitment_plane.models import CommitmentObject, CommitmentTrustVerdictModel
from app.commitment_plane.enums import CommitmentTrustVerdict
from app.commitment_plane.base import TrustEvaluatorBase

class CommitmentTrustEvaluator(TrustEvaluatorBase):
    def evaluate(self, commitment: CommitmentObject) -> CommitmentTrustVerdictModel:
        if not commitment.owners or not commitment.binding:
            verdict = CommitmentTrustVerdict.BLOCKED
        else:
            verdict = CommitmentTrustVerdict.TRUSTED

        return CommitmentTrustVerdictModel(
            verdict=verdict,
            factors={"binding_clarity": "present", "owner_accountability": "present"},
            breakdown={"details": "Evaluated based on standard criteria"}
        )
