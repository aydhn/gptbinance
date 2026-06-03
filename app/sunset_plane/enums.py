from enum import Enum

class SunsetClass(Enum):
    SERVICE_RETIREMENT_SUNSET = "service_retirement_sunset"
    POLICY_DECOMMISSION_SUNSET = "policy_decommission_sunset"
    AUTONOMY_RETIREMENT_SUNSET = "autonomy_retirement_sunset"
    ORCHESTRATION_SHUTDOWN_SUNSET = "orchestration_shutdown_sunset"
    ASSURANCE_SURFACE_RETIREMENT_SUNSET = "assurance_surface_retirement_sunset"
    STEWARDSHIP_TRANSFER_OR_RETIRE_SUNSET = "stewardship_transfer_or_retire_sunset"
    FEDERATED_DISCONNECT_SUNSET = "federated_disconnect_sunset"
    BENEFICIARY_EXIT_SUNSET = "beneficiary_exit_sunset"
    DATA_RETENTION_DELETION_SUNSET = "data_retention_deletion_sunset"
    CROSS_PLANE_SAFE_TERMINATION_SUNSET = "cross_plane_safe_termination_sunset"

class TriggerClass(Enum):
    VIABILITY_TRIGGER = "viability_trigger"
    LEGITIMACY_TRIGGER = "legitimacy_trigger"
    SECURITY_TRIGGER = "security_trigger"
    OBSOLESCENCE_TRIGGER = "obsolescence_trigger"

class CriteriaClass(Enum):
    SATISFIED_CRITERIA = "satisfied_criteria"
    MISSING_CRITERIA = "missing_criteria"
    CONTRADICTORY_CRITERIA = "contradictory_criteria"
    COSMETIC_CRITERIA = "cosmetic_criteria"

class DecommissionClass(Enum):
    READY_PLAN = "ready_plan"
    INCOMPLETE_PLAN = "incomplete_plan"
    STALE_PLAN = "stale_plan"
    UNSAFE_PLAN = "unsafe_plan"

class ArchiveClass(Enum):
    COMPLETE_ARCHIVE = "complete_archive"
    PARTIAL_ARCHIVE = "partial_archive"
    UNREADABLE_ARCHIVE = "unreadable_archive"
    FALSE_ARCHIVE_CLAIM = "false_archive_claim"

class DeletionClass(Enum):
    LAWFUL_DELETION = "lawful_deletion"
    SCOPED_DELETION = "scoped_deletion"
    OVERBROAD_DELETION = "overbroad_deletion"
    INCOMPLETE_DELETION = "incomplete_deletion"

class TombstoneClass(Enum):
    CORRECT_TOMBSTONE = "correct_tombstone"
    STALE_TOMBSTONE = "stale_tombstone"
    MISLEADING_TOMBSTONE = "misleading_tombstone"
    ZOMBIE_ENABLING_TOMBSTONE = "zombie_enabling_tombstone"

class ObligationClass(Enum):
    BOUNDED_RESIDUAL_OBLIGATION = "bounded_residual_obligation"
    CONTRACT_TAIL = "contract_tail"
    REMEDY_TAIL = "remedy_tail"
    HIDDEN_RESIDUAL_OBLIGATION = "hidden_residual_obligation"

class AfterlifeClass(Enum):
    OBLIGATION_FREE_CLOSURE = "obligation_free_closure"
    RESIDUAL_TAIL_AFTERLIFE = "residual_tail_afterlife"
    ZOMBIE_PRONE_AFTERLIFE = "zombie_prone_afterlife"

class SunsetEquivalenceVerdictEnum(Enum):
    EQUIVALENT = "equivalent"
    PARTIALLY_EQUIVALENT = "partially_equivalent"
    DIVERGENT = "divergent"
    BENEFICIARY_SENSITIVE_DIVERGENCE = "beneficiary_sensitive_divergence"

class SunsetTrustVerdictEnum(Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
