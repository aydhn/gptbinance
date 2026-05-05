from app.migrations.recipes import (
    create_workspace_manifest_upgrade_recipe,
    create_policy_rule_schema_upgrade,
)


def test_workspace_manifest_upgrade_recipe():
    recipe = create_workspace_manifest_upgrade_recipe("m1", "1.0", "2.0")
    assert recipe.id == "m1"
    assert recipe.version_from == "1.0"
    assert recipe.version_to == "2.0"
    assert not recipe.compatibility.mixed_version_safe


def test_policy_rule_schema_upgrade_recipe():
    recipe = create_policy_rule_schema_upgrade("m2", "1.0", "2.0")
    assert recipe.id == "m2"
    assert recipe.compatibility.mixed_version_safe
