from enum import Enum


class SecretSourceType(str, Enum):
    ENV_VAR = "env_var"
    LOCAL_FILE = "local_file"
    KEYRING = "keyring"
    HARDCODED = "hardcoded"
    MISSING = "missing"


class SecretStatus(str, Enum):
    SAFE = "safe"
    UNSAFE = "unsafe"
    MISSING = "missing"
    UNUSED = "unused"


class BackupScope(str, Enum):
    FULL = "full"
    CONFIG_ONLY = "config_only"
    STATE_ONLY = "state_only"
    AUDIT_ONLY = "audit_only"


class BackupType(str, Enum):
    SNAPSHOT = "snapshot"
    ARCHIVE = "archive"


class RestoreVerdict(str, Enum):
    SAFE_TO_RESTORE = "safe_to_restore"
    CONFLICT_DETECTED = "conflict_detected"
    UNSAFE = "unsafe"
    DRY_RUN_SUCCESS = "dry_run_success"


class IntegritySeverity(str, Enum):
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"


class EvidenceStatus(str, Enum):
    VALID = "valid"
    TAMPER_SUSPECTED = "tamper_suspected"
    MISSING_LINK = "missing_link"


class RetentionClass(str, Enum):
    HOT = "hot"
    WARM = "warm"
    ARCHIVE = "archive"
    DISPOSABLE = "disposable"


class SecurityVerdict(str, Enum):
    PASS = "pass"
    WARN = "warn"
    FAIL = "fail"


class DRRehearsalVerdict(str, Enum):
    SUCCESS = "success"
    PARTIAL = "partial"
    FAIL = "fail"
