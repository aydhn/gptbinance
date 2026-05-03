import uuid
from datetime import datetime, timezone
from typing import List, Set
from app.universe.models import UniverseSnapshot, UniverseDiff, InstrumentRef

class DiffEngine:
    def compute_diff(self, old_snap: UniverseSnapshot, new_snap: UniverseSnapshot) -> UniverseDiff:

        def to_set(refs: List[InstrumentRef]) -> Set[str]:
            return {f"{r.symbol}_{r.product_type.value}" for r in refs}

        def get_ref(refs: List[InstrumentRef], key: str) -> InstrumentRef:
            for r in refs:
                if f"{r.symbol}_{r.product_type.value}" == key:
                    return r
            raise ValueError(f"Ref not found for key {key}")

        old_all = to_set(old_snap.eligible_instruments + old_snap.caution_instruments + old_snap.blocked_instruments)
        new_all = to_set(new_snap.eligible_instruments + new_snap.caution_instruments + new_snap.blocked_instruments)

        added_keys = new_all - old_all
        removed_keys = old_all - new_all

        all_new_refs = new_snap.eligible_instruments + new_snap.caution_instruments + new_snap.blocked_instruments
        all_old_refs = old_snap.eligible_instruments + old_snap.caution_instruments + old_snap.blocked_instruments

        added = [get_ref(all_new_refs, k) for k in added_keys]
        removed = [get_ref(all_old_refs, k) for k in removed_keys]

        # Eligibility changes
        old_elig_map = {f"{r.symbol}_{r.product_type.value}": "eligible" for r in old_snap.eligible_instruments}
        old_elig_map.update({f"{r.symbol}_{r.product_type.value}": "caution" for r in old_snap.caution_instruments})
        old_elig_map.update({f"{r.symbol}_{r.product_type.value}": "blocked" for r in old_snap.blocked_instruments})

        new_elig_map = {f"{r.symbol}_{r.product_type.value}": "eligible" for r in new_snap.eligible_instruments}
        new_elig_map.update({f"{r.symbol}_{r.product_type.value}": "caution" for r in new_snap.caution_instruments})
        new_elig_map.update({f"{r.symbol}_{r.product_type.value}": "blocked" for r in new_snap.blocked_instruments})

        elig_changed = []
        for k in new_all.intersection(old_all):
            if old_elig_map[k] != new_elig_map[k]:
                elig_changed.append(get_ref(all_new_refs, k))

        return UniverseDiff(
            diff_id=f"diff_{uuid.uuid4().hex[:8]}",
            old_snapshot_id=old_snap.snapshot_id,
            new_snapshot_id=new_snap.snapshot_id,
            added=added,
            removed=removed,
            status_changed=[], # Handled via lifecycle events mostly, kept simple here
            eligibility_changed=elig_changed,
            created_at=datetime.now(timezone.utc)
        )
