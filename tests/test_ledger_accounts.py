from app.ledger.accounts import LedgerAccountRegistry
from app.ledger.enums import LedgerAccountType, ScopeType


def test_account_creation():
    reg = LedgerAccountRegistry()
    acct = reg.create_account(
        "Main USDT", LedgerAccountType.ASSET, ScopeType.PAPER, "USDT"
    )
    assert acct.name == "Main USDT"
    assert acct.type == LedgerAccountType.ASSET
    assert acct.ref.scope == ScopeType.PAPER
