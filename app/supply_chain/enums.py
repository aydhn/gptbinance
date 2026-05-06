from enum import Enum


class ArtifactClass(str, Enum):
    SOURCE_SNAPSHOT = "source_snapshot"
    DEPENDENCY_SNAPSHOT = "dependency_snapshot"
    BUILD_MANIFEST = "build_manifest"
    RELEASE_BUNDLE = "release_bundle"
    CANDIDATE_BUNDLE = "candidate_bundle"
    CONFIG_BUNDLE = "config_bundle"
    RUNTIME_SURFACE = "runtime_surface"


class SourceClass(str, Enum):
    GIT_COMMIT = "git_commit"
    GIT_TREE = "git_tree"
    DETACHED_SNAPSHOT = "detached_snapshot"


class DependencyClass(str, Enum):
    DIRECT = "direct"
    TRANSITIVE = "transitive"
    TOOLCHAIN = "toolchain"


class AttestationClass(str, Enum):
    BUILD_SYSTEM = "build_system"
    HUMAN_REVIEWER = "human_reviewer"
    SECURITY_SCANNER = "security_scanner"


class IntegrityVerdict(str, Enum):
    VERIFIED = "verified"
    MISMATCH = "mismatch"
    UNVERIFIABLE = "unverifiable"


class ReproducibilityClass(str, Enum):
    DETERMINISTIC = "deterministic"
    NON_DETERMINISTIC = "non_deterministic"
    UNTESTED = "untested"


class DriftSeverity(str, Enum):
    NONE = "none"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class TrustVerdict(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"


class RuntimeEquivalence(str, Enum):
    EQUIVALENT = "equivalent"
    PARTIAL = "partial"
    MISMATCH = "mismatch"
    UNKNOWN = "unknown"


class SupplyChainState(str, Enum):
    CLEAN = "clean"
    DRIFTED = "drifted"
    TAMPERED = "tampered"
    ORPHANED = "orphaned"
