class CostPlaneError(Exception):
    pass

class InvalidCostObjectError(CostPlaneError):
    pass

class InvalidBudgetDefinitionError(CostPlaneError):
    pass

class InvalidAllocationPolicyError(CostPlaneError):
    pass

class InvalidAmortizationRecordError(CostPlaneError):
    pass

class InvalidUnitEconomicsRecordError(CostPlaneError):
    pass

class BudgetViolationError(CostPlaneError):
    pass

class VarianceViolationError(CostPlaneError):
    pass

class OptimizationViolationError(CostPlaneError):
    pass

class CostStorageError(CostPlaneError):
    pass
