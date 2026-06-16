from enum import Enum

class IndemnityClass(str, Enum):
    WARRANTY_BREACH = "warranty_breach"
    RELIANCE_HARM = "reliance_harm"
    ATTESTATION_MISSTATEMENT = "attestation_misstatement"
    EFFECTUATION_FAILURE = "effectuation_failure"
    RELEASE_REGRESSION = "release_regression"
    MIGRATION_CLEANUP = "migration_cleanup"
    SUCCESSOR_RESIDUE = "successor_residue"
    SUNSET_GHOST_PATH = "sunset_ghost_path"
    FEDERATED_LOSS = "federated_loss"
    CROSS_PLANE_CLAIM_LOSS = "cross_plane_claim_loss"
    GENERIC = "generic"

class LossClass(str, Enum):
    FIRST_PARTY = "first_party"
    THIRD_PARTY = "third_party"

class IndemnitorClass(str, Enum):
    DIRECT = "direct"
    DELEGATED = "delegated"
    EXTERNAL = "external"
    SHADOW = "shadow"

class CoverageClass(str, Enum):
    BOUNDED = "bounded"
    PARTIAL = "partial"
    BROAD = "broad"
    HIDDEN_GAP = "hidden_gap"

class ExclusionClass(str, Enum):
    CLEAR = "clear"
    NARROW = "narrow"
    OVERBROAD = "overbroad"
    HIDDEN = "hidden"

class DefenseClass(str, Enum):
    DUTY_TO_DEFEND = "duty_to_defend"
    DUTY_TO_REIMBURSE = "duty_to_reimburse"
    NO_DUTY = "no_duty"
    SILENT = "silent"

class ReimbursementClass(str, Enum):
    VALID = "valid"
    PARTIAL = "partial"
    DENIED = "denied"
    COSMETIC = "cosmetic"

class NoticeClass(str, Enum):
    VALID = "valid"
    LATE = "late"
    DEFECTIVE = "defective"
    HIDDEN_TRAP = "hidden_trap"

class DebtClass(str, Enum):
    STALE_CLAIM = "stale_claim"
    NOTICE_TRAP = "notice_trap"
    DEFENSE_CONFLICT = "defense_conflict"
    REIMBURSEMENT_DRAG = "reimbursement_drag"
    ILLUSORY_COVERAGE = "illusory_coverage"

class EquivalenceVerdict(str, Enum):
    EQUIVALENT = "equivalent"
    PARTIAL = "partial"
    DIVERGENT = "divergent"

class TrustVerdict(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
