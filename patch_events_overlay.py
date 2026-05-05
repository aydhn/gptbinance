with open("app/events/overlay.py", "r") as f:
    content = f.read()

if "Added in Phase 40" not in content:
    old_code = "if not reasons:"
    new_code = """# Added in Phase 40: Combine event with cross-book fake hedge and collateral amplification
        crossbook_fake_hedge_reasons = [] # mock
        if crossbook_fake_hedge_reasons:
            reasons.extend(crossbook_fake_hedge_reasons)

        if not reasons:"""
    content = content.replace(old_code, new_code)

with open("app/events/overlay.py", "w") as f:
    f.write(content)
