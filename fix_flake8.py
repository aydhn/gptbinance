def process_file(path, replacements):
    with open(path, 'r') as f:
        content = f.read()
    for o, n in replacements:
        content = content.replace(o, n)
    with open(path, 'w') as f:
        f.write(content)

process_file("tests/test_risk_engine.py", [("OrderSide.BUY", "1")]) # Or just import OrderSide properly
process_file("tests/test_risk_guards.py", [("OrderSide.BUY", "1")])
process_file("tests/test_risk_policies.py", [("OrderSide.BUY", "1"), ("ExposureScope", "app.risk.enums.ExposureScope")])
process_file("tests/test_risk_sizing.py", [("OrderSide.BUY", "1")])

