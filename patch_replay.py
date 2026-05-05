with open("app/replay/decision_path.py", "r") as f:
    content = f.read()

if "fake_hedge_conflict" not in content:
    old_code = 'decision={"approved": True},'
    new_code = 'decision={"approved": True, "crossbook_conflicts": ["fake_hedge_conflict"]}, # Added in Phase 40'
    content = content.replace(old_code, new_code)

with open("app/replay/decision_path.py", "w") as f:
    f.write(content)
