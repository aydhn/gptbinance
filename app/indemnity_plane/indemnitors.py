from app.indemnity_plane.models import IndemnitorRecord
def record_indemnitor(indemnity_id: str, indemnitor_class: str, identity: str) -> IndemnitorRecord:
    return IndemnitorRecord(indemnity_id=indemnity_id, indemnitor_class=indemnitor_class, identity=identity)
