class CapitalGovernanceError(Exception):
    """Base exception for capital governance errors."""

    pass


class InvalidCapitalTierError(CapitalGovernanceError):
    """Raised when an invalid capital tier is referenced or requested."""

    pass


class InvalidTrancheDefinitionError(CapitalGovernanceError):
    """Raised when a tranche definition is invalid or inconsistent."""

    pass


class InvalidExposureBudgetError(CapitalGovernanceError):
    """Raised when an exposure budget is malformed."""

    pass


class EscalationPolicyViolationError(CapitalGovernanceError):
    """Raised when an escalation attempt violates the governance policy."""

    pass


class ScaleTransitionError(CapitalGovernanceError):
    """Raised when a scale up/down transition fails validation."""

    pass


class FreezePolicyError(CapitalGovernanceError):
    """Raised when operations are attempted during a capital freeze."""

    pass


class StaleEvidenceError(CapitalGovernanceError):
    """Raised when required capital evidence is stale or missing."""

    pass


class ScopeMismatchError(CapitalGovernanceError):
    """Raised when attempting cross-scope (workspace/profile) capital operations."""

    pass


class LossBudgetError(CapitalGovernanceError):
    """Raised when a hard loss budget is breached or misconfigured."""

    pass
