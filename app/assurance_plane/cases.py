from app.assurance_plane.models import AssuranceCaseRecord

def create_assurance_case(case_id: str, assurance_id: str, claims: list, packs: list, sufficiencies: list, is_complete: bool) -> AssuranceCaseRecord:
    return AssuranceCaseRecord(
        case_id=case_id,
        assurance_id=assurance_id,
        claims=claims,
        packs=packs,
        sufficiencies=sufficiencies,
        is_complete=is_complete
    )
