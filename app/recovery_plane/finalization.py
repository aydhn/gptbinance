from typing import List

def check_recovery_assurance(assurance_record) -> List[str]:
    cautions = []
    if not assurance_record.cases:
        cautions.append("recovery finalized treated assured closure without assurance evidence explicit caution")
    return cautions

def finalize_recovery_accountability(recovery_id: str, accountable_reviewer: str = None):
    if not accountable_reviewer:
        return {'status': 'caution', 'message': 'Recovery finalization marked safe without accountable reviewer.'}
    return {'status': 'success'}
