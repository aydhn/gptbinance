import pytest
import os
from datetime import datetime, timezone
from app.portfolio.models import (
    PortfolioSummary,
    PortfolioDecisionBatch,
    ConcentrationSeverity,
)
from app.portfolio.storage import PortfolioStorage


def test_storage():
    db_path = "test_portfolio.sqlite"
    if os.path.exists(db_path):
        os.remove(db_path)

    storage = PortfolioStorage(db_path=db_path)

    timestamp = datetime.now(timezone.utc)
    summary = PortfolioSummary(
        timestamp=timestamp,
        run_id="run1",
        total_intents_evaluated=10,
        total_approved=5,
        total_reduced=2,
        total_deferred=1,
        total_rejected=2,
        total_allocated_notional=1000.0,
        concentration_severity=ConcentrationSeverity.NORMAL,
    )

    storage.save_summary(summary)
    loaded = storage.load_summary("run1")

    assert loaded is not None
    assert loaded.total_intents_evaluated == 10
    assert loaded.total_allocated_notional == 1000.0

    # Clean up
    if os.path.exists(db_path):
        os.remove(db_path)
