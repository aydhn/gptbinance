from app.governance.decay import DecayChecker


def test_decay_checker():
    checker = DecayChecker()
    reports = checker.check_decay("test_bundle")
    assert len(reports) == 1
    assert reports[0].bundle_id == "test_bundle"
