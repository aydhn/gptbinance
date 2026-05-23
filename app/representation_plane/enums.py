from enum import Enum

class RepresentationClass(str, Enum):
    STATEMENT = "statement"
    DISCLOSURE = "disclosure"
    ATTESTATION = "attestation"
    NOTICE = "notice"
    ASSURANCE = "assurance"
    CERTIFICATION = "certification"

class ModiferClass(str, Enum):
    RESERVATION = "reservation"
    CAVEAT = "caveat"
    DISCLAIMER = "disclaimer"
    CLARIFICATION = "clarification"
    CORRECTION = "correction"
    RETRACTION = "retraction"

class AudienceClass(str, Enum):
    INTERNAL = "internal"
    BENEFICIARY = "beneficiary"
    REGULATOR = "regulator"
    PARTNER = "partner"

class MaterialityClass(str, Enum):
    MATERIAL = "material"
    NON_MATERIAL = "non_material"
    OMITTED_MATERIAL = "omitted_material"

class RelianceClass(str, Enum):
    REASONABLE = "reasonable"
    BOUNDED = "bounded"
    PROHIBITED = "prohibited"
    INDUCED = "induced"

class TrustVerdictEnum(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
