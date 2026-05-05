from app.migrations.enums import MigrationDomain

DOMAIN_DEFAULTS = {
    MigrationDomain.CONFIG: {"safe_window_days": 30},
    MigrationDomain.WORKSPACE: {"safe_window_days": 15},
    MigrationDomain.DATA_GOVERNANCE: {"safe_window_days": 7},
    MigrationDomain.UNIVERSE: {"safe_window_days": 1},
    MigrationDomain.POLICY_KERNEL: {
        "safe_window_days": 0
    },  # Immediate compliance needed
    MigrationDomain.LEDGER_METADATA: {"safe_window_days": 30},
    MigrationDomain.SHADOW_STATE: {"safe_window_days": 7},
    MigrationDomain.QUALIFICATION: {"safe_window_days": 15},
    MigrationDomain.KNOWLEDGE_CATALOG: {"safe_window_days": 60},
    MigrationDomain.REMEDIATION: {"safe_window_days": 14},
    MigrationDomain.RELEASE_MANIFEST: {"safe_window_days": 7},
}
