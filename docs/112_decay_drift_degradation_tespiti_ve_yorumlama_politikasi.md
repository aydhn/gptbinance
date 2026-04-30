# Phase 21: Decay, Drift ve Degradation Tespiti

Bu doküman decay sinyallerini ve bunların nasıl yorumlandığını açıklar.

## Decay Sinyalleri
1. **OOS Decay**: Walk-forward testlerde out-of-sample performansın beklenen aralığın dışına çıkması.
2. **Live-Paper Divergence**: Canlı ortamdaki execution kalitesiyle paper ortamdaki beklentilerin uyuşmaması.
3. **Calibration Decay**: ML modellerinin confidence skorlarının zamanla kayması.
4. **Drift-driven Degradation**: Feature bazlı schema veya dağılım kaymalarının (data drift) stratejiyi etkilemesi.

## Severity (Şiddet)
- Low: İzlemeye al.
- Medium: Uyarı üret, research refresh tetikle.
- High/Critical: Aktif bundle için caution flag'i kaldır, rollback planı iste.
