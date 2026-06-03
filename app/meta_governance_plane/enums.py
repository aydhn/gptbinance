from enum import Enum, auto

class MetaGovernanceClass(Enum):
    CANON_EVOLUTION = auto()
    RULE_SUPERSESSION = auto()
    DEPRECATION_CONTROL = auto()
    COMPATIBILITY_WINDOW = auto()
    GOVERNANCE_DEPENDENCY = auto()
    CONSTITUTIONAL_CONFLICT = auto()
    HISTORICAL_TRUTH_PRESERVATION = auto()
    SHADOW_CANON_DETECTION = auto()
    FEDERATED_RULE_ALIGNMENT = auto()
    EMERGENCY_PATCH_CONTROL = auto()
    RUNTIME_POLICY_ALIGNMENT = auto()
    CROSS_PLANE_CANON_INTEGRITY = auto()

class ProposalClass(Enum):
    NEW_CANON = auto()
    CANON_UPDATE = auto()
    HOTFIX = auto()
    DEPRECATION = auto()

class CanonClass(Enum):
    ACTIVE = auto()
    LEGACY = auto()
    STALE = auto()

class VersionClass(Enum):
    CURRENT = auto()
    SUPERSEDED = auto()
    HOTFIX = auto()
    ORPHANED = auto()

class SupersessionClass(Enum):
    SAFE = auto()
    PARTIAL = auto()
    INVALID = auto()
    SHADOW = auto()

class DeprecationClass(Enum):
    BOUNDED = auto()
    STAGED = auto()
    UNSAFE = auto()
    FAKE = auto()

class CompatibilityClass(Enum):
    BOUNDED = auto()
    OVERLONG = auto()
    CONFLICTING = auto()
    INFINITE = auto()

class MigrationClass(Enum):
    SAFE = auto()
    PARTIAL = auto()
    STALLED = auto()
    FALSE_CLAIM = auto()

class ConflictClass(Enum):
    DIRECT = auto()
    LATENT = auto()
    RESOLVED = auto()
    BURIED = auto()

class MetaGovernanceEquivalenceVerdict(Enum):
    EQUIVALENT = auto()
    PARTIALLY_EQUIVALENT = auto()
    DIVERGENT = auto()

class MetaGovernanceTrustVerdict(Enum):
    TRUSTED = auto()
    CAUTION = auto()
    DEGRADED = auto()
    BLOCKED = auto()
    REVIEW_REQUIRED = auto()
