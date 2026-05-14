def evaluate_migration_precheck(migration_id: str):
    return {
        "migration_id": migration_id,
        "expected_platform_leverage_ref": "pl_lev_1",
        "cost_of_delay_ref": "cod_mig_1",
        "temporary_negative_externality_refs": ["ext_mig_1"],
        "status": "benefit_horizon_clear" # Migration without clear horizon block/caution
    }
