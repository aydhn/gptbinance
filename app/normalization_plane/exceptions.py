
class NormalizationPlaneError(Exception): pass
class InvalidNormalizationObjectError(NormalizationPlaneError): pass
class PrematureReopenError(NormalizationPlaneError): pass
class HiddenResidualScarError(NormalizationPlaneError): pass
class InvalidLimitLiftError(NormalizationPlaneError): pass
