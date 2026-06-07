from abc import ABC, abstractmethod
from typing import List
from app.exception_plane.models import ExceptionObject

class ExceptionRegistryBase(ABC):
    @abstractmethod
    def register(self, obj: ExceptionObject): pass

class ExceptionEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, obj: ExceptionObject): pass
