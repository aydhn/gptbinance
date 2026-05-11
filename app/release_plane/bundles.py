from typing import List, Optional
import hashlib
import json
from app.release_plane.models import ReleaseBundle, ReleaseBundleEntry, BundlePin
from app.release_plane.enums import BundleClass
from app.release_plane.exceptions import InvalidCandidateBundle

class BundleBuilder:
    def __init__(self, bundle_id: str, bundle_class: BundleClass):
        self.bundle_id = bundle_id
        self.bundle_class = bundle_class
        self.entries: List[ReleaseBundleEntry] = []

    def add_entry(self, entry: ReleaseBundleEntry) -> 'BundleBuilder':
        # Enforce no partial freeform bundle mutation
        self.entries.append(entry)
        return self

    def _compute_hash(self) -> str:
        # Sort and serialize entries to create an immutable hash
        serialized = []
        for e in self.entries:
            serialized.append({
                "entry_id": e.entry_id,
                "entry_type": e.entry_type,
                "manifest_ref": e.manifest_ref,
                "pins": [{"id": p.artifact_id, "hash": p.version_hash} for p in e.pins]
            })

        serialized.sort(key=lambda x: x["entry_id"])
        data_str = json.dumps(serialized, sort_keys=True)
        return hashlib.sha256(data_str.encode()).hexdigest()

    def build(self) -> ReleaseBundle:
        if not self.entries:
            raise InvalidCandidateBundle("Bundle must contain at least one entry.")

        bundle_hash = self._compute_hash()
        return ReleaseBundle(
            bundle_id=self.bundle_id,
            bundle_class=self.bundle_class,
            entries=self.entries,
            bundle_hash=bundle_hash
        )

class ReleaseBundleMigrationRef:
    def required_migration_refs(self, refs=None):
        pass
