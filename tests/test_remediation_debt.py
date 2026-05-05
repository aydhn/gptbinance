from app.remediation.debt import DebtGovernance
from app.remediation.findings import FindingIntake
from app.remediation.enums import DebtSeverity


def test_debt_assessment():
    intake = FindingIntake()
    f1 = intake.normalize_finding("F-1", "shadow_state", "low", {})
    f2 = intake.normalize_finding("F-2", "shadow_state", "critical", {})

    gov = DebtGovernance()
    debts = gov.assess_debt([f1, f2])

    assert len(debts) == 2
    assert debts[0].severity == DebtSeverity.WARNING
    assert debts[1].severity == DebtSeverity.BLOCKER
    assert debts[1].is_qualification_blocker is True
