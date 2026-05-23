class RepresentationDebtTracker:
    @staticmethod
    def calculate_debt(rep, trust_verdict):
        debt = []
        if trust_verdict.verdict in ["blocked", "degraded", "caution"]:
            for b in trust_verdict.blockers:
                debt.append({"type": "blocker_debt", "issue": b})
            for w in trust_verdict.warnings:
                debt.append({"type": "warning_debt", "issue": w})
        return debt
