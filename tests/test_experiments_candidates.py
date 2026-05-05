from app.experiments.candidates import CandidateRegistry
from app.experiments.models import CandidateReference


def test_candidate_registry():
    reg = CandidateRegistry()
    c = CandidateReference(
        candidate_id="c_1",
        hypothesis_id="h_1",
        changed_surfaces=["filter.threshold"],
        diff_summary="relaxed threshold",
    )
    reg.register(c)

    assert reg.get("c_1").diff_summary == "relaxed threshold"
    assert len(reg.list_by_hypothesis("h_1")) == 1
