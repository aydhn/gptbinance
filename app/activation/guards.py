class ActivationGuards:
    def enforce_allocation_equivalence(self, is_equivalent: bool):
        # Missing allocation trust or broken budget produces block semantics
        if not is_equivalent:
            raise Exception("Activation Guard Blocked: Allocation Equivalence Broken")

class ExecutionActivationGuard:
    @staticmethod
    def check_guards(manifest_present: bool, filters_valid: bool) -> list:
        blockers = []
        if not manifest_present:
            blockers.append("missing_execution_manifest")
        if not filters_valid:
            blockers.append("invalid_venue_filters")
        return blockers
