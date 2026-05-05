from app.readiness_board.storage import ReadinessBoardStorage
from app.readiness_board.models import CandidateRecord, CandidateScope
from app.readiness_board.enums import CandidateClass


def test_storage():
    storage = ReadinessBoardStorage()
    record = CandidateRecord(
        candidate_id="c1",
        candidate_class=CandidateClass.PAPER_SHADOW,
        scope=CandidateScope(),
    )
    storage.save_candidate(record)
    assert storage.get_candidate("c1") is not None
    assert storage.get_candidate("c2") is None
