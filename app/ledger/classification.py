from app.ledger.enums import MovementClass, LedgerEntryType


class MovementClassifier:
    @staticmethod
    def classify(entry_type: LedgerEntryType, amount: float) -> MovementClass:
        if entry_type in [LedgerEntryType.FEE]:
            return MovementClass.FEE_BURDEN
        elif entry_type in [LedgerEntryType.FUNDING]:
            return MovementClass.FUNDING_BURDEN
        elif entry_type in [LedgerEntryType.DEPOSIT]:
            return MovementClass.INFLOW
        elif entry_type in [LedgerEntryType.WITHDRAWAL]:
            return MovementClass.OUTFLOW
        return MovementClass.INTERNAL_TRANSFER
