import pytest
from app.drift_plane.signals import SignalManager
from app.drift_plane.enums import SignalClass

def test_signal_creation():
    manager = SignalManager()
    manager.add_signal("signal-1", SignalClass.CORROBORATED, "source-1")

    signal = manager.get_signal("signal-1")
    assert signal is not None
    assert signal.signal_id == "signal-1"
    assert signal.class_type == SignalClass.CORROBORATED
    assert signal.source == "source-1"
