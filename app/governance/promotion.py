class PromotionGate:
    def check_perf_readiness(self, regression_severity: str) -> bool:
        if regression_severity in ["MAJOR", "CRITICAL"]:
            print(
                f"[GOVERNANCE] Promotion Blocked: Bad Perf Regression ({regression_severity})"
            )
            return False
        return True

    # Added in Phase 38
    def check_stress_risk_refs(self, candidate_bundle):
        pass
