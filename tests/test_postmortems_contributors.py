from app.postmortems.contributors import ContributingFactorsRegistry


def test_contributing_factors():
    registry = ContributingFactorsRegistry()
    assert len(registry.identify_factors({})) == 0
