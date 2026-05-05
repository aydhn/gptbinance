from app.experiments.findings import FindingIntake
from app.experiments.hypotheses import HypothesisRegistry


def test_finding_intake():
    registry = HypothesisRegistry()
    intake = FindingIntake(registry)

    f_id = intake.process_finding(
        {"finding_id": "f_123", "summary": "high friction observed"}
    )
    assert f_id is not None

    backlog = intake.get_research_backlog()
    assert len(backlog) == 1
    assert backlog[0]["finding_id"] == "f_123"
