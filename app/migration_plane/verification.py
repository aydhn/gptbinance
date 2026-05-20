def check_migration_provenance(migration_id: str, custody_gap: bool) -> str:
    if custody_gap:
        return 'TRUST_DEGRADED: migration verified under broken custody gap'
    return 'TRUSTED'
