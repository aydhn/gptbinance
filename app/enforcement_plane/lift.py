from typing import List

def check_enforcement_lift_assurance(assurance_record) -> List[str]:
    cautions = []
    if assurance_record.expiry and assurance_record.expiry.is_expired:
        cautions.append("lift granted on expired certificate explicit caution")
    return cautions
