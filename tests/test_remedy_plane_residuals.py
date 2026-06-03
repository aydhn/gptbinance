from app.remedy_plane.models import ResidualHarmRecord

def test_residual():
    r = ResidualHarmRecord(residual_id="r-1", original_harm_id="h-1", residual_class="res", description="desc", is_accepted=False, recourse_available=False)
    assert not r.is_accepted
