with open("app/telegram/templates.py", "r") as f:
    content = f.read()

if "CROSSBOOK_FAKE_HEDGE_TEMPLATE" not in content:
    content += """
# Added in Phase 40
CROSSBOOK_FAKE_HEDGE_TEMPLATE = \"\"\"
🚨 *CROSSBOOK FAKE HEDGE DETECTED*
*Asset*: {asset}
*Reason*:
{reason}
\"\"\"

CROSSBOOK_COLLATERAL_PRESSURE_TEMPLATE = \"\"\"
⚠️ *COLLATERAL PRESSURE WARNING*
*Pressure Ratio*: {ratio}
*Details*:
{details}
\"\"\"

CROSSBOOK_COMBINED_EXPOSURE_BREACH_TEMPLATE = \"\"\"
🚨 *COMBINED EXPOSURE BREACH*
*Asset*: {asset}
*Amount*: {amount}
*Details*:
{details}
\"\"\"
"""
with open("app/telegram/templates.py", "w") as f:
    f.write(content)
