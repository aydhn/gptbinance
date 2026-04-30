class ProductError(Exception):
    """Base exception for product domain errors."""
    pass


class UnsupportedProductType(ProductError):
    pass


class InvalidProductConfig(ProductError):
    pass


class LeverageModeError(ProductError):
    pass


class MarginModeError(ProductError):
    pass


class LiquidationModelError(ProductError):
    pass


class CarryCostError(ProductError):
    pass
