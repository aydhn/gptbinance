from app.remediation.recipes import RecipeRegistry
from app.remediation.enums import RemediationClass


def test_recipe_registry_lookup():
    registry = RecipeRegistry()
    recipe = registry.get_recipe("refresh_venue_shadow_snapshot")
    assert recipe is not None
    assert recipe.safety_class == RemediationClass.READ_ONLY


def test_recipe_registry_find_by_source():
    registry = RecipeRegistry()
    recipes = registry.find_recipes_for_source("order_lifecycle")
    assert len(recipes) > 0
    names = [r.recipe_id for r in recipes]
    assert "request_orphan_order_review" in names
