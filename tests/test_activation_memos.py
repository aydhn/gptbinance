import pytest
from app.activation.memos import MemoBuilder
from app.activation.models import ActivationIntent, ActivationScope
from app.activation.enums import ActivationClass


def test_memo_builder():
    intent = ActivationIntent(
        intent_id="i-1",
        activation_class=ActivationClass.CANARY_LIMITED,
        board_decision_ref="b-1",
        candidate_id="c-1",
        scope=ActivationScope(),
    )
    memo = MemoBuilder.build(intent)
    assert memo.intent_id == "i-1"
    assert "b-1" in memo.rationale
