from enum import Enum

class PostmortemClass(str, Enum):
    INCIDENT_FULL_RCA = "incident_full_rca"
    INCIDENT_LIGHTWEIGHT_REVIEW = "incident_lightweight_review"
    REPEATED_INCIDENT_FAMILY_REVIEW = "repeated_incident_family_review"
    RELEASE_FAILURE_POSTMORTEM = "release_failure_postmortem"
    WORKFLOW_FAILURE_POSTMORTEM = "workflow_failure_postmortem"
    CONTROL_FAILURE_POSTMORTEM = "control_failure_postmortem"
    DATA_INTEGRITY_POSTMORTEM = "data_integrity_postmortem"
    EXECUTION_LOSS_POSTMORTEM = "execution_loss_postmortem"
    STRATEGY_FAILURE_POSTMORTEM = "strategy_failure_postmortem"
    EXPERIMENT_FALSE_WINNER_POSTMORTEM = "experiment_false_winner_postmortem"
    RELIABILITY_DEBT_POSTMORTEM = "reliability_debt_postmortem"

class CauseClass(str, Enum):
    SYMPTOM = "symptom"
    PROXIMATE_CAUSE = "proximate_cause"
    ROOT_CAUSE = "root_cause"
    BROKEN_GUARD = "broken_guard"
    LATENT_CONDITION = "latent_condition"

class ContributorClass(str, Enum):
    PROCESS_GAP = "process_gap"
    AUTOMATION_GAP = "automation_gap"
    STALE_DEPENDENCY = "stale_dependency"
    MISSING_GATE = "missing_gate"
    HIDDEN_OVERRIDE = "hidden_override"
    ENVIRONMENT_DRIFT = "environment_drift"
    HUMAN_DECISION_ERROR = "human_decision_error"
    VERIFICATION_GAP = "verification_gap"

class ActionClass(str, Enum):
    CORRECTIVE = "corrective"
    PREVENTIVE = "preventive"

class VerificationClass(str, Enum):
    IMPLEMENTED = "implemented"
    EFFECTIVENESS = "effectiveness"
    NO_REGRESSION = "no_regression"
    QUIET_PERIOD = "quiet_period"
    FAILED = "failed"
    PARTIAL = "partial"
    PENDING = "pending"

class EffectivenessClass(str, Enum):
    OBSERVED_IMPROVEMENT = "observed_improvement"
    UNCHANGED_RECURRENCE_RISK = "unchanged_recurrence_risk"
    PARTIAL_MITIGATION_ONLY = "partial_mitigation_only"
    HIDDEN_SIDE_EFFECT_DETECTED = "hidden_side_effect_detected"

class DebtClass(str, Enum):
    OVERDUE = "overdue"
    DEFERRED = "deferred"
    ACCEPTED = "accepted"
    BLOCKED = "blocked"

class DebtInterestClass(str, Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

class RecurrenceClass(str, Enum):
    SAME_FAMILY = "same_family"
    ADJACENT_PATTERN = "adjacent_pattern"

class RecurrenceEscalationClass(str, Enum):
    ESCALATED = "escalated"
    UNCHANGED = "unchanged"
    REDUCED = "reduced"

class ClosureClass(str, Enum):
    READY = "ready"
    BLOCKED_ACTION_DEBT = "blocked_action_debt"
    BLOCKED_VERIFICATION = "blocked_verification"
    BLOCKED_INCIDENT_OPEN = "blocked_incident_open"
    BLOCKED_EVIDENCE = "blocked_evidence"
    CLOSED = "closed"

class EquivalenceVerdict(str, Enum):
    EQUIVALENT = "equivalent"
    PARTIAL_EQUIVALENT = "partial_equivalent"
    DIVERGENT = "divergent"

class TrustVerdict(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
