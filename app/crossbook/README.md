# Cross Book Exposure Governance

This module provides a unified view of exposure across Spot, Margin, and Futures books without automatically netting or hedging.

## Why no auto-hedging?
Auto-hedging creates execution risks and can result in mode conflicts. The goal here is strict visibility, reporting fake hedges, borrowing dependencies, and collateral pressure so that the Execution and Risk layers can make fully informed decisions.

## Flow
1. Load books (Spot, Margin, Futures)
2. Map to UnifiedExposureNode
3. Build ExposureGraph
4. Calculate NetExposureSnapshot
5. Run ConflictDetector, CollateralAnalyzer, BorrowAnalyzer, etc.
6. Evaluate CrossBookOverlayEngine for gating
