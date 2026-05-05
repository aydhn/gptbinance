from app.readiness_board.storage import ReadinessBoardStorage
from app.readiness_board.evidence import EvidenceIntake
from app.readiness_board.enums import EvidenceClass


def test_submit_evidence():
    storage = ReadinessBoardStorage()
    intake = EvidenceIntake(storage)

    ev = intake.submit_evidence(
        "cand_123",
        EvidenceClass.POLICY_DECISION_PROOFS,
        {"has_hard_blocks": False},
        "source1",
    )
    assert ev.submission_id.startswith("evid_")

    fetched = storage.get_evidence_for_candidate("cand_123")
    assert len(fetched) == 1
