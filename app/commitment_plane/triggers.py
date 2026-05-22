from app.commitment_plane.models import TriggerRecord

class TriggerManager:
    @staticmethod
    def create_trigger(trigger_type: str, description: str, ambiguity_notes: str = None) -> TriggerRecord:
        valid_types = ['incident', 'release', 'contract', 'policy']
        if trigger_type not in valid_types:
            raise ValueError(f"Invalid trigger type. Must be one of {valid_types}")

        return TriggerRecord(
            trigger_type=trigger_type,
            description=description,
            ambiguity_notes=ambiguity_notes,
            lineage_refs=[]
        )
