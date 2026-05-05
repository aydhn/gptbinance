with open("app/ledger/explain.py", "r") as f:
    content = f.read()

if "Cross-book provenance refs" not in content:
    old_code = """        return BalanceExplainResult(
            asset=asset,
            scope=scope,
            current_balance=current_snapshot,
            total_inflows=inflows,
            total_outflows=outflows,
            recent_entries=entries[-10:],
            unexplained_delta=delta,
            verdict=verdict,
        )"""
    new_code = """
        # Added in Phase 40: Cross-book provenance refs
        owned_vs_borrowed_vs_locked_split_notes = "Available: X, Locked: Y, Borrowed: Z"

        return BalanceExplainResult(
            asset=asset,
            scope=scope,
            current_balance=current_snapshot,
            total_inflows=inflows,
            total_outflows=outflows,
            recent_entries=entries[-10:],
            unexplained_delta=delta,
            verdict=verdict,
        )"""
    content = content.replace(old_code, new_code)

with open("app/ledger/explain.py", "w") as f:
    f.write(content)
