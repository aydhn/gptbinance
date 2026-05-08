import pytest
from app.ledger_plane.transfers import TransferManager
from app.ledger_plane.enums import TransferClass

def test_transfer_creation():
    record = TransferManager.build_record(
        transfer_class=TransferClass.INTERNAL,
        asset="USDT",
        amount=100.0,
        source_scope="binance_spot",
        target_scope="binance_futures",
        status="settled"
    )
    chain = TransferManager.build_chain([record])
    assert len(chain.records) == 1
    assert chain.records[0].status == "settled"
    assert chain.records[0].source_scope == "binance_spot"
