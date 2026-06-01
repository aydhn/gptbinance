from typing import List

def check_epistemic_assurance(assurance_record) -> List[str]:
    cautions = []
    if not assurance_record.cases:
        cautions.append("assurance-sounding claim without claim/evidence/surveillance basis explicit caution")
    return cautions
