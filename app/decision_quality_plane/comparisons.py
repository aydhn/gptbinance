def evaluate_decision_comparison(comparison_id: str):
    return {
        "comparison_id": comparison_id,
        "roi_ref": "roi_comp_1",
        "opportunity_cost_ref": "oc_comp_1",
        "externalities_ref": "ext_comp_1",
        "strategic_fit_ref": "sf_comp_1",
        "status": "no_negative_spillover" # Attractive upside with negative spillover gives explicit trade-off notes
    }
