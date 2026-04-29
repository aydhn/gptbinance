def process_file(path, replacements):
    with open(path, 'r') as f:
        content = f.read()
    for o, n in replacements:
        content = content.replace(o, n)
    with open(path, 'w') as f:
        f.write(content)

process_file("tests/test_risk_policies.py", [("app.risk.enums.ExposureScope", "ExposureScope")])

with open("tests/test_risk_policies.py", "r") as f:
    c = f.read()
c = "from app.risk.enums import ExposureScope\n" + c
with open("tests/test_risk_policies.py", "w") as f:
    f.write(c)
