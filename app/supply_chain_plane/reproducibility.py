from typing import Dict, Any
from app.supply_chain_plane.models import ComponentRef, BuildRecipe
from app.supply_chain_plane.enums import BuildClass


class ReproducibilityEvaluator:
    def evaluate(self, recipe: BuildRecipe) -> Dict[str, Any]:
        if recipe.build_class == BuildClass.DETERMINISTIC:
            return {
                "is_reproducible": True,
                "notes": "Build recipe is classed as deterministic.",
                "rebuild_mismatch_reasons": [],
            }

        return {
            "is_reproducible": False,
            "notes": "Build recipe is classed as non-deterministic.",
            "rebuild_mismatch_reasons": [
                "Non-deterministic build toolchain or inputs."
            ],
        }
