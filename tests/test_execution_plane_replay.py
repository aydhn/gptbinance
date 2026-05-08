from app.execution_plane.replay import ReplayExecutionEnv


def test_replay_env():
    env = ReplayExecutionEnv()
    res = env.reconstruct({})
    assert res["status"] == "reconstructed"
