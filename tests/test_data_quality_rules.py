from app.data_governance import QualityRuleRegistry, QualitySeverity


def test_quality_rule_registry():
    registry = QualityRuleRegistry()
    rule = registry.get_rule("duplicate_primary_keys")
    assert rule is not None
    assert rule.severity == QualitySeverity.CRITICAL
