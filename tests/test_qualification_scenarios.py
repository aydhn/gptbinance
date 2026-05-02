from app.qualification.scenarios import GoldenPathRunner


def test_golden_path_runner():
    runner = GoldenPathRunner()
    results = runner.run_suite(["gold-risk-to-exec"])
    assert len(results) == 1
    assert results[0].passed is True
