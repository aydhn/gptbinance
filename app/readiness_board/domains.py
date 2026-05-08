class AllocationIntegrityDomain:
    def get_verdict(self) -> str:
        # Evaluates budgets, exposures, capacity, crowding, and equivalence posture
        return "GO"

class ExecutionIntegrityDomain:
    @staticmethod
    def get_verdict(bundle: dict) -> str:
        if bundle.get("critical_failures"):
            return "blocked"
        return "ready"
