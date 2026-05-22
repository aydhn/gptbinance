from app.commitment_plane.models import ConditionRecord

class ConditionManager:
    @staticmethod
    def create_condition(condition_type: str, description: str, proof_notes: str = None) -> ConditionRecord:
        valid_types = ['activation', 'discharge', 'relief', 'invalidation']
        if condition_type not in valid_types:
            raise ValueError(f"Invalid condition type. Must be one of {valid_types}")

        return ConditionRecord(
            condition_type=condition_type,
            description=description,
            proof_notes=proof_notes,
            lineage_refs=[]
        )
