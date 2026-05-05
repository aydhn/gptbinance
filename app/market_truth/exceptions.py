class MarketTruthError(Exception):
    """Base exception for Market Truth layer."""

    pass


class InvalidSourceAdapterError(MarketTruthError):
    pass


class StaleFeedError(MarketTruthError):
    pass


class SequenceIntegrityError(MarketTruthError):
    pass


class GapDetectionError(MarketTruthError):
    pass


class DedupError(MarketTruthError):
    pass


class OrderingError(MarketTruthError):
    pass


class ConvergenceError(MarketTruthError):
    pass


class ClockDriftError(MarketTruthError):
    pass


class MarketTruthStorageError(MarketTruthError):
    pass
