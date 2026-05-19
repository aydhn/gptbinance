class RegistryBase:
    pass


class BoundaryEvaluatorBase:
    def evaluate_boundary(self, boundary_id: str) -> bool:
        return True


class PortabilityEvaluatorBase:
    def evaluate_portability(self, portability_id: str) -> bool:
        return True


class TrustEvaluatorBase:
    def evaluate_trust(self) -> str:
        return "trusted"
