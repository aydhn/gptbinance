import pytest
from app.adversarial_plane.registry import CanonicalAdversarialRegistry
from app.adversarial_plane.objects import create_authoritative_adversarial_object
from app.adversarial_plane.enums import AdversarialClass
from app.adversarial_plane.exceptions import InvalidAdversarialObjectError

def test_registry():
    registry = CanonicalAdversarialRegistry()
    obj = create_authoritative_adversarial_object("adv-1", AdversarialClass.METRIC_GAMING, "Metric Gaming", "Team A", "Global", "Hostile", "High")
    registry.register(obj)
    fetched = registry.get("adv-1")
    assert fetched.adversarial_id == "adv-1"

    with pytest.raises(InvalidAdversarialObjectError):
        invalid_obj = create_authoritative_adversarial_object("", AdversarialClass.METRIC_GAMING, "Gaming", "Team A", "Global", "Hostile", "High")
        registry.register(invalid_obj)

import os
