import re

with open("app/main.py", "r") as f:
    content = f.read()

# Add imports
imports = """
from app.replay.models import ReplayConfig, ReplaySourceRef, CounterfactualSpec
from app.replay.enums import ReplayScope, ReplaySourceType, CounterfactualType
from app.replay.repository import replay_repository
from app.replay.reporting import (
    format_summary,
    format_timeline,
    format_decision_path,
    format_diff,
    format_counterfactual_summary,
    format_replayability_score
)
"""

content = content.replace("import sys", "import sys\n" + imports)

# Add CLI arguments
cli_args = """
    parser.add_argument("--run-replay", action="store_true", help="Run deterministic replay")
    parser.add_argument("--replay-scope", type=str, help="Replay scope (trade, session, incident, etc.)")
    parser.add_argument("--replay-source-ref", type=str, help="Source reference for replay")
    parser.add_argument("--replay-window", type=str, help="Window for replay (start:end ISO strings)")
    parser.add_argument("--show-replay-summary", action="store_true", help="Show replay summary")
    parser.add_argument("--show-replay-timeline", action="store_true", help="Show event timeline")
    parser.add_argument("--show-decision-path", action="store_true", help="Show decision path")
    parser.add_argument("--show-replay-diff", action="store_true", help="Show replay diffs")
    parser.add_argument("--run-counterfactual", action="store_true", help="Run counterfactual simulation")
    parser.add_argument("--counterfactual-type", type=str, help="Counterfactual type (e.g. ml_disabled)")
    parser.add_argument("--show-counterfactual-summary", action="store_true", help="Show counterfactual summary")
    parser.add_argument("--build-forensic-bundle", action="store_true", help="Build forensic bundle")
    parser.add_argument("--show-replayability-score", action="store_true", help="Show replayability score")
    parser.add_argument("--run-id", type=str, help="Run ID for displaying results")
"""

content = content.replace('parser.add_argument("--run-governance",', cli_args + '\n    parser.add_argument("--run-governance",')

# Add CLI logic
cli_logic = """
    if args.run_replay:
        if not args.replay_scope or not args.replay_source_ref:
            logger.error("--replay-scope and --replay-source-ref are required for --run-replay")
            sys.exit(1)

        scope = ReplayScope(args.replay_scope)
        # simplistic parsing for demonstration
        src_parts = args.replay_source_ref.split(":")
        src_type = ReplaySourceType.PAPER_SESSION if src_parts[0] == "paper" else ReplaySourceType.INCIDENT # Simplified

        sources = [ReplaySourceRef(source_type=src_type, ref_id=src_parts[1] if len(src_parts)>1 else src_parts[0])]

        config = ReplayConfig(scope=scope, sources=sources)
        if args.build_forensic_bundle:
             config.include_forensics = True

        result = replay_repository.run_and_save(config)
        logger.info(f"Replay run {result.run_id} completed.")
        sys.exit(0)

    if args.run_counterfactual:
        if not args.run_id or not args.counterfactual_type:
            logger.error("--run-id and --counterfactual-type are required for --run-counterfactual")
            sys.exit(1)
        # Note: in a real system we'd probably re-run with the counterfactual spec
        # Here we'll just log it for dummy implementation
        logger.info(f"Counterfactual simulation requested for run {args.run_id} with type {args.counterfactual_type}")
        sys.exit(0)

    if args.show_replay_summary and args.run_id:
        res = replay_repository.get_run(args.run_id)
        if res:
             print(format_summary(res))
        else:
             print("Run not found")
        sys.exit(0)

    if args.show_replay_timeline and args.run_id:
        res = replay_repository.get_run(args.run_id)
        if res:
             print(format_timeline(res))
        else:
             print("Run not found")
        sys.exit(0)

    if args.show_decision_path and args.run_id:
        res = replay_repository.get_run(args.run_id)
        if res:
             print(format_decision_path(res))
        else:
             print("Run not found")
        sys.exit(0)

    if args.show_replay_diff and args.run_id:
        res = replay_repository.get_run(args.run_id)
        if res:
             print(format_diff(res))
        else:
             print("Run not found")
        sys.exit(0)

    if args.show_counterfactual_summary and args.run_id:
         res = replay_repository.get_run(args.run_id)
         if res:
             print(format_counterfactual_summary(res))
         else:
             print("Run not found")
         sys.exit(0)

    if args.show_replayability_score and args.run_id:
         res = replay_repository.get_run(args.run_id)
         if res:
             print(format_replayability_score(res))
         else:
             print("Run not found")
         sys.exit(0)
"""

content = content.replace("if args.run_governance:", cli_logic + "\n    if args.run_governance:")

with open("app/main.py", "w") as f:
    f.write(content)
