from app.activation.base import RevertPlannerBase
from app.activation.models import RevertPlan, ActiveSetRecord
from app.activation.enums import RevertClass, ActiveSetStatus


class RevertPlanner(RevertPlannerBase):
    def __init__(self, repository):
        self.repository = repository

    def plan_revert(self, intent_id: str) -> RevertPlan:
        # Find active record for intent
        snapshot = self.repository.get_snapshot("latest")  # Simplified lookup
        target_record = None
        prior_record = None
        if snapshot:
            for record in snapshot.active_records:
                if record.intent_id == intent_id:
                    target_record = record
            # Find superseded record with same scope
            if target_record:
                for record in snapshot.active_records:
                    # Check if it was superseded and shares the same core scope definitions.
                    # In a full app this would be a robust overlap check.
                    if (
                        record.status == ActiveSetStatus.SUPERSEDED
                        and record.scope.allowed_profiles
                        == target_record.scope.allowed_profiles
                    ):
                        prior_record = record

        if not target_record:
            return RevertPlan(
                intent_id=intent_id,
                revert_class=RevertClass.NO_REVERT_AVAILABLE,
                steps=["Cannot find active record for intent"],
                risks=["Target active set not found"],
            )

        if not prior_record:
            return RevertPlan(
                intent_id=intent_id,
                revert_class=RevertClass.PARTIAL_SCOPE_REVERT,  # Or NO_REVERT depending on policy
                steps=[
                    f"Disable active set for intent {intent_id}. No prior set found to restore."
                ],
                risks=["This will leave the scope without an active candidate."],
            )

        return RevertPlan(
            intent_id=intent_id,
            revert_class=RevertClass.FULL_REVERT,
            prior_active_set_ref=prior_record.record_id,
            steps=[
                f"Halt intent {intent_id}",
                f"Restore prior intent {prior_record.intent_id}",
                "Verify state after revert",
            ],
            risks=[
                "Inflight orders may need manual intervention",
                "Reconciliation required after revert",
            ],
        )
