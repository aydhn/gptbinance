import re

with open('app/main.py', 'r') as f:
    content = f.read()

parser_args = """
    parser.add_argument("--run-job-now", action="store_true", help="Run job manually")
    parser.add_argument("--job-id", type=str, help="Job ID")

    # Phase 26 Observability
    parser.add_argument("--show-metrics-summary", action="store_true")
    parser.add_argument("--show-component-health", action="store_true")
    parser.add_argument("--component", type=str)
    parser.add_argument("--show-system-health", action="store_true")
    parser.add_argument("--show-active-alerts", action="store_true")
    parser.add_argument("--show-alert-history", action="store_true")
    parser.add_argument("--show-alert-correlations", action="store_true")
    parser.add_argument("--show-slo-summary", action="store_true")
    parser.add_argument("--show-observability-digest", action="store_true")
    parser.add_argument("--scope", type=str, default="daily")
    parser.add_argument("--verify-runbook-mapping", action="store_true")
    parser.add_argument("--run-observability-checks", action="store_true")
"""

content = content.replace("""    parser.add_argument("--run-job-now", action="store_true", help="Run job manually")
    parser.add_argument("--job-id", type=str, help="Job ID")""", parser_args)

with open('app/main.py', 'w') as f:
    f.write(content)
