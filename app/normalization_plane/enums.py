
from enum import Enum

class NormalizationClass(Enum):
    POST_RESOLUTION = "post_resolution"
    POST_RECAPITALIZATION = "post_recapitalization"
    CUSTOMER_SAFE_REOPEN = "customer_safe_reopen"
    SECURITY_HARDENING = "security_hardening"
    FULL_NORMAL = "full_normal"

class ReentryGateStatus(Enum):
    BLOCKED = "blocked"
    PROVISIONAL = "provisional"
    CLEARED = "cleared"
    STALE = "stale"

class AuthorizationClass(Enum):
    DOMAIN_SPECIFIC = "domain_specific"
    PROVISIONAL = "provisional"
    FULL = "full"
    DEFECTIVE = "defective"

class GuardrailClass(Enum):
    PERSISTENT = "persistent"
    TEMPORARY = "temporary"
    RETIRED = "retired"
    HIDDEN_REMOVAL = "hidden_removal"

class LimitLiftClass(Enum):
    STAGED = "staged"
    DOMAIN = "domain"
    PREMATURE = "premature"
    REVOKED = "revoked"

class ResidualScarClass(Enum):
    VISIBLE = "visible"
    BOUNDED = "bounded"
    HIDDEN = "hidden"
    ACCUMULATING = "accumulating"

class NormalizationTrustVerdict(Enum):
    TRUSTED = "trusted"
    CAUTION = "caution"
    DEGRADED = "degraded"
    BLOCKED = "blocked"
    REVIEW_REQUIRED = "review_required"
