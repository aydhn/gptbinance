from app.cost_plane.experiments import ExperimentLinkage
def test_experiment_linkage():
    linkage = ExperimentLinkage()
    assert linkage.calculate_burn_budget()["experiment_burn"] == 200
