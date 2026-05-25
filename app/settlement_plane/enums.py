from enum import Enum

class SettlementClass(Enum):
    DISPUTE_RESOLUTION = "dispute_resolution"
    LIABILITY_RELEASE = "liability_release"
    RIGHTS_PRESERVING = "rights_preserving"
    ENFORCEMENT_LIFT = "enforcement_lift"
    REMEDY_EXECUTION = "remedy_execution"
    CONTRACT_BREACH = "contract_breach"
    COMPLIANCE_RESOLUTION = "compliance_resolution"
    FINALITY_REOPENABLE = "finality_reopenable"
    AUTHORITY_DEFECT_CURE = "authority_defect_cure"
    FEDERATED_LOSS = "federated_loss"
    CUSTOMER_BENEFICIARY = "customer_beneficiary"
    CROSS_PLANE_CLOSURE = "cross_plane_closure"

class ReleaseClass(Enum):
    FULL = "full"
    PARTIAL = "partial"
    CLAIM_SPECIFIC = "claim_specific"
    DEFECTIVE = "defective"

class ReservationClass(Enum):
    EXPRESS = "express"
    SURVIVAL = "survival"
    FUTURE_CLAIM = "future_claim"
    AMBIGUOUS = "ambiguous"

class CarveOutClass(Enum):
    CLAIM = "claim"
    BENEFICIARY = "beneficiary"
    REGULATORY = "regulatory"
    SECURITY = "security"

class ConsiderationClass(Enum):
    MONETARY = "monetary"
    NON_MONETARY = "non_monetary"
    MIXED = "mixed"
    INSUFFICIENT = "insufficient"

class PerformanceClass(Enum):
    STRUCTURED = "structured"
    INSTALLMENT = "installment"
    STAGED = "staged"
    VERIFIED = "verified"
    INCOMPLETE = "incomplete"

class ClosureClass(Enum):
    PARTIAL_ISSUE = "partial_issue"
    PARTIAL_CLAIMANT = "partial_claimant"
    PARTIAL_TEMPORAL = "partial_temporal"
    FULL_FINAL_SCOPE = "full_final_scope"
    FULL_FINAL_CARVEOUT = "full_final_carveout"
    PROVISIONAL = "provisional"

class DefaultClass(Enum):
    PAYMENT = "payment"
    PERFORMANCE = "performance"
    NOTICE = "notice"
    CURED = "cured"

class ReopenClass(Enum):
    ON_DEFAULT = "on_default"
    ON_FRAUD_DEFECT = "on_fraud_defect"
    DENIED = "denied"
    STALE = "stale"

class SurvivalClass(Enum):
    RIGHTS = "rights"
    DUTIES = "duties"
    REGULATORY = "regulatory"
    DISPUTE_PATH = "dispute_path"

class EquivalenceVerdict(Enum):
    EQUIVALENT = "equivalent"
    DIVERGENT = "divergent"
    UNVERIFIABLE = "unverifiable"

class TrustVerdict(Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
