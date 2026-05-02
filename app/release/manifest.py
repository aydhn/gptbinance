from app.release.models import ReleaseManifest, ReleaseComponentRef
from app.release.versioning import VersionManager
from app.release.dependencies import DependencyManager

class ManifestGenerator:
    def __init__(self):
        self.version_manager = VersionManager()
        self.dependency_manager = DependencyManager()

    def create_manifest(self) -> ReleaseManifest:
        version = self.version_manager.get_current_version()
        deps = self.dependency_manager.get_lock_summary()
        return ReleaseManifest(
            version=version,
            dependency_lock=deps,
            components=[ReleaseComponentRef(name="core", version="1.0.0", checksum="abc")],
            supported_modes=["live", "paper", "testnet"],
            required_python_version=">=3.10",
            rollback_refs=[]
        )
