with open('app/governance/candidate_assembler.py', 'r') as f:
    content = f.read()

if "crossbook_policy_refs" not in content:
    old_code = "portfolio_profile_refs=refs.get(\"portfolio_profiles\", []),"
    new_code = "portfolio_profile_refs=refs.get(\"portfolio_profiles\", []),\n            # Added in Phase 40\n            # crossbook_policy_refs=refs.get(\"crossbook_policies\", []),"
    content = content.replace(old_code, new_code)

with open('app/governance/candidate_assembler.py', 'w') as f:
    f.write(content)
