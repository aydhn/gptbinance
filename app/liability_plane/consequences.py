from typing import List

def check_liability_assurance(assurance_record) -> List[str]:
    cautions = []
    if not assurance_record.cases or not any(c.is_complete for c in assurance_record.cases):
        cautions.append("liability consequence hidden behind false assurance explicit caution")
    return cautions
