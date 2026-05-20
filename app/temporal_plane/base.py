from app.temporal_plane.models import TemporalObjectRef
import abc

class TemporalRegistryBase(abc.ABC):
    @abc.abstractmethod
    def register(self, t_obj, family): pass
    @abc.abstractmethod
    def get(self, t_id): pass

class FreshnessEvaluatorBase(abc.ABC):
    @abc.abstractmethod
    def evaluate_freshness(self, ref: TemporalObjectRef): pass

class OrderingEvaluatorBase(abc.ABC):
    @abc.abstractmethod
    def evaluate_ordering(self, ref: TemporalObjectRef): pass

class TrustEvaluatorBase(abc.ABC):
    @abc.abstractmethod
    def evaluate_trust(self, ref: TemporalObjectRef): pass
