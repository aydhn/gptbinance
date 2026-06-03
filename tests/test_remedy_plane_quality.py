from app.remedy_plane.models import RemedyObject, ContainmentRecord
from app.remedy_plane.enums import RemedyClass, ContainmentClass
from app.remedy_plane.trust import RemedyTrustVerdictEngine

def test_quality_rollback_theater():
    remedy = RemedyObject(
        remedy_id="rem-002",
        remedy_class=RemedyClass.RELEASE_FAILURE_REMEDY,
        owner="release", scope="prod",
        harms=[],
        containments=[ContainmentRecord(containment_id="c-1", containment_class=ContainmentClass.BLAST_RADIUS_CONTAINMENT, description="rolled back", target_harm_id="h-1", is_rollback=True, caveats="")]
    )
    report = RemedyTrustVerdictEngine.evaluate(remedy)
    assert any("Rollback Theater" in b for b in report.blockers)
