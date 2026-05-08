class LedgerPlaneError(Exception):
    pass


class InvalidLedgerEntry(LedgerPlaneError):
    pass


class InvalidBalanceState(LedgerPlaneError):
    pass


class InvalidCollateralState(LedgerPlaneError):
    pass


class InvalidTransferRecord(LedgerPlaneError):
    pass


class CashflowAttributionError(LedgerPlaneError):
    pass


class DivergenceError(LedgerPlaneError):
    pass


class EquivalenceError(LedgerPlaneError):
    pass


class TrustVerdictError(LedgerPlaneError):
    pass


class LedgerStorageError(LedgerPlaneError):
    pass
