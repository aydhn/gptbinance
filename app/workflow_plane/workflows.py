from app.workflow_plane.registry import registry
from app.workflow_plane.models import WorkflowDefinition
from typing import List

class WorkflowManager:
    def get_workflows(self) -> List[WorkflowDefinition]:
        return registry.get_all()
