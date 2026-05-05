from app.readiness_board.decisions import DecisionEngine
from app.readiness_board.storage import ReadinessBoardStorage
from app.readiness_board.models import ReadinessDossier, ReadinessDomainVerdict
from app.readiness_board.enums import ReadinessDomain, DomainVerdict, BoardVerdict


def test_conditional_go():
    storage = ReadinessBoardStorage()
    engine = DecisionEngine(storage)

    dossier = ReadinessDossier(
        dossier_id="dos1",
        candidate_id="c1",
        snapshot_id="s1",
        domain_verdicts={
            ReadinessDomain.POLICY: ReadinessDomainVerdict(
                domain=ReadinessDomain.POLICY, verdict=DomainVerdict.CAUTION
            )
        },
        conflicts=[],
    )

    dec = engine.evaluate_dossier(dossier)
    assert dec.verdict == BoardVerdict.CONDITIONAL_GO
    assert dec.conditional_terms is not None
