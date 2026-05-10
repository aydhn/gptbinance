import pytest
from app.postmortem_plane.evidence import EvidenceBuilder
from app.postmortem_plane.exceptions import PostmortemPlaneError

def test_evidence_builder():
    evidence = EvidenceBuilder.build_review("E-1", "logs", "fresh", "Sufficient to show lock")
    assert evidence.evidence_id == "E-1"

    with pytest.raises(PostmortemPlaneError):
        EvidenceBuilder.build_review("E-2", "logs", "fresh", "")
