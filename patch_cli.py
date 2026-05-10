with open("app/main.py", "r") as f:
    content = f.read()

lines = content.split('\n')
new_lines = []

for line in lines:
    new_lines.append(line)
    if 'parser.add_argument("--show-workflow-runs", action="store_true")' in line:
        new_lines.extend([
            '    parser.add_argument("--show-release-registry", action="store_true")',
            '    parser.add_argument("--show-release", type=str, help="--release-id <id>")',
            '    parser.add_argument("--show-release-candidates", action="store_true")',
            '    parser.add_argument("--show-release-bundles", action="store_true")',
            '    parser.add_argument("--show-bundle-pins", action="store_true")',
            '    parser.add_argument("--show-environment-targets", action="store_true")',
            '    parser.add_argument("--show-release-compatibility", action="store_true")',
            '    parser.add_argument("--show-rollout-plans", action="store_true")',
            '    parser.add_argument("--show-canary-records", action="store_true")',
            '    parser.add_argument("--show-release-diffs", action="store_true")',
            '    parser.add_argument("--show-release-supersession", action="store_true")',
            '    parser.add_argument("--show-hotfix-records", action="store_true")',
            '    parser.add_argument("--show-rollback-packages", action="store_true")',
            '    parser.add_argument("--show-release-equivalence", action="store_true")',
            '    parser.add_argument("--show-release-trust", action="store_true")',
            '    parser.add_argument("--show-release-review-packs", action="store_true")'
        ])

with open("app/main.py", "w") as f:
    f.write('\n'.join(new_lines))
