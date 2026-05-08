import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--show-simulation-registry", action="store_true")
    parser.add_argument("--show-simulation-run", type=str, help="--run-id <id>")
    parser.add_argument("--show-simulation-modes", action="store_true")
    parser.add_argument("--show-simulation-windows", action="store_true")
    parser.add_argument("--show-simulation-partitions", action="store_true")
    parser.add_argument("--show-simulation-assumptions", action="store_true")
    parser.add_argument("--show-walk-forward-report", action="store_true")
    parser.add_argument("--show-oos-report", action="store_true")
    parser.add_argument("--show-simulation-sensitivities", action="store_true")
    parser.add_argument("--show-simulation-divergence", action="store_true")
    parser.add_argument("--show-simulation-equivalence", action="store_true")
    parser.add_argument("--show-simulation-trust", action="store_true")
    parser.add_argument("--show-simulation-review-packs", action="store_true")

    args = parser.parse_args()

    if args.show_simulation_registry:
        print("Simulation Registry: [production, exploratory]")
    elif args.show_simulation_run:
        print(f"Run ID {args.show_simulation_run}")
    # ... other branches
    else:
        print("No simulation CLI argument provided.")

if __name__ == "__main__":
    main()
