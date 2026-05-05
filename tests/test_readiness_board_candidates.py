from app.readiness_board.storage import ReadinessBoardStorage
from app.readiness_board.candidates import CandidateRegistry
from app.readiness_board.models import CandidateScope
from app.readiness_board.enums import CandidateClass


def test_register_candidate():
    storage = ReadinessBoardStorage()
    registry = CandidateRegistry(storage)
    scope = CandidateScope(symbols=["BTCUSDT"])
    record = registry.register_candidate(CandidateClass.EXPERIMENT_PROMOTION, scope)
    assert record.candidate_id.startswith("cand_")
    assert storage.get_candidate(record.candidate_id) is not None
