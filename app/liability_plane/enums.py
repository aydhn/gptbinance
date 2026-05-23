from enum import Enum

class LiabilityClass(str, Enum):
    INCIDENT_LIABILITY = "incident_liability"
    CONTRACT_BREACH_LIABILITY = "contract_breach_liability"
    CUSTOMER_HARM_LIABILITY = "customer_harm_liability"
    COMPLIANCE_BREACH_LIABILITY = "compliance_breach_liability"
    SECURITY_EVENT_LIABILITY = "security_event_liability"
    AUTONOMY_ERROR_LIABILITY = "autonomy_error_liability"
    RELEASE_FAILURE_LIABILITY = "release_failure_liability"
    MIGRATION_DEFECT_LIABILITY = "migration_defect_liability"
    AUTHORITY_MISUSE_LIABILITY = "authority_misuse_liability"
    FEDERATED_SHARED_LIABILITY = "federated_shared_liability"
    REMEDY_INSUFFICIENCY_LIABILITY = "remedy_insufficiency_liability"
    CROSS_PLANE_CONSEQUENCE_ALLOCATION_LIABILITY = "cross_plane_consequence_allocation_liability"
    OTHER = "other"

class ResponsibilityClass(str, Enum):
    PRIMARY = "primary"
    SUPERVISORY = "supervisory"
    PROCESS = "process"
    INSTITUTIONAL = "institutional"

class CulpabilityClass(str, Enum):
    INTENTIONAL = "intentional"
    RECKLESS = "reckless"
    NEGLIGENT = "negligent"
    NON_CULPABLE = "non_culpable"

class FaultClass(str, Enum):
    DIRECT = "direct"
    CONTROL = "control"
    PROCESS = "process"
    COMMUNICATION = "communication"

class NegligenceClass(str, Enum):
    ORDINARY = "ordinary"
    GROSS = "gross"
    REVIEW = "review"
    MITIGATION = "mitigation"

class StrictLiabilityClass(str, Enum):
    NO_FAULT = "no_fault"
    REGIME_IMPOSED = "regime_imposed"
    CUSTOMER_FACING = "customer_facing"

class CausationClass(str, Enum):
    DIRECT = "direct"
    PROXIMATE = "proximate"
    CONTRIBUTING = "contributing"
    SUPERSEDING = "superseding"

class ContributionClass(str, Enum):
    MATERIAL = "material"
    PARTIAL = "partial"
    DOWNSTREAM = "downstream"
    FEDERATED = "federated"

class SharedLiabilityClass(str, Enum):
    PROPORTIONED = "proportioned"
    UNEQUAL = "unequal"
    UNRESOLVED = "unresolved"

class JointLiabilityClass(str, Enum):
    JOINT_EXPOSURE = "joint_exposure"
    JOINT_REMEDY_BEARING = "joint_remedy_bearing"
    JOINT_WITH_RECOURSE = "joint_with_recourse"

class SeveralLiabilityClass(str, Enum):
    SEPARATE_EXPOSURE = "separate_exposure"
    APPORTIONED = "apportioned"
    BENEFICIARY_SPECIFIC = "beneficiary_specific"

class IndemnityClass(str, Enum):
    CONTRACTUAL = "contractual"
    SCOPED = "scoped"
    PARTIAL = "partial"
    FAILED = "failed"

class ExonerationClass(str, Enum):
    FULL = "full"
    PARTIAL = "partial"
    SCOPE_LIMITED = "scope_limited"
    INVALID = "invalid"

class LimitationClass(str, Enum):
    SCOPE = "scope"
    TEMPORAL = "temporal"
    BENEFICIARY = "beneficiary"
    REGIME = "regime"

class LiabilityCapClass(str, Enum):
    HARD_CAP = "hard_cap"
    BENEFICIARY_CAP = "beneficiary_cap"
    CONTRACT_CAP = "contract_cap"
    INVALID_CAP = "invalid_cap"

class ConsequenceClass(str, Enum):
    FINANCIAL = "financial"
    OPERATIONAL = "operational"
    GOVERNANCE = "governance"
    REPUTATIONAL = "reputational"

class CostBearerClass(str, Enum):
    DIRECT = "direct"
    SHARED = "shared"
    REIMBURSABLE = "reimbursable"
    PROVISIONAL = "provisional"

class DutyToMitigateClass(str, Enum):
    HARMED_PARTY = "harmed_party"
    OPERATOR = "operator"
    PARTNER = "partner"
    BREACHED = "breached"

class ResidualExposureClass(str, Enum):
    UNRESOLVED = "unresolved"
    POST_REMEDY = "post_remedy"
    CONTINGENT = "contingent"
    HIDDEN = "hidden"

class LiabilityState(str, Enum):
    ACTIVE = "active"
    CHALLENGED = "challenged"
    SETTLED = "settled"
    CAPPED = "capped"

class EquivalenceVerdict(str, Enum):
    EQUIVALENT = "equivalent"
    PARTIAL_DIVERGENCE = "partial_divergence"
    FULL_DIVERGENCE = "full_divergence"

class TrustVerdict(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
