from app.cost_plane.equivalence import EquivalenceManager
from app.cost_plane.enums import CostEquivalenceVerdict

def test_equivalence():
    manager = EquivalenceManager()
    record = manager.evaluate_equivalence("workload-1", ["live", "paper"], CostEquivalenceVerdict.DIVERGENT)
    assert record.verdict == CostEquivalenceVerdict.DIVERGENT
