from app.security.models import DisasterRecoveryPlan

class DisasterRecoveryManager:
    def generate_plan(self, scenario: str) -> DisasterRecoveryPlan:
        return DisasterRecoveryPlan(
            scenario=scenario,
            steps=["Verify host", "Fetch latest backup", "Run restore dry-run", "Execute restore", "Run integrity check", "Start application"],
            estimated_rto_minutes=15
        )
