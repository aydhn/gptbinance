from enum import Enum

class CollateralClass(str, Enum):
    LIQUID = "liquid"
    ILLIQUID = "illiquid"
    VOLATILE = "volatile"
    INELIGIBLE_DISGUISED = "ineligible_disguised"

class EligibilityClass(str, Enum):
    ELIGIBLE = "eligible"
    CONDITIONALLY_ELIGIBLE = "conditionally_eligible"
    INELIGIBLE = "ineligible"

class ValuationClass(str, Enum):
    FRESH = "fresh"
    AGING = "aging"
    STALE = "stale"
    MANIPULATED = "manipulated"

class PerfectionClass(str, Enum):
    PERFECTED = "perfected"
    PARTIALLY_PERFECTED = "partially_perfected"
    UNPERFECTED = "unperfected"
    STALE_PERFECTION = "stale_perfection"

class LiquidationClass(str, Enum):
    VALID = "valid"
    PARTIAL = "partial"
    WRONGFUL = "wrongful"
    AUTHORITY_DEFECTIVE = "authority_defective"

class TrustVerdictType(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
