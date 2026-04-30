from app.ml.feature_selection import FeatureSelector


def test_feature_selector():
    selector = FeatureSelector()
    assert selector.select(None, None) is None
