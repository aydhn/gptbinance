from app.environment_plane.models import EnvironmentObject, EnvironmentTrustVerdict

class EnvironmentRegistryBase:
    def register(self, env: EnvironmentObject) -> None:
        pass
    def get(self, environment_id: str) -> EnvironmentObject:
        pass

class ParityEvaluatorBase:
    def evaluate(self, env: EnvironmentObject) -> None:
        pass

class PromotionEvaluatorBase:
    def evaluate(self, env: EnvironmentObject) -> None:
        pass

class TrustEvaluatorBase:
    def evaluate(self, env: EnvironmentObject) -> EnvironmentTrustVerdict:
        pass
