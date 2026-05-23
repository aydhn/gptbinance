from app.liability_plane.repository import LiabilityRepository

class ReportingManager:
    def __init__(self, repository: LiabilityRepository):
        self.repository = repository

    def generate_summary(self, liability_id: str) -> str:
        record = self.repository.get_liability_record(liability_id)
        if not record:
            return "Liability not found."

        lines = []
        lines.append(f"Liability ID: {record.liability.liability_id}")
        lines.append(f"Class: {record.liability.liability_class}")
        lines.append(f"State: {record.liability.state}")
        lines.append(f"Causation Posture: {record.liability.causation_posture}")
        lines.append(f"Exposure Posture: {record.liability.exposure_posture}")

        if record.trust_verdict:
            lines.append(f"Trust Verdict: {record.trust_verdict.verdict}")

        return "\n".join(lines)
