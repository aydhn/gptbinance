import pytest
from app.policy_kernel.evidence import assemble_evidence_bundle
from app.policy_kernel.enums import EvidenceFreshness


def test_assemble_evidence_bundle():
    bundle = assemble_evidence_bundle(qualification_refs={"ok": True})
    assert bundle.qualification_refs == {"ok": True}
    assert bundle.freshness["qualification"] == EvidenceFreshness.FRESH
    assert bundle.freshness["stress"] == EvidenceFreshness.MISSING
    assert bundle.is_complete is False
