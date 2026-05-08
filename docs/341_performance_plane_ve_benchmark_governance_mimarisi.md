# Performance Plane ve Benchmark Governance Mimarisi

## Neden Performance Plane?
PnL bilmek yetmez. Neden oluştuğunu bilmiyorsan sistemden öğrenemezsin. Execution drag sinyal zayıflığı sanılabilir, risk block yüzünden kaçan trade'ler başarısızlık sayılabilir, benchmark yanlış seçilebilir. Bu yüzden `Returns -> Benchmarks -> Attribution -> Drags -> Opportunity -> Trust` zincirinin şeffaf ve denetlenebilir olması şarttır.

## Akış
1. **Returns:** Gerçekleşen (realized) ve marklanan (equity/unrealized) getiriler.
2. **Benchmarks:** Açık tipli (cash_baseline, regime_matched vb.) karşılaştırma referansları. Gizli değişim yasak.
3. **Attribution:** PnL'in bileşenlerine (signal, timing, allocation, execution, risk-block) bölünmesi. Kalan kısım `unexplained_residual` olarak tutulur.
4. **Drags:** Sürtünmeler (slippage, fee, funding, carry, idle-cash) şeffafça drag surface olarak eklenir.
5. **Opportunity:** Kaçırılan (foregone, risk_blocked, clipped) fırsatlar. Kesin kar gibi sunulmaz, strict caveatler taşır.
6. **Trust:** Replay/Paper/Live farkları (Equivalence) ve genel veri kalitesi, 'Trusted Performance Verdict' oluşturur.

## Prensipler
- **No Vanity Tearsheets:** Sadece pazarlama amaçlı Sharpe vb. üretilmez.
- **Benchmark Discipline:** Cherry-picking yapılamaz; her getiri beyanı baseline kanıtı gerektirir.
- **Governance:** Performans gerçeği, bir incident root cause veya readiness domain onayı olabilir.
