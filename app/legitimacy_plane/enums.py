from enum import Enum

class LegitimacyClass(Enum):
    BENEFICIARY = "beneficiary"
    GOVERNANCE_BURDEN = "governance_burden"
    AUTONOMY_ACCEPTABILITY = "autonomy_acceptability"
    ORCHESTRATION_INTERVENTION = "orchestration_intervention"
    ACCOUNTABILITY_CONSEQUENCE = "accountability_consequence"
    ASSURANCE_REQUIREMENT = "assurance_requirement"
    RESILIENCE_DEGRADATION = "resilience_degradation"
    VIABILITY_AFFORDABILITY = "viability_affordability"
    FEDERATED_STAKEHOLDER = "federated_stakeholder"
    RIGHTS_AND_REMEDY = "rights_and_remedy"
    MANDATE_AND_SCOPE = "mandate_and_scope"
    CROSS_PLANE_LICENSE = "cross_plane_license"

class StakeholderClass(Enum):
    PRIMARY = "primary"
    SECONDARY = "secondary"
    VULNERABLE = "vulnerable"
    MISCLASSIFIED = "misclassified"

class JustificationClass(Enum):
    STRONG = "strong"
    WEAK = "weak"
    BURDEN_BLIND = "burden_blind"
    COSMETIC = "cosmetic"

class DisclosureClass(Enum):
    SUFFICIENT = "sufficient"
    PARTIAL = "partial"
    OVERLOADED = "overloaded"
    MISLEADING = "misleading"

class ConsultationClass(Enum):
    MEANINGFUL = "meaningful"
    NARROW = "narrow"
    SYMBOLIC = "symbolic"
    CAPTURED = "captured"

class ProportionalityClass(Enum):
    PROPORTIONAL = "proportional"
    STRAINED = "strained"
    DISPROPORTIONAL = "disproportional"
    HIDDEN_DISPROPORTIONALITY = "hidden_disproportionality"

class ContestabilityClass(Enum):
    ACCESSIBLE = "accessible"
    NARROW = "narrow"
    INACCESSIBLE = "inaccessible"
    FAKE = "fake"

class AcceptanceClass(Enum):
    STABLE = "stable"
    CONDITIONAL = "conditional"
    SILENT = "silent"
    FRAGILE = "fragile"

class DriftClass(Enum):
    SCOPE_DRIFT = "scope_drift"
    BURDEN_DRIFT = "burden_drift"
    REPRESENTATION_DRIFT = "representation_drift"

class EquivalenceVerdict(Enum):
    EQUIVALENT = "equivalent"
    DIVERGENT = "divergent"

class TrustVerdict(Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
