from app.incident_plane.blast_radius import IncidentBlastRadiusEngine

def test_unknown_blast_radius_caution():
    result = IncidentBlastRadiusEngine.calculate([], [])
    assert result["status"] == "UNKNOWN"
    assert result["caution"] == "Unknown blast radius!"

    result_known = IncidentBlastRadiusEngine.calculate(["workflow"], ["BTCUSDT"])
    assert result_known["planes"] == ["workflow"]
