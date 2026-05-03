from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseValidator(ABC):
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

class BaseEvaluator(ABC):
    @abstractmethod
    def evaluate(self, data: Any) -> Dict[str, Any]:
        pass

class BaseBuilder(ABC):
    @abstractmethod
    def build(self, data: Any) -> Any:
        pass
