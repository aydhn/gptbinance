import pytest
from app.continuity_plane.workflows import ContinuityWorkflowLinkage

def test_workflow_linkage():
    linkage = ContinuityWorkflowLinkage()
    assert linkage is not None
