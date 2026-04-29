from app.optimizer.models import SearchSpace, ParameterSpec, ConstraintSpec
from app.optimizer.enums import ParameterType


def get_trend_follow_space() -> SearchSpace:
    return SearchSpace(
        name="default_trend_follow",
        strategy_family="trend_follow_core",
        parameters=[
            ParameterSpec(
                name="trend_threshold",
                param_type=ParameterType.FLOAT,
                bounds=[0.0, 2.0],
                step=0.5,
                default_value=0.0,
            ),
            ParameterSpec(
                name="volatility_multiplier",
                param_type=ParameterType.FLOAT,
                bounds=[1.0, 3.0],
                step=0.5,
                default_value=1.5,
            ),
        ],
    )


def get_mean_reversion_space() -> SearchSpace:
    return SearchSpace(
        name="default_mean_reversion",
        strategy_family="mean_reversion_core",
        parameters=[
            ParameterSpec(
                name="rsi_oversold",
                param_type=ParameterType.FLOAT,
                bounds=[20.0, 40.0],
                step=5.0,
                default_value=30.0,
            ),
            ParameterSpec(
                name="rsi_overbought",
                param_type=ParameterType.FLOAT,
                bounds=[60.0, 80.0],
                step=5.0,
                default_value=70.0,
            ),
        ],
        constraints=[
            ConstraintSpec(param1="rsi_oversold", operator="<", param2="rsi_overbought")
        ],
    )


def get_breakout_space() -> SearchSpace:
    return SearchSpace(
        name="default_breakout",
        strategy_family="breakout_core",
        parameters=[
            ParameterSpec(
                name="volume_multiplier",
                param_type=ParameterType.FLOAT,
                bounds=[1.2, 2.5],
                step=0.2,
                default_value=1.5,
            )
        ],
    )


def get_structure_space() -> SearchSpace:
    return SearchSpace(
        name="default_structure",
        strategy_family="structure_divergence_core",
        parameters=[
            ParameterSpec(
                name="score_weight",
                param_type=ParameterType.FLOAT,
                bounds=[1.0, 2.0],
                step=0.5,
                default_value=1.5,
            )
        ],
    )


def get_space_by_name(name: str) -> SearchSpace:
    spaces = {
        "default_trend_follow": get_trend_follow_space(),
        "default_mean_reversion": get_mean_reversion_space(),
        "default_breakout": get_breakout_space(),
        "default_structure": get_structure_space(),
    }
    return spaces.get(name)
