from app.allocation.models import AllocationDiffRecord, AllocationManifest


class DiffEngine:
    def compare(
        self, base: AllocationManifest, new_manifest: AllocationManifest
    ) -> AllocationDiffRecord:
        deltas = []
        base_intents = {i.intent_id: i for i in base.intents}

        for new_i in new_manifest.intents:
            if new_i.intent_id not in base_intents:
                deltas.append(f"new_intent_{new_i.intent_id}")
            elif base_intents[new_i.intent_id].clipped_size != new_i.clipped_size:
                deltas.append(f"size_change_{new_i.intent_id}")

        return AllocationDiffRecord(
            diff_id=f"diff_{base.manifest_id}_{new_manifest.manifest_id}",
            baseline_manifest_id=base.manifest_id,
            candidate_manifest_id=new_manifest.manifest_id,
            semantic_deltas=deltas,
            divergence_score=len(deltas) * 0.1,
        )
