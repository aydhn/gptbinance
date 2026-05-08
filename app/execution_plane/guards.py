class ExecutionGuards:
    @staticmethod
    def check_preflight_guards(allocation_trusted: bool, market_truth_fresh: bool,
                               capital_allowed: bool, policy_blocked: bool) -> list[str]:
        blockers = []
        if not allocation_trusted:
             blockers.append("allocation_not_trusted")
        if not market_truth_fresh:
             blockers.append("stale_market_truth")
        if not capital_allowed:
             blockers.append("insufficient_capital_or_margin")
        if policy_blocked:
             blockers.append("policy_hard_block")

        return blockers
