from typing import List

def check_recovery_assurance(assurance_record) -> List[str]:
    cautions = []
    if not assurance_record.cases:
        cautions.append("recovery finalized treated assured closure without assurance evidence explicit caution")
    return cautions
