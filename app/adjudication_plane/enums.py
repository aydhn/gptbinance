from enum import Enum

class AdjudicationClass(Enum):
    INVESTIGATION_DISPOSITION = "investigation_disposition"
    OVERSIGHT_ESCALATION = "oversight_escalation"
    APPEAL_REMAND = "appeal_remand"
    SANCTION_BASIS = "sanction_basis"
    RIGHTS_AND_REMEDY = "rights_and_remedy"
    SUCCESSION_CONFLICT = "succession_conflict"
    SUNSET_RESIDUAL = "sunset_residual"
    LEGITIMACY_BURDEN = "legitimacy_burden"
    FEDERATED_CASE = "federated_case"
    CROSS_PLANE_BINDING = "cross_plane_binding"

class CaseClass(Enum):
    CLEAR = "clear"
    COMPOUND = "compound"
    PARTIAL = "partial"
    MALFORMED = "malformed"

class IssueClass(Enum):
    VALID_FRAME = "valid_frame"
    NARROW = "narrow"
    OVERBROAD = "overbroad"
    HIDDEN_EXCLUDED = "hidden_excluded"

class ProofClass(Enum):
    PREPONDERANCE = "preponderance"
    CLEAR_AND_CONVINCING = "clear_and_convincing"
    BEYOND_REASONABLE_GOVERNANCE_DOUBT = "beyond_reasonable_governance_doubt"
    HEIGHTENED_BENEFICIARY_PROTECTION = "heightened_beneficiary_protection"

class PanelClass(Enum):
    BALANCED = "balanced"
    MIXED = "mixed"
    CAPTURED = "captured"
    FIGUREHEAD = "figurehead"

class AdmissibilityClass(Enum):
    ADMITTED = "admitted"
    CONDITIONALLY_ADMITTED = "conditionally_admitted"
    EXCLUDED = "excluded"
    INCONSISTENT = "inconsistent"

class DeterminationClass(Enum):
    REASONED = "reasoned"
    PARTIAL = "partial"
    OPAQUE = "opaque"
    UNSUPPORTED = "unsupported"

class DispositionClass(Enum):
    BOUNDED = "bounded"
    MIXED = "mixed"
    DISPROPORTIONAL = "disproportional"
    AUTHORITY_DEFECTIVE = "authority_defective"

class DebtClass(Enum):
    REASONING_GAP = "reasoning_gap"
    CONFLICT = "conflict"
    DEFERRED_DISPOSITION = "deferred_disposition"
    AUTHORITY_DEFECT = "authority_defect"
    DISPROPORTIONALITY = "disproportionality"

class EquivalenceVerdict(Enum):
    EQUIVALENT = "equivalent"
    PARTIAL = "partial"
    DIVERGENT = "divergent"

class TrustVerdict(Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
