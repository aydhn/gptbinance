from app.postmortems.admissibility import AdmissibilityRulesEngine
from app.postmortems.enums import EvidenceVerdict


def test_evidence_admissibility():
    engine = AdmissibilityRulesEngine()
    assert engine.evaluate({}) == EvidenceVerdict.ACCEPTED
