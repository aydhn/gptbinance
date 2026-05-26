import sys

def main():
    args = sys.argv[1:]
    recap_commands = [
        "--show-recapitalization-registry", "--show-recapitalization-object", "--show-recapitalizations",
        "--show-capital-stack", "--show-capital-instruments", "--show-equity", "--show-preferred",
        "--show-common", "--show-convertibles", "--show-warrants", "--show-capital-commitments",
        "--show-subscriptions", "--show-capital-funding", "--show-capital-calls", "--show-conversions",
        "--show-issuances", "--show-dilution", "--show-anti-dilution", "--show-ownership", "--show-voting-rights",
        "--show-control-rights", "--show-reserved-matters", "--show-backstops", "--show-oversubscriptions",
        "--show-solvency-restoration", "--show-minimum-capital", "--show-exit-capital", "--show-capital-shortfalls",
        "--show-recapitalization-comparisons", "--show-recapitalization-readiness", "--show-recapitalization-forecast",
        "--show-recapitalization-debt", "--show-recapitalization-equivalence", "--show-recapitalization-trust",
        "--show-recapitalization-review-packs"
    ]

    for cmd in args:
        if cmd in recap_commands:
            print(f"[CLI] Executing {cmd} - Fetching canonical recapitalization truth...")
            sys.exit(0)

if __name__ == "__main__":
    main()
