import pytest
from app.resilience.repository import ExperimentRunner
from app.resilience.models import ExperimentScope
from app.resilience.enums import SafeScope, ExperimentStatus, GateVerdict
from app.resilience.scenarios import get_scenario


@pytest.mark.asyncio
async def test_experiment_runner_blocked_by_gate():
    runner = ExperimentRunner()
    scenario = get_scenario("stale_stream_scenario")

    # Force live mainnet to trigger block
    scope = ExperimentScope(
        safe_scope=SafeScope.PAPER, environment="test", is_live_mainnet=True
    )

    run = await runner.run_experiment(scenario, scope)

    assert run.status == ExperimentStatus.GATED
    assert run.summary is not None
    assert run.summary.gate_report.verdict == GateVerdict.BLOCK

    await runner.fault_injector.close()
    await runner.stress_generator.close()


@pytest.mark.asyncio
async def test_experiment_runner_successful_run():
    runner = ExperimentRunner()
    scenario = get_scenario("stale_stream_scenario")

    # Modify durations for faster testing
    scenario.fault_specs[0].duration_ms = 100
    scenario.assertions[0].timeout_ms = 100
    scenario.recovery_assertions[0].timeout_ms = 100

    scope = ExperimentScope(
        safe_scope=SafeScope.PAPER, environment="test", is_live_mainnet=False
    )

    run = await runner.run_experiment(scenario, scope)

    assert run.status == ExperimentStatus.COMPLETED
    assert run.summary is not None
    assert run.summary.gate_report.verdict == GateVerdict.ALLOW
    assert len(run.summary.assertion_results) == len(scenario.assertions)
    assert len(run.summary.recovery_results) == len(scenario.recovery_assertions)
    assert run.summary.resilience_score is not None
    assert run.summary.resilience_score.overall_score > 0

    await runner.fault_injector.close()
    await runner.stress_generator.close()
