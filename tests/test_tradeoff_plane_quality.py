import pytest
from app.tradeoff_plane.models import TradeoffObject, ObjectiveSetRecord, ObjectiveRecord, BurdenRecord, SacrificeRecord
from app.tradeoff_plane.enums import TradeoffClass, ObjectiveClass, BurdenClass, SacrificeClass
from app.tradeoff_plane.quality import quality_checker

def test_quality_checker_hidden_burden():
    obj_set = ObjectiveSetRecord(set_id="os1", objectives=[])
    burden = BurdenRecord(
        burden_id="b1",
        burden_class=BurdenClass.DELAYED,
        description="test",
        is_hidden=True
    )

    obj = TradeoffObject(
        tradeoff_id="t1",
        tradeoff_class=TradeoffClass.LOCAL,
        owner="team_a",
        scope="local",
        objective_set=obj_set,
        burden_posture=[burden]
    )

    result = quality_checker.check_quality(obj)
    assert not result["is_high_quality"]
    assert "hidden_burden_shift_warning" in result["warnings"]

def test_quality_checker_single_metric_theater():
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

    sacrifice = SacrificeRecord(
        sacrifice_id="s1",
        sacrifice_class=SacrificeClass.TEMPORARY,
        description="test"
    )

    obj = TradeoffObject(
        tradeoff_id="t1",
        tradeoff_class=TradeoffClass.LOCAL,
        owner="team_a",
        scope="local",
        objective_set=obj_set,
        burden_posture=[burden],
        sacrifices=[sacrifice]
    )

    result = quality_checker.check_quality(obj)
    assert not result["is_high_quality"]
    assert "single_metric_theater_warning" in result["warnings"]
    assert "sacrifice_burial_warning" not in result["warnings"]

def test_quality_checker_sacrifice_burial():
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
    obj_set = ObjectiveSetRecord(set_id="os1", objectives=[objective1, objective2])

    burden = BurdenRecord(
        burden_id="b1",
        burden_class=BurdenClass.DIRECT,
        description="test"
    )

    obj = TradeoffObject(
        tradeoff_id="t1",
        tradeoff_class=TradeoffClass.LOCAL,
        owner="team_a",
        scope="local",
        objective_set=obj_set,
        burden_posture=[burden],
        sacrifices=[] # Burdens exist but no explicit sacrifices
    )

    result = quality_checker.check_quality(obj)
    assert not result["is_high_quality"]
    assert "sacrifice_burial_warning" in result["warnings"]

def test_quality_checker_high_quality():
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
    obj_set = ObjectiveSetRecord(set_id="os1", objectives=[objective1, objective2])

    burden = BurdenRecord(
        burden_id="b1",
        burden_class=BurdenClass.DIRECT,
        description="test",
        is_hidden=False
    )

    sacrifice = SacrificeRecord(
        sacrifice_id="s1",
        sacrifice_class=SacrificeClass.TEMPORARY,
        description="test"
    )

    obj = TradeoffObject(
        tradeoff_id="t1",
        tradeoff_class=TradeoffClass.LOCAL,
        owner="team_a",
        scope="local",
        objective_set=obj_set,
        burden_posture=[burden],
        sacrifices=[sacrifice]
    )

    result = quality_checker.check_quality(obj)
    assert result["is_high_quality"]
    assert len(result["warnings"]) == 0
