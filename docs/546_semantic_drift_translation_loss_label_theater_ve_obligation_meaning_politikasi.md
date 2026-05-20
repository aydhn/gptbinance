# Semantic Drift & Label Theater

## Label Theater
Treating a simple label (e.g., `status="healthy"`) as carrying complex meaning without canonical semantics is Label Theater.

## Semantic Drift
When a metric's formula or a threshold's meaning slowly changes over time without explicit re-registration, the Semantic Plane flags this as Semantic Drift.

## Translation Loss
Translating semantics across domains (e.g., from external API to internal representations) often sheds context. This loss must be explicitly calculated to warn about portability issues.
