from app.qualification.requirements import get_requirement, get_all_requirements
from app.qualification.enums import RequirementCriticality


def test_get_requirement():
    req = get_requirement("REQ-001")
    assert req is not None
    assert req.criticality == RequirementCriticality.CRITICAL


def test_get_all_requirements():
    reqs = get_all_requirements()
    assert len(reqs) > 0
