class TelegramTemplates:
    PERF_REGRESSION_WARNING = "⚠️ Perf Regression Detected: {msg}"
    HOST_CAPACITY_CAUTION = "⚠️ Host Capacity Caution: {msg}"
    LATENCY_BUDGET_BREACH = "⏱️ Latency Budget Breach: {msg}"
    WEEKLY_PERF_DIGEST = "📊 Weekly Perf Digest:\n{msg}"
    QUALIFICATION_PERF_BLOCKER = "🛑 Qualification Blocked by Perf: {msg}"

    DATA_GOVERNANCE_ALERT = """
🚨 <b>Data Governance Alert</b>
Type: {event_type}
Severity: {severity}
Dataset: {dataset_id} (v{version})
Details: {details}
Runbook: {runbook_url}
"""
    DATA_GOVERNANCE_SUMMARY = """
📊 <b>Data Governance Summary</b>
Total Datasets: {total_datasets}
Trusted: {trusted_count}
Caution: {caution_count}
Blocked: {blocked_count}
"""
