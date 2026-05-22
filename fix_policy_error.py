import os
def replace_in_file(filepath, old, new):
    if not os.path.exists(filepath): return
    with open(filepath, "r") as f:
        content = f.read()
    content = content.replace(old, new)
    with open(filepath, "w") as f:
        f.write(content)

replace_in_file("app/policy_plane/evaluations.py", """class PrecedentIntegrations:
    def check_precedent(self, action):
        pass""", """class PrecedentIntegrations:
    def check_precedent(self, action):
        return {"obligations": [], "deny": False}
    def produce_obligations(self):
        pass
""")
