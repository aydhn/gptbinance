# Delegation, Temporary Elevation, and Breakglass Policy

## Delegation
Capabilities can be temporarily transferred (delegated) with a strict TTL.
Certain high-risk capabilities (e.g., `FINALIZE_POSTMORTEM`, `REVIEW_BREAKGLASS`) are strictly non-delegable.

## Temporary Elevation
Users can request elevated capabilities (Purpose Bound). Requires approval and has a strict TTL.

## Breakglass
Emergency override.
- Activates immediately.
- Records explicit reason.
- Mandates a Post-Event Review by a separate authority.
