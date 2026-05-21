import pytest
from app.tradeoff_plane.models import TradeoffObject, ObjectiveSetRecord, ObjectiveRecord, BurdenRecord, SacrificeRecord
from app.tradeoff_plane.enums import TradeoffClass, ObjectiveClass, BurdenClass, SacrificeClass, TrustVerdict
from app.tradeoff_plane.trust import trust_evaluator

def test_trust_evaluator_missing_objectives():
    obj_set = ObjectiveSetRecord(set_id="os1", objectives=[])

    obj = TradeoffObject(
        tradeoff_id="t1",
        tradeoff_class=TradeoffClass.LOCAL,
        owner="team_a",
        scope="local",
        objective_set=obj_set,
        burden_posture=[]
    )

    verdict = trust_evaluator.evaluate(obj)
    assert verdict.verdict == TrustVerdict.BLOCKED
    assert verdict.factors["objective_clarity"] == "missing_objectives"

def test_trust_evaluator_hidden_burdens():
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

    verdict = trust_evaluator.evaluate(obj)
    assert verdict.verdict == TrustVerdict.DEGRADED
    assert verdict.factors["burden_visibility"] == "hidden_burdens_detected"

def test_trust_evaluator_no_burdens_caution():
    objective = ObjectiveRecord(
        objective_id="o1",
        name="Speed",
        description="Go fast",
        objective_class=ObjectiveClass.SPEED,
        scope="local"
    )
    obj_set = ObjectiveSetRecord(set_id="os1", objectives=[objective])

    obj = TradeoffObject(
        tradeoff_id="t1",
        tradeoff_class=TradeoffClass.LOCAL,
        owner="team_a",
        scope="local",
        objective_set=obj_set,
        burden_posture=[]
    )

    verdict = trust_evaluator.evaluate(obj)
    assert verdict.verdict == TrustVerdict.CAUTION
    assert verdict.factors["burden_visibility"] == "no_burdens_declared"

def test_trust_evaluator_trusted():
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

    verdict = trust_evaluator.evaluate(obj)
    assert verdict.verdict == TrustVerdict.TRUSTED
    assert verdict.factors["objective_clarity"] == "clear"
    assert verdict.factors["burden_visibility"] == "visible"
    assert verdict.factors["sacrifice_explicitness"] == "explicit"
