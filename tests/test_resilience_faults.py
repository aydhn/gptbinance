import pytest
import asyncio
from app.resilience.faults import FaultInjector
from app.resilience.models import FaultInjectionSpec, TargetComponentRef
from app.resilience.enums import FaultType, TargetComponent


@pytest.mark.asyncio
async def test_fault_injector_auto_cleanup():
    injector = FaultInjector()
    spec = FaultInjectionSpec(
        fault_type=FaultType.LATENCY_INJECTION,
        target=TargetComponentRef(component=TargetComponent.DATA_STREAM),
        duration_ms=100,
    )

    run_id = "test_run"
    await injector.inject(spec, run_id)

    fault_key = f"{run_id}_{spec.target.component.value}_{spec.fault_type.value}"
    assert fault_key in injector.active_faults

    # Wait for auto-cleanup
    await asyncio.sleep(0.2)

    assert fault_key not in injector.active_faults
    await injector.close()


@pytest.mark.asyncio
async def test_fault_injector_manual_cleanup():
    injector = FaultInjector()
    spec = FaultInjectionSpec(
        fault_type=FaultType.LATENCY_INJECTION,
        target=TargetComponentRef(component=TargetComponent.DATA_STREAM),
        duration_ms=5000,
    )

    run_id = "test_run"
    await injector.inject(spec, run_id)

    fault_key = f"{run_id}_{spec.target.component.value}_{spec.fault_type.value}"
    assert fault_key in injector.active_faults

    await injector.cleanup(spec, run_id)
    assert fault_key not in injector.active_faults
    await injector.close()
