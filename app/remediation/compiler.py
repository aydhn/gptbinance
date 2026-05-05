import uuid
from typing import Optional

from app.remediation.enums import RemediationClass
from app.remediation.exceptions import InvalidRemediationRecipe, StaleFindingError
from app.remediation.models import (
    RemediationAction,
    RemediationFindingRef,
    RemediationPack,
    RemediationScope,
)
from app.remediation.recipes import RecipeRegistry


class RemediationCompiler:
    def __init__(self):
        self.registry = RecipeRegistry()

    def compile_pack(
        self, finding: RemediationFindingRef, explicit_recipe_id: Optional[str] = None
    ) -> RemediationPack:
        if finding.is_stale:
            raise StaleFindingError(
                f"Finding {finding.finding_id} is stale. Cannot compile pack."
            )

        recipe = None
        if explicit_recipe_id:
            recipe = self.registry.get_recipe(explicit_recipe_id)
        else:
            # Simple heuristic: pick the first supported recipe for the domain
            recipes = self.registry.find_recipes_for_source(finding.source_domain)
            if recipes:
                recipe = recipes[0]

        if not recipe:
            raise InvalidRemediationRecipe(
                f"No suitable recipe found for finding {finding.finding_id} in domain {finding.source_domain}."
            )

        action = RemediationAction(
            action_id=f"ACT-{uuid.uuid4().hex[:6]}",
            type="execute_recipe",
            parameters={
                "target": finding.context.get("target", "all"),
                "recipe_id": recipe.recipe_id,
            },
            is_reversible=(
                recipe.safety_class
                not in [RemediationClass.VENUE_AFFECTING, RemediationClass.REVIEW_ONLY]
            ),
        )

        scope = RemediationScope(
            workspace=finding.context.get("workspace", "default"),
            profile=finding.context.get("profile"),
            symbol=finding.context.get("symbol"),
            run_id=finding.context.get("run_id"),
        )

        return RemediationPack(
            pack_id=f"PACK-{uuid.uuid4().hex[:8].upper()}",
            finding_ref=finding,
            recipe=recipe,
            scope=scope,
            actions=[action],
        )
