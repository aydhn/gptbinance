from app.liability_plane.repository import LiabilityRepository

class QualityManager:
    def __init__(self, repository: LiabilityRepository):
        self.repository = repository

    def check_quality(self, liability_id: str):
        record = self.repository.get_liability_record(liability_id)
        if not record:
            return []
        warnings = []
        if not record.causation:
            warnings.append("Missing causation basis")
        if record.caps and not record.residual_exposure:
            warnings.append("Cap comfort warning: Cap applied without explicit residual exposure tracking")
        if record.indemnity and not record.residual_exposure:
            warnings.append("Indemnity laundering warning: Indemnity invoked without residual exposure check")
        if record.exoneration and len(record.exoneration) > len(record.responsibility):
            warnings.append("Exoneration inflation warning")
        return warnings
