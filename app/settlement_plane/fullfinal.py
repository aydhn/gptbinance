from typing import List

def check_settlement_assurance(assurance_record) -> List[str]:
    cautions = []
    if assurance_record.revocations:
        cautions.append("full-final asserted while assurance revocable explicit caution")
    return cautions
