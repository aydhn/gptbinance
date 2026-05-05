import re
import os

files = [
    'app/experiments/models.py',
    'app/experiments/offline.py',
    'app/experiments/baselines.py',
    'tests/test_experiments_packs.py',
    'tests/test_experiments_baselines.py'
]

def fix():
    for f in files:
        if not os.path.exists(f): continue
        with open(f, 'r') as file:
            content = file.read()

        content = content.replace("from datetime import datetime", "from datetime import datetime, timezone")
        content = content.replace("datetime.utcnow", "lambda: datetime.now(timezone.utc)")
        content = content.replace("datetime.utcnow()", "datetime.now(timezone.utc)")
        content = content.replace("lambda: datetime.now(timezone.utc)()", "datetime.now(timezone.utc)")

        with open(f, 'w') as file:
            file.write(content)

if __name__ == '__main__':
    fix()
