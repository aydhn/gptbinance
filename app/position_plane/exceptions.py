class PositionPlaneError(Exception):
    pass


class InvalidPositionLotError(PositionPlaneError):
    pass


class InvalidLifecycleTransitionError(PositionPlaneError):
    pass


class InvalidCostBasisStateError(PositionPlaneError):
    pass


class PnlAttributionError(PositionPlaneError):
    pass


class ExposureTruthError(PositionPlaneError):
    pass


class PositionDivergenceError(PositionPlaneError):
    pass


class EquivalenceError(PositionPlaneError):
    pass


class TrustVerdictError(PositionPlaneError):
    pass


class PositionStorageError(PositionPlaneError):
    pass
