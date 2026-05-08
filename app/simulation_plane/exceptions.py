class SimulationPlaneError(Exception):
    pass


class InvalidSimulationDefinitionError(SimulationPlaneError):
    pass


class InvalidRunContractError(SimulationPlaneError):
    pass


class InvalidAssumptionManifestError(SimulationPlaneError):
    pass


class InvalidPartitionSchemeError(SimulationPlaneError):
    pass


class WalkForwardViolationError(SimulationPlaneError):
    pass


class OOSViolationError(SimulationPlaneError):
    pass


class CounterfactualMisuseError(SimulationPlaneError):
    pass


class EquivalenceError(SimulationPlaneError):
    pass


class SimulationStorageError(SimulationPlaneError):
    pass
