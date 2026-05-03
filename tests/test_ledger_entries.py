from app.ledger.entries import LedgerEntryManager
from app.ledger.postings import PostingBuilder
from app.ledger.accounts import LedgerAccountRegistry
from app.ledger.enums import (
    LedgerAccountType,
    ScopeType,
    LedgerEntryType,
    MovementClass,
)
from app.ledger.exceptions import PostingImbalanceError
import pytest


def test_entry_balancing():
    reg = LedgerAccountRegistry()
    asset_acct = reg.create_account(
        "Asset", LedgerAccountType.ASSET, ScopeType.PAPER, "USDT"
    )
    equity_acct = reg.create_account(
        "Equity", LedgerAccountType.EQUITY, ScopeType.PAPER, "USDT"
    )

    postings = PostingBuilder.create_pair(
        100.0, "USDT", asset_acct.ref, equity_acct.ref
    )

    entry = LedgerEntryManager.validate_and_create(
        "entry_1",
        postings,
        LedgerEntryType.DEPOSIT,
        "ref_1",
        ScopeType.PAPER,
        MovementClass.INFLOW,
    )
    assert entry.entry_id == "entry_1"


def test_imbalance_raises():
    reg = LedgerAccountRegistry()
    asset_acct = reg.create_account(
        "Asset", LedgerAccountType.ASSET, ScopeType.PAPER, "USDT"
    )
    equity_acct = reg.create_account(
        "Equity", LedgerAccountType.EQUITY, ScopeType.PAPER, "USDT"
    )

    # Intentionally corrupt the amount
    postings = PostingBuilder.create_pair(
        100.0, "USDT", asset_acct.ref, equity_acct.ref
    )
    postings[1].amount = 99.0

    with pytest.raises(PostingImbalanceError):
        LedgerEntryManager.validate_and_create(
            "entry_1",
            postings,
            LedgerEntryType.DEPOSIT,
            "ref_1",
            ScopeType.PAPER,
            MovementClass.INFLOW,
        )
