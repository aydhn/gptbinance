sed -i 's/from typing import Dict, Any, List/from typing import List/' app/simulation_plane/base.py
sed -i 's/from typing import List, Dict, Optional, Any/from typing import List, Dict, Any/' app/simulation_plane/models.py
sed -i 's/SimulationMode, PartitionClass, AssumptionClass, SensitivityClass,/SimulationMode, PartitionClass, SensitivityClass,/' app/simulation_plane/models.py
sed -i 's/EquivalenceVerdict, TrustVerdict, CounterfactualConfidence/EquivalenceVerdict, TrustVerdict/' app/simulation_plane/models.py
sed -i 's/for p2 in partitions\[i + 1 :\]:/for p2 in partitions[i + 1:]:/' app/simulation_plane/partitions.py
sed -i 's/from app.simulation_plane.models import SimulationRun//' app/simulation_plane/reporting.py
sed -i 's/from typing import Dict, Any/from typing import Any/' app/simulation_plane/storage.py
sed -i 's/from app.simulation_plane.exceptions import WalkForwardViolationError//' app/simulation_plane/walkforward.py
sed -i 's/from typing import List//' app/simulation_plane/windows.py
