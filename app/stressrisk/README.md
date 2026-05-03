# Phase 38: Stress-Risk & Tail-Loss Overlay Architecture

Bu katmanın amacı, sistemin mevcut risk, portföy, derivatives ve event-risk bileşenlerinin üstüne, muhafazakâr, senaryo odaklı, stress-test yapılabilir ve açıklanabilir bir "tail-loss görünürlüğü" eklemektir.

## Neden Bu Katman Gerekti?
Sıradan volatilite ve korelasyon varsayımları altında güvenli görünen portföyler; ani gap, likidite daralması, execution bozulması (spread widening, slippage), funding şokları gibi uç durumlarda kabul edilemez kayıplara (tail-loss) yol açabilir.

## Ne Yapmaz?
- Otomatik hedge açmaz.
- Sessiz pozisyon kapatmaz veya auto de-risking yapmaz.
- Matematiksel "sihirli" tek bir risk skoru (örn. gizli VaR) üretmez, breakdown ve vulnerability şeffaflığı sunar.
- Risk/portfolio safety gate'leri bypass etmez.

## Akış (Flow)
1. **Scenarios -> Shocks:** Ön tanımlı senaryolar (örn. Exchange Liquidity Freeze) şok vektörlerine çevrilir.
2. **Losses:** Şoklar altındaki pozisyonların (sembol/portföy bazlı) tahmini kayıpları hesaplanır.
3. **Budgets:** Profil bazlı tail-loss bütçeleriyle (live, paper, canary_live vb.) kıyaslanır.
4. **Overlay:** Karar mekanizması (allow, caution, block vb.) risk ve portföy yönetim katmanlarına "evidence" (delil) olarak sunulur.

## Dosya Organizasyonu
- `scenarios.py`: Scenario registry.
- `shocks.py`: Şok üretim motoru.
- `losses.py`: Kayıp tahmincisi.
- `budgets.py`: Bütçe kontrolörü.
- `correlation.py` / `liquidity.py`: Spesifik risk faktörleri overlayleri.
- `portfolio.py` / `derivatives.py`: Portfolio ve kaldıraç kırılganlık analizleri.
- `overlay.py`: Overlay karar üretim motoru.
