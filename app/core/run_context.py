import uuid
import datetime
from dataclasses import dataclass
from app.core.enums import EnvironmentProfile, AppRunMode


@dataclass
class RunContext:
    run_id: str
    start_time_utc: datetime.datetime
    profile: EnvironmentProfile
    run_mode: AppRunMode

    @classmethod
    def create(cls, profile: EnvironmentProfile, run_mode: AppRunMode) -> "RunContext":
        return cls(
            run_id=str(uuid.uuid4()),
            start_time_utc=datetime.datetime.now(datetime.timezone.utc),
            profile=profile,
            run_mode=run_mode,
        )


# Global context holder, will be initialized during bootstrap
_active_context: RunContext | None = None


def get_active_context() -> RunContext | None:
    return _active_context


def set_active_context(context: RunContext):
    global _active_context
    _active_context = context
