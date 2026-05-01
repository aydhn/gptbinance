from typing import List, Dict, Set
from app.automation.models import WorkflowDefinition
from app.automation.exceptions import DependencyError


def check_cycles(workflow: WorkflowDefinition) -> None:
    """Check for cycles in a workflow definition using DFS."""
    adj_list: Dict[str, List[str]] = {
        step.id: step.dependencies for step in workflow.steps
    }
    visited: Set[str] = set()
    rec_stack: Set[str] = set()

    def dfs(node: str) -> bool:
        visited.add(node)
        rec_stack.add(node)

        for neighbor in adj_list.get(node, []):
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True

        rec_stack.remove(node)
        return False

    for step in workflow.steps:
        if step.id not in visited:
            if dfs(step.id):
                raise DependencyError(f"Cycle detected in workflow {workflow.id}")


def get_execution_order(workflow: WorkflowDefinition) -> List[str]:
    """Get a valid execution order for workflow steps (Topological Sort)."""
    check_cycles(workflow)

    adj_list: Dict[str, List[str]] = {
        step.id: step.dependencies for step in workflow.steps
    }
    visited: Set[str] = set()
    order: List[str] = []

    def dfs(node: str):
        visited.add(node)
        # To get dependencies to run first, visit them before appending node
        for dep in adj_list.get(node, []):
            if dep not in visited:
                dfs(dep)
        order.append(node)

    for step in workflow.steps:
        if step.id not in visited:
            dfs(step.id)

    return order
