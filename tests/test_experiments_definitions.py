from app.experiments.definitions import ExperimentDefinitionBuilder


def test_experiment_definition_builder():
    builder = ExperimentDefinitionBuilder()
    builder.add_baseline_arm("base_1")
    builder.add_candidate_arm("cand_1")

    dfn = builder.build("def_1", "hyp_1", ["pnl", "friction"])
    assert len(dfn.arms) == 2
    assert dfn.metrics == ["pnl", "friction"]
