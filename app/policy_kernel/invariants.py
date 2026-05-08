class PolicyInvariants:
    def check_allocation_invariants(self, trust_verdict: str, budget_integrity: bool):
        # Enforce: no high-risk allocation under broken budget integrity, etc.
        if not budget_integrity:
            return False
        return True

class ExecutionInvariants:
    @staticmethod
    def check_invariants(has_idempotency: bool, filters_ok: bool, truth_ok: bool, ambiguous_cr: bool) -> list:
        violations = []
        if not has_idempotency:
            violations.append("no_send_attempt_without_valid_idempotency_record")
        if not filters_ok:
            violations.append("no_execution_under_broken_required_venue_filters")
        if not truth_ok:
            violations.append("no_aggressive_routing_under_critical_stale_market_truth")
        if ambiguous_cr:
            violations.append("no_cancel_replace_chain_under_unresolved_ambiguous_original_state")
        return violations
