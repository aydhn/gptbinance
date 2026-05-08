from app.simulation_plane.equivalence import EquivalenceEvaluator
from app.simulation_plane.enums import SimulationMode, EquivalenceVerdict


def test_equivalence():
    evaluator = EquivalenceEvaluator()
    report = evaluator.evaluate(
        "run1", SimulationMode.REPLAY_EVENT_TRUTH, ["fill_assumption"]
    )
    assert report.verdict == EquivalenceVerdict.PARTIAL_EQUIVALENCE
