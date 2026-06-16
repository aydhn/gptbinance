def generate_summary_report(waterfall_id: str, data: dict) -> str:
    return f"Waterfall Report for {waterfall_id}:\nPools: {data.get('pools')}\nDistributions: {data.get('distributions')}"
