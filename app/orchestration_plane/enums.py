from enum import Enum

class OrchestrationClass(Enum):
    ASSURANCE_RESPONSE = "assurance_response_orchestration"
    IMMUNITY_GAP = "immunity_gap_orchestration"
    ADAPTATION_EXECUTION = "adaptation_execution_orchestration"
    DRIFT_RESPONSE = "drift_response_orchestration"
    NORMALIZATION_REENTRY = "normalization_reentry_orchestration"
    BENEFICIARY_PROTECTION = "beneficiary_protection_orchestration"
    CONTROL_STABILIZATION = "control_stabilization_orchestration"
    COMPLIANCE_RESPONSE = "compliance_response_orchestration"
    RELEASE_RECOVERY = "release_recovery_orchestration"
    MIGRATION_REPAIR = "migration_repair_orchestration"
    FEDERATED_ALIGNMENT = "federated_alignment_orchestration"
    CROSS_PLANE_SAFE_EXECUTION = "cross_plane_safe_execution_orchestration"

class IntentClass(Enum):
    PREVENTIVE = "preventive"
    CORRECTIVE = "corrective"
    CONTAINMENT = "containment"
    AMBIGUOUS = "ambiguous"

class PlanClass(Enum):
    READY = "ready"
    INCOMPLETE = "incomplete"
    STALE = "stale"
    NO_OP = "no_op"

class ActionClass(Enum):
    EXECUTABLE = "executable"
    ADVISORY = "advisory"
    BLOCKED = "blocked"
    SHADOW = "shadow"

class GateClass(Enum):
    READINESS = "readiness"
    POLICY = "policy"
    APPROVAL = "approval"
    BENEFICIARY_SAFETY = "beneficiary_safety"
    STALE = "stale"

class TrustVerdict(Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
