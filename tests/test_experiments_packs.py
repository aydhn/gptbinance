from app.experiments.packs import ExperimentPackBuilder
from app.experiments.models import (
    ExperimentDefinition,
    BaselineReference,
    CandidateReference,
    ExperimentScope,
)
from app.experiments.enums import ExperimentType, ScopeType
from datetime import datetime, timezone


def test_pack_builder():
    scope = ExperimentScope(
        scope_type=ScopeType.PROFILE,
        allowed_profiles=["p"],
        allowed_symbols=["s"],
        time_windows=[],
    )
    dfn = ExperimentDefinition(
        definition_id="d1",
        hypothesis_id="h1",
        experiment_type=ExperimentType.BASELINE_COMPARISON,
        scope=scope,
        arms=[],
        metrics=[],
    )
    base = BaselineReference(
        baseline_id="b1",
        strategy_id="s1",
        profile_id="p1",
        frozen_at=datetime.now(timezone.utc),
        manifest_hash="m1",
    )
    cand = CandidateReference(
        candidate_id="c1", hypothesis_id="h1", changed_surfaces=[], diff_summary=""
    )

    builder = ExperimentPackBuilder(dfn, base)
    builder.add_candidate(cand)
    pack = builder.build()

    assert pack.definition.definition_id == "d1"
    assert pack.baseline.baseline_id == "b1"
    assert len(pack.candidates) == 1
