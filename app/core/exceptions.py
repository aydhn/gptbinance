class StorageError(Exception):
    """Base exception for storage-related errors."""

    pass


class MarketDataStoreError(StorageError):
    """Raised when there is an error reading or writing market data."""

    pass
