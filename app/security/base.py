from abc import ABC, abstractmethod

class SecurityProviderBase(ABC):
    @abstractmethod
    def initialize(self):
        pass
