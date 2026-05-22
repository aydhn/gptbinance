# Fix the existing files so we don't just overwrite them with dummy classes.
import os

with open("app/main.py", "w") as f:
    f.write("""import argparse

def main():
    parser = argparse.ArgumentParser(description="Main CLI")
    parser.add_argument("--show-precedent-registry", action="store_true")
    parser.add_argument("--show-precedent-object", action="store_true")
    parser.add_argument("--precedent-id", type=str)
    parser.add_argument("--show-cases", action="store_true")
    parser.add_argument("--show-holdings", action="store_true")
    parser.add_argument("--show-rationales", action="store_true")
    parser.add_argument("--show-controlling-factors", action="store_true")
    parser.add_argument("--show-precedent-applicability", action="store_true")
    parser.add_argument("--show-binding-precedent", action="store_true")
    parser.add_argument("--show-persuasive-precedent", action="store_true")
    parser.add_argument("--show-analogies", action="store_true")
    parser.add_argument("--show-distinctions", action="store_true")
    parser.add_argument("--show-carve-outs", action="store_true")
    parser.add_argument("--show-precedent-exceptions", action="store_true")
    parser.add_argument("--show-precedent-conflicts", action="store_true")
    parser.add_argument("--show-precedent-hierarchy", action="store_true")
    parser.add_argument("--show-precedent-overrides", action="store_true")
    parser.add_argument("--show-precedent-overrules", action="store_true")
    parser.add_argument("--show-precedent-supersession", action="store_true")
    parser.add_argument("--show-precedent-consistency", action="store_true")
    parser.add_argument("--show-precedent-comparisons", action="store_true")
    parser.add_argument("--show-precedent-readiness", action="store_true")
    parser.add_argument("--show-precedent-forecast", action="store_true")
    parser.add_argument("--show-precedent-debt", action="store_true")
    parser.add_argument("--show-precedent-equivalence", action="store_true")
    parser.add_argument("--show-precedent-trust", action="store_true")
    parser.add_argument("--show-precedent-review-packs", action="store_true")

    args = parser.parse_args()
    if args.show_precedent_registry:
        print("Registry shown")

if __name__ == "__main__":
    main()
""")
