from enum import Enum

class EscrowClass(Enum):
    WATERFALL = "waterfall"
    COLLATERAL = "collateral"
    INSURANCE = "insurance"
    INDEMNITY = "indemnity"
    WARRANTY = "warranty"
    ADJUDICATED = "adjudicated"
    SUCCESSOR = "successor"
    SUNSET = "sunset"
    FEDERATED = "federated"
    CROSS_PLANE = "cross_plane"

class AssetClass(Enum):
    CASH = "cash"
    SECURITIES = "securities"
    MIXED = "mixed"

class ConditionClass(Enum):
    MILESTONE = "milestone"
    DOCUMENTARY = "documentary"
    ADJUDICATED = "adjudicated"

class InstructionClass(Enum):
    VALID = "valid"
    PARTIAL = "partial"
    FORGED = "forged"
    STALE = "stale"

class ReleaseClass(Enum):
    VALID = "valid"
    BLOCKED = "blocked"
    PREMATURE = "premature"
    AUTHORITY_DEFECTIVE = "authority_defective"

class DisputeClass(Enum):
    VALID = "valid"
    PARTIAL = "partial"
    IGNORED = "ignored"

class ExpiryClass(Enum):
    BOUNDED = "bounded"
    ROLLING = "rolling"
    SILENT = "silent"

class DebtClass(Enum):
    FAKE_SEGREGATION = "fake_segregation"
    STALE_EVIDENCE = "stale_evidence"
    DISPUTE_IGNORE = "dispute_ignore"
    RELEASE_DRIFT = "release_drift"
    REVERSAL_FAILURE = "reversal_failure"

class EquivalenceVerdict(Enum):
    EQUIVALENT = "equivalent"
    DIVERGENT = "divergent"

class TrustVerdict(Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
