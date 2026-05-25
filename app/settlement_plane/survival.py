from app.settlement_plane.models import SurvivalRecord, SurvivalClass

def evaluate_survival(survival: SurvivalRecord):
    return {"status": "surviving", "survival_id": survival.id, "class": survival.survival_class.value}
