from typing import List

def check_settlement_assurance(assurance_record) -> List[str]:
    cautions = []
    if assurance_record.revocations:
        cautions.append("full-final asserted while assurance revocable explicit caution")
    return cautions

def assert_full_final_accountability(settlement_id: str, restitution_owner_unclear: bool = True):
    if restitution_owner_unclear:
        return {'status': 'caution', 'message': 'Full-final closure while restitution owner unclear.'}
    return {'status': 'success'}
