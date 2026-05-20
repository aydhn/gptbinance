import pytest
from app.provenance_plane.explainability import check_explainability
from app.provenance_plane.registry import registry
from app.provenance_plane.exceptions import InvalidExplainabilityRecord

def test_explainability_sufficiency():
    registry.register("expl-obj-1", {"provenance_id": "expl-obj-1", "explanation": "Rule Y executed"})
    assert check_explainability("expl-obj-1") is True

def test_non_defensible_explanation():
    registry.register("expl-obj-2", {"provenance_id": "expl-obj-2", "explanation": ""})
    with pytest.raises(InvalidExplainabilityRecord):
        check_explainability("expl-obj-2")
