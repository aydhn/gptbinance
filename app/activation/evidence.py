from app.activation.models import ActivationEvidenceBundle


class EvidenceCollector:
    @staticmethod
    def collect(intent_id: str, board_ref: str) -> ActivationEvidenceBundle:
        # In a real system, fetch policy proofs, candidate details, etc.
        return ActivationEvidenceBundle(
            intent_id=intent_id,
            board_decision_ref=board_ref,
            policy_proof_refs=["proof-123"],
            candidate_freeze_ref="cand-hash-abc",
            probation_evidence_refs=[],
        )
