class LiveRuntimeError(Exception):
    pass


class InvalidLiveSessionConfig(LiveRuntimeError):
    pass


class LiveStartGateViolation(LiveRuntimeError):
    pass


class CapitalCapViolation(LiveRuntimeError):
    pass


class FlattenError(LiveRuntimeError):
    pass


class RollbackError(LiveRuntimeError):
    pass


class AccountSyncError(LiveRuntimeError):
    pass


class LivePnlError(LiveRuntimeError):
    pass


class AuditError(LiveRuntimeError):
    pass
