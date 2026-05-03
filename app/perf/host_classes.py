from typing import Dict, List
from app.perf.enums import HostClass
from app.perf.models import HostClassDefinition


class HostClassRegistry:
    _classes: Dict[HostClass, HostClassDefinition] = {}

    @classmethod
    def register(cls, definition: HostClassDefinition) -> None:
        cls._classes[definition.host_class] = definition

    @classmethod
    def get(cls, host_class: HostClass) -> HostClassDefinition:
        if host_class not in cls._classes:
            # Fallback to a safe default if not explicitly registered but enum exists
            return HostClassDefinition(
                host_class=host_class,
                expected_cores=2,
                expected_ram_gb=4,
                recommended_modes=["dev"],
                caution_modes=["live"],
            )
        return cls._classes[host_class]


_builtin_host_classes = [
    HostClassDefinition(
        host_class=HostClass.LOCAL_MINIMAL,
        expected_cores=2,
        expected_ram_gb=4,
        recommended_modes=["dev", "paper"],
        caution_modes=["testnet", "live"],
    ),
    HostClassDefinition(
        host_class=HostClass.LOCAL_AVERAGE,
        expected_cores=4,
        expected_ram_gb=8,
        recommended_modes=["dev", "paper", "testnet"],
        caution_modes=["live", "analytics_batch"],
    ),
    HostClassDefinition(
        host_class=HostClass.LOCAL_ENHANCED,
        expected_cores=8,
        expected_ram_gb=16,
        recommended_modes=["dev", "paper", "testnet", "live", "analytics_batch"],
        caution_modes=[],
    ),
    HostClassDefinition(
        host_class=HostClass.WORKSTATION_GPU_OPTIONAL,
        expected_cores=16,
        expected_ram_gb=32,
        recommended_modes=[
            "dev",
            "paper",
            "testnet",
            "live",
            "analytics_batch",
            "ml_inference_batch",
        ],
        caution_modes=[],
    ),
]

for hc in _builtin_host_classes:
    HostClassRegistry.register(hc)
