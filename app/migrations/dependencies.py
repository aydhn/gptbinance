from typing import List, Dict
from app.migrations.models import MigrationDefinition
from app.migrations.exceptions import DependencyResolutionError


class MigrationDependencyResolver:
    def resolve(
        self,
        migrations: List[MigrationDefinition],
        available_migrations: Dict[str, MigrationDefinition],
    ) -> List[MigrationDefinition]:
        graph = {}
        in_degree = {}

        for m in migrations:
            graph[m.id] = []
            in_degree[m.id] = 0

        for m in migrations:
            for dep in m.dependencies:
                if dep.required and dep.migration_id not in available_migrations:
                    raise DependencyResolutionError(
                        f"Missing required dependency: {dep.migration_id} for migration {m.id}"
                    )

                # Simple topological logic considering only passed migrations
                if dep.migration_id in [mig.id for mig in migrations]:
                    graph[dep.migration_id].append(m.id)
                    in_degree[m.id] += 1

        queue = [m_id for m_id, degree in in_degree.items() if degree == 0]
        resolved_order = []

        while queue:
            current_id = queue.pop(0)
            resolved_order.append(available_migrations[current_id])

            for neighbor in graph[current_id]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        if len(resolved_order) != len(migrations):
            raise DependencyResolutionError("Cyclic dependency detected in migrations")

        return resolved_order
