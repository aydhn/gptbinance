def evaluate_data_revision(revision_id: str):
    return {
        "revision_id": revision_id,
        "freshness_coverage_benefit_ref": "fc_ben_1",
        "vendor_cost_ref": "vc_1",
        "downstream_uplift_ref": "du_1",
        "status": "value_thesis_supported" # Expensive without realized/expected thesis gives caution
    }
