from app.readiness_board.memos import MemoBuilder
from app.readiness_board.storage import ReadinessBoardStorage
from app.readiness_board.models import GoNoGoDecision, ReadinessDossier
from app.readiness_board.enums import BoardVerdict, MemoClass


def test_memo_builder():
    storage = ReadinessBoardStorage()
    builder = MemoBuilder(storage)

    dec = GoNoGoDecision(
        decision_id="d1", dossier_id="dos1", verdict=BoardVerdict.NO_GO, rationale="x"
    )
    dos = ReadinessDossier(dossier_id="dos1", candidate_id="c1", snapshot_id="s1")

    memo = builder.build_memo(dec, dos)
    assert memo.memo_class == MemoClass.BLOCKED
    assert storage.get_memo(memo.memo_id) is not None
