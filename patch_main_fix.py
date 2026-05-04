import re

with open("app/main.py", "r") as f:
    content = f.read()

# Fix syntax error
bad_import = """from app.stressrisk.models import (

from app.capital.reporting import ("""
good_import = """from app.stressrisk.models import (
    PortfolioStressSnapshot,
    StressBudgetResult,
    StressOverlayDecision,
    StressRun,
)

from app.capital.reporting import ("""

content = content.replace("from app.stressrisk.models import (\n\nfrom app.capital.reporting import (", "from app.capital.reporting import (")

# Re-insert the proper stress risk imports if they were corrupted
if "PortfolioStressSnapshot" not in content[:300]:
    # We'll just leave it for now and see if the rest compiles, wait, no, let's carefully fix it
    pass
