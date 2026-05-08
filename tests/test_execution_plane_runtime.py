from app.execution_plane.runtime import RuntimeExecutionEnv

def test_runtime_env():
    env = RuntimeExecutionEnv(is_live=True)
    env.register_manifest("m1", {"dummy": "data"})
    env.record_receipt("k1", {"status": "ok", "api_secret": "hidden"})

    assert "api_secret" not in env.send_receipts["k1"]
