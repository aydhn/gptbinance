from app.release.models import ReleaseBundle
from app.release.manifest import ManifestGenerator
from app.release.checksums import ChecksumManager
from datetime import datetime, timezone
import os

class BundleGenerator:
    def __init__(self):
        self.manifest_gen = ManifestGenerator()
        self.checksum_mgr = ChecksumManager()

    def generate_bundle(self, output_dir: str) -> ReleaseBundle:
        manifest = self.manifest_gen.create_manifest()
        bundle_path = os.path.join(output_dir, f"bundle_{manifest.version.version}.tar.gz")
        # Simulate bundle creation
        with open(bundle_path, "w") as f:
            f.write("mock bundle data")

        checksum = self.checksum_mgr.generate_checksum(bundle_path)

        return ReleaseBundle(
            manifest=manifest,
            archive_path=bundle_path,
            checksum=checksum,
            created_at=datetime.now(timezone.utc)
        )
