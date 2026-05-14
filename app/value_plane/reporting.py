from app.value_plane.registry import value_registry
from app.value_plane.objectives import objective_registry

def generate_value_registry_summary():
    values = value_registry.list_all()
    return f"Total Value Objects: {len(values)}"

def generate_objectives_summary():
    objectives = objective_registry.list_all()
    return f"Total Objectives: {len(objectives)}"
