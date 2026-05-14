from app.cost_plane.storage import CostStorage

def test_cost_storage():
    storage = CostStorage()
    storage.save("test_coll", "1", {"key": "value"})
    assert storage.get("test_coll", "1") == {"key": "value"}
