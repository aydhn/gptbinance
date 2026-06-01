from typing import List

def check_remedy_assurance(assurance_record) -> List[str]:
    cautions = []
    if assurance_record.caveats:
        cautions.append("remedy safe asserted under caveat-heavy assurance explicit caution")
    return cautions
