from app.order_lifecycle.client_ids import ClientOrderIdGenerator


def test_client_id_generation():
    cid = ClientOrderIdGenerator.generate("plan_abcdefghi", "leg_jklmnop", 0)
    assert "cdefghi" in cid
    assert "jklmnop" in cid
    assert "_0_" in cid
