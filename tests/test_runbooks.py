import pytest
from app.observability.runbooks import RunbookRegistry
from app.observability.models import RunbookRef


@pytest.fixture
def registry():
    return RunbookRegistry()


def test_runbook_registry(registry):
    # Verify seeded runbooks
    runbooks = registry.list_runbooks()
    assert len(runbooks) >= 2

    rb = registry.get_runbook("RB-STREAM-001")
    assert rb is not None
    assert "Binance API" in rb.investigation_steps[0]

    # Test custom registration
    new_rb = RunbookRef(
        ref_id="RB-TEST-001",
        title="Test Runbook",
        description="A test runbook",
        investigation_steps=["Check logs"],
        mitigation_steps=["Restart"],
    )
    registry.register(new_rb)
    assert registry.get_runbook("RB-TEST-001") == new_rb
