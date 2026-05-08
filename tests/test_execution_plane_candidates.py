from app.execution_plane.candidates import AllocationIntentCompiler
from app.execution_plane.venues import create_default_venue_registry

class DummyIntent:
    intent_id = "i1"
    symbol = "ETHUSDT"
    target_size = 5.0
    direction = "long"
    is_reduce_only = False
    venue_class_preference = "binance_spot_mainnet"

def test_intent_compiler():
    registry = create_default_venue_registry()
    compiler = AllocationIntentCompiler(registry)

    intent = DummyIntent()
    candidate = compiler.compile(intent)

    assert candidate.symbol == "ETHUSDT"
    assert candidate.side == "buy"
    assert "binance_spot_mainnet" in candidate.venue_eligibility
    assert candidate.size_viable is True

    intent.target_size = -1
    candidate2 = compiler.compile(intent)
    assert candidate2.size_viable is False
