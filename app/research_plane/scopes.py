from app.research_plane.models import ResearchScope
from app.research_plane.exceptions import ResearchPlaneError


class ScopeHandler:
    def check_generalization(
        self, original_scope: ResearchScope, target_scope: ResearchScope
    ) -> bool:
        # Prevent wrong-scope generalization.
        # Simple check for now: target must be subset of original if we don't have explicit broadening proofs.
        # (This can be more sophisticated)
        if original_scope.symbols and target_scope.symbols:
            if not set(target_scope.symbols).issubset(set(original_scope.symbols)):
                raise ResearchPlaneError(
                    "Target scope symbols exceed original research scope."
                )
        return True
