from app.strategies.explain import ExplanationGenerator
from app.strategies.models import StrategyRationale
from app.strategies.enums import RationaleCategory


def test_format_rationales():
    rationales = [
        StrategyRationale(category=RationaleCategory.RULE_PASS, reason="A passed"),
        StrategyRationale(
            category=RationaleCategory.SCORE_PENALTY, reason="Penalty applied"
        ),
    ]

    text = ExplanationGenerator.format_rationales(rationales)
    assert "✅ RULE_PASS" in text
    assert "❌ SCORE_PENALTY" in text
