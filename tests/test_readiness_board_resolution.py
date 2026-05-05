from app.readiness_board.resolution import ContradictionResolver
from app.readiness_board.models import EvidenceConflict
from app.readiness_board.enums import ContradictionClass, ReadinessDomain


def test_contradiction_resolver():
    resolver = ContradictionResolver()
    c = EvidenceConflict(
        conflict_id="c1",
        contradiction_class=ContradictionClass.OTHER,
        description="desc",
        involved_domains=[ReadinessDomain.POLICY],
    )
    res = resolver.resolve([c])
    assert len(res) == 1
    assert res[0].resolved is False
