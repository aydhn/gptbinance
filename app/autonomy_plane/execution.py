def check_execution_provenance(autonomy_id: str, provenance_refs: list) -> str:
    if not provenance_refs:
        return 'CAUTION: execution exists but provenance chain incomplete'
    return 'TRUSTED'
