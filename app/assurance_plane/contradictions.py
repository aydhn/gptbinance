from app.assurance_plane.models import ContradictionRecord

def create_contradiction(contradiction_id: str, assurance_id: str, description: str, is_material: bool) -> ContradictionRecord:
    return ContradictionRecord(
        contradiction_id=contradiction_id,
        assurance_id=assurance_id,
        description=description,
        is_material=is_material,
        is_resolved=False
    )
