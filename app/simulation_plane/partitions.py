from typing import List
from app.simulation_plane.models import SimulationPartition
from app.simulation_plane.enums import PartitionClass
from app.simulation_plane.exceptions import InvalidPartitionSchemeError


class PartitionEvaluator:
    def evaluate(self, partitions: List[SimulationPartition]) -> List[str]:
        caveats = []
        has_train = any(p.partition_class == PartitionClass.TRAIN for p in partitions)
        has_oos = any(
            p.partition_class in (PartitionClass.TEST, PartitionClass.OUT_OF_SAMPLE)
            for p in partitions
        )

        if has_train and not has_oos:
            caveats.append(
                "Training partition exists without Out-Of-Sample partition. High risk of overfitting."
            )

        for i, p1 in enumerate(partitions):
            for p2 in partitions[i + 1 :]:
                # Check for overlap between disjoint sets if necessary (simplified)
                if (
                    p1.partition_class == PartitionClass.TRAIN
                    and p2.partition_class
                    in (PartitionClass.TEST, PartitionClass.OUT_OF_SAMPLE)
                ):
                    if max(p1.window.start_time, p2.window.start_time) < min(
                        p1.window.end_time, p2.window.end_time
                    ):
                        raise InvalidPartitionSchemeError(
                            f"Overlap detected between {p1.partition_id} and {p2.partition_id}. Leakage suspected."
                        )
        return caveats
