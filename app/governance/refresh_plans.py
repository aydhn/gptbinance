from app.governance.models import RefreshPlan


def get_fast_refresh_plan() -> RefreshPlan:
    return RefreshPlan(
        name="fast_refresh",
        components=["data", "features", "decay_check"],
        is_deep=False,
        risk_level="low",
    )


def get_research_refresh_plan() -> RefreshPlan:
    return RefreshPlan(
        name="research_refresh",
        components=["data", "features", "validation", "strategy", "optimizer", "ml"],
        is_deep=False,
        risk_level="medium",
    )


def get_deep_refresh_plan() -> RefreshPlan:
    return RefreshPlan(
        name="deep_refresh",
        components=[
            "data",
            "features",
            "validation",
            "strategy",
            "optimizer",
            "ml",
            "promotion",
        ],
        is_deep=True,
        risk_level="high",
    )


def get_manual_refresh_plan(components: list) -> RefreshPlan:
    return RefreshPlan(
        name="manual_refresh",
        components=components,
        is_deep=False,
        risk_level="variable",
    )
