def check_rollout_provenance(rollout_id: str, provenance_refs: list) -> str:
    if not provenance_refs:
        return 'BLOCKER/CAUTION: rollout anomaly without provenance chain'
    return 'TRUSTED'
