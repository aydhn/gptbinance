from typing import List
from app.release_plane.models import BundlePin
from app.release_plane.exceptions import InvalidPinSet

class PinValidator:
    @staticmethod
    def validate_pins(pins: List[BundlePin]) -> None:
        if not pins:
            raise InvalidPinSet("Missing pin blockers: Bundle entry must have at least one pin.")

        for pin in pins:
            if not pin.artifact_id or not pin.version_hash:
                 raise InvalidPinSet("Artifact ID and version hash are required for all pins.")

            # Environment specific pins logic could be expanded here.
