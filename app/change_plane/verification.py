def verify_change_provenance(change_id: str, provenance_refs: list) -> str:
    if not provenance_refs:
        return 'CAUTION: verified change without attributable lineage'
    return 'TRUSTED'
