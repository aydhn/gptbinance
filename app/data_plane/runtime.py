class RuntimeDataHooks:
    def __init__(self, active_release_bundle_ref: str = None):
        self.active_release_bundle_ref = active_release_bundle_ref

    def register_consumer(self, consumer_id: str):
        pass

    def check_schema_compatibility(self, schema_version: str):
        # Enforce release-specific data schema compatibility
        pass
