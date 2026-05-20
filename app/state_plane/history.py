def check_state_transition_provenance(state_id: str, attributable_actor: str) -> str:
    if not attributable_actor:
        return 'ANOMALY: state change without attributable actor or cause'
    return 'TRUSTED'
