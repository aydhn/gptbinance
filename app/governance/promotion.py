# Mock Governance Promotion
def get_promotion_readiness(bundle_id: str, qualification_run_id: str):
    return {
        "bundle_id": bundle_id,
        "qualification_ref": qualification_run_id,
        "certified_for_shadow": True,
        "certified_for_testnet": True,
        "ready_for_promotion": True,
    }
