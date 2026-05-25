from app.settlement_plane.quality import check_quality

def test_check_quality_warnings():
    res = check_quality("S1", {"overrelease": True})
    assert "overrelease warning" in res["quality_warnings"]

def test_check_quality_clean():
    res = check_quality("S2", {})
    assert len(res["quality_warnings"]) == 0
