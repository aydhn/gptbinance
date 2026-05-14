from abc import ABC, abstractmethod

class CostRegistryBase(ABC):
    @abstractmethod
    def register_cost(self, cost_object) -> None:
        pass

    @abstractmethod
    def get_cost(self, cost_id: str):
        pass

class AllocationEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, allocation_policy, target_spend) -> list:
        pass

class ForecastEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, spend_history: list):
        pass

class TrustEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, metrics: dict):
        pass
