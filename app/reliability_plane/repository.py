from .budgets import ErrorBudgetManager
from .objectives import ReliabilityObjectiveManager
from .quality import QualityAnalyzer
from .registry import CanonicalReliabilityRegistry
from .services import ReliabilityServiceManager
from .slis import SliManager
from .slos import SloManager
from .storage import StorageAdapter
from .trust import TrustManager


class ReliabilityRepository:
    def __init__(self, storage_path: str = "/tmp/reliability_plane"):
        self.storage = StorageAdapter(storage_path)
        self.registry = CanonicalReliabilityRegistry()
        self.services = ReliabilityServiceManager(self.registry)
        self.objectives = ReliabilityObjectiveManager(self.registry)
        self.slis = SliManager(self.registry)
        self.slos = SloManager(self.registry)
        self.budgets = ErrorBudgetManager()
        self.quality = QualityAnalyzer(self.registry, self.budgets)
        self.trust = TrustManager(self.registry, self.quality)

        # In a complete implementation, this would load from storage on init
        # and trigger saves on modifications.
