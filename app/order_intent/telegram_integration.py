from app.order_intent.models import IntentCompilationResult
from app.order_intent.enums import CompileVerdict


class OrderIntentNotifier:
    def notify_compile_result(self, result: IntentCompilationResult):
        # Mock telegram notifier
        if result.verdict in [CompileVerdict.BLOCKED, CompileVerdict.FAILED]:
            print(
                f"[TELEGRAM ALERT] CRITICAL: Intent Compile Failed/Blocked. Run ID: {result.audit_record.run_id}. Reasons: {result.audit_record.reasons}"
            )
        elif result.verdict == CompileVerdict.CAUTION:
            print(
                f"[TELEGRAM ALERT] WARNING: Intent Compile Caution. Run ID: {result.audit_record.run_id}. Reasons: {result.audit_record.reasons}"
            )
        # We don't spam success logs to telegram normally, unless requested.
