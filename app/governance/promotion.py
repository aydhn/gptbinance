class PromotionGate:
    def check_perf_readiness(self, regression_severity: str) -> bool:
        if regression_severity in ["MAJOR", "CRITICAL"]:
            print(f"[GOVERNANCE] Promotion Blocked: Bad Perf Regression ({regression_severity})")
            return False
        return True
