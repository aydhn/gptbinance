import sys

content = ""
with open("app/main.py", "r") as f:
    content = f.read()

import_statement = (
    "from app.reliability.cli import add_reliability_args, handle_reliability_cli\n"
)
if "add_reliability_args" not in content:
    content = content.replace(
        "from app.main_activation_cli import",
        import_statement + "from app.main_activation_cli import",
    )

add_args_statement = "    add_reliability_args(parser)\n"
if "add_reliability_args(parser)" not in content:
    content = content.replace(
        "    add_activation_args(parser)",
        add_args_statement + "    add_activation_args(parser)",
    )

handler_statement = """
    reliability_commands = [
        "show_reliability_summary", "show_slo_registry", "show_error_budgets",
        "show_burn_rate", "show_readiness_decay", "show_health_scorecards",
        "show_freeze_recommendations", "show_operational_holds", "show_reliability_trends",
        "show_operational_cadence", "show_reliability_evidence", "show_domain_health"
    ]
    if any(getattr(args, cmd, False) for cmd in reliability_commands):
        handle_reliability_cli(args)
        sys.exit(0)
"""

if "reliability_commands =" not in content:
    content = content.replace(
        "if any(getattr(args, cmd, False) for cmd in activation_commands):",
        handler_statement
        + "\n    if any(getattr(args, cmd, False) for cmd in activation_commands):",
    )

with open("app/main.py", "w") as f:
    f.write(content)
