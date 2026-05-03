from app.stressrisk.qualification import QualificationStressEvidence


def test_qualification_evidence():
    evidence = QualificationStressEvidence()
    ev = evidence.get_evidence("run1")
    assert ev["status"] == "PASS"
