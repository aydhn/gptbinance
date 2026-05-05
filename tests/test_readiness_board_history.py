from app.readiness_board.history import HistoryManager
from app.readiness_board.storage import ReadinessBoardStorage
from app.readiness_board.models import GoNoGoDecision, ReadinessDossier
from app.readiness_board.enums import BoardVerdict


def test_history_manager():
    storage = ReadinessBoardStorage()
    dos1 = ReadinessDossier(dossier_id="dos1", candidate_id="c1", snapshot_id="s1")
    dos2 = ReadinessDossier(dossier_id="dos2", candidate_id="c1", snapshot_id="s2")
    storage.save_dossier(dos1)
    storage.save_dossier(dos2)

    dec1 = GoNoGoDecision(
        decision_id="d1", dossier_id="dos1", verdict=BoardVerdict.NO_GO, rationale="x"
    )
    dec2 = GoNoGoDecision(
        decision_id="d2", dossier_id="dos2", verdict=BoardVerdict.GO, rationale="y"
    )
    storage.save_decision(dec1)
    storage.save_decision(dec2)

    hm = HistoryManager(storage)
    history = hm.get_candidate_history("c1")
    assert len(history) == 2
