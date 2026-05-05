# Debt Governance, Verification, and Truthfulness

## 1. Verification is Mandatory
A remediation is not considered successful until the post-apply Verification step explicitly confirms the finding is resolved. If the finding persists, the remediation has effectively failed (or was only partial).

## 2. Outcomes
- **FIXED**: The finding is gone, the shadow state is healthy.
- **IMPROVED**: The finding is less severe, but still present.
- **UNCHANGED**: The remediation had no operational effect on the finding.
- **REGRESSED**: The remediation made the finding worse or spawned new findings.

## 3. Debt Escalation
Findings that cannot be automatically or manually remediated (or have failed remediation attempts) accrue "Remediation Debt".
High remediation debt severity acts as a strict blocker for qualification, live promotions, and capital escalations.
