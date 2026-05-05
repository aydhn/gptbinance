from app.readiness_board.decisions import DecisionEngine
from app.readiness_board.storage import ReadinessBoardStorage
from app.readiness_board.models import (
    ReadinessDossier,
    ReadinessDomainVerdict,
    EvidenceConflict,
)
from app.readiness_board.enums import (
    ReadinessDomain,
    DomainVerdict,
    ContradictionClass,
    BoardVerdict,
)


def test_decision_engine():
    storage = ReadinessBoardStorage()
    engine = DecisionEngine(storage)

    dossier = ReadinessDossier(
        dossier_id="dos1",
        candidate_id="c1",
        snapshot_id="s1",
        domain_verdicts={
            ReadinessDomain.POLICY: ReadinessDomainVerdict(
                domain=ReadinessDomain.POLICY, verdict=DomainVerdict.PASS
            )
        },
        conflicts=[],
    )

    dec1 = engine.evaluate_dossier(dossier)
    assert dec1.verdict == BoardVerdict.GO

    dossier_blocked = ReadinessDossier(
        dossier_id="dos2",
        candidate_id="c1",
        snapshot_id="s1",
        domain_verdicts={
            ReadinessDomain.POLICY: ReadinessDomainVerdict(
                domain=ReadinessDomain.POLICY,
                verdict=DomainVerdict.BLOCK,
                blockers=["b1"],
            )
        },
        conflicts=[],
    )
    dec2 = engine.evaluate_dossier(dossier_blocked)
    assert dec2.verdict == BoardVerdict.NO_GO

    c = EvidenceConflict(
        conflict_id="c1",
        contradiction_class=ContradictionClass.OTHER,
        description="desc",
        involved_domains=[ReadinessDomain.POLICY],
    )
    dossier_conflict = ReadinessDossier(
        dossier_id="dos3",
        candidate_id="c1",
        snapshot_id="s1",
        domain_verdicts={},
        conflicts=[c],
    )
    dec3 = engine.evaluate_dossier(dossier_conflict)
    assert dec3.verdict == BoardVerdict.NEEDS_REVIEW
