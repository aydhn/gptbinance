import os
def replace_in_file(filepath, old, new):
    if not os.path.exists(filepath): return
    with open(filepath, "r") as f:
        content = f.read()
    content = content.replace(old, new)
    with open(filepath, "w") as f:
        f.write(content)

replace_in_file("app/policy_kernel/context.py", """class PrecedentContext:
    def __init__(self):
        self.precedent_posture = None""", """class PrecedentContext:
    def __init__(self):
        self.precedent_posture = None
        self.active_conflicts = []
        self.stale_analogies = []
        self.exception_inflation = False
        self.rationale_coverage = []
""")
