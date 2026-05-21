import pytest
from app.tradeoff_plane.models import TradeoffObject, ObjectiveSetRecord, ObjectiveRecord, BurdenRecord
from app.tradeoff_plane.enums import TradeoffClass, ObjectiveClass, BurdenClass, EquivalenceVerdict
from app.tradeoff_plane.equivalence import equivalence_evaluator

def test_equivalence_evaluator_equivalent():
    objective = ObjectiveRecord(
        objective_id="o1",
        name="Speed",
        description="Go fast",
        objective_class=ObjectiveClass.SPEED,
        scope="local"
    )
    obj_set = ObjectiveSetRecord(set_id="os1", objectives=[objective])

    burden = BurdenRecord(
        burden_id="b1",
        burden_class=BurdenClass.DIRECT,
        description="test"
    )

    obj1 = TradeoffObject(
        tradeoff_id="t1",
        tradeoff_class=TradeoffClass.LOCAL,
        owner="team_a",
        scope="local",
        objective_set=obj_set,
        burden_posture=[burden]
    )

    obj2 = TradeoffObject(
        tradeoff_id="t1",
        tradeoff_class=TradeoffClass.LOCAL,
        owner="team_a",
        scope="local",
        objective_set=obj_set,
        burden_posture=[burden]
    )

    envs = ["paper", "live"]
    objects = {"paper": obj1, "live": obj2}

    report = equivalence_evaluator.evaluate(envs, objects)
    assert report.verdict == EquivalenceVerdict.EQUIVALENT
    assert len(report.divergence_sources) == 0

def test_equivalence_evaluator_divergent_objectives():
    objective1 = ObjectiveRecord(
        objective_id="o1",
        name="Speed",
        description="Go fast",
        objective_class=ObjectiveClass.SPEED,
        scope="local"
    )
    objective2 = ObjectiveRecord(
        objective_id="o2",
        name="Safety",
        description="Stay safe",
        objective_class=ObjectiveClass.SAFETY,
        scope="local"
    )

    obj_set1 = ObjectiveSetRecord(set_id="os1", objectives=[objective1])
    obj_set2 = ObjectiveSetRecord(set_id="os2", objectives=[objective1, objective2])

    obj1 = TradeoffObject(
        tradeoff_id="t1",
        tradeoff_class=TradeoffClass.LOCAL,
        owner="team_a",
        scope="local",
        objective_set=obj_set1,
        burden_posture=[]
    )

    obj2 = TradeoffObject(
        tradeoff_id="t1",
        tradeoff_class=TradeoffClass.LOCAL,
        owner="team_a",
        scope="local",
        objective_set=obj_set2,
        burden_posture=[]
    )

    envs = ["paper", "live"]
    objects = {"paper": obj1, "live": obj2}

    report = equivalence_evaluator.evaluate(envs, objects)
    assert report.verdict == EquivalenceVerdict.DIVERGENT
    assert "objective_divergence_in_live" in report.divergence_sources
