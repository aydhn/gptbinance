from app.optimizer.strategy_spaces import get_space_by_name
from app.optimizer.search_space import SearchSpaceEvaluator


def test_default_spaces_are_valid():
    names = [
        "default_trend_follow",
        "default_mean_reversion",
        "default_breakout",
        "default_structure",
    ]

    for name in names:
        space = get_space_by_name(name)
        assert space is not None
        assert space.name == name

        # Validates syntax and rules
        SearchSpaceEvaluator.validate_space(space)
