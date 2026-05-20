def check_assurance_evidence_provenance(evidence_id: str, provenance_broken: bool) -> str:
    if provenance_broken:
        return 'CAUTION: evidence trusted but provenance broken'
    return 'TRUSTED'
