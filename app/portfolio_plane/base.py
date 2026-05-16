from abc import ABC, abstractmethod

class PortfolioRegistryBase(ABC):
    @abstractmethod
    def register_portfolio_object(self, obj):
        pass

class PrioritizationEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, context):
        pass

class SequencingEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, context):
        pass

class TrustEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, context):
        pass
