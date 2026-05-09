from app.workflow_plane.workflows import WorkflowManager

def test_workflow_manager():
    wm = WorkflowManager()
    # Relies on the default registry populated in registry.py
    assert len(wm.get_workflows()) >= 3
