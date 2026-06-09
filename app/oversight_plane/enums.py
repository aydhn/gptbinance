from enum import Enum

class OversightClass(str, Enum):
    AUTHORITATIVE = "authoritative"
    LOCAL = "local"
    FEDERATED = "federated"
    BENEFICIARY = "beneficiary"

class SupervisorClass(str, Enum):
    DIRECT = "direct"
    EXTERNAL = "external"
    MIXED = "mixed"
    MISSING = "missing"

class TriggerClass(str, Enum):
    THRESHOLD = "threshold"
    EVENT = "event"
    AUDIT_CYCLE = "audit_cycle"
    BENEFICIARY_HARM = "beneficiary_harm"

class ScopeClass(str, Enum):
    FULL = "full"
    BOUNDED = "bounded"
    TRUNCATED = "truncated"
    HIDDEN_EXCLUDED = "hidden_excluded"

class ScrutinyClass(str, Enum):
    LIGHT = "light"
    FOCUSED = "focused"
    INTENSIVE = "intensive"
    FALSE_CLAIM = "false_claim"

class FindingClass(str, Enum):
    CLEAN = "clean"
    CAUTION = "caution"
    ADVERSE = "adverse"
    HIDDEN_SUPPRESSION = "hidden_suppression"

class MaterialityClass(str, Enum):
    IMMATERIAL = "immaterial"
    MATERIAL = "material"
    SEVERE = "severe"
    LAUNDERED = "laundered"

class InterventionClass(str, Enum):
    BINDING = "binding"
    ADVISORY = "advisory"
    WEAK = "weak"
    UNENFORCEABLE = "unenforceable"

class DebtClass(str, Enum):
    BACKLOG = "backlog"
    CAPTURE = "capture"
    BLINDSPOT = "blindspot"
    NON_ACTION = "non_action"
    PREMATURE_CLEARANCE = "premature_clearance"

class EquivalenceVerdictEnum(str, Enum):
    EQUIVALENT = "equivalent"
    PARTIAL = "partial"
    DIVERGENT = "divergent"

class TrustVerdictEnum(str, Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
