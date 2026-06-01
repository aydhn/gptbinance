from typing import List

def check_revalidation_assurance(assurance_record) -> List[str]:
    cautions = []
    if not assurance_record.surveillance:
        cautions.append("immunity revalidated treated assured without assurance case explicit caution")
    return cautions
