import pytest
from app.observability.slo import SloEngine
from app.observability.models import SliDefinition, SloDefinition
from app.observability.enums import ComponentType, SloStatus


@pytest.fixture
def engine():
    return SloEngine()


def test_slo_evaluation(engine):
    sli = SliDefinition(
        sli_id="SLI-1",
        name="Stream Freshness",
        component=ComponentType.DATA_STREAM,
        query="max_lag",
        target_percentage=99.9,
    )
    slo = SloDefinition(
        slo_id="SLO-1",
        name="Stream Freshness SLO",
        sli_id="SLI-1",
        warning_threshold=5000.0,  # e.g. lag ms
        breach_threshold=30000.0,
    )

    engine.register_sli(sli)
    engine.register_slo(slo)

    # Healthy
    engine.record_sli_snapshot("SLI-1", 1000.0, 60)
    evals = engine.get_latest_evaluations()
    assert len(evals) == 1
    assert evals[0].status == SloStatus.HEALTHY

    # Caution (over breach logically, but let's look at the engine logic)
    # the code says: if < breach -> breach, if < warning -> caution. Wait, the logic in slo.py says "assuming higher is better".
    # Wait, for lag, LOWER is better. The SLO engine currently assumes higher is better.
    # Let's test what's there.
    # If higher is better (e.g. success rate)

    sli2 = SliDefinition(
        sli_id="SLI-2",
        name="Success Rate",
        component=ComponentType.EXECUTION,
        query="success_rate",
        target_percentage=99.0,
    )
    slo2 = SloDefinition(
        slo_id="SLO-2",
        name="Success Rate SLO",
        sli_id="SLI-2",
        warning_threshold=95.0,
        breach_threshold=90.0,
    )
    engine.register_sli(sli2)
    engine.register_slo(slo2)

    engine.record_sli_snapshot("SLI-2", 99.9, 60)
    evals = engine.get_latest_evaluations()
    slo2_eval = next(e for e in evals if e.slo_id == "SLO-2")
    assert slo2_eval.status == SloStatus.HEALTHY

    engine.record_sli_snapshot("SLI-2", 92.0, 60)
    evals = engine.get_latest_evaluations()
    slo2_eval = next(e for e in evals if e.slo_id == "SLO-2")
    assert slo2_eval.status == SloStatus.CAUTION

    engine.record_sli_snapshot("SLI-2", 85.0, 60)
    evals = engine.get_latest_evaluations()
    slo2_eval = next(e for e in evals if e.slo_id == "SLO-2")
    assert slo2_eval.status == SloStatus.BREACH
