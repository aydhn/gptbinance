class GovernanceError(Exception):
    """Base exception for governance related errors."""

    pass


class InvalidRefreshPlanError(GovernanceError):
    pass


class CandidateAssemblyError(GovernanceError):
    pass


class DecayEvaluationError(GovernanceError):
    pass


class PromotionReadinessError(GovernanceError):
    pass


class RollbackReferenceError(GovernanceError):
    pass


class StageTransitionError(GovernanceError):
    pass


class ActivationGuardViolation(GovernanceError):
    pass
