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
