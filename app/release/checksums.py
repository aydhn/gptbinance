import hashlib
import os
from typing import Dict
from app.release.models import ReleaseArtifactManifest


class ChecksumManager:
    def generate_checksum(self, file_path: str) -> str:
        sha256 = hashlib.sha256()
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
        return sha256.hexdigest()

    def create_manifest(self, directory: str) -> ReleaseArtifactManifest:
        files = {}
        for root, _, filenames in os.walk(directory):
            for filename in filenames:
                path = os.path.join(root, filename)
                files[os.path.relpath(path, directory)] = self.generate_checksum(path)
        return ReleaseArtifactManifest(files=files)

    def verify_manifest(
        self, manifest: ReleaseArtifactManifest, directory: str
    ) -> bool:
        for rel_path, expected_checksum in manifest.files.items():
            path = os.path.join(directory, rel_path)
            if not os.path.exists(path):
                return False
            if self.generate_checksum(path) != expected_checksum:
                return False
        return True
