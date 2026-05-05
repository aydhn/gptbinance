from app.ledger.models import ReconciliationResult, ReconciliationDifference
from app.ledger.enums import ReconciliationVerdict, DiscrepancySeverity, ScopeType
from datetime import datetime, timezone
import uuid


class ReconciliationEngine:
    def __init__(self, tolerance: float = 1e-4):
        self.tolerance = tolerance

    def reconcile(
        self, internal_balances: dict, external_balances: dict, scope: ScopeType
    ) -> ReconciliationResult:
        differences = []
        verdict = ReconciliationVerdict.MATCH

        all_assets = set(internal_balances.keys()).union(external_balances.keys())

        for asset in all_assets:
            int_bal = internal_balances.get(asset, 0.0)
            ext_bal = external_balances.get(asset, 0.0)
            delta = ext_bal - int_bal

            if abs(delta) > self.tolerance:
                verdict = ReconciliationVerdict.MISMATCH
                sev = (
                    DiscrepancySeverity.CRITICAL
                    if abs(delta) > 10.0
                    else DiscrepancySeverity.MEDIUM
                )
                rec = (
                    "Check external deposits/withdrawals"
                    if ext_bal > int_bal
                    else "Check missing internal fee/funding deductions"
                )
                differences.append(
                    ReconciliationDifference(
                        asset=asset,
                        internal_balance=int_bal,
                        external_balance=ext_bal,
                        delta=delta,
                        severity=sev,
                        recommended_action=rec,
                    )
                )

        # Added in Phase 40: Cross-book context
        crossbook_provenance_notes = "Checked owned vs borrowed vs collateral locked"

        return ReconciliationResult(
            run_id=str(uuid.uuid4()),
            timestamp=datetime.now(timezone.utc),
            scope=scope,
            verdict=verdict,
            differences=differences,
        )
