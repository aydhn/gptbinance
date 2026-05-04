with open('app/execution/live/pretrade_validation.py', 'r') as f:
    content = f.read()

import_stmt = "from app.crossbook.enums import CrossBookVerdict\n"
if "CrossBookVerdict" not in content:
    content = import_stmt + content

if "check_crossbook_overlay_verdict" not in content:
    new_method = """
    # Added in Phase 40
    def check_crossbook_overlay_verdict(self, verdict):
        if verdict == CrossBookVerdict.BLOCK:
            raise PretradeValidationError("Blocked by cross-book exposure overlay.")
        elif verdict == CrossBookVerdict.REDUCE:
            logger.warning("Cross-book overlay suggests reducing exposure.")
"""
    content += new_method

with open('app/execution/live/pretrade_validation.py', 'w') as f:
    f.write(content)
