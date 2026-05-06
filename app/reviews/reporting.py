from app.reviews.queues import QueueEngine


class ReportingEngine:
    def __init__(self, queue_engine: QueueEngine):
        self.queue_engine = queue_engine

    def summarize_queues(self):
        report = []
        items = self.queue_engine.get_pending_items()
        report.append(f"Total Pending Reviews: {len(items)}")

        from collections import defaultdict

        q_counts = defaultdict(int)
        p_counts = defaultdict(int)
        for item in items:
            q_counts[item.queue_id] += 1
            p_counts[item.priority] += 1

        report.append("\nPriority Breakdown:")
        for p, count in p_counts.items():
            report.append(f"  - {p.value}: {count}")

        return "\n".join(report)
