import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + "\n")

write_file("tests/test_remedy_plane_breach_harms.py", """
from app.remedy_plane.models import BreachHarmRecord

def test_breach_harm():
    b = BreachHarmRecord(breach_harm_id="b-1", original_harm_id="h-1", breach_type="sla_breach", commitment_ref="c-1", description="delayed", proof_notes="")
    assert b.breach_type == "sla_breach"
""")

write_file("tests/test_remedy_plane_cures.py", """
from app.remedy_plane.models import CureRecord
from app.remedy_plane.enums import CureClass

def test_cure_record():
    c = CureRecord(cure_id="c-1", cure_class=CureClass.PARTIAL_CURE, description="partial", target_harm_id="h-1", proof_notes="")
    assert c.cure_class == CureClass.PARTIAL_CURE
""")

write_file("tests/test_remedy_plane_residuals.py", """
from app.remedy_plane.models import ResidualHarmRecord

def test_residual():
    r = ResidualHarmRecord(residual_id="r-1", original_harm_id="h-1", residual_class="res", description="desc", is_accepted=False, recourse_available=False)
    assert not r.is_accepted
""")

write_file("tests/test_remedy_plane_compensation.py", """
from app.remedy_plane.models import CompensationRecord
from app.remedy_plane.enums import CompensationClass

def test_compensation():
    c = CompensationRecord(compensation_id="c-1", compensation_class=CompensationClass.SERVICE_CREDIT, amount_or_value="$100", beneficiary="user1", target_harm_id="h-1", proof_notes="")
    assert c.amount_or_value == "$100"
""")

write_file("tests/test_remedy_plane_containment.py", """
from app.remedy_plane.models import ContainmentRecord
from app.remedy_plane.enums import ContainmentClass

def test_containment():
    c = ContainmentRecord(containment_id="c-1", containment_class=ContainmentClass.BLAST_RADIUS_CONTAINMENT, description="desc", target_harm_id="h-1", is_rollback=True, caveats="")
    assert c.is_rollback
""")

write_file("tests/test_remedy_plane_quality.py", """
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
""")
