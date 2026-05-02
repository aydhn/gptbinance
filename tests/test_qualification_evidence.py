from app.qualification.evidence import EvidenceCollector
from app.qualification.enums import EvidenceStatus


def test_evidence_collector():
    collector = EvidenceCollector()
    refs = collector.collect_refs("security_refs")
    assert len(refs) == 1
    assert refs[0].status == EvidenceStatus.COMPLETE
