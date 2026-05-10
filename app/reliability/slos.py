class ReleaseIntegritySLO:
    def __init__(self, slo_family: str, window: str, budget: float):
        self.slo_family = slo_family
        self.window = window
        self.budget = budget

# Families:
# - active release manifest completeness
# - hidden hotfix absence
# - rollback readiness cleanliness
# - rollout equivalence cleanliness
# - trusted release degraded ratio
