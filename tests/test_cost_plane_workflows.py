from app.cost_plane.workflows import WorkflowLinkage
def test_workflow_linkage():
    linkage = WorkflowLinkage()
    assert linkage.get_queue_run_cost()["retry_amplification_cost"] == 50
