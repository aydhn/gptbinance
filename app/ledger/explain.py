from app.crossbook.reporting import CrossBookReporter
from app.ledger.models import BalanceExplainResult
from app.ledger.enums import ScopeType, LedgerVerdict
from app.ledger.provenance import ProvenanceTracker


class BalanceExplainer:
    def __init__(self, provenance: ProvenanceTracker):
        self.provenance = provenance

    def explain(
        self, asset: str, scope: ScopeType, current_snapshot: float
    ) -> BalanceExplainResult:
        entries = self.provenance.get_lineage(asset)
        inflows = sum(
            p.amount
            for e in entries
            for p in e.postings
            if p.asset == asset and p.direction == 1
        )
        outflows = sum(
            p.amount
            for e in entries
            for p in e.postings
            if p.asset == asset and p.direction == -1
        )
        calculated_balance = inflows - outflows

        delta = current_snapshot - calculated_balance
        verdict = (
            LedgerVerdict.VERIFIED if abs(delta) < 1e-4 else LedgerVerdict.SUSPICIOUS
        )

# Cross-book integration: distinguish owned vs borrowed vs collateral locked
        reporter = CrossBookReporter()
        crossbook_summary = reporter.generate_summary()
        import logging
        logger = logging.getLogger(__name__)
        logger.info(f"Balance explanation cross-book provenance refs: {crossbook_summary}")

        return BalanceExplainResult(
            asset=asset,
            scope=scope,
            current_balance=current_snapshot,
            total_inflows=inflows,
            total_outflows=outflows,
            recent_entries=entries[-10:],
            unexplained_delta=delta,
            verdict=verdict,
        )
