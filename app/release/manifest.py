class ReleaseManifest:
    def __init__(self):
        self.migration_lineage_refs = []
        self.required_migration_versions = {}
        self.compatibility_matrix_refs = []
