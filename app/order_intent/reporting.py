from app.order_intent.models import IntentCompilationResult


class PlanReporter:
    def summarize(self, result: IntentCompilationResult) -> str:
        summary = [
            f"--- Intent Compile Summary: {result.audit_record.run_id} ---",
            f"Intent: {result.intent.intent_type.value} on {result.intent.symbol} ({result.intent.size} {result.intent.side.value})",
            f"Verdict: {result.verdict.value}",
        ]

        if result.plan:
            summary.append(f"Plan Type: {result.plan.plan_type.value}")
            for leg in result.plan.legs:
                leg_str = f"  Leg [{leg.leg_id}]: {leg.leg_type.value} {leg.symbol} size={leg.size}"
                if leg.side:
                    leg_str += f" side={leg.side.value}"
                if leg.reduce_only:
                    leg_str += " (ReduceOnly)"
                if leg.close_position:
                    leg_str += " (ClosePos)"
                summary.append(leg_str)

        if result.validation_result and not result.validation_result.is_valid:
            summary.append(f"Validation Errors: {result.validation_result.errors}")

        return "\n".join(summary)
