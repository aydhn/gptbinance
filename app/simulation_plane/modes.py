from typing import Dict
from app.simulation_plane.enums import SimulationMode


class ModeRegistry:
    CAVEATS: Dict[SimulationMode, str] = {
        SimulationMode.REPLAY_EVENT_TRUTH: "Assumes exact event ordering; missing data may cause drift.",
        SimulationMode.BAR_APPROXIMATION: "Aggregates events into bars; intra-bar path is obscured. High risk of fill approximation errors.",
        SimulationMode.PAPER_PROJECTION: "Forward projection with delayed truth alignment. Vulnerable to market impact discrepancies.",
        SimulationMode.HYBRID_EXECUTION_APPROXIMATION: "Combines historical state with simulated execution latency/slippage.",
        SimulationMode.FROZEN_FEATURE_MODEL_TRIAL: "Tests model outputs on historical features without dynamic execution feedback.",
    }

    @classmethod
    def get_caveat(cls, mode: SimulationMode) -> str:
        return cls.CAVEATS.get(mode, "Unknown mode caveats.")
