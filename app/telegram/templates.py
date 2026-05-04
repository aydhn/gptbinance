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
FAKE_HEDGE_DETECTED_TEMPLATE = """
⚠️ *FAKE HEDGE DETECTED*
*Details*:
{details}
"""

COLLATERAL_PRESSURE_WARNING_TEMPLATE = """
⚠️ *COLLATERAL PRESSURE WARNING*
*Pressure*: {pressure}
"""

BORROW_DEPENDENCY_CAUTION_TEMPLATE = """
⚠️ *BORROW DEPENDENCY CAUTION*
*Dependency Class*: {dependency_class}
"""

COMBINED_EXPOSURE_BREACH_TEMPLATE = """
🚨 *COMBINED EXPOSURE BREACH*
*Details*:
{details}
"""

FUNDING_BURDEN_DIGEST_TEMPLATE = """
📊 *FUNDING BURDEN DIGEST*
*Symbol*: {symbol}
*Expected Drag*: {drag}
"""

CROSSBOOK_POSTURE_SUMMARY_TEMPLATE = """
📊 *CROSSBOOK POSTURE SUMMARY*
*Summary*:
{summary}
"""
