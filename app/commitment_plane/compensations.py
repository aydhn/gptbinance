from app.commitment_plane.models import CompensatingObligationRecord

class CompensationManager:
    @staticmethod
    def create_compensation(obligation_type: str, description: str, sufficiency_notes: str = None) -> CompensatingObligationRecord:
        valid_types = ['delivery', 'review', 'reporting', 'control']
        if obligation_type not in valid_types:
            raise ValueError(f"Invalid compensation obligation type. Must be one of {valid_types}")

        return CompensatingObligationRecord(
            obligation_type=obligation_type,
            description=description,
            sufficiency_notes=sufficiency_notes,
            lineage_refs=[]
        )
