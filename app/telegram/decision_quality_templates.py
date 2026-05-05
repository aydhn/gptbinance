DECISION_FUNNEL_DEGRADED = """
⚠️ <b>Decision Funnel Degraded</b>
<i>The signal-to-action funnel is showing an abnormal drop-off rate.</i>

<b>Stage:</b> {stage}
<b>Drop-off Rate:</b> {drop_off_rate}%
<b>Primary Block Reason:</b> {primary_reason}

<i>Please review the diagnostic logs to ensure safety boundaries aren't incorrectly configured.</i>
"""

BLOCK_CLUSTER_WARNING = """
🚨 <b>Block Reason Cluster Elevated</b>
<i>A specific block reason is triggering unusually often.</i>

<b>Reason Class:</b> {reason_class}
<b>Count:</b> {count} in the last {timeframe}
<b>Severity:</b> {severity}

<i>Review policy or market truth constraints for potential issues.</i>
"""

OPPORTUNITY_QUALITY_SUMMARY = """
📊 <b>Opportunity Quality Summary</b>
<i>Snapshot of the decision quality over the last {timeframe}.</i>

<b>Total Opportunities:</b> {total}
<b>Executed:</b> {executed}
<b>Blocked:</b> {blocked}
<b>Skipped/Suppressed:</b> {skipped}

<b>Top Friction Source:</b> {top_friction}

<i>Run `--show-opportunity-quality` for details.</i>
"""
