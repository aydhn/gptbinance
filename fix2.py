import re

with open("app/readiness_board/admissibility.py", "r") as f:
    text = f.read()
text = text.replace("from app.readiness_board.exceptions import InadmissibleEvidenceError", "")
text = "from typing import List\n" + text
with open("app/readiness_board/admissibility.py", "w") as f:
    f.write(text)

with open("app/readiness_board/decisions.py", "r") as f:
    text = f.read()
text = text.replace("from app.readiness_board.enums import BoardVerdict, DomainVerdict, ReadinessDomain", "from app.readiness_board.enums import BoardVerdict, DomainVerdict")
text = "from typing import Optional\nfrom app.readiness_board.storage import ReadinessBoardStorage\n" + text
with open("app/readiness_board/decisions.py", "w") as f:
    f.write(text)

with open("app/readiness_board/domains.py", "r") as f:
    text = f.read()
text = "from typing import List\n" + text
with open("app/readiness_board/domains.py", "w") as f:
    f.write(text)

with open("app/readiness_board/dossier.py", "r") as f:
    text = f.read()
text = text.replace("    app.readiness_board.models import (", "from app.readiness_board.models import (")
with open("app/readiness_board/dossier.py", "w") as f:
    f.write(text)
