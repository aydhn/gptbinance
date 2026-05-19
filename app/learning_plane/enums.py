from enum import Enum, auto

class LearningClass(Enum):
    INCIDENT_LEARNING = "incident_learning"
    NEAR_MISS_LEARNING = "near_miss_learning"
    RELEASE_LEARNING = "release_learning"
    CHANGE_FAILURE_LEARNING = "change_failure_learning"
    MIGRATION_LEARNING = "migration_learning"
    SCENARIO_MISS_LEARNING = "scenario_miss_learning"
    CONSTITUTIONAL_PRECEDENT_LEARNING = "constitutional_precedent_learning"
    CONTRACT_DRIFT_LEARNING = "contract_drift_learning"
    ENVIRONMENT_ROT_LEARNING = "environment_rot_learning"
    ASSURANCE_GAP_LEARNING = "assurance_gap_learning"
    OPERATING_MODEL_LEARNING = "operating_model_learning"
    CONTROL_HARDENING_LEARNING = "control_hardening_learning"
    VALUE_SURPRISE_LEARNING = "value_surprise_learning"
    DECISION_MISTAKE_LEARNING = "decision_mistake_learning"
    CONTINUITY_GAP_LEARNING = "continuity_gap_learning"
    SECURITY_BYPASS_LEARNING = "security_bypass_learning"

class SignalClass(Enum):
    EXPLICIT_FAILURE = "explicit_failure"
    NEAR_MISS = "near_miss"
    WEAK_ANOMALY = "weak_anomaly"
    AVOIDED_FAILURE = "avoided_failure"
    REPEATED_WORKAROUND = "repeated_workaround"
    POLICY_STRESS = "policy_stress"
    ASSURANCE_WEAKNESS = "assurance_weakness"

class OriginClass(Enum):
    INCIDENT = "incident"
    POSTMORTEM = "postmortem"
    SCENARIO_DIVERGENCE = "scenario_divergence"
    AUDIT = "audit"
    ASSURANCE = "assurance"
    OPERATOR_ESCALATION = "operator_escalation"
    RELEASE = "release"
    MIGRATION = "migration"
    CHANGE_REVIEW = "change_review"
    DECISION_REVIEW = "decision_review"

class OutcomeClass(Enum):
    LOSS = "loss"
    AVOIDED_LOSS = "avoided_loss"
    DEGRADED_BUT_SURVIVED = "degraded_but_survived"
    DELAYED_FAILURE = "delayed_failure"

class FailureClass(Enum):
    GOVERNANCE_FAILURE = "governance_failure"
    CONTRACT_FAILURE = "contract_failure"
    STATE_FAILURE = "state_failure"
    ENVIRONMENT_FAILURE = "environment_failure"
    HUMAN_PROCESS_FAILURE = "human_process_failure"
    COVERAGE_FAILURE = "coverage_failure"
    RECOVERY_FAILURE = "recovery_failure"

class FindingClass(Enum):
    DIRECT_FINDING = "direct_finding"
    SYSTEMIC_FINDING = "systemic_finding"
    CROSS_PLANE_FINDING = "cross_plane_finding"
    RECURRENCE_FINDING = "recurrence_finding"

class LessonClass(Enum):
    OPERATIONAL_LESSON = "operational_lesson"
    CONSTITUTIONAL_LESSON = "constitutional_lesson"
    TECHNICAL_HARDENING_LESSON = "technical_hardening_lesson"
    HUMAN_PROCESS_LESSON = "human_process_lesson"

class HardeningClass(Enum):
    CONTROL_HARDENING = "control_hardening"
    CONTRACT_HARDENING = "contract_hardening"
    WORKFLOW_HARDENING = "workflow_hardening"
    ENVIRONMENT_HARDENING = "environment_hardening"
    CONSTITUTIONAL_HARDENING = "constitutional_hardening"

class ValidationClass(Enum):
    ANTI_RECURRENCE_VALIDATION = "anti_recurrence_validation"
    GUARD_EFFECTIVENESS_VALIDATION = "guard_effectiveness_validation"
    SCENARIO_IMPROVED_VALIDATION = "scenario_improved_validation"
    FALSE_CONFIDENCE_DETECTION = "false_confidence_detection"

class RecurrenceClass(Enum):
    SAME_FAILURE = "same_failure"
    SIBLING_FAILURE = "sibling_failure"
    LESSON_BYPASS = "lesson_bypass"

class EquivalenceVerdict(Enum):
    EQUIVALENT = "equivalent"
    DIVERGENT = "divergent"
    UNKNOWN = "unknown"
    PARTIAL = "partial"

class TrustVerdict(Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"

class ReadinessClass(Enum):
    READY = "ready"
    NEEDS_REVIEW = "needs_review"
    NOT_READY = "not_ready"

class UncertaintyClass(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"

class AdoptionStatus(Enum):
    DOCUMENTED = "documented"
    ENFORCED = "enforced"
    VALIDATED = "validated"
    PARTIAL = "partial"
    STALE = "stale"
