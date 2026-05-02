import hashlib
import os
from typing import List
from app.security.models import IntegrityCheckResult
from app.security.enums import IntegritySeverity


class IntegrityChecker:
    def intentional_fault_simulation(self):
        pass

    def generate_manifest(self, directory: str) -> dict:
        manifest = {}
        for root, dirs, files in os.walk(directory):
            for file in files:
                path = os.path.join(root, file)
                manifest[path] = self._hash_file(path)
        return manifest

    def verify_manifest(self, manifest: dict) -> List[IntegrityCheckResult]:
        results = []
        for path, expected_hash in manifest.items():
            if not os.path.exists(path):
                results.append(
                    IntegrityCheckResult(
                        file_path=path,
                        expected_hash=expected_hash,
                        actual_hash="MISSING",
                        severity=IntegritySeverity.CRITICAL,
                    )
                )
                continue
            actual_hash = self._hash_file(path)
            if actual_hash != expected_hash:
                results.append(
                    IntegrityCheckResult(
                        file_path=path,
                        expected_hash=expected_hash,
                        actual_hash=actual_hash,
                        severity=IntegritySeverity.CRITICAL,
                    )
                )
        return results

    def _hash_file(self, path: str) -> str:
        sha256 = hashlib.sha256()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
        return sha256.hexdigest()

    def verify_release_bundle(self, bundle_path: str, expected_checksum: str) -> bool:
        actual = self._hash_file(bundle_path)
        return actual == expected_checksum
