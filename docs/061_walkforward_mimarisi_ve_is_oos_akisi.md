# Phase 11: Walk-forward Orchestration

Tek parça backtest raporları piyasa koşullarına karşı dayanıklılığı test etmez.
Bu katman Walk-Forward analizi sunar:
- Windowing (IS / OOS)
- Candidate Selection & Freeze (Parametre sabitleme)
- Segment Execution
- Aggregation (Sadece OOS sonuçları birleştirilir)
