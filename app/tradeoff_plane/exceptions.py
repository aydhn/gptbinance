class TradeoffPlaneError(Exception):
    """Base exception for tradeoff plane errors."""
    pass

class InvalidTradeoffObjectError(TradeoffPlaneError):
    pass

class InvalidObjectiveDefinitionError(TradeoffPlaneError):
    pass

class InvalidBurdenRecordError(TradeoffPlaneError):
    pass

class InvalidSacrificeError(TradeoffPlaneError):
    pass

class InvalidExternalityMappingError(TradeoffPlaneError):
    pass

class DominanceViolationError(TradeoffPlaneError):
    pass

class HiddenBurdenShiftViolationError(TradeoffPlaneError):
    pass

class TradeoffStorageError(TradeoffPlaneError):
    pass

class NonCompensableViolationError(TradeoffPlaneError):
    pass
