from app.remediation.models import RemediationFindingRef, RemediationDebtRecord
from app.remediation.enums import DebtSeverity


class DebtGovernance:
    def assess_debt(
        self, unresolved_findings: list[RemediationFindingRef]
    ) -> list[RemediationDebtRecord]:
        debts = []
        for finding in unresolved_findings:
            sev = DebtSeverity.WARNING
            if finding.severity == "critical":
                sev = DebtSeverity.BLOCKER

            debts.append(
                RemediationDebtRecord(
                    debt_id=f"DEBT-{finding.finding_id}",
                    finding_ref=finding,
                    severity=sev,
                    failed_attempts=1,
                    aging_days=2,
                    is_qualification_blocker=(sev == DebtSeverity.BLOCKER),
                )
            )
        return debts
