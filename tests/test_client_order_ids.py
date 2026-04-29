from app.execution.live.client_order_ids import ClientOrderIdGenerator


def test_client_order_id_generation():
    gen = ClientOrderIdGenerator("SESSION1")
    cid = gen.generate("BTCUSDT", "BUY", "INT123")
    assert cid.startswith("SESSION1-BTCUSDT-B-INT1-")
    assert len(cid) <= 36
