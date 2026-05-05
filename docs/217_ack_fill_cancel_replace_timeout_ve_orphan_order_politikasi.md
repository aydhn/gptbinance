# Ack, Fill, Cancel, Replace, Timeout and Orphan Order Policy

This document outlines the strict handling of venue execution events.

## Strict Rules
- **No Optimistic Success:** If we don't know the state (e.g. timeout on ack), the state is `TIMEOUT_UNKNOWN`.
- **Orphan Orders:** If a venue event arrives with no known local attempt, it is registered as an `ORPHANED` order and escalated.
- **Cancel/Replace Race Conditions:** We handle partial fills arriving after cancel intent without assuming optimistic cancel.
