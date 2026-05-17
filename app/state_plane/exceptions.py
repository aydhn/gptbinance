class StatePlaneError(Exception):
    pass

class IllegalStateJumpError(StatePlaneError):
    pass

class SplitBrainError(StatePlaneError):
    pass

class GuardViolationError(StatePlaneError):
    pass
