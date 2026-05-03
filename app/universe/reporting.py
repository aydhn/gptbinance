from app.universe.models import ProductInstrument, TradabilityReport, LiquiditySnapshot, SpreadSnapshot, UniverseSnapshot, UniverseDiff, LifecycleEvent, UniverseImpactReport

class UniverseReporter:
    def format_instrument(self, inst: ProductInstrument) -> str:
        s = f"Symbol: {inst.ref.symbol} ({inst.ref.canonical_symbol}) | Product: {inst.ref.product_type.value}\n"
        s += f"  Status: {inst.status.value}\n"
        s += f"  Freshness: {inst.freshness.value} (Last Update: {inst.last_update.isoformat()})\n"
        if inst.filters.tick_size:
            s += f"  Tick Size: {inst.filters.tick_size.tick_size} (Min: {inst.filters.tick_size.min_price})\n"
        if inst.filters.step_size:
            s += f"  Step Size: {inst.filters.step_size.step_size} (Min: {inst.filters.step_size.min_qty})\n"
        return s

    def format_tradability(self, rep: TradabilityReport) -> str:
        s = f"[{rep.ref.symbol}] Verdict: {rep.verdict.value} | Class: {rep.tradability_class.value}\n"
        if rep.reasons:
            s += "  Reasons:\n"
            for r in rep.reasons:
                s += f"    - {r}\n"
        return s

    def format_liquidity(self, liq: LiquiditySnapshot) -> str:
        return f"[{liq.ref.symbol}] Vol: {liq.rolling_volume:.2f} | Quote Vol: {liq.quote_volume:.2f} | Severity: {liq.severity.value}"

    def format_spread(self, spread: SpreadSnapshot) -> str:
        return f"[{spread.ref.symbol}] Spread: {spread.bid_ask_spread:.6f} ({spread.relative_spread*10000:.2f} bps) | Severity: {spread.severity.value}"

    def format_snapshot(self, snap: UniverseSnapshot) -> str:
        s = f"Snapshot: {snap.snapshot_id} | Profile: {snap.profile.value} | Created: {snap.created_at.isoformat()}\n"
        s += f"  Eligible: {len(snap.eligible_instruments)}\n"
        s += f"  Caution:  {len(snap.caution_instruments)}\n"
        s += f"  Blocked:  {len(snap.blocked_instruments)}\n"
        return s

    def format_diff(self, diff: UniverseDiff) -> str:
        s = f"Diff: {diff.diff_id} ({diff.old_snapshot_id} -> {diff.new_snapshot_id})\n"
        s += f"  Added:   {len(diff.added)}\n"
        s += f"  Removed: {len(diff.removed)}\n"
        s += f"  Status Changed: {len(diff.status_changed)}\n"
        s += f"  Elig Changed:   {len(diff.eligibility_changed)}\n"
        return s

    def format_lifecycle(self, evt: LifecycleEvent) -> str:
        return f"[{evt.event_time.isoformat()}] {evt.ref.symbol}: {evt.event_type.value} - {evt.description}"

    def format_impact(self, imp: UniverseImpactReport) -> str:
        s = f"Impact Report: {imp.report_id} | Diff: {imp.diff_id} | Severity: {imp.severity}\n"
        if imp.impacted_strategies:
            s += f"  Strategies: {', '.join(imp.impacted_strategies)}\n"
        if imp.recommendations:
            s += "  Recommendations:\n"
            for r in imp.recommendations:
                s += f"    - {r}\n"
        return s
