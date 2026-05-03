class LedgerError(Exception):
    pass


class InvalidLedgerAccountError(LedgerError):
    pass


class InvalidLedgerEntryError(LedgerError):
    pass


class PostingImbalanceError(LedgerError):
    pass


class ReconciliationError(LedgerError):
    pass


class CostBasisError(LedgerError):
    pass


class LotAssignmentError(LedgerError):
    pass


class ScopeMismatchError(LedgerError):
    pass


class ProvenanceError(LedgerError):
    pass


class BalanceExplainError(LedgerError):
    pass
