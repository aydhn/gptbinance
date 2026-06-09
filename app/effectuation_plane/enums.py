from enum import Enum

class EffectuationClass(Enum):
    STANDARD = "standard"
    ADJUDICATED = "adjudicated"
    CORRECTIVE = "corrective"

class OrderClass(Enum):
    EXECUTABLE = "executable"
    ADVISORY = "advisory"

class TargetClass(Enum):
    SYSTEM = "system"
    ACTOR = "actor"
    PROCESS = "process"

class DependencyClass(Enum):
    HARD = "hard"
    SOFT = "soft"

class ProofClass(Enum):
    CRYPTOGRAPHIC = "cryptographic"
    OBSERVABLE = "observable"
    ATTESTATION = "attestation"

class VerificationClass(Enum):
    CLEAN = "clean"
    LIMITED = "limited"
    CONFLICTED = "conflicted"
    FAKE = "fake"

class ComplianceClass(Enum):
    FULL = "full"
    SHAM = "sham"
    PAPER = "paper"

class RollbackClass(Enum):
    JUSTIFIED = "justified"
    HIDDEN = "hidden"

class DebtClass(Enum):
    SLIPPAGE = "slippage"
    SHAM_COMPLIANCE = "sham_compliance"
    VERIFICATION = "verification"
    RESIDUAL_TAIL = "residual_tail"

class EquivalenceVerdict(Enum):
    EQUIVALENT = "equivalent"
    DIVERGENT = "divergent"

class TrustVerdict(Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
