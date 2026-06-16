
class WaterfallPlaneError(Exception): pass
class InvalidWaterfallObjectError(WaterfallPlaneError): pass
class InvalidClaimRankError(WaterfallPlaneError): pass
class InvalidProceedsPoolError(WaterfallPlaneError): pass
class InvalidReserveError(WaterfallPlaneError): pass
class InvalidDistributionError(WaterfallPlaneError): pass
class InvalidClawbackError(WaterfallPlaneError): pass
class WaterfallTheaterViolation(WaterfallPlaneError): pass
class WaterfallStorageError(WaterfallPlaneError): pass
