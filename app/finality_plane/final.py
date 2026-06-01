from typing import List

def check_finality_assurance(assurance_record) -> List[str]:
    cautions = []
    if assurance_record.expiry and assurance_record.expiry.is_expired:
        cautions.append("final label under stale or degraded assurance explicit caution")
    return cautions
