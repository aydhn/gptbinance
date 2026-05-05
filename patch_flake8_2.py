import re
import os

def fix_file(file_path, old_content, new_content):
    if not os.path.exists(file_path): return
    with open(file_path, 'r') as f:
        content = f.read()
    with open(file_path, 'w') as f:
        f.write(content.replace(old_content, new_content))

fix_file('app/experiments/models.py', '    PromotionClass,\n    ExperimentVerdict,\n    ScopeType,\n', '    PromotionClass,\n    ScopeType,\n')
