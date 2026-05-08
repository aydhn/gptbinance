from app.simulation_plane.partitions import PartitionEvaluator
from app.simulation_plane.models import SimulationPartition, SimulationWindow
from app.simulation_plane.enums import PartitionClass
from datetime import datetime


def test_partitions_no_oos():
    evaluator = PartitionEvaluator()
    w = SimulationWindow(start_time=datetime(2023, 1, 1), end_time=datetime(2023, 2, 1))
    p = SimulationPartition(
        partition_id="p1", partition_class=PartitionClass.TRAIN, window=w
    )
    caveats = evaluator.evaluate([p])
    assert (
        "Training partition exists without Out-Of-Sample partition. High risk of overfitting."
        in caveats
    )
