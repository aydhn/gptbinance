from abc import ABC, abstractmethod

class ConstitutionRegistryBase(ABC):
    @abstractmethod
    def register(self, obj): pass

class PrecedenceEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, domain_a, domain_b, scope): pass

class VerdictSynthesisBase(ABC):
    @abstractmethod
    def synthesize(self, object_id, bundles, precedences): pass

class TrustEvaluatorBase(ABC):
    @abstractmethod
    def evaluate(self, final_verdict, equivalence, freshness): pass
