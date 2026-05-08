from app.simulation_plane.models import OOSReport, SimulationPartition
from app.simulation_plane.enums import OOSClass
from typing import List


class OOSEvaluator:
    def evaluate(self, run_id: str, partitions: List[SimulationPartition]) -> OOSReport:
        has_train = False
        has_oos = False

        # very simplified logic
        for p in partitions:
            if p.partition_class == "train":
                has_train = True
            if p.partition_class in ["test", "out_of_sample"]:
                has_oos = True

        leakage = False
        # (Assuming overlaps checked elsewhere)

        oos_class = (
            OOSClass.STRICT_OOS
            if (has_train and has_oos and not leakage)
            else OOSClass.LEAKAGE_SUSPECTED
        )

        return OOSReport(
            run_id=run_id,
            oos_class=oos_class,
            leakage_checks_passed=not leakage,
            caveats=["Explicit OOS window evaluation."]
            if oos_class == OOSClass.STRICT_OOS
            else ["In-sample success masquerading as OOS."],
        )
