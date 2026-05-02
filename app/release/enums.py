from enum import Enum

class ReleaseStage(str, Enum):
    ALPHA = "alpha"
    BETA = "beta"
    RC = "rc"
    PRODUCTION = "production"

class BundleType(str, Enum):
    FULL = "full"
    PATCH = "patch"
    CONFIG_ONLY = "config_only"

class CompatibilityVerdict(str, Enum):
    COMPATIBLE = "compatible"
    MIGRATION_REQUIRED = "migration_required"
    INCOMPATIBLE = "incompatible"

class MigrationDirection(str, Enum):
    UPGRADE = "upgrade"
    DOWNGRADE = "downgrade"

class MigrationSeverity(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    DESTRUCTIVE = "destructive"

class InstallVerdict(str, Enum):
    PASS = "pass"
    CAUTION = "caution"
    FAIL = "fail"

class UpgradeVerdict(str, Enum):
    PASS = "pass"
    CAUTION = "caution"
    FAIL = "fail"

class RollbackVerdict(str, Enum):
    PASS = "pass"
    CAUTION = "caution"
    FAIL = "fail"

class HostReadiness(str, Enum):
    READY = "ready"
    CAUTION = "caution"
    UNREADY = "unready"

class DependencyStatus(str, Enum):
    SYNCED = "synced"
    DRIFT_DETECTED = "drift_detected"
    MISSING_REQUIRED = "missing_required"
