import pytest
from app.ledger_plane.manifests import LedgerManifestBuilder
from app.ledger_plane.models import LedgerManifestEntry

def test_ledger_manifest_creation():
    entry1 = LedgerManifestEntry(ref_id="ref1", ref_type="entry")
    entry2 = LedgerManifestEntry(ref_id="ref2", ref_type="balance")

    manifest = LedgerManifestBuilder.build([entry1, entry2])
    assert len(manifest.entries) == 2
    assert manifest.manifest_id is not None
    assert manifest.hash_value is not None
