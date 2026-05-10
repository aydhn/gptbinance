import pytest
from app.release_plane.pins import PinValidator
from app.release_plane.models import BundlePin
from app.release_plane.exceptions import InvalidPinSet

def test_valid_pins():
    pins = [BundlePin(artifact_id="1", version_hash="abc", pin_type="t")]
    PinValidator.validate_pins(pins)

def test_empty_pins():
    with pytest.raises(InvalidPinSet):
        PinValidator.validate_pins([])

def test_missing_hash():
    pins = [BundlePin(artifact_id="1", version_hash="", pin_type="t")]
    with pytest.raises(InvalidPinSet):
        PinValidator.validate_pins(pins)
