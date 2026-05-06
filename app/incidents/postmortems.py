from .models import PostmortemSeed, IncidentRecord

class PostmortemBuilder:
    @staticmethod
    def seed(incident: IncidentRecord) -> PostmortemSeed:
        return PostmortemSeed(
            incident_id=incident.incident_id,
            summary=f"Incident {incident.incident_id} ({incident.severity.value})",
            trigger_chain=[s.type.value for s in incident.signals],
            frozen_evidence_refs=[snap.snapshot_id for snap in incident.snapshots],
            unresolved_questions=["What was the exact trigger?"],
            follow_up_seeds=["Review market truth threshold"]
        )
