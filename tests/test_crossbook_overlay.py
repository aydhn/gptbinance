from app.crossbook.overlay import CrossBookOverlay
from app.crossbook.enums import CrossBookVerdict

def test_crossbook_overlay():
    overlay = CrossBookOverlay()
    decision = overlay.decide()
    assert decision.verdict == CrossBookVerdict.ALLOW
