# Validation Layer

This module provides a rigorous validation layer for backtest results. It prevents self-deception by automatically running benchmark strategies (like Buy & Hold, Flat, Naive Trend), performing ablation studies (turning features off to see their impact), and executing research honesty guards (flagging low trade counts, excessive DD, etc.).
