from typing import Dict, List, Optional
from app.supply_chain_plane.models import BuildRecipe, ComponentRef


class BuildRecipeRegistry:
    def __init__(self):
        self._recipes: Dict[str, BuildRecipe] = {}

    def register_recipe(self, recipe: BuildRecipe) -> None:
        self._recipes[recipe.recipe_id] = recipe

    def get_recipe(self, recipe_id: str) -> Optional[BuildRecipe]:
        return self._recipes.get(recipe_id)

    def get_recipe_for_component(self, component_id: str) -> Optional[BuildRecipe]:
        for recipe in self._recipes.values():
            if recipe.component_ref.component_id == component_id:
                return recipe
        return None
