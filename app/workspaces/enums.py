from enum import Enum

class WorkspaceType(str, Enum):
    RESEARCH = "research"
    TRADING = "trading"
    SECURITY = "security"
    TESTING = "testing"

class ProfileType(str, Enum):
    PAPER_DEFAULT = "paper_default"
    TESTNET_EXEC = "testnet_exec"
    SHADOW_RESEARCH = "shadow_research"
    CANARY_LIVE_CAUTION = "canary_live_caution"
    DERIVATIVES_TESTNET = "derivatives_testnet"
    SECURITY_RECOVERY_LAB = "security_recovery_lab"

class ContextStatus(str, Enum):
    ACTIVE = "active"
    STALE = "stale"
    ARCHIVED = "archived"
    PENDING_SWITCH = "pending_switch"

class BoundarySeverity(str, Enum):
    INFO = "info"
    WARNING = "warning"
    BLOCKER = "blocker"

class IsolationVerdict(str, Enum):
    ISOLATED = "isolated"
    CONTAMINATED = "contaminated"
    SUSPICIOUS = "suspicious"

class SwitchVerdict(str, Enum):
    ALLOWED = "allowed"
    CAUTION = "caution"
    DENIED = "denied"

class ScopeType(str, Enum):
    WORKSPACE = "workspace"
    PROFILE = "profile"
    GLOBAL = "global"

class ProfileSensitivity(str, Enum):
    LOW = "low"      # Paper, purely local
    MEDIUM = "medium"   # Testnet, shadow
    HIGH = "high"     # Live canary, real funds
    CRITICAL = "critical" # Security lab with root access

class WorkspaceReadiness(str, Enum):
    READY = "ready"
    NOT_READY = "not_ready"
    DEGRADED = "degraded"

class ContaminationSeverity(str, Enum):
    LOW = "low"       # Unused temp files mixed
    MEDIUM = "medium"    # Config overlap but same environment
    HIGH = "high"      # State or evidence mix between different environments
    CRITICAL = "critical"  # Live secret or state in paper/testnet
