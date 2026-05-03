class UniverseError(Exception):
    """Base exception for universe module."""
    pass

class InvalidInstrumentMetadataError(UniverseError):
    pass

class SymbolNormalizationError(UniverseError):
    pass

class ExchangeFilterError(UniverseError):
    pass

class EligibilityEvaluationError(UniverseError):
    pass

class LiquidityEvaluationError(UniverseError):
    pass

class UniverseDiffError(UniverseError):
    pass

class LifecycleError(UniverseError):
    pass

class StaleMetadataError(UniverseError):
    pass

class ImpactAnalysisError(UniverseError):
    pass
