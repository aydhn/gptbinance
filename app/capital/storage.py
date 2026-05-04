import json
import os
from typing import Dict, Any, List
from app.capital.models import CapitalPostureSnapshot, CapitalTierRef

_STORAGE_DIR = "data/capital"


class CapitalStorage:
    def __init__(self):
        os.makedirs(_STORAGE_DIR, exist_ok=True)
        self.snapshots_file = os.path.join(_STORAGE_DIR, "posture_snapshots.json")
        self.tier_history_file = os.path.join(_STORAGE_DIR, "tier_history.json")

    def save_snapshot(self, snapshot: CapitalPostureSnapshot):
        data = []
        if os.path.exists(self.snapshots_file):
            with open(self.snapshots_file, "r") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    pass

        # Serialize datetime
        snap_dict = snapshot.model_dump()
        snap_dict["timestamp"] = snap_dict["timestamp"].isoformat()

        # Tranche serialization
        for t in snap_dict["active_tranches"]:
            t["activated_at"] = t["activated_at"].isoformat()
            if t["deactivated_at"]:
                t["deactivated_at"] = t["deactivated_at"].isoformat()

        data.append(snap_dict)
        with open(self.snapshots_file, "w") as f:
            json.dump(data, f, indent=2)

    def record_tier_change(self, ref: CapitalTierRef):
        data = []
        if os.path.exists(self.tier_history_file):
            with open(self.tier_history_file, "r") as f:
                try:
                    data = json.load(f)
                except json.JSONDecodeError:
                    pass

        ref_dict = ref.model_dump()
        ref_dict["assigned_at"] = ref_dict["assigned_at"].isoformat()

        data.append(ref_dict)
        with open(self.tier_history_file, "w") as f:
            json.dump(data, f, indent=2)


capital_storage = CapitalStorage()
