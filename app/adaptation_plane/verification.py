from typing import List

def check_adaptation_assurance(assurance_record) -> List[str]:
    cautions = []
    if not assurance_record.certifications:
        cautions.append("adaptation verified treated assured without assurance posture explicit caution")
    return cautions
