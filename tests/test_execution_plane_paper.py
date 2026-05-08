from app.execution_plane.paper import PaperExecutionEnv


def test_paper_env():
    env = PaperExecutionEnv()
    res = env.simulate_fill("s1", 10.0, 50.0, True)
    assert res["filled_qty"] == 10.0
