from enum import Enum, auto


class ArtefactType(Enum):
    POLICY_DECISION = auto()
    READINESS_MEMO = auto()
    ACTIVATION_INTENT = auto()
    ACTIVATION_HISTORY = auto()
    INCIDENT_SNAPSHOT = auto()
    CONTAINMENT_PLAN = auto()
    POSTMORTEM_REPORT = auto()
    CAPA_RECORD = auto()
    REMEDIATION_PACK = auto()
    MIGRATION_PLAN = auto()
    MARKET_TRUTH_EVIDENCE = auto()
    SHADOW_DRIFT_FINDING = auto()
    ORDER_LIFECYCLE_SUMMARY = auto()
    CROSS_BOOK_OVERLAY = auto()
    CAPITAL_POSTURE = auto()
    EXPERIMENT_PACK = auto()
    DECISION_QUALITY_FINDING = auto()
    RELIABILITY_SCORECARD = auto()
    QUALIFICATION_OUTPUT = auto()
    GOVERNANCE_PROMOTION = auto()
    RELEASE_MANIFEST = auto()
    UNKNOWN = auto()


class RelationType(Enum):
    DERIVED_FROM = auto()
    CITES = auto()
    BLOCKS = auto()
    SUPPORTS = auto()
    SUPERSEDES = auto()
    DEPENDS_ON = auto()
    TRIGGERED = auto()
    LED_TO = auto()
    INCLUDED_IN = auto()
    INVALIDATED_BY = auto()
    REVIEWED_BY = auto()
    PROMOTED_FROM = auto()
    REVERTED_TO = auto()
    EXPLAINS = auto()
    FOLLOWS_INCIDENT = auto()
    ADDRESSES = auto()
    MITIGATES = auto()


class QueryClass(Enum):
    BY_ARTEFACT = auto()
    BY_SYMBOL = auto()
    BY_PROFILE = auto()
    BY_WORKSPACE = auto()
    BY_CANDIDATE = auto()
    BY_INCIDENT = auto()
    BY_TIME_WINDOW = auto()


class TraversalClass(Enum):
    BACKWARD = auto()
    FORWARD = auto()


class CaseFileClass(Enum):
    CANDIDATE_READINESS_CASE = auto()
    ACTIVATION_PROBATION_CASE = auto()
    INCIDENT_CASE = auto()
    POSTMORTEM_CASE = auto()
    REMEDIATION_CASE = auto()
    MIGRATION_CASE = auto()
    POLICY_CONFLICT_CASE = auto()
    RELIABILITY_DEGRADATION_CASE = auto()


class CompletenessClass(Enum):
    COMPLETE = auto()
    PARTIAL = auto()
    MISSING_CRITICAL = auto()
    REDACTED = auto()


class RedactionClass(Enum):
    NONE = auto()
    RESTRICTED_SCOPE = auto()
    SENSITIVE_DATA = auto()
    MANUAL_OVERRIDE = auto()


class GraphGapSeverity(Enum):
    INFO = auto()
    WARNING = auto()
    CRITICAL = auto()


class ScopeClass(Enum):
    GLOBAL = auto()
    WORKSPACE = auto()
    PROFILE = auto()
    SYMBOL = auto()
    SESSION = auto()


class EvidenceGraphVerdict(Enum):
    PASS = auto()
    FAIL = auto()
    REQUIRES_REVIEW = auto()
