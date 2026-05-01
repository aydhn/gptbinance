from app.governance.storage import GovernanceStorage
from app.governance.bundle_registry import BundleRegistry


class GovernanceRepository:
    def __init__(self, storage: GovernanceStorage, registry: BundleRegistry):
        self.storage = storage
        self.registry = registry

    def save_bundle(self, bundle):
        self.storage.save_bundle(bundle)
        self.registry.register(bundle)

    def get_bundle(self, bundle_id):
        return self.registry.get(bundle_id)

    def get_active_bundle(self):
        return self.registry.get_active_bundle()

    # Phase 22 Analytics hook
    def get_analytics_refs(self) -> dict:
        return {
            "active_bundle": self.get_active_bundle(),
            "candidate_lineage": [], # Mock
            "decay_reports": [], # Mock
            "promotion_reports": [] # Mock
        }
