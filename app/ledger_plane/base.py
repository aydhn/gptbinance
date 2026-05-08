from typing import Dict, Any


class LedgerPlaneBase:
    pass


class EntryBuilderBase(LedgerPlaneBase):
    pass


class BalanceReducerBase(LedgerPlaneBase):
    pass


class CollateralEvaluatorBase(LedgerPlaneBase):
    pass


class TrustEvaluatorBase(LedgerPlaneBase):
    pass
