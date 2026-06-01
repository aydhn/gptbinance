from typing import List

def check_authority_assurance(assurance_record) -> List[str]:
    cautions = []
    if not assurance_record.certifications:
        cautions.append("assurance action by actor lacking certification authority explicit caution")
    return cautions

def duty_bearing_approval_accountability(approval_id: str, accountable_duty: str = None):
    if not accountable_duty:
        return {'status': 'caution', 'message': 'Approval action detached from accountable duty.'}
    return {'status': 'success'}
