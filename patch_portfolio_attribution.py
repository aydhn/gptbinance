with open('app/analytics/portfolio_attribution.py', 'r') as f:
    content = f.read()

if "tag_crossbook_vulnerable_sleeves" not in content:
    content += """
    # Added in Phase 40
def tag_crossbook_vulnerable_sleeves(self, vulnerability_data):
    pass
"""
with open('app/analytics/portfolio_attribution.py', 'w') as f:
    f.write(content)
