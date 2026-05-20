from enum import Enum

class SemanticClass(str, Enum):
    BUSINESS_TERM = "business_term"
    ENTITY = "entity"
    METRIC = "metric"
    RISK = "risk"
    STATE_LABEL = "state_label"
    CONTRACT_FIELD = "contract_field"
    ENVIRONMENT_CLASS = "environment_class"
    INCIDENT_SEVERITY = "incident_severity"
    AUTONOMY_ACTION = "autonomy_action"
    CONSTITUTIONAL_VERDICT = "constitutional_verdict"
    COMPLIANCE_OBLIGATION = "compliance_obligation"
    TEMPORAL_WINDOW = "temporal_window"
    CROSS_PLANE_ONTOLOGY = "cross_plane_ontology"

class TermClass(str, Enum):
    CANONICAL = "canonical"
    OVERLOADED = "overloaded"
    DEPRECATED = "deprecated"
    LOCAL_JARGON = "local_jargon"

class EntityClass(str, Enum):
    CUSTOMER = "customer"
    TENANT = "tenant"
    ACCOUNT = "account"
    ORDER = "order"
    TRADE = "trade"
    POSITION = "position"

class MetricClass(str, Enum):
    BUSINESS = "business"
    RISK = "risk"
    PERFORMANCE = "performance"
    OPERATIONAL = "operational"

class UnitClass(str, Enum):
    CURRENCY = "currency"
    TIME = "time"
    RATE = "rate"
    PERCENTAGE = "percentage"
    BASIS_POINT = "basis_point"
    DIMENSIONLESS = "dimensionless"

class ThresholdClass(str, Enum):
    ALERT = "alert"
    BLOCKER = "blocker"
    ESCALATION = "escalation"
    POLICY = "policy"

class LabelClass(str, Enum):
    STATE = "state"
    SEVERITY = "severity"
    READINESS = "readiness"
    TRUST = "trust"

class AliasClass(str, Enum):
    SAFE = "safe"
    HISTORICAL = "historical"
    DANGEROUS = "dangerous"
    TRANSLATION = "translation"

class ConflictClass(str, Enum):
    SAME_NAME_DIFFERENT_MEANING = "same_name_different_meaning"
    ALIAS_CONFLICT = "alias_conflict"
    UNIT_CONFLICT = "unit_conflict"
    THRESHOLD_CONFLICT = "threshold_conflict"
    SEMANTIC_SPLIT_BRAIN = "semantic_split_brain"

class InterpretationClass(str, Enum):
    OPERATIONAL = "operational"
    POLICY = "policy"
    CONSTITUTIONAL = "constitutional"
    REPORTING = "reporting"

class EquivalenceVerdict(str, Enum):
    EQUIVALENT = "equivalent"
    PARTIAL = "partial"
    DIVERGENT = "divergent"
    UNKNOWN = "unknown"

class TrustVerdict(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
