# tests/test_walkforward_promotion_gates.py has 4 checks instead of 3 due to the Risk Policy addition
with open("tests/test_walkforward_promotion_gates.py", "r") as f:
    content = f.read()

content = content.replace("assert len(res.checks) == 3", "assert len(res.checks) == 4")

with open("tests/test_walkforward_promotion_gates.py", "w") as f:
    f.write(content)
