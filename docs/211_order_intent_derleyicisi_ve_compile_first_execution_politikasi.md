# Order Intent Compiler & Compile-First Execution Policy

## Overview
This document outlines the policy of using a compile-first approach to execution. Instead of sending raw orders directly from strategies to the exchange, high-level intents (e.g., "open_long", "reduce_position") are submitted to the **Order Intent Compiler**.

## Why Compile-First?
1. **Safety**: Venue-specific rules (like positionSide for futures, or reduceOnly flags) must be strictly managed. Without compilation, missing a flag can lead to unintended exposure.
2. **Account Mode Compatibility**: Compiling ensures that the intent is valid against the active account mode (e.g., One-way vs Hedge mode).
3. **Auditability**: We can store the *plan* vs the *intent* to show exactly why a specific set of raw orders was created (e.g., adding a borrow leg for margin).

## Lineage
High-Level Intent -> Context + Policy Check -> Compiled Order Plan -> Validation -> Submission.
We never submit raw orders without an underlying Compiled Order Plan.
