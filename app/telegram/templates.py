# Integration hook for ledger accounting phase 35

# Ledger accounting integration hook for phase 35 (balance provenance)


CAPITAL_ESCALATION_BLOCKED_TEMPLATE = """
⚠️ *CAPITAL ESCALATION BLOCKED*
*Target Tier*: {target_tier}
*Blockers*:
{blockers}
"""

CAPITAL_FREEZE_RECOMMENDED_TEMPLATE = """
❄️ *CAPITAL FREEZE RECOMMENDED*
*Reasons*:
{reasons}
"""

LOSS_BUDGET_BREACH_TEMPLATE = """
🚨 *LOSS BUDGET BREACH*
*Details*:
{details}
"""

TRANCHE_ACTIVATION_CAUTION_TEMPLATE = """
⚠️ *TRANCHE ACTIVATION CAUTION*
*Tranche ID*: {tranche_id}
*Warnings*:
{warnings}
"""

STALE_CAPITAL_EVIDENCE_TEMPLATE = """
⚠️ *STALE CAPITAL EVIDENCE DETECTED*
*Stale Items*:
{stale_items}
"""

CAPITAL_POSTURE_DIGEST_TEMPLATE = """
📊 *CAPITAL POSTURE DIGEST*
*Active Tier*: {active_tier}
*State*: {state}
*Deployed Capital*: {deployed_capital}
*Headroom*: {headroom}
"""

# Added in Phase 40
CROSSBOOK_FAKE_HEDGE_TEMPLATE = """
🚨 *CROSSBOOK FAKE HEDGE DETECTED*
*Asset*: {asset}
*Reason*:
{reason}
"""

CROSSBOOK_COLLATERAL_PRESSURE_TEMPLATE = """
⚠️ *COLLATERAL PRESSURE WARNING*
*Pressure Ratio*: {ratio}
*Details*:
{details}
"""

CROSSBOOK_COMBINED_EXPOSURE_BREACH_TEMPLATE = """
🚨 *COMBINED EXPOSURE BREACH*
*Asset*: {asset}
*Amount*: {amount}
*Details*:
{details}
"""
