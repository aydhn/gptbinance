from enum import Enum

class SecurityClass(Enum):
    ESCROW = "escrow"
    RESERVE = "reserve"
    HOLDBACK = "holdback"
    COLLATERAL = "collateral"
    GUARANTEE = "guarantee"
    SUPPORT = "support"

class SecuredObligationClass(Enum):
    FULLY_SECURED = "fully_secured"
    PARTIALLY_SECURED = "partially_secured"
    CONTINGENT = "contingent"
    UNDER_SECURED = "under_secured"
    UNSECURED_MASQUERADE = "unsecured_masquerade"

class CollateralClass(Enum):
    PLEDGED = "pledged"
    FLOATING = "floating"
    IMPAIRED = "impaired"
    DUPLICATE_PLEDGED = "duplicate_pledged"
    PHANTOM = "phantom"

class GuaranteeClass(Enum):
    CAPPED = "capped"
    UNCAPPED_LIKE = "uncapped_like"
    CONDITIONAL = "conditional"
    DENIAL_PRONE = "denial_prone"

class FundingClass(Enum):
    FULLY_FUNDED = "fully_funded"
    PARTIALLY_FUNDED = "partially_funded"
    UNFUNDED = "unfunded"
    IN_TRANSIT = "in_transit"

class DrawClass(Enum):
    IMMEDIATE = "immediate"
    CONDITIONAL = "conditional"
    DISPUTED = "disputed"
    BLOCKED = "blocked"

class ReleaseClass(Enum):
    PARTIAL = "partial"
    FULL = "full"
    BLOCKED = "blocked"
    WRONGFUL = "wrongful"

class ImpairmentClass(Enum):
    COLLATERAL_IMPAIRMENT = "collateral_impairment"
    LEGAL_IMPAIRMENT = "legal_impairment"
    DRAWABILITY_IMPAIRMENT = "drawability_impairment"
    HIDDEN_IMPAIRMENT = "hidden_impairment"

class PriorityClass(Enum):
    FIRST = "first"
    PARI_LIKE = "pari_like"
    SUBORDINATED = "subordinated"
    CONTESTED = "contested"

class ExhaustionClass(Enum):
    FULLY_EXHAUSTED = "fully_exhausted"
    PARTIALLY_EXHAUSTED = "partially_exhausted"
    NOT_EXHAUSTED = "not_exhausted"
    FALSELY_EXHAUSTED = "falsely_exhausted"

class SecurityEquivalenceVerdict(Enum):
    EQUIVALENT = "equivalent"
    PARTIALLY_EQUIVALENT = "partially_equivalent"
    DIVERGENT = "divergent"
    UNVERIFIABLE = "unverifiable"

class SecurityTrustVerdict(Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
