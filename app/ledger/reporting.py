class LedgerReporter:
    @staticmethod
    def format_summary(entries_count, active_accounts):
        return f"LEDGER SUMMARY\nEntries: {entries_count}\nActive Accounts: {active_accounts}\nStatus: IMMUTABLE"
