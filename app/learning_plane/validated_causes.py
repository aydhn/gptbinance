def check_validated_cause_provenance(cause_id: str, defensible_chain: bool) -> str:
    if not defensible_chain:
        return 'CAUTION: validated cause without defensible provenance chain'
    return 'TRUSTED'
