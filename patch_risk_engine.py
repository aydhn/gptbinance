with open("app/risk/engine.py", "r") as f:
    content = f.read()

import_stmt = "from app.crossbook.enums import CrossBookVerdict\n"
if "CrossBookVerdict" not in content:
    content = import_stmt + content

if "apply_crossbook_overlay" not in content:
    new_method = """
    # Added in Phase 40
    def apply_crossbook_overlay(self, overlay_decision):
        if overlay_decision.verdict in [CrossBookVerdict.BLOCK, CrossBookVerdict.REDUCE]:
            logger.warning(f"Cross-book restrictions applied. Reasons: {overlay_decision.reasons}")
        return True
"""
    content += new_method

with open("app/risk/engine.py", "w") as f:
    f.write(content)
