from app.data_governance import CanonicalResolver, CanonicalId, CanonicalEntityType

def test_canonical_resolver_basic():
    resolver = CanonicalResolver()
    cid = CanonicalId(
        canonical_id="BTCUSDT",
        entity_type=CanonicalEntityType.SYMBOL,
        aliases=["BTC-USDT", "btcusdt"]
    )
    resolver.register(cid)

    resolved = resolver.resolve("BTC-USDT", CanonicalEntityType.SYMBOL)
    assert resolved.canonical_id == "BTCUSDT"

def test_canonical_resolver_ambiguous():
    resolver = CanonicalResolver()
    cid1 = CanonicalId(canonical_id="BTCUSDT_SPOT", entity_type=CanonicalEntityType.SYMBOL, aliases=["BTCUSDT"])
    cid2 = CanonicalId(canonical_id="BTCUSDT_FUTURES", entity_type=CanonicalEntityType.SYMBOL, aliases=["BTCUSDT"])

    resolver.register(cid1)
    resolver.register(cid2)

    resolved = resolver.resolve("BTCUSDT", CanonicalEntityType.SYMBOL)
    assert resolved.is_ambiguous == True
