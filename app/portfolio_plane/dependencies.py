from typing import Dict, Optional
from app.portfolio_plane.models import DependencyConstraint
from app.portfolio_plane.exceptions import InvalidDependencyConstraintError, PortfolioStorageError

class DependencyManager:
    def __init__(self):
        self._constraints: Dict[str, DependencyConstraint] = {}

    def register(self, constraint: DependencyConstraint):
        if constraint.dependency_id in self._constraints:
            raise PortfolioStorageError(f"Dependency {constraint.dependency_id} already exists")
        if constraint.source_portfolio_id == constraint.target_portfolio_id:
            raise InvalidDependencyConstraintError("A portfolio object cannot depend on itself.")
        self._constraints[constraint.dependency_id] = constraint

    def get(self, constraint_id: str) -> Optional[DependencyConstraint]:
        return self._constraints.get(constraint_id)

    def get_all(self) -> Dict[str, DependencyConstraint]:
        return self._constraints.copy()
