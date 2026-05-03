from app.ledger.models import LedgerAccount, LedgerAccountRef
from app.ledger.enums import LedgerAccountType, ScopeType
import uuid
from datetime import datetime, timezone


class LedgerAccountRegistry:
    def __init__(self):
        self._accounts = {}

    def create_account(
        self,
        name: str,
        acct_type: LedgerAccountType,
        scope: ScopeType,
        asset: str = None,
    ) -> LedgerAccount:
        ref = LedgerAccountRef(
            account_id=str(uuid.uuid4()),
            workspace_id="default",
            profile_id="default",
            scope=scope,
        )
        account = LedgerAccount(ref=ref, name=name, type=acct_type, asset=asset)
        self._accounts[ref.account_id] = account
        return account

    def get_account(self, account_id: str) -> LedgerAccount:
        return self._accounts.get(account_id)

    def list_accounts(self):
        return list(self._accounts.values())
