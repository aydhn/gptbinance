from app.allocation.models import AllocationManifest
from app.allocation.enums import EquivalenceVerdict


class EquivalenceEngine:
    def evaluate(
        self, offline: AllocationManifest, runtime: AllocationManifest
    ) -> EquivalenceVerdict:
        if offline.lineage_hash == runtime.lineage_hash:
            return EquivalenceVerdict.EQUIVALENT
        if offline.portfolio_gross_exposure != runtime.portfolio_gross_exposure:
            return EquivalenceVerdict.DIVERGED_CRITICAL
        return EquivalenceVerdict.DIVERGED_SAFE
