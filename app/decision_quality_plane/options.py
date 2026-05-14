from typing import List, Dict
from app.decision_quality_plane.models import OptionRecord
from app.decision_quality_plane.exceptions import InvalidOptionSetError

class OptionManager:
    def __init__(self):
        self._options: Dict[str, List[OptionRecord]] = {}

    def add_option(self, decision_id: str, option: OptionRecord):
        if decision_id not in self._options:
            self._options[decision_id] = []
        self._options[decision_id].append(option)

    def validate_option_set(self, decision_id: str) -> bool:
        opts = self._options.get(decision_id, [])
        if len(opts) < 2:
            raise InvalidOptionSetError(f"Decision {decision_id} must have at least 2 options (including defer/no-op)")
        has_noop = any(o.option_class.value == "defer_no_op" for o in opts)
        if not has_noop:
            raise InvalidOptionSetError("Missing required DEFER_NO_OP alternative")
        return True

    def get_options(self, decision_id: str) -> List[OptionRecord]:
        return self._options.get(decision_id, [])
