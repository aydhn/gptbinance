def check_scenario_provenance(compare_id: str, realized_trace: bool) -> str:
    if not realized_trace:
        return 'CAUTION: scenario compare without realized provenance trace'
    return 'TRUSTED'
