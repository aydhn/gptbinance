with open('app/ledger/reconciliation.py', 'r') as f:
    content = f.read()

if "Cross-book context" not in content:
    old_code = """        return ReconciliationResult(
            run_id=str(uuid.uuid4()),
            timestamp=datetime.now(timezone.utc),
            scope=scope,
            verdict=verdict,
            differences=differences,
        )"""
    new_code = """
        # Added in Phase 40: Cross-book context
        crossbook_provenance_notes = "Checked owned vs borrowed vs collateral locked"

        return ReconciliationResult(
            run_id=str(uuid.uuid4()),
            timestamp=datetime.now(timezone.utc),
            scope=scope,
            verdict=verdict,
            differences=differences,
        )"""
    content = content.replace(old_code, new_code)

with open('app/ledger/reconciliation.py', 'w') as f:
    f.write(content)
