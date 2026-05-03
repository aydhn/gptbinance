# Phase 37: Universe & Instrument Lifecycle Layer

This module provides an event-aware, non-scraping framework to manage the trading universe.

## Why this layer?
A trading system is only as safe as its instrument definitions. We must know:
- Which symbols are eligible for a given profile?
- Are the exchange filters (tick size, min notional) present and valid?
- What is the liquidity and spread severity?
- Has the symbol been delisted or halted?

## Key Principles
1. **No HTML Scraping**: We only use official JSON API endpoints for metadata.
2. **Product-Aware**: A symbol like `BTCUSDT` is distinct across Spot, Margin, and Futures.
3. **Conservative Fallbacks**: If metadata is stale or missing, the symbol is blocked or marked with caution.
4. **Profile-Specific Eligibility**: `canary_live_caution` has strict liquidity/spread requirements, while `paper_default` is more permissive.
5. **No Discretionary Expansion**: Symbols are filtered systematically, avoiding automated "hype chasing".
