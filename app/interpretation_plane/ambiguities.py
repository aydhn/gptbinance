from app.interpretation_plane.models import InterpretationObject, AmbiguityRecord, ReadingRecord, CanonicalMeaningRecord
from app.interpretation_plane.exceptions import AmbiguityLaunderingViolation

def resolve_ambiguity(obj: InterpretationObject, ambiguity_id: str, canon: CanonicalMeaningRecord):
    ambiguity = obj.ambiguities.get(ambiguity_id)
    if not ambiguity:
        return

    if not obj.clarifications:
        raise AmbiguityLaunderingViolation(f"Cannot resolve ambiguity {ambiguity_id} into canon {canon.canon_id} without explicit clarification.")

    ambiguity.is_resolved = True
    ambiguity.resolution_ref = canon.canon_id
