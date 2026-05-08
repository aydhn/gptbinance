import pytest
from app.ledger_plane.entries import TypedLedgerEntryBuilder
from app.ledger_plane.enums import LedgerClass

def test_typed_ledger_entry_creation():
    entry = TypedLedgerEntryBuilder.build(
        ledger_class=LedgerClass.FILL,
        asset="USDT",
        amount=100.0,
        account_scope="binance_spot",
        source_ref="fill_123"
    )
    assert entry.ledger_class == LedgerClass.FILL
    assert entry.asset == "USDT"
    assert entry.amount == 100.0
    assert entry.account_scope == "binance_spot"
    assert entry.source_ref == "fill_123"
    assert entry.id is not None
