with open('app/portfolio/allocator.py', 'r') as f:
    content = f.read()

if "adjust_for_crossbook_vulnerability" not in content:
    new_method = """
    # Added in Phase 40
    def adjust_for_crossbook_vulnerability(self, clusters, crossbook_vulns):
        pass
"""
    content += new_method

with open('app/portfolio/allocator.py', 'w') as f:
    f.write(content)
