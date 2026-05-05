from typing import Optional
from app.migrations.models import (
    MigrationDefinition,
    MigrationPlan,
)
from app.migrations.storage import storage_engine


class MigrationRepository:
    def save_definition(self, definition: MigrationDefinition) -> None:
        storage_engine.save("definitions", definition.id, definition)

    def load_definition(self, id: str) -> Optional[MigrationDefinition]:
        data = storage_engine.load("definitions", id)
        return MigrationDefinition(**data) if data else None

    def save_plan(self, plan: MigrationPlan) -> None:
        storage_engine.save("plans", plan.id, plan)

    def load_plan(self, id: str) -> Optional[MigrationPlan]:
        data = storage_engine.load("plans", id)
        return MigrationPlan(**data) if data else None


migration_repo = MigrationRepository()
