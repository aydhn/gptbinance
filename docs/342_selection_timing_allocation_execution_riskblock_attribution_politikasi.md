# Selection, Timing, Allocation, Execution ve Risk-Block Attribution Politikası

Attribution sınıflandırması, kazanılan (veya kaybedilen) paranın *hangi karardan* dolayı oluştuğunu kesinleştirir.

## Sınıflar
- **SIGNAL_SELECTION:** Modelin/Stratejinin doğru sembolü seçip seçmediği.
- **TIMING:** Giriş/çıkış anının ne kadar optimize olduğu.
- **ALLOCATION_SIZING:** Sermaye büyüklüğü veya clipping nedeniyle oluşan etki.
- **EXECUTION:** Slippage, markout ve fill kalitesinin yarattığı sürtünme (drag).
- **RISK_BLOCK_COOLDOWN:** Risk engellerinin (freeze, no_new_exposure) performans üstündeki fırsat maliyeti.
- **FEE_FUNDING_CARRY:** Doğrudan operasyonel maliyetler.
- **RESIDUAL_UNEXPLAINED:** Açıklanamayan bakiye. Bu bakiyenin belirli bir %'yi aşması durumunda trust verdict *degraded* olur.

Bu ayrımlar, execution drag'in sinyal hatası sanılmasını (veya tam tersini) engeller.
