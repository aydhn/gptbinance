import re

with open("app/main.py", "r") as f:
    content = f.read()

suspension_args = """
    parser.add_argument("--show-suspension-registry", action="store_true")
    parser.add_argument("--show-suspension-object", help="--show-suspension-object --suspension-id <id>")
    parser.add_argument("--suspension-id")
    parser.add_argument("--show-suspensions", action="store_true")
    parser.add_argument("--show-suspension-triggers", action="store_true")
    parser.add_argument("--show-suspension-scopes", action="store_true")
    parser.add_argument("--show-hold-conditions", action="store_true")
    parser.add_argument("--show-freeze-boundaries", action="store_true")
    parser.add_argument("--show-quarantines", action="store_true")
    parser.add_argument("--show-partial-suspension", action="store_true")
    parser.add_argument("--show-residual-operations", action="store_true")
    parser.add_argument("--show-residual-duties", action="store_true")
    parser.add_argument("--show-beneficiary-safeguards", action="store_true")
    parser.add_argument("--show-access-restrictions", action="store_true")
    parser.add_argument("--show-execution-hold", action="store_true")
    parser.add_argument("--show-decision-freeze", action="store_true")
    parser.add_argument("--show-data-freeze", action="store_true")
    parser.add_argument("--show-change-freeze", action="store_true")
    parser.add_argument("--show-resumption-criteria", action="store_true")
    parser.add_argument("--show-unsuspension", action="store_true")
    parser.add_argument("--show-timeboxes", action="store_true")
    parser.add_argument("--show-indefinite-suspension", action="store_true")
    parser.add_argument("--show-shadow-execution", action="store_true")
    parser.add_argument("--show-bypass-attempts", action="store_true")
    parser.add_argument("--show-scope-leakage", action="store_true")
    parser.add_argument("--show-suspension-comparisons", action="store_true")
    parser.add_argument("--show-suspension-readiness", action="store_true")
    parser.add_argument("--show-suspension-forecast", action="store_true")
    parser.add_argument("--show-suspension-debt", action="store_true")
    parser.add_argument("--show-suspension-equivalence", action="store_true")
    parser.add_argument("--show-suspension-trust", action="store_true")
    parser.add_argument("--show-suspension-review-packs", action="store_true")
"""

if "show-suspension-registry" not in content:
    content = content.replace("args = parser.parse_args()", suspension_args + "\n    args = parser.parse_args()")

with open("app/main.py", "w") as f:
    f.write(content)
print("app/main.py patched.")
