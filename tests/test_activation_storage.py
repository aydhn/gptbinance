import pytest
from app.activation.storage import ActivationStorage
from app.activation.models import ActivationIntent, ActivationScope
from app.activation.enums import ActivationClass


def test_storage_save_load_intent():
    intent = ActivationIntent(
        intent_id="i-storage-test",
        activation_class=ActivationClass.CANARY_LIMITED,
        board_decision_ref="b-1",
        candidate_id="c-1",
        scope=ActivationScope(),
    )
    ActivationStorage.save_intent(intent)
    loaded = ActivationStorage.load_intent("i-storage-test")
    assert loaded is not None
    assert loaded.intent_id == "i-storage-test"
    assert loaded.activation_class == ActivationClass.CANARY_LIMITED
