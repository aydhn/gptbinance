from app.indemnity_plane.models import SettlementConsentRecord
def evaluate_settlement(indemnity_id: str, consent_granted: bool) -> SettlementConsentRecord:
    return SettlementConsentRecord(indemnity_id=indemnity_id, consent_granted=consent_granted)
