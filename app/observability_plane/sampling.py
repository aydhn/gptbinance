from typing import Dict, List, Optional
from .models import SamplingRecord
from .enums import SamplingClass
from .exceptions import InvalidSamplingDefinitionError

class SamplingRegistry:
    def __init__(self):
        self._sampling: Dict[str, SamplingRecord] = {}

    def register_sampling(self, record: SamplingRecord) -> None:
        if record.sampling_class == SamplingClass.RATE and not (0.0 < record.sampling_rate <= 1.0):
            raise InvalidSamplingDefinitionError("Rate sampling requires a valid rate > 0 and <= 1.0")
        self._sampling[record.telemetry_id] = record

    def get_sampling(self, telemetry_id: str) -> Optional[SamplingRecord]:
        return self._sampling.get(telemetry_id)

    def list_sampling(self) -> List[SamplingRecord]:
        return list(self._sampling.values())
