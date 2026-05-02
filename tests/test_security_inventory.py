from app.security.inventory import SecretInventory


def test_inventory_contains_keys():
    inv = SecretInventory().get_inventory()
    assert len(inv) > 0
    assert any(i.ref.key == "BINANCE_API_KEY" for i in inv)
