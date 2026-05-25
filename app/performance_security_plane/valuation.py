from app.performance_security_plane.models import ValuationRecord

class ValuationManager:
    def create_valuation(self, security_id: str, valuation_type: str, value: float, freshness_note: str) -> ValuationRecord:
        return ValuationRecord(
            security_id=security_id,
            type=valuation_type,
            value=value,
            freshness_note=freshness_note,
            lineage_refs=[f"valuation_{security_id}"]
        )
