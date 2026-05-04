with open('app/telegram/notifier.py', 'r') as f:
    content = f.read()

if "notify_crossbook_breach" not in content:
    content += """
    # Added in Phase 40
async def notify_crossbook_breach(self, profile: str, amount: float, reasons: str):
    pass
"""
with open('app/telegram/notifier.py', 'w') as f:
    f.write(content)
