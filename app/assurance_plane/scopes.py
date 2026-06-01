from app.assurance_plane.models import AssuranceScopeRecord

def create_scope(scope_id: str, assurance_id: str, boundaries: str) -> AssuranceScopeRecord:
    return AssuranceScopeRecord(
        scope_id=scope_id,
        assurance_id=assurance_id,
        boundaries=boundaries
    )
