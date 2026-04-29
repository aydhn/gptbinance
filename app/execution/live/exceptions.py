class ExecutionError(Exception):
    pass


class InvalidExecutionConfig(ExecutionError):
    pass


class ExecutionGateViolation(ExecutionError):
    pass


class PretradeValidationError(ExecutionError):
    pass


class DuplicateClientOrderIdError(ExecutionError):
    pass


class OrderSubmissionError(ExecutionError):
    pass


class ReconciliationError(ExecutionError):
    pass


class UserStreamError(ExecutionError):
    pass


class CancelError(ExecutionError):
    pass


class ReplaceError(ExecutionError):
    pass
