def check_security_provenance(claim_id: str, custody_gap: bool, ambiguous_attribution: bool) -> str:
    if custody_gap or ambiguous_attribution:
        return 'CAUTION: secure claim under custody gap or ambiguous attribution'
    return 'TRUSTED'
