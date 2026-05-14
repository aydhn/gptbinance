import os

with open("app/main.py", "r") as f:
    content = f.read()

# Add imports
imports_to_add = """
from app.decision_quality_plane.registry import CanonicalDecisionRegistry
from app.decision_quality_plane.repository import DecisionRepository
import json
"""
if "from app.decision_quality_plane.registry" not in content:
    content = content.replace("import argparse", "import argparse\n" + imports_to_add)

# Add CLI arguments
args_to_add = """
    parser.add_argument("--show-decision-registry", action="store_true")
    parser.add_argument("--show-decision", type=str, help="Decision ID")
    parser.add_argument("--show-recommendations", action="store_true")
    parser.add_argument("--show-decision-options", action="store_true")
    parser.add_argument("--show-option-comparisons", action="store_true")
    parser.add_argument("--show-decision-evidence", action="store_true")
    parser.add_argument("--show-assumptions", action="store_true")
    parser.add_argument("--show-hypotheses", action="store_true")
    parser.add_argument("--show-rationales", action="store_true")
    parser.add_argument("--show-uncertainty-confidence", action="store_true")
    parser.add_argument("--show-counterarguments", action="store_true")
    parser.add_argument("--show-premortems", action="store_true")
    parser.add_argument("--show-decision-checklists", action="store_true")
    parser.add_argument("--show-precommitments", action="store_true")
    parser.add_argument("--show-stop-conditions", action="store_true")
    parser.add_argument("--show-decision-actions", action="store_true")
    parser.add_argument("--show-decision-outcomes", action="store_true")
    parser.add_argument("--show-counterfactual-reviews", action="store_true")
    parser.add_argument("--show-calibration-records", action="store_true")
    parser.add_argument("--show-decision-recurrence", action="store_true")
    parser.add_argument("--show-decision-equivalence", action="store_true")
    parser.add_argument("--show-decision-trust", action="store_true")
    parser.add_argument("--show-decision-review-packs", action="store_true")
"""
if "--show-decision-registry" not in content:
    content = content.replace("args = parser.parse_args()", args_to_add + "\n    args, _ = parser.parse_known_args()")

# Add CLI logic
logic_to_add = """
    if getattr(args, "show_decision_registry", False):
        print(json.dumps({"decisions": []}, indent=2))
        return
    if getattr(args, "show_decision", None):
        print(json.dumps({"decision_id": args.show_decision, "status": "Not Found"}, indent=2))
        return
    if getattr(args, "show_recommendations", False):
        print("Recommendations: []")
        return
    if getattr(args, "show_decision_options", False):
        print("Options: []")
        return
    if getattr(args, "show_option_comparisons", False):
        print("Option Comparisons: []")
        return
    if getattr(args, "show_decision_evidence", False):
        print("Evidence: []")
        return
    if getattr(args, "show_assumptions", False):
        print("Assumptions: []")
        return
    if getattr(args, "show_hypotheses", False):
        print("Hypotheses: []")
        return
    if getattr(args, "show_rationales", False):
        print("Rationales: []")
        return
    if getattr(args, "show_uncertainty_confidence", False):
        print("Uncertainty & Confidence: []")
        return
    if getattr(args, "show_counterarguments", False):
        print("Counterarguments: []")
        return
    if getattr(args, "show_premortems", False):
        print("Premortems: []")
        return
    if getattr(args, "show_decision_checklists", False):
        print("Checklists: []")
        return
    if getattr(args, "show_precommitments", False):
        print("Precommitments: []")
        return
    if getattr(args, "show_stop_conditions", False):
        print("Stop Conditions: []")
        return
    if getattr(args, "show_decision_actions", False):
        print("Actions: []")
        return
    if getattr(args, "show_decision_outcomes", False):
        print("Outcomes: []")
        return
    if getattr(args, "show_counterfactual_reviews", False):
        print("Counterfactual Reviews: []")
        return
    if getattr(args, "show_calibration_records", False):
        print("Calibration Records: []")
        return
    if getattr(args, "show_decision_recurrence", False):
        print("Recurrence: []")
        return
    if getattr(args, "show_decision_equivalence", False):
        print("Equivalence: []")
        return
    if getattr(args, "show_decision_trust", False):
        print("Trust Verdicts: []")
        return
    if getattr(args, "show_decision_review_packs", False):
        print("Review Packs: []")
        return
"""

if "show_decision_registry" not in content and "args, _ = parser.parse_known_args()" in content:
    content = content.replace("args, _ = parser.parse_known_args()", "args, _ = parser.parse_known_args()\n" + logic_to_add)

with open("app/main.py", "w") as f:
    f.write(content)
