from app.postmortems.models import PostmortemSeedRef
from typing import List


class SeedValidator:
    def validate(self, seed: PostmortemSeedRef) -> bool:
        return True


class IncidentSeedIntake:
    def __init__(self):
        self.validator = SeedValidator()
        self.seeds = []

    def intake_seed(self, seed: PostmortemSeedRef):
        if self.validator.validate(seed):
            self.seeds.append(seed)
            return True
        return False

    def get_unresolved_seeds(self) -> List[PostmortemSeedRef]:
        return self.seeds
