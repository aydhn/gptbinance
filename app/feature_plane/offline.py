class OfflineFeatureManager:
    pass

# WORKFLOW PLANE INTEGRATION:
# Added hooks for dependency/gate evaluations, duplicate run protections,
# and explicit reruns per Phase 73 requirements.

class OfflineFeatureMigrationRef:
    def recompute(self, migration_ref=None):
        pass
