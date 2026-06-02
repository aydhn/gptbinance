class IncentivePlaneError(Exception):
    pass

class InvalidIncentiveObjectError(IncentivePlaneError):
    pass

class InvalidIncentiveSubjectError(IncentivePlaneError):
    pass

class InvalidBehavioralTargetError(IncentivePlaneError):
    pass

class InvalidRewardFormulaError(IncentivePlaneError):
    pass

class InvalidPenaltyTriggerError(IncentivePlaneError):
    pass

class InvalidClawbackError(IncentivePlaneError):
    pass

class IncentiveTheaterViolation(IncentivePlaneError):
    pass

class IncentiveStorageError(IncentivePlaneError):
    pass
