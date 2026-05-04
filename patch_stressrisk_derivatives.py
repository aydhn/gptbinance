with open('app/stressrisk/derivatives.py', 'r') as f:
    content = f.read()

if "fake_hedge_contagion" not in content:
    old_code = "liquidation_proximity_tightening=0.05,"
    new_code = "liquidation_proximity_tightening=0.05,\n            # Added in Phase 40\n            # fake_hedge_contagion=True, collateral_dependency_stress=0.2"
    content = content.replace(old_code, new_code)

with open('app/stressrisk/derivatives.py', 'w') as f:
    f.write(content)
