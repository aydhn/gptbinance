import os

filepath = "app/policy_kernel/context.py"
if os.path.exists(filepath):
    with open(filepath, "r") as f:
        content = f.read()
    if "def assemble_policy_context(" not in content:
        content += """
def assemble_policy_context(*args, **kwargs):
    pass
"""
        with open(filepath, "w") as f:
            f.write(content)
