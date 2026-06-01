from enum import Enum

class AdaptationClass(Enum):
    DRIFT_CORRECTION = "drift_correction"
    BENEFICIARY_HARM_REDUCTION = "beneficiary_harm_reduction"
    COMPLIANCE_REPAIR = "compliance_repair"
    SECURITY_HARDENING = "security_hardening"

class TriggerClass(Enum):
    DRIFT_TRIGGERED = "drift_triggered"
    INCIDENT_TRIGGERED = "incident_triggered"

class HypothesisClass(Enum):
    PRIMARY = "primary"
    COMPETING = "competing"

class CorrectiveClass(Enum):
    SCOPED = "scoped"
    MULTI_DOMAIN = "multi_domain"

class HardeningClass(Enum):
    STRUCTURAL = "structural"
    TEMPORARY = "temporary"

class RecalibrationClass(Enum):
    SAFE = "safe"
    COMPENSATORY = "compensatory"

class VerificationClass(Enum):
    SHORT = "short"
    MATURE = "mature"

class SideEffectClass(Enum):
    ACCEPTABLE = "acceptable"
    MATERIAL = "material"

class FitnessClass(Enum):
    BOUNDED = "bounded"
    PARTIAL = "partial"

class RenormalizationClass(Enum):
    ELIGIBLE = "eligible"
    DEFERRED = "deferred"

class EquivalenceVerdict(Enum):
    EQUIVALENT = "equivalent"
    DIVERGENT = "divergent"

class TrustVerdict(Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
