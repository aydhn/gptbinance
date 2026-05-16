from app.program_plane.models import DeliveryRiskRecord

class DeliveryRiskManager:
    def evaluate_risks(self, program_id: str) -> DeliveryRiskRecord:
        return DeliveryRiskRecord(
            risk_id=f"risk_{program_id}",
            program_id=program_id,
            risk_type="dependency_risk",
            mitigation_notes="Mitigation applied"
        )
