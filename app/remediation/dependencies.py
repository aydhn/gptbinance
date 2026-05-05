from typing import List, Dict
from app.remediation.models import RemediationPack


class DependencyAnalyzer:
    def analyze_dependencies(
        self, packs: List[RemediationPack]
    ) -> Dict[str, List[str]]:
        # Mock dependency graph builder
        # Returns a dict of pack_id -> list of dependent pack_ids
        dependencies = {}
        for pack in packs:
            dependencies[pack.pack_id] = []

        # Example naive heuristic: READ_ONLY packs should happen before LOCAL_RECOMPUTE
        read_only_packs = [
            p for p in packs if p.recipe.safety_class.value == "read_only"
        ]
        recompute_packs = [
            p for p in packs if p.recipe.safety_class.value == "local_recompute"
        ]

        for r_pack in recompute_packs:
            for ro_pack in read_only_packs:
                # If they share the same scope, recompute depends on read_only
                if (
                    r_pack.scope.workspace == ro_pack.scope.workspace
                    and r_pack.scope.profile == ro_pack.scope.profile
                ):
                    dependencies[r_pack.pack_id].append(ro_pack.pack_id)

        return dependencies

    def detect_conflicts(self, packs: List[RemediationPack]) -> List[tuple[str, str]]:
        conflicts = []
        # Mock conflict detection:
        # Cannot have venue affecting and local recompute on same symbol at same time safely
        venue_packs = [
            p for p in packs if p.recipe.safety_class.value == "venue_affecting"
        ]
        recompute_packs = [
            p for p in packs if p.recipe.safety_class.value == "local_recompute"
        ]

        for v_pack in venue_packs:
            for r_pack in recompute_packs:
                if v_pack.scope.symbol and v_pack.scope.symbol == r_pack.scope.symbol:
                    conflicts.append((v_pack.pack_id, r_pack.pack_id))
        return conflicts
