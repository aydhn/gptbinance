from app.postmortems.models import ChronologyRecord, ChronologyEvent

from typing import List, Dict, Any


class ChronologyBuilder:
    def build(self, events: List[Dict[str, Any]]) -> ChronologyRecord:
        chrono_events = []
        is_verified = True

        # Ensure chronological order
        events.sort(key=lambda x: x.get("timestamp", ""))

        for idx, e in enumerate(events):
            if "timestamp" not in e or "event_type" not in e:
                is_verified = False
            else:
                chrono_events.append(
                    ChronologyEvent(
                        timestamp=e["timestamp"],
                        event_type=e["event_type"],
                        description=e.get("description", ""),
                    )
                )

            # Simulate basic gap check
            if idx > 0:
                prev = events[idx - 1]
                if "timestamp" in e and "timestamp" in prev:
                    # In a real system, calculate time diffs. Just a basic placeholder.
                    pass

        return ChronologyRecord(events=chrono_events, is_verified=is_verified)
