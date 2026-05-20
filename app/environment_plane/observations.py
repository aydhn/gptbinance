def check_env_observation_provenance(observation_id: str, chain_of_custody: list) -> str:
    if not chain_of_custody:
        return 'CAUTION: environment anomaly without chain-of-custody'
    return 'TRUSTED'
