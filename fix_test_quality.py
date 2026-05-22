import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + "\n")

test_content = """
from app.remedy_plane.models import RemedyObject, ContainmentRecord, HarmRecord
from app.remedy_plane.enums import RemedyClass, ContainmentClass, HarmClass
from app.remedy_plane.trust import RemedyTrustVerdictEngine

def test_quality_rollback_theater():
    remedy = RemedyObject(
        remedy_id="rem-002",
        remedy_class=RemedyClass.RELEASE_FAILURE_REMEDY,
        owner="release", scope="prod",
        harms=[HarmRecord(harm_id="h-1", harm_class=HarmClass.CUSTOMER_HARM, description="data unavailable", affected_party="cust-1", proof_notes="")],
        containments=[ContainmentRecord(containment_id="c-1", containment_class=ContainmentClass.BLAST_RADIUS_CONTAINMENT, description="rolled back", target_harm_id="h-1", is_rollback=True, caveats="")]
    )
    report = RemedyTrustVerdictEngine.evaluate(remedy)
    assert any("Rollback Theater" in b for b in report.blockers)
"""

write_file("tests/test_remedy_plane_quality.py", test_content)
