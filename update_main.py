import sys

def modify_main():
    main_file = "app/main.py"
    with open(main_file, "r") as f:
        content = f.read()

    lines = [
        "    group.add_argument('--show-incident-registry', action='store_true', help='Show incident registry')",
        "    group.add_argument('--show-incident-signals', action='store_true', help='Show incident signals')",
        "    group.add_argument('--show-incident-triage', action='store_true', help='Show incident triage')",
        "    group.add_argument('--show-incident-severity', action='store_true', help='Show incident severity')",
        "    group.add_argument('--show-incident-urgency', action='store_true', help='Show incident urgency')",
        "    group.add_argument('--show-incident-blast-radius', action='store_true', help='Show incident blast radius')",
        "    group.add_argument('--show-incident-ownership', action='store_true', help='Show incident ownership')",
        "    group.add_argument('--show-incident-status-timeline', action='store_true', help='Show incident status timeline')",
        "    group.add_argument('--show-incident-actions', action='store_true', help='Show incident actions')",
        "    group.add_argument('--show-incident-containment', action='store_true', help='Show incident containment')",
        "    group.add_argument('--show-incident-recovery', action='store_true', help='Show incident recovery')",
        "    group.add_argument('--show-incident-dedup-correlation', action='store_true', help='Show incident dedup and correlation')",
        "    group.add_argument('--show-incident-closure', action='store_true', help='Show incident closure')",
        "    group.add_argument('--show-incident-equivalence', action='store_true', help='Show incident equivalence')",
        "    group.add_argument('--show-incident-review-packs', action='store_true', help='Show incident review packs')",
    ]

    new_content = content.replace(
        '    group.add_argument("--show-incident-registry", action="store_true", help="Show registered incident families")',
        '\\n'.join(lines)
    )

    with open(main_file, "w") as f:
        f.write(new_content)

if __name__ == "__main__":
    modify_main()
