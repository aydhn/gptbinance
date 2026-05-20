def check_contract_runtime_provenance(observation_id: str, provenance_trace: list) -> str:
    if not provenance_trace:
        return 'CAUTION: runtime mismatch without provenance trace'
    return 'TRUSTED'
