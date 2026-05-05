from datetime import datetime, timezone
from typing import List, Dict, Optional
from app.universe.models import ProductInstrument, LifecycleEvent
from app.universe.enums import LifecycleEventType, InstrumentStatus


class LifecycleManager:
    def detect_changes(
        self,
        old_inst: Optional[ProductInstrument],
        new_inst: ProductInstrument,
        event_id_prefix: str = "evt_",
    ) -> List[LifecycleEvent]:
        events = []
        now = datetime.now(timezone.utc)

        if not old_inst:
            events.append(
                LifecycleEvent(
                    event_id=f"{event_id_prefix}{int(now.timestamp())}_listed",
                    ref=new_inst.ref,
                    event_type=LifecycleEventType.LISTED,
                    new_status=new_inst.status,
                    description=f"Instrument listed with status {new_inst.status.value}",
                    event_time=now,
                )
            )
            return events

        if old_inst.status != new_inst.status:
            evt_type = LifecycleEventType.STATUS_CHANGED
            desc = f"Status changed from {old_inst.status.value} to {new_inst.status.value}"

            if new_inst.status == InstrumentStatus.DELISTED:
                evt_type = LifecycleEventType.DELISTED
                desc = "Instrument delisted"
            elif new_inst.status == InstrumentStatus.MAINTENANCE:
                evt_type = LifecycleEventType.MAINTENANCE_STARTED
                desc = "Instrument entered maintenance"
            elif (
                old_inst.status == InstrumentStatus.MAINTENANCE
                and new_inst.status == InstrumentStatus.TRADING
            ):
                evt_type = LifecycleEventType.MAINTENANCE_ENDED
                desc = "Instrument exited maintenance"

            events.append(
                LifecycleEvent(
                    event_id=f"{event_id_prefix}{int(now.timestamp())}_status",
                    ref=new_inst.ref,
                    event_type=evt_type,
                    old_status=old_inst.status,
                    new_status=new_inst.status,
                    description=desc,
                    event_time=now,
                )
            )

        # Basic filter change detection (can be expanded)
        filters_changed = False
        if old_inst.filters.tick_size and new_inst.filters.tick_size:
            if (
                old_inst.filters.tick_size.tick_size
                != new_inst.filters.tick_size.tick_size
            ):
                filters_changed = True

        if old_inst.filters.step_size and new_inst.filters.step_size:
            if (
                old_inst.filters.step_size.step_size
                != new_inst.filters.step_size.step_size
            ):
                filters_changed = True

        if filters_changed:
            events.append(
                LifecycleEvent(
                    event_id=f"{event_id_prefix}{int(now.timestamp())}_filters",
                    ref=new_inst.ref,
                    event_type=LifecycleEventType.FILTERS_CHANGED,
                    description="Exchange filters changed (tick size or step size)",
                    event_time=now,
                )
            )

        return events
