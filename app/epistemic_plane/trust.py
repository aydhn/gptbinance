from app.epistemic_plane.models import EpistemicTrustVerdictRecord, EpistemicTrustVerdict

class TrustManager:
    def evaluate_trust(self, claim_id: str) -> EpistemicTrustVerdictRecord:
        return EpistemicTrustVerdictRecord(
            verdict=EpistemicTrustVerdict.TRUSTED,
            factors={"claim_classification_rigor": "pass", "evidence_sufficiency": "pass"}
        )
