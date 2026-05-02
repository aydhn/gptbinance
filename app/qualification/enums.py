from enum import Enum


class QualificationScope(str, Enum):
    STRATEGY = "strategy"
    RISK = "risk"
    PORTFOLIO = "portfolio"
    EXECUTION = "execution"
    RELEASE = "release"
    SECURITY = "security"
    OBSERVABILITY = "observability"
    RESILIENCE = "resilience"
    CONTROL = "control"
    GOVERNANCE = "governance"
    SYSTEM_WIDE = "system_wide"


class QualificationProfile(str, Enum):
    PAPER_READY = "paper_ready"
    SHADOW_READY = "shadow_ready"
    TESTNET_EXEC_READY = "testnet_exec_ready"
    CANARY_LIVE_CAUTION_READY = "canary_live_caution_ready"
    DERIVATIVES_TESTNET_READY = "derivatives_testnet_ready"
    ANALYTICS_GOVERNANCE_READY = "analytics_governance_ready"
    SECURITY_RECOVERY_READY = "security_recovery_ready"
    FULL_LIVE = "full_live"  # Target state, usually blocked by default


class RequirementCriticality(str, Enum):
    CRITICAL = "critical"  # Must pass, cannot be waived for live
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class ScenarioType(str, Enum):
    GOLDEN_PATH = "golden_path"
    NEGATIVE_PATH = "negative_path"
    FORBIDDEN_ACTION = "forbidden_action"
    CONTRACT_VERIFICATION = "contract_verification"
    RECOVERY = "recovery"


class ContractSeverity(str, Enum):
    CRITICAL = "critical"
    WARNING = "warning"


class CertificationVerdict(str, Enum):
    PASS = "pass"
    CAUTION = "caution"
    FAIL = "fail"
    BLOCKED = "blocked"


class EvidenceStatus(str, Enum):
    COMPLETE = "complete"
    INCOMPLETE = "incomplete"
    MISSING = "missing"
    STALE = "stale"


class WaiverStatus(str, Enum):
    ACTIVE = "active"
    EXPIRED = "expired"
    REVOKED = "revoked"
    REJECTED = "rejected"


class EnvironmentReadiness(str, Enum):
    NOT_READY = "not_ready"
    PAPER_READY = "paper_ready"
    SHADOW_READY = "shadow_ready"
    TESTNET_READY = "testnet_ready"
    LIVE_CAUTION_READY = "live_caution_ready"
    LIVE_READY = "live_ready"


class GoNoGoVerdict(str, Enum):
    GO = "go"
    LIMITED_GO = "limited_go"
    CAUTION = "caution"
    NO_GO = "no_go"
    BLOCKED = "blocked"
