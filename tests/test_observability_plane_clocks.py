import pytest
from app.observability_plane.clocks import ClockSemanticsRegistry
from app.observability_plane.models import ClockSemanticRecord
from app.observability_plane.enums import ClockClass
from app.observability_plane.exceptions import InvalidClockSemanticsError

def test_clock_semantics_enforcement():
    reg = ClockSemanticsRegistry()
    reg.register_clock(ClockSemanticRecord(telemetry_id="t1", clock_class=ClockClass.EVENT_TIME))

    with pytest.raises(InvalidClockSemanticsError):
        reg.assert_valid_clocks(["t1", "t2"])

    reg.assert_valid_clocks(["t1"])
