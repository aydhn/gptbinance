def fix_file(filename, to_replace, replacement):
    with open(filename, 'r') as f:
        content = f.read()
    content = content.replace(to_replace, replacement)
    with open(filename, 'w') as f:
        f.write(content)

fix_file('app/crossbook/graph.py', 'from typing import List, Dict', 'from typing import List')
fix_file('app/crossbook/graph.py', 'import uuid\n', '')
fix_file('app/crossbook/graph.py', 'target_id=f"node_USDT"', 'target_id="node_USDT"')

fix_file('app/crossbook/models.py', 'from typing import List, Dict, Any, Optional', 'from typing import List, Dict, Any')
fix_file('app/crossbook/models.py', 'from decimal import Decimal\n', '')
fix_file('app/crossbook/models.py', '    CollateralType,\n', '')

fix_file('app/crossbook/netting.py', 'from datetime import datetime, timezone\n', '')
fix_file('app/crossbook/netting.py', 'ExposureClass, HedgeQuality, BookType', 'ExposureClass, HedgeQuality')

fix_file('app/crossbook/policies.py', 'from typing import Dict, Any\n', '')
fix_file('app/crossbook/storage.py', 'from typing import Dict, Any\n', 'from typing import Any\n')

