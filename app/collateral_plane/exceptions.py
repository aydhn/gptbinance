class CollateralPlaneError(Exception):
    pass

class InvalidCollateralObjectError(CollateralPlaneError):
    pass

class InvalidEligibilityError(CollateralPlaneError):
    pass

class InvalidValuationError(CollateralPlaneError):
    pass

class InvalidPerfectionError(CollateralPlaneError):
    pass

class InvalidLiquidationError(CollateralPlaneError):
    pass

class CollateralTheaterViolationError(CollateralPlaneError):
    pass
