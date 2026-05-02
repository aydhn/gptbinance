import pytest
import asyncio
from app.resilience.stress import StressGenerator
from app.resilience.models import StressSpec, TargetComponentRef
from app.resilience.enums import StressType, TargetComponent


@pytest.mark.asyncio
async def test_stress_generator_auto_cleanup():
    generator = StressGenerator()
    spec = StressSpec(
        stress_type=StressType.QUEUE_PRESSURE,
        target=TargetComponentRef(component=TargetComponent.SCHEDULER),
        duration_ms=100,
    )

    run_id = "test_run"
    await generator.apply_stress(spec, run_id)

    stress_key = f"{run_id}_{spec.target.component.value}_{spec.stress_type.value}"
    assert stress_key in generator.active_stress

    # Wait for auto-cleanup
    await asyncio.sleep(0.2)

    assert stress_key not in generator.active_stress
    await generator.close()


@pytest.mark.asyncio
async def test_stress_generator_manual_cleanup():
    generator = StressGenerator()
    spec = StressSpec(
        stress_type=StressType.QUEUE_PRESSURE,
        target=TargetComponentRef(component=TargetComponent.SCHEDULER),
        duration_ms=5000,
    )

    run_id = "test_run"
    await generator.apply_stress(spec, run_id)

    stress_key = f"{run_id}_{spec.target.component.value}_{spec.stress_type.value}"
    assert stress_key in generator.active_stress

    await generator.remove_stress(spec, run_id)
    assert stress_key not in generator.active_stress
    await generator.close()
