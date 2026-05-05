class ActivationControllerError(Exception):
    pass


class InvalidActivationIntent(ActivationControllerError):
    pass


class InvalidRolloutPlan(ActivationControllerError):
    pass


class ActiveSetConflictError(ActivationControllerError):
    pass


class ProbationEvaluationError(ActivationControllerError):
    pass


class ScopeViolationError(ActivationControllerError):
    pass


class RevertPlanningError(ActivationControllerError):
    pass


class BoardDecisionMismatchError(ActivationControllerError):
    pass


class ActivationPolicyViolation(ActivationControllerError):
    pass


class ActivationStorageError(ActivationControllerError):
    pass
