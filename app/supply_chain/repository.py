from app.supply_chain.storage import SupplyChainStorage


class SupplyChainRepository:
    def __init__(self, storage: SupplyChainStorage):
        self.storage = storage

    # Wrapper methods to abstract storage interactions
    def store_source_snapshot(self, snap):
        self.storage.save_source(snap)

    def fetch_source_snapshot(self, id):
        return self.storage.get_source(id)

    # ... similarly for others ...

    def store_dependency_snapshot(self, snap):
        self.storage.save_dependency(snap)

    def fetch_dependency_snapshot(self, id):
        return self.storage.get_dependency(id)

    def store_build_manifest(self, manifest):
        self.storage.save_build(manifest)

    def fetch_build_manifest(self, id):
        return self.storage.get_build(id)

    def store_attestation(self, att):
        self.storage.save_attestation(att)

    def fetch_attestations(self, build_id):
        return self.storage.get_attestations(build_id)

    def store_reproducibility(self, repro):
        self.storage.save_reproducibility(repro)

    def fetch_reproducibility(self, id):
        return self.storage.get_reproducibility(id)

    def store_runtime_eq(self, eq):
        self.storage.save_runtime_eq(eq)

    def fetch_runtime_eq(self, id):
        return self.storage.get_runtime_eq(id)
