import re

with open("app/telegram/notifier.py", "r") as f:
    content = f.read()

notifier_logic = """
    def notify_capital_escalation_blocked(self, tier: str, blockers: list):
        \"\"\"Send notification when capital escalation is blocked.\"\"\"
        if not self._check_rate_limit("capital_escalation_blocked"):
            return

        msg = f"⚠️ *CAPITAL ESCALATION BLOCKED*\\nTier: {tier}\\nBlockers: {', '.join(blockers)}"
        self._send_message(msg)

    def notify_capital_freeze_recommended(self, reasons: list):
        \"\"\"Send notification for capital freeze recommendation.\"\"\"
        if not self._check_rate_limit("capital_freeze_recommended"):
            return

        msg = f"❄️ *CAPITAL FREEZE RECOMMENDED*\\nReasons: {', '.join(reasons)}"
        self._send_message(msg)

    def notify_loss_budget_breach(self, breach_details: str):
        \"\"\"Send notification for loss budget breach.\"\"\"
        if not self._check_rate_limit("loss_budget_breach"):
            return

        msg = f"🚨 *LOSS BUDGET BREACH*\\nDetails: {breach_details}"
        self._send_message(msg)

    def notify_tranche_activated(self, tranche_id: str):
        \"\"\"Send notification when a tranche is activated.\"\"\"
        msg = f"🟢 *TRANCHE ACTIVATED*\\nTranche ID: {tranche_id}"
        self._send_message(msg)

    def notify_stale_capital_evidence(self, stale_items: list):
        \"\"\"Send notification for stale capital evidence.\"\"\"
        if not self._check_rate_limit("stale_capital_evidence"):
            return

        msg = f"⚠️ *STALE CAPITAL EVIDENCE*\\nItems: {', '.join(stale_items)}"
        self._send_message(msg)
"""

if "notify_capital_escalation_blocked" not in content:
    content = re.sub(r'(class TelegramNotifier.*?\n.*?)(?=class|$)', r'\1' + notifier_logic + '\n', content, count=1)

with open("app/telegram/notifier.py", "w") as f:
    f.write(content)

with open("app/telegram/templates.py", "r") as f:
    content = f.read()

template_logic = """
CAPITAL_ESCALATION_BLOCKED_TEMPLATE = \"\"\"
⚠️ *CAPITAL ESCALATION BLOCKED*
*Target Tier*: {target_tier}
*Blockers*:
{blockers}
\"\"\"

CAPITAL_FREEZE_RECOMMENDED_TEMPLATE = \"\"\"
❄️ *CAPITAL FREEZE RECOMMENDED*
*Reasons*:
{reasons}
\"\"\"

LOSS_BUDGET_BREACH_TEMPLATE = \"\"\"
🚨 *LOSS BUDGET BREACH*
*Details*:
{details}
\"\"\"

TRANCHE_ACTIVATION_CAUTION_TEMPLATE = \"\"\"
⚠️ *TRANCHE ACTIVATION CAUTION*
*Tranche ID*: {tranche_id}
*Warnings*:
{warnings}
\"\"\"

STALE_CAPITAL_EVIDENCE_TEMPLATE = \"\"\"
⚠️ *STALE CAPITAL EVIDENCE DETECTED*
*Stale Items*:
{stale_items}
\"\"\"

CAPITAL_POSTURE_DIGEST_TEMPLATE = \"\"\"
📊 *CAPITAL POSTURE DIGEST*
*Active Tier*: {active_tier}
*State*: {state}
*Deployed Capital*: {deployed_capital}
*Headroom*: {headroom}
\"\"\"
"""
if "CAPITAL_ESCALATION_BLOCKED_TEMPLATE" not in content:
    content += "\n" + template_logic

with open("app/telegram/templates.py", "w") as f:
    f.write(content)
