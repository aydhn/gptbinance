import pytest
from app.activation.intents import IntentCompiler
from app.activation.exceptions import InvalidActivationIntent
from app.activation.enums import ActivationClass


def test_compile_valid_conditional_go():
    decision = {
        "decision": "CONDITIONAL_GO",
        "candidate_id": "cand-999",
        "decision_id": "board-ref-001",
        "activation_class": "canary_limited",
        "scope": {"allowed_symbols": ["BTCUSDT", "ETHUSDT"], "ttl_seconds": 3600},
    }
    compiler = IntentCompiler()
    intent = compiler.compile_intent(decision)

    assert intent.activation_class == ActivationClass.CANARY_LIMITED
    assert intent.candidate_id == "cand-999"
    assert "BTCUSDT" in intent.scope.allowed_symbols
    assert intent.scope.ttl_seconds == 3600


def test_reject_no_go_decision():
    decision = {"decision": "NO_GO", "candidate_id": "cand-888"}
    compiler = IntentCompiler()
    with pytest.raises(InvalidActivationIntent):
        compiler.compile_intent(decision)
