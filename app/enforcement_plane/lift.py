from typing import List

def check_enforcement_lift_assurance(assurance_record) -> List[str]:
    cautions = []
    if assurance_record.expiry and assurance_record.expiry.is_expired:
        cautions.append("lift granted on expired certificate explicit caution")
    return cautions

def grant_enforcement_lift_accountability(lift_id: str, accountable_approval_chain: str = None):
    if not accountable_approval_chain:
        return {'status': 'caution', 'message': 'Lift granted without accountable approval chain.'}
    return {'status': 'success'}
