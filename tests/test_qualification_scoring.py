from app.qualification.scoring import calculate_score
from app.qualification.models import EvidencePack, QualificationFinding
from app.qualification.enums import RequirementCriticality


def test_calculate_score_perfect():
    pack = EvidencePack(run_id="run-1", is_complete=True)
    score = calculate_score([], [], [], [], pack)
    assert score.overall_score == 1.0
    assert score.critical_findings_count == 0


def test_calculate_score_with_critical():
    pack = EvidencePack(run_id="run-1", is_complete=True)
    findings = [
        QualificationFinding(
            description="Test", criticality=RequirementCriticality.CRITICAL
        )
    ]
    score = calculate_score([], [], [], findings, pack)
    assert score.critical_findings_count == 1
    assert score.overall_score == 0.0  # Forced to 0
