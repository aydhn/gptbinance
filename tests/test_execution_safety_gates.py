from app.execution.live.safety_gates import SafetyGateManager, MainnetDisarmedGate
from app.execution.live.models import ExecutionConfig
from app.execution.live.enums import ExecutionEnvironment


def test_mainnet_disarmed_gate():
    manager = SafetyGateManager()

    # Testnet should pass
    config_test = ExecutionConfig(environment=ExecutionEnvironment.TESTNET)
    res = manager.evaluate_all(config_test, {"is_session_ready": True})
    assert res.passed

    # Mainnet unarmed should fail
    config_main = ExecutionConfig(
        environment=ExecutionEnvironment.MAINNET, mainnet_armed=False
    )
    res2 = manager.evaluate_all(config_main, {"is_session_ready": True})
    assert not res2.passed

    # Mainnet armed should pass
    config_main_armed = ExecutionConfig(
        environment=ExecutionEnvironment.MAINNET, mainnet_armed=True
    )
    res3 = manager.evaluate_all(config_main_armed, {"is_session_ready": True})
    assert res3.passed
