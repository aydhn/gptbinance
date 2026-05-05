from app.migrations.models import MigrationPlan, MigrationDryRunResult
from app.migrations.exceptions import DryRunFailure


class DryRunEngine:
    def simulate(self, plan: MigrationPlan) -> MigrationDryRunResult:
        # Simulate dry run logic
        try:
            return MigrationDryRunResult(
                plan_id=plan.id,
                expected_state_deltas={"config": "v1 -> v2"},
                touched_files=["config.json"],
                compatibility_expectations="Backward compatible read, write requires v2",
                potential_side_effects=["Old replays may need compatibility shims"],
                expected_verification_outcomes=[
                    "Version check passes",
                    "Schema validates",
                ],
                is_noop=False,
                simulation_logs=[
                    "Dry run started",
                    "Simulating step 1",
                    "Dry run finished",
                ],
            )
        except Exception as e:
            raise DryRunFailure(f"Dry run failed: {str(e)}")
