from app.perf.benchmarks import DeterministicBenchmarkRunner


def test_benchmarks():
    runner = DeterministicBenchmarkRunner()
    res = runner.run("test", 3, lambda: None)
    assert res.success is True
    assert res.data["iterations"] == 3
