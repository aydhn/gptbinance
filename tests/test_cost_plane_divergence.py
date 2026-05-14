from app.cost_plane.divergence import DivergenceManager

def test_divergence():
    manager = DivergenceManager()
    record = manager.report_divergence("live", "paper", 100.0, "USD", "medium")
    assert record.divergence_amount == 100.0
