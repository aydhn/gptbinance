with open('app/execution/derivatives/pretrade_validation.py', 'r') as f:
    content = f.read()

import_stmt = "from app.crossbook.enums import CrossBookVerdict\n"
if "CrossBookVerdict" not in content:
    content = import_stmt + content

if "crossbook_verdict" not in content:
    old_code = "return True"
    new_code = """
        # Added in Phase 40: Cross-book validation
        if hasattr(intent, 'crossbook_verdict') and intent.crossbook_verdict == CrossBookVerdict.BLOCK:
            logger.error("Blocked by cross-book exposure governance.")
            return False

        return True"""
    content = content.replace(old_code, new_code)

with open('app/execution/derivatives/pretrade_validation.py', 'w') as f:
    f.write(content)
