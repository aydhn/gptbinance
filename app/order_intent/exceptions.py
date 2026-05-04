class IntentCompilerError(Exception):
    pass


class InvalidHighLevelIntent(IntentCompilerError):
    pass


class VenueSemanticsError(IntentCompilerError):
    pass


class AccountModeMismatch(IntentCompilerError):
    pass


class PositionModeMismatch(IntentCompilerError):
    pass


class ReduceOnlyViolation(IntentCompilerError):
    pass


class BorrowRepayPlanningError(IntentCompilerError):
    pass


class MultiLegDependencyError(IntentCompilerError):
    pass


class CompilePolicyViolation(IntentCompilerError):
    pass


class PlanValidationError(IntentCompilerError):
    pass
