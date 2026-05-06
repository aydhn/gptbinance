with open("app/evidence_graph/artefacts.py", "r") as f:
    content = f.read()

if "from typing import" in content and "Optional" not in content:
    content = content.replace("from typing import Dict, Any, List", "from typing import Dict, Any, List, Optional")
elif "from typing import" not in content:
    content = "from typing import Dict, Any, List, Optional\n" + content

with open("app/evidence_graph/artefacts.py", "w") as f:
    f.write(content)
