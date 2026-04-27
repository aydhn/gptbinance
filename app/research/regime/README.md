# Regime (Context) Engine

This module is responsible for analyzing the market environment and classifying it into distinct regimes (e.g., Trending, Volatile, Mean-Reverting) based on the computed features.

**It does not generate trading signals.** Instead, it provides the necessary context for the Strategy Engine to decide *whether* to trade and *which* strategies are suitable for the current conditions.

## Key Components
- **Evaluators**: Assess specific market dimensions (Trend, Volatility, etc.).
- **Registry**: Manages the available evaluators.
- **Transitions**: Detects shifts between regimes to warn about market instability (whipsaws).
- **MTF Context**: Aligns multiple timeframes to provide a cohesive macro and micro view.
- **Suitability**: Maps the current regime to strategy families to indicate which approaches are favored.
