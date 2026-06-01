from typing import List

def check_authority_assurance(assurance_record) -> List[str]:
    cautions = []
    if not assurance_record.certifications:
        cautions.append("assurance action by actor lacking certification authority explicit caution")
    return cautions
