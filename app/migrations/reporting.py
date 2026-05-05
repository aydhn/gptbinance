from typing import List
from app.migrations.models import MigrationPlan, MigrationDebtRecord


class ReportingEngine:
    @staticmethod
    def generate_plan_summary(plan: MigrationPlan) -> str:
        summary = f"Migration Plan {plan.id}\n"
        summary += "=" * 40 + "\n"
        summary += f"Steps: {len(plan.steps)}\n"
        for step in plan.steps:
            summary += f"  - Order {step.order}: {step.migration_id}\n"
        return summary

    @staticmethod
    def generate_debt_summary(debt_records: List[MigrationDebtRecord]) -> str:
        if not debt_records:
            return "No migration debt.\n"
        summary = "Migration Debt Summary\n"
        summary += "=" * 40 + "\n"
        for rec in debt_records:
            summary += f"[{rec.severity.value}] {rec.migration_id} in {rec.domain.value} - {rec.status.value}\n"
        return summary
