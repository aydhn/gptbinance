from enum import Enum

class SuspensionClass(str, Enum):
    INCIDENT_SUSPENSION = "incident_suspension"
    DRIFT_CONTROL_SUSPENSION = "drift_control_suspension"
    AUTONOMY_QUARANTINE = "autonomy_quarantine_suspension"
    ORCHESTRATION_HOLD = "orchestration_hold_suspension"
    BENEFICIARY_PROTECTION = "beneficiary_protection_suspension"
    RELEASE_FREEZE = "release_freeze_suspension"
    MIGRATION_HOLD = "migration_hold_suspension"
    POLICY_PAUSE = "policy_pause_suspension"
    EVIDENCE_GAP = "evidence_gap_suspension"
    FEDERATED_DISCONNECT = "federated_disconnect_suspension"
    CROSS_PLANE_PROTECTIVE = "cross_plane_protective_suspension"


class TriggerClass(str, Enum):
    INCIDENT_TRIGGER = "incident_trigger"
    EVIDENCE_GAP = "evidence_gap_trigger"
    AUTHORITY_TRIGGER = "authority_trigger"
    BENEFICIARY_PROTECTION = "beneficiary_protection_trigger"

class ScopeClass(str, Enum):
    NARROW = "narrow_scope"
    BROAD = "broad_scope"
    DISPUTED = "disputed_scope"
    LEAKING = "leaking_scope"

class FreezeClass(str, Enum):
    EXECUTION = "execution_freeze"
    CHANGE = "change_freeze"
    DECISION = "decision_freeze"
    DATA = "data_freeze"

class QuarantineClass(str, Enum):
    BOUNDED = "bounded_quarantine"
    POROUS = "porous_quarantine"
    BENEFICIARY_AWARE = "beneficiary_aware_quarantine"

class ResidualClass(str, Enum):
    APPROVED = "approved_residual"
    EMERGENCY = "emergency_residual"
    HIDDEN = "hidden_residual"
    EXCESSIVE = "excessive_residual"

class ResumptionClass(str, Enum):
    COMPLETE = "complete_resumption"
    PARTIAL = "partial_resumption"
    STALE = "stale_resumption"
    UNSAFE = "unsafe_resumption"

class TimeboxClass(str, Enum):
    BOUNDED = "bounded_timebox"
    RENEWABLE = "renewable_timebox"
    STALE = "stale_timebox"
    MISSING = "missing_timebox"

class DebtClass(str, Enum):
    STALE_HOLD = "stale_hold_debt"
    BYPASS = "bypass_debt"
    INDEFINITE = "indefinite_suspension_debt"
    LEAKAGE = "leakage_debt"
    SHADOW = "shadow_execution_debt"

class EquivalenceVerdict(str, Enum):
    EQUIVALENT = "equivalent"
    DIVERGENT = "divergent"

class TrustVerdict(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
