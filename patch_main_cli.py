import os
import re

def main():
    path = "app/main.py"
    if not os.path.exists(path):
        with open(path, "w") as f:
            f.write("def main():\n    pass\n")

    with open(path, "r") as f:
        content = f.read()

    commands = """    # Escrow Plane Commands
    parser.add_argument('--show-escrow-registry', action='store_true')
    parser.add_argument('--show-escrow-object', action='store_true')
    parser.add_argument('--escrow-id', type=str)
    parser.add_argument('--show-escrows', action='store_true')
    parser.add_argument('--show-escrow-subjects', action='store_true')
    parser.add_argument('--show-deposited-assets', action='store_true')
    parser.add_argument('--show-depositors', action='store_true')
    parser.add_argument('--show-escrow-beneficiaries', action='store_true')
    parser.add_argument('--show-escrow-agents', action='store_true')
    parser.add_argument('--show-agent-authority', action='store_true')
    parser.add_argument('--show-agent-neutrality', action='store_true')
    parser.add_argument('--show-escrow-capacity', action='store_true')
    parser.add_argument('--show-escrow-segregation', action='store_true')
    parser.add_argument('--show-commingling', action='store_true')
    parser.add_argument('--show-escrow-custody', action='store_true')
    parser.add_argument('--show-hold-conditions', action='store_true')
    parser.add_argument('--show-condition-evidence', action='store_true')
    parser.add_argument('--show-milestone-release', action='store_true')
    parser.add_argument('--show-documentary-release', action='store_true')
    parser.add_argument('--show-adjudicated-release', action='store_true')
    parser.add_argument('--show-dual-consent-release', action='store_true')
    parser.add_argument('--show-unilateral-release-prohibition', action='store_true')
    parser.add_argument('--show-escrow-instructions', action='store_true')
    parser.add_argument('--show-instruction-validation', action='store_true')
    parser.add_argument('--show-dispute-holds', action='store_true')
    parser.add_argument('--show-reserved-portions', action='store_true')
    parser.add_argument('--show-partial-release', action='store_true')
    parser.add_argument('--show-wrong-beneficiary-release', action='store_true')
    parser.add_argument('--show-release-actions', action='store_true')
    parser.add_argument('--show-release-reversal', action='store_true')
    parser.add_argument('--show-clawback-style-recovery', action='store_true')
    parser.add_argument('--show-escrow-expiry', action='store_true')
    parser.add_argument('--show-abandonment', action='store_true')
    parser.add_argument('--show-disposal-path', action='store_true')
    parser.add_argument('--show-yield', action='store_true')
    parser.add_argument('--show-negative-carry', action='store_true')
    parser.add_argument('--show-escrow-comparisons', action='store_true')
    parser.add_argument('--show-escrow-readiness', action='store_true')
    parser.add_argument('--show-escrow-forecast', action='store_true')
    parser.add_argument('--show-escrow-debt', action='store_true')
    parser.add_argument('--show-escrow-equivalence', action='store_true')
    parser.add_argument('--show-escrow-trust', action='store_true')
    parser.add_argument('--show-escrow-review-packs', action='store_true')
"""
    if "--show-escrow-registry" not in content:
        # try to find a place to inject or just append
        # assuming there's an argparse setup somewhere
        if "parser.parse_args()" in content:
            content = content.replace("args = parser.parse_args()", commands + "\n    args = parser.parse_args()")
        else:
            content += "\n" + commands

        with open(path, "w") as f:
            f.write(content)

if __name__ == "__main__":
    main()
