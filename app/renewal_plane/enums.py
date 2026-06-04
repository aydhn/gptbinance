from enum import Enum

class RenewalClass(Enum):
    MANDATE_RENEWAL = "mandate_renewal"
    AUTHORITY_REAUTHORIZATION = "authority_reauthorization"
    BENEFICIARY_SERVICE_RENEWAL = "beneficiary_service_renewal"
    AUTONOMY_GRANT_RENEWAL = "autonomy_grant_renewal"
    ORCHESTRATION_OWNER_RENEWAL = "orchestration_owner_renewal"
    ASSURANCE_SCOPE_RENEWAL = "assurance_scope_renewal"
    STEWARDSHIP_CHARTER_RENEWAL = "stewardship_charter_renewal"
    POLICY_RECHARTER_RENEWAL = "policy_recharter_renewal"
    FEDERATED_RELATIONSHIP_RENEWAL = "federated_relationship_renewal"
    SUNSET_OR_NONRENEWAL_DECISION = "sunset_or_nonrenewal_decision"
    SUCCESSION_COUPLED_RENEWAL = "succession_coupled_renewal"
    CROSS_PLANE_CONTINUED_OPERATION_RENEWAL = "cross_plane_continued_operation_renewal"

class TriggerClass(Enum):
    SCHEDULED_TRIGGER = "scheduled_trigger"
    EVIDENCE_TRIGGER = "evidence_trigger"
    BURDEN_TRIGGER = "burden_trigger"
    EMERGENCY_TRIGGER = "emergency_trigger"

class IntervalClass(Enum):
    FIXED_INTERVAL = "fixed_interval"
    CONDITIONAL_INTERVAL = "conditional_interval"
    STALE_INTERVAL = "stale_interval"
    AMBIGUOUS_INTERVAL = "ambiguous_interval"

class CriteriaClass(Enum):
    SUFFICIENT_CRITERIA = "sufficient_criteria"
    PARTIAL_CRITERIA = "partial_criteria"
    STALE_CRITERIA = "stale_criteria"
    COSMETIC_CRITERIA = "cosmetic_criteria"

class EvidenceFreshness(Enum):
    FRESH = "fresh"
    AGING = "aging"
    STALE = "stale"
    REUSED_WITHOUT_JUSTIFICATION = "reused_without_justification"

class ContinuationClass(Enum):
    FULL_RENEWAL = "full_renewal"
    EXTENSION = "extension"
    PROVISIONAL = "provisional"
    CONDITIONAL = "conditional"

class NonRenewalClass(Enum):
    BOUNDED_NON_RENEWAL = "bounded_non_renewal"
    SUNSET_COUPLED = "sunset_coupled"
    SUCCESSION_COUPLED = "succession_coupled"
    ZOMBIE_GAP = "zombie_gap"

class RenewalDriftClass(Enum):
    CRITERIA_DRIFT = "criteria_drift"
    BURDEN_DRIFT = "burden_drift"
    CADENCE_DRIFT = "cadence_drift"
    HIDDEN_DRIFT = "hidden_drift"

class RenewalDebtClass(Enum):
    STALE_EVIDENCE = "stale_evidence"
    INDEFINITE_EXTENSION = "indefinite_extension"
    CHECKBOX_RENEWAL = "checkbox_renewal"
    BURDEN_DRIFT = "burden_drift"
    CONTINUATION_WITHOUT_PROOF = "continuation_without_proof"

class EquivalenceVerdict(Enum):
    CLEAN = "clean"
    DIVERGENT = "divergent"
    UNVERIFIABLE = "unverifiable"

class TrustVerdict(Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
