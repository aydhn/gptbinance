from typing import List

def check_normalization_assurance(assurance_record) -> List[str]:
    cautions = []
    if not assurance_record.cases or not any(c.is_complete for c in assurance_record.cases):
        cautions.append("full normal asserted without assurance case explicit caution")
    return cautions
