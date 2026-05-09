import re

with open('app/main.py', 'r') as f:
    content = f.read()

new_args = """
    parser.add_argument("--show-command-registry", action="store_true", help="Show typed command registry")
    parser.add_argument("--show-control-action", type=str, metavar="ACTION_ID", help="Show specific action details")
    parser.add_argument("--show-control-scopes", action="store_true")
    parser.add_argument("--show-action-previews", action="store_true")
    parser.add_argument("--show-action-dry-runs", action="store_true")
    parser.add_argument("--show-approval-chains", action="store_true")
    parser.add_argument("--show-approval-decisions", action="store_true")
    parser.add_argument("--show-exception-tokens", action="store_true")
    parser.add_argument("--show-kill-switches", action="store_true")
    parser.add_argument("--show-freezes-unfreezes", action="store_true")
    parser.add_argument("--show-control-rollbacks", action="store_true")
    parser.add_argument("--show-control-revokes", action="store_true")
    parser.add_argument("--show-control-equivalence", action="store_true")
    parser.add_argument("--show-control-trust", action="store_true")
    parser.add_argument("--show-control-review-packs", action="store_true")
"""

if "--show-command-registry" not in content:
    content = re.sub(
        r'(parser = argparse.ArgumentParser\(\))',
        r'\1' + new_args,
        content
    )

with open('app/main.py', 'w') as f:
    f.write(content)
