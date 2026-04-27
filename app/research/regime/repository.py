from datetime import datetime
from typing import Dict, Any, Optional
from app.research.regime.engine import RegimeEngine
from app.research.regime.storage import RegimeStorage
from app.research.regime.models import (
    RegimeFeatureBundle,
    RegimeSnapshot,
    MultiTimeframeRegimeContext,
)
from app.research.regime.explain import explain_context
from app.research.regime.mtf_context import build_mtf_context


class RegimeRepository:
    def __init__(self):
        self.engine = RegimeEngine()
        self.storage = RegimeStorage()

    def evaluate_and_store(
        self, timestamp: datetime, symbol: str, interval: str, features: Dict[str, Any]
    ) -> RegimeSnapshot:
        bundle = RegimeFeatureBundle(
            timestamp=timestamp, symbol=symbol, interval=interval, features=features
        )

        context = self.engine.evaluate_bundle(bundle)

        snapshot = RegimeSnapshot(
            timestamp=timestamp, symbol=symbol, interval=interval, context=context
        )

        self.storage.save_snapshot(snapshot)
        return snapshot

    def build_mtf(
        self, base_snapshot: RegimeSnapshot, higher_snapshots: Dict[str, RegimeSnapshot]
    ) -> MultiTimeframeRegimeContext:
        higher_contexts = {k: v.context for k, v in higher_snapshots.items()}
        mtf_context = build_mtf_context(base_snapshot.context, higher_contexts)
        base_snapshot.mtf_context = mtf_context
        # We might want to re-save the base snapshot here, but avoiding for simplicity
        return mtf_context

    def get_last_snapshot(self, symbol: str, interval: str) -> Optional[RegimeSnapshot]:
        snaps = self.storage.load_recent_snapshots(symbol, interval, limit=1)
        return snaps[0] if snaps else None

    def summarize(self, symbol: str, interval: str) -> str:
        snap = self.get_last_snapshot(symbol, interval)
        if not snap:
            return f"No regime data found for {symbol} {interval}."
        return explain_context(snap.context)
