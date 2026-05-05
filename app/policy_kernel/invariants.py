# Stub for policy invariants
def check_invariants(context):
    if context.market_truth.get("clock_integrity") == "BROKEN":
        raise Exception("Invariant failed: Broken market clock integrity")
