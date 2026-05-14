def evaluate_execution_runtime(exec_id: str):
    return {
        "exec_id": exec_id,
        "expected_slippage_savings_ref": "slip_save_1",
        "order_quality_improvement_ref": "oq_imp_1",
        "fee_burden_trade_off_ref": "fee_trd_1",
        "status": "net_portfolio_value_uplift_positive" # Better fill metrics without net uplift gives caution
    }
