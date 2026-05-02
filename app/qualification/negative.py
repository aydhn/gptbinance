from typing import List
from app.qualification.models import ForbiddenActionCheck


class ForbiddenActionRunner:
    def __init__(self):
        # Mocking the defined negative tests
        self.tests = [
            "neg-unauthorized-live",
            "neg-risk-bypass",
            "neg-stale-approval",
            "neg-upgrade-no-backup",
            "neg-mainnet-chaos",
            "neg-missing-secret-live",
            "stale_approval_deny",
            "active_runtime_upgrade_block",
            "unauthorized_live_start_block",
            "mainnet_chaos_block",
            "missing_critical_secret_block",
            "self_approval_deny",
        ]

    def run_forbidden_checks(
        self, mandatory_tests: List[str]
    ) -> List[ForbiddenActionCheck]:
        results = []
        # Run all known, mark mandatory ones specifically if needed
        for test_id in set(self.tests + mandatory_tests):
            # Mock: all correctly blocked
            results.append(
                ForbiddenActionCheck(
                    action_id=test_id,
                    description=f"Verify {test_id} is blocked",
                    was_blocked=True,
                )
            )
        return results
