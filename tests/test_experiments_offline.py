from app.experiments.offline import OfflineExperimentRunner


def test_offline_runner():
    runner = OfflineExperimentRunner()
    run_id = runner.run("pack_1")
    assert run_id is not None
