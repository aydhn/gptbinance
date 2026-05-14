from app.cost_plane.quality import QualityManager

def test_quality():
    manager = QualityManager()
    record = manager.check_quality(["warning 1"], "low")
    assert record["verdict"] == "fail"
