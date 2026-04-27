class BinanceConnectorError(Exception):
    """Base exception for all Binance connector errors."""

    pass


class BinanceConfigError(BinanceConnectorError):
    """Raised when the connector is improperly configured."""

    pass


class BinanceConnectivityError(BinanceConnectorError):
    """Raised when there are network or connection issues with Binance."""

    pass


class BinanceMetadataParseError(BinanceConnectorError):
    """Raised when exchange metadata cannot be parsed or normalized."""

    pass


class BinanceAPIError(BinanceConnectorError):
    """Raised when the Binance API returns an error response."""

    def __init__(self, message: str, status_code: int = None, error_code: int = None):
        super().__init__(message)
        self.status_code = status_code
        self.error_code = error_code


class BinanceRateLimitError(BinanceAPIError):
    """Raised when a rate limit is exceeded."""

    pass
