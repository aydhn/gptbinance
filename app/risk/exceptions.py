class RiskError(Exception):
    """Base exception for risk-related errors."""

    pass


class InvalidRiskConfigError(RiskError):
    pass


class SizingError(RiskError):
    pass


class ExposureAccountingError(RiskError):
    pass


class RiskVetoError(RiskError):
    pass


class DrawdownBrakeError(RiskError):
    pass


class KillSwitchError(RiskError):
    pass


class PolicyViolationError(RiskError):
    pass
