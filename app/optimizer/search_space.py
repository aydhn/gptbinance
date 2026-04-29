from typing import List, Dict, Any, Union
import numpy as np
from app.optimizer.models import SearchSpace, ParameterSpec, ConstraintSpec
from app.optimizer.enums import ParameterType
from app.optimizer.exceptions import InvalidSearchSpace, InvalidParameterSpec


class SearchSpaceEvaluator:
    @staticmethod
    def validate_space(space: SearchSpace) -> None:
        if not space.parameters:
            raise InvalidSearchSpace("Search space must define at least one parameter.")

        param_names = set()
        for p in space.parameters:
            if p.name in param_names:
                raise InvalidParameterSpec(f"Duplicate parameter name: {p.name}")
            param_names.add(p.name)

            if p.param_type in [ParameterType.INT, ParameterType.FLOAT]:
                if not p.whitelist and not p.bounds:
                    raise InvalidParameterSpec(
                        f"Numeric parameter {p.name} must have bounds or whitelist."
                    )
                if p.bounds and len(p.bounds) != 2:
                    raise InvalidParameterSpec(
                        f"Bounds for {p.name} must have exactly 2 elements [min, max]."
                    )
                if p.bounds and p.bounds[0] > p.bounds[1]:
                    raise InvalidParameterSpec(
                        f"Bounds for {p.name} must be [min, max] where min <= max."
                    )
            elif p.param_type == ParameterType.CATEGORICAL:
                if not p.whitelist:
                    raise InvalidParameterSpec(
                        f"Categorical parameter {p.name} must have a whitelist."
                    )

        for c in space.constraints:
            if c.param1 not in param_names:
                raise InvalidSearchSpace(
                    f"Constraint references unknown parameter: {c.param1}"
                )
            if c.param2 not in param_names:
                raise InvalidSearchSpace(
                    f"Constraint references unknown parameter: {c.param2}"
                )
            if c.operator not in ["<", "<=", ">", ">=", "!=", "=="]:
                raise InvalidSearchSpace(f"Unknown constraint operator: {c.operator}")

    @staticmethod
    def is_valid_combination(
        values: Dict[str, Union[int, float, str]], constraints: List[ConstraintSpec]
    ) -> bool:
        for c in constraints:
            if c.param1 not in values or c.param2 not in values:
                continue

            v1 = values[c.param1]
            v2 = values[c.param2]

            if isinstance(v1, str) or isinstance(v2, str):
                if c.operator == "==" and v1 != v2:
                    return False
                if c.operator == "!=" and v1 == v2:
                    return False
                continue

            try:
                if c.operator == "<" and not (v1 < v2):
                    return False
                if c.operator == "<=" and not (v1 <= v2):
                    return False
                if c.operator == ">" and not (v1 > v2):
                    return False
                if c.operator == ">=" and not (v1 >= v2):
                    return False
                if c.operator == "==" and not (v1 == v2):
                    return False
                if c.operator == "!=" and not (v1 != v2):
                    return False
            except TypeError:
                return False

        return True

    @staticmethod
    def expand_parameter(spec: ParameterSpec) -> List[Union[int, float, str]]:
        if spec.whitelist is not None and len(spec.whitelist) > 0:
            return spec.whitelist

        if spec.param_type == ParameterType.INT:
            if spec.bounds:
                step = int(spec.step) if spec.step else 1
                return list(range(int(spec.bounds[0]), int(spec.bounds[1]) + 1, step))
            return [spec.default_value]

        elif spec.param_type == ParameterType.FLOAT:
            if spec.bounds:
                step = float(spec.step) if spec.step else 0.1
                values = np.arange(
                    float(spec.bounds[0]), float(spec.bounds[1]) + (step / 2), step
                )
                return [round(v, 6) for v in values.tolist()]
            return [spec.default_value]

        elif spec.param_type == ParameterType.CATEGORICAL:
            if spec.whitelist:
                return spec.whitelist
            return [spec.default_value]

        return [spec.default_value]
