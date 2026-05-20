def check_portability_provenance(verdict_id: str, portable_provenance: bool) -> str:
    if not portable_provenance:
        return 'BLOCKER/CAUTION: portable verdict without portable provenance'
    return 'TRUSTED'
