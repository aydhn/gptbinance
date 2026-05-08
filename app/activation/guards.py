class ActivationGuards:
    def enforce_allocation_equivalence(self, is_equivalent: bool):
        # Missing allocation trust or broken budget produces block semantics
        if not is_equivalent:
            raise Exception("Activation Guard Blocked: Allocation Equivalence Broken")
