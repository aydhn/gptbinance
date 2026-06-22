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
    CLEARING_SETTLEMENT = "clearing_settlement"
    NETTED_CASH_SETTLEMENT = "netted_cash_settlement"
    COLLATERAL_DELIVERY_SETTLEMENT = "collateral_delivery_settlement"
    INSURANCE_PAYOUT_SETTLEMENT = "insurance_payout_settlement"
    INDEMNITY_REIMBURSEMENT_SETTLEMENT = "indemnity_reimbursement_settlement"
    REMEDIAL_AWARD_SETTLEMENT = "remedial_award_settlement"
    SUCCESSOR_TRANSFER_SETTLEMENT = "successor_transfer_settlement"
    SUNSET_TAIL_SETTLEMENT = "sunset_tail_settlement"
    FEDERATED_SETTLEMENT_BRIDGE = "federated_settlement_bridge"
    CROSS_PLANE_FINAL_TRANSFER_SETTLEMENT = "cross_plane_final_transfer_settlement"

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

class InstructionClass(Enum):
    VALID_INSTRUCTION = "valid_instruction"
    PARTIAL_INSTRUCTION = "partial_instruction"
    STALE_INSTRUCTION = "stale_instruction"
    DUPLICATE_INSTRUCTION = "duplicate_instruction"

class MatchClass(Enum):
    CLEAN_MATCH = "clean_match"
    PARTIAL_MATCH = "partial_match"
    FALSE_MATCH = "false_match"

class FinalityClass(Enum):
    CLEAN_FINALITY = "clean_finality"
    CONDITIONAL_FINALITY = "conditional_finality"
    NON_FINAL_POSTURE = "non_final_posture"
    FALSE_FINALITY_CLAIM = "false_finality_claim"

class FailClass(Enum):
    EXPLICIT_FAIL = "explicit_fail"
    BOUNDED_FAIL = "bounded_fail"
    CHRONIC_FAIL = "chronic_fail"
    HIDDEN_FAIL = "hidden_fail"

class BuyInClass(Enum):
    VALID_BUY_IN = "valid_buy_in"
    PARTIAL_BUY_IN = "partial_buy_in"
    FAILED_BUY_IN = "failed_buy_in"
    COSMETIC_BUY_IN = "cosmetic_buy_in"

class ReversalClass(Enum):
    VALID_REVERSAL = "valid_reversal"
    PARTIAL_REVERSAL = "partial_reversal"
    FAILED_REVERSAL = "failed_reversal"
    HIDDEN_REVERSAL_GAP = "hidden_reversal_gap"

class DebtClass(Enum):
    SSI_DEBT = "ssi_debt"
    FAIL_DISCIPLINE_DEBT = "fail_discipline_debt"
    DUPLICATE_SETTLEMENT_DEBT = "duplicate_settlement_debt"
    FINALITY_DEBT = "finality_debt"
    REVERSAL_DEBT = "reversal_debt"

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
