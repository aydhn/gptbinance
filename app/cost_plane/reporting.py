class CostReporter:
    def generate_summary(self, data: dict) -> str:
        report = []
        report.append("=== Cost Plane Summary ===")
        report.append(f"Cost Objects: {data.get('cost_objects_count', 0)}")
        report.append(f"Spend Records: {data.get('spend_records_count', 0)}")
        report.append(f"Active Budgets: {data.get('budgets_count', 0)}")
        report.append(f"Trust Verdict: {data.get('trust_verdict', 'unknown')}")
        return "\n".join(report)
