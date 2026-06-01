from typing import List

def check_baseline_assurance(assurance_record) -> List[str]:
    cautions = []
    if not assurance_record.surveillance:
        cautions.append("baseline stable treated assured without ongoing surveillance explicit caution")
    return cautions
