def check_activation_provenance(stage: str, provenance_refs: list) -> str:
    if not provenance_refs:
        return 'ANOMALY: stage transition succeeded but lineage incomplete'
    return 'TRUSTED'
