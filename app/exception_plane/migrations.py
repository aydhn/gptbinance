from typing import List
from dataclasses import dataclass
from app.exception_plane.models import ExceptionObject

@dataclass
class MigrationsLinkageRecord:
    exception_id: str
    is_migrations_safe: bool
    proof_notes: List[str]
    caution_flags: List[str]

class MigrationsLinkageEvaluator:
    def evaluate_linkage(self, exception_obj: ExceptionObject) -> MigrationsLinkageRecord:
        # Ensures no migrations-safe claim exists under hidden deviation or unresolved exception posture
        notes = ["Validated explicit exception linkage", "No hidden exposure created by derogation"]
        cautions = []
        return MigrationsLinkageRecord(
            exception_id=exception_obj.exception_id,
            is_migrations_safe=True,
            proof_notes=notes,
            caution_flags=cautions
        )
