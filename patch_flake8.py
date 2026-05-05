import re
import os

def fix_file(file_path, old_content, new_content):
    if not os.path.exists(file_path): return
    with open(file_path, 'r') as f:
        content = f.read()
    with open(file_path, 'w') as f:
        f.write(content.replace(old_content, new_content))

fix_file('app/experiments/comparisons.py', 'from app.experiments.models import ExperimentComparison\n', '')
fix_file('app/experiments/fragility.py', 'from app.experiments.models import ExperimentFragilityReport\n', '')
fix_file('app/experiments/models.py', 'from typing import Dict, List, Optional, Any, Union', 'from typing import Dict, List, Optional, Any')
fix_file('app/experiments/models.py', 'PromotionClass, ExperimentVerdict, ScopeType', 'PromotionClass, ScopeType')
fix_file('app/experiments/offline.py', 'run = ExperimentRun(', 'ExperimentRun(')
fix_file('app/experiments/reporting.py', 'report = f"=== EXPERIMENT REPORT ===\\n"', 'report = "=== EXPERIMENT REPORT ===\\n"')
fix_file('tests/test_experiments_baselines.py', 'assert reg.check_freshness("b_1") == True', 'assert reg.check_freshness("b_1") is True')
