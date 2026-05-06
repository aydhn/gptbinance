from enum import Enum


class ReviewClass(str, Enum):
    POLICY_CONFLICT = "policy_conflict"
    BOARD_CONTRADICTION = "board_contradiction"
    ACTIVATION_EXPANSION = "activation_expansion"
    ACTIVATION_HALT = "activation_halt"
    INCIDENT_CONTAINMENT = "incident_containment"
    RECOVERY_READINESS = "recovery_readiness"
    POSTMORTEM_FINALIZE = "postmortem_finalize"
    CAPA_EFFECTIVENESS = "capa_effectiveness"
    MIGRATION_SCOPE = "migration_scope"
    MIGRATION_NON_REVERSIBLE = "migration_non_reversible"
    REMEDIATION_APPLY = "remediation_apply"
    EVIDENCE_PACK = "evidence_pack"
    RELEASE_HOLD = "release_hold"
    RELIABILITY_FREEZE = "reliability_freeze"


class QueueClass(str, Enum):
    INCIDENTS = "incidents"
    READINESS_BOARD = "readiness_board"
    ACTIVATION = "activation"
    MIGRATIONS = "migrations"
    REMEDIATION = "remediation"
    POSTMORTEMS = "postmortems"
    RELIABILITY = "reliability"
    RELEASE = "release"
    POLICY = "policy"
    GENERAL = "general"


class ReviewPriority(str, Enum):
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class SLASeverity(str, Enum):
    STRICT = "strict"
    STANDARD = "standard"
    RELAXED = "relaxed"


class AssignmentClass(str, Enum):
    REVIEWER = "reviewer"
    APPROVER = "approver"
    CONSULTED = "consulted"


class ChecklistVerdict(str, Enum):
    COMPLETED = "completed"
    INCOMPLETE = "incomplete"
    WAIVED = "waived"


class AdjudicationVerdict(str, Enum):
    APPROVE_FOR_NEXT_STEP = "approve_for_next_step"
    DENY = "deny"
    HOLD = "hold"
    NEEDS_ADDITIONAL_EVIDENCE = "needs_additional_evidence"
    ESCALATE = "escalate"
    RE_REVIEW_REQUIRED = "re_review_required"
    CONDITIONAL_APPROVAL = "conditional_approval"


class EscalationClass(str, Enum):
    SLA_BREACH = "sla_breach"
    CRITICAL_CONTRADICTION = "critical_contradiction"
    UNRESOLVED_HIGH_RISK = "unresolved_high_risk"
    STALE_EVIDENCE = "stale_evidence"
    SOD_CONFLICT = "sod_conflict"


class HandoffClass(str, Enum):
    INCOMPLETE_REVIEW = "incomplete_review"
    SHIFT_CHANGE = "shift_change"
    ESCALATION = "escalation"


class ReviewState(str, Enum):
    PENDING = "pending"
    ASSIGNED = "assigned"
    IN_PROGRESS = "in_progress"
    CHECKLIST_COMPLETED = "checklist_completed"
    ADJUDICATED = "adjudicated"
    ESCALATED = "escalated"
    CLOSED = "closed"
