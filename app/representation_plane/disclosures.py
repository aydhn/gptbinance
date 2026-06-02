from typing import List

def check_representation_assurance(assurance_record) -> List[str]:
    cautions = []
    if not assurance_record.cases or not any(c.is_complete for c in assurance_record.cases):
        cautions.append("assured represented while evidence insufficient explicit caution")
    return cautions

def check_disclosure_accountability(disclosure_id: str, appeal_or_restitution_open: bool = True):
    if appeal_or_restitution_open:
        return {'status': 'caution', 'message': 'Accountability represented as complete while appeal or restitution open.'}
    return {'status': 'success'}
