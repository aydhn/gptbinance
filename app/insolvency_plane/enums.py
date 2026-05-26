from enum import Enum

class InsolvencyClass(str, Enum):
    SETTLEMENT_FAILURE_INSOLVENCY = "settlement_failure_insolvency"
    PERFORMANCE_SECURITY_EXHAUSTION_INSOLVENCY = "performance_security_exhaustion_insolvency"
    RECOVERY_SHORTFALL_INSOLVENCY = "recovery_shortfall_insolvency"
    CUSTOMER_MASS_IMPAIRMENT_INSOLVENCY = "customer_mass_impairment_insolvency"
    CONTRACT_CURE_FAILURE_INSOLVENCY = "contract_cure_failure_insolvency"
    COMPLIANCE_RESTITUTION_INSOLVENCY = "compliance_restitution_insolvency"
    FEDERATED_PARTNER_COLLAPSE_INSOLVENCY = "federated_partner_collapse_insolvency"
    MIGRATION_LOSS_INSOLVENCY = "migration_loss_insolvency"
    RELEASE_REGRESSION_LOSS_INSOLVENCY = "release_regression_loss_insolvency"
    LIABILITY_SPIRAL_INSOLVENCY = "liability_spiral_insolvency"
    CROSS_PLANE_ESTATE_INSOLVENCY = "cross_plane_estate_insolvency"
    RESTRUCTURING_PLAN_INSOLVENCY = "restructuring_plan_insolvency"

class DistressTriggerClass(str, Enum):
    CASH_FLOW_INSOLVENCY = "cash_flow_insolvency"
    BALANCE_SHEET_INSOLVENCY = "balance_sheet_insolvency"
    MASS_DEFAULT = "mass_default"
    REGULATORY_ACTION = "regulatory_action"
    COVENANT_BREACH = "covenant_breach"

class EstateClass(str, Enum):
    FORMED = "formed"
    INCOMPLETE = "incomplete"
    CONTAMINATED = "contaminated"
    LEAK_RISK = "leak_risk"

class ClaimClass(str, Enum):
    FILED = "filed"
    AMENDED = "amended"
    DISPUTED = "disputed"
    WITHDRAWN = "withdrawn"

class AdmissionClass(str, Enum):
    ALLOWED = "allowed"
    CONDITIONALLY_ALLOWED = "conditionally_allowed"
    DISALLOWED = "disallowed"
    PARTIALLY_ALLOWED = "partially_allowed"

class PriorityClass(str, Enum):
    STATUTORY_LIKE = "statutory_like"
    BENEFICIARY_PROTECTIVE = "beneficiary_protective"
    CONTESTED = "contested"

class StayClass(str, Enum):
    AUTOMATIC_LIKE = "automatic_like"
    SCOPED = "scoped"
    LIFTED = "lifted"
    VIOLATED = "violated"

class PlanClass(str, Enum):
    PROPOSED = "proposed"
    AMENDED = "amended"
    SUPPORTED = "supported"
    FAILED = "failed"

class ConfirmationClass(str, Enum):
    CONFIRMED = "confirmed"
    DENIED = "denied"
    PROVISIONAL = "provisional"
    STAYED = "stayed"

class LiquidationClass(str, Enum):
    ORDERLY = "orderly"
    DISTRESSED = "distressed"
    PARTIAL = "partial"
    LEAK_RISK = "leak_risk"

class EquivalenceVerdict(str, Enum):
    EQUIVALENT = "equivalent"
    PARTIAL_EQUIVALENT = "partial_equivalent"
    DIVERGED = "diverged"

class InsolvencyTrustVerdict(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
