import re

with open('app/main.py', 'r') as f:
    content = f.read()

new_logic = """
    if args.show_command_registry:
        from app.control_plane.repository import ControlPlaneRepository
        repo = ControlPlaneRepository()
        print("\\n--- Canonical Command Registry ---")
        for cmd in repo.registry.list_commands():
            print(f"- {cmd.command_id.value} (Class: {cmd.action_class.value}, Reversible: {cmd.reversibility.value})")
        return

    if args.show_kill_switches:
        from app.control_plane.repository import ControlPlaneRepository
        repo = ControlPlaneRepository()
        print("\\n--- Active Kill Switches ---")
        switches = repo.kill_switches.get_active_switches()
        if not switches:
            print("No active kill switches.")
        for s in switches:
            print(f"[{s.kill_switch_id}] {s.kill_switch_class.value} on {s.scope_ref} by {s.actor}")
        return

    if args.show_control_trust:
        from app.control_plane.repository import ControlPlaneRepository
        repo = ControlPlaneRepository()
        trust = repo.trust_evaluator.evaluate()
        print("\\n--- Control Trust Verdict ---")
        print(f"Verdict: {trust.verdict.value}")
        print(f"Reasons: {trust.reasons}")
        return
"""

if "args.show_command_registry:" not in content:
    content = re.sub(
        r'(if args.show_simulation_registry:)',
        new_logic.replace("\\n", "\\\\n") + r'\n    \1',
        content
    )

with open('app/main.py', 'w') as f:
    f.write(content)
