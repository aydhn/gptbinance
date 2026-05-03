# Stress-Risk ve Tail-Loss Mimarisi ve Scenario Politikası

## Neden Tail-Risk Katmanı Gerekli?
Mevcut risk kontrolleri genelde "ortalama" piyasa koşulları veya bilinen limitler dahilinde çalışır. Ancak piyasalarda aniden oluşan boşluklar (gaps), korelasyonların bir anda 1.0'e çıkması veya likiditenin aniden kuruyup slipajın sıçraması "tail risk" dediğimiz kuyruk risklerini oluşturur. Bu doküman, Phase 38 itibariyle devreye giren bu yeni katmanın temel mimarisini ve kurallarını açıklar.

## Mimari Akış
1. **Scenario Registry (`scenarios.py`)**: Olası şok durumlarını tanımlar (örn. Macro Gap Down).
2. **Shock Vectors (`shocks.py`)**: Senaryoların portföy veya sembol üzerindeki matematiksel etkilerini hesaplar.
3. **Loss Estimation (`losses.py`)**: Şoklar uygulandıktan sonra ne kadar kayıp yaşanacağını çıkarır.
4. **Tail-Loss Budgets (`budgets.py`)**: İlgili profile (live, paper, testnet_exec) göre kabul edilebilir azami kayıp miktarlarını belirler.
5. **Overlay Decision (`overlay.py`)**: Tüm çıktılar birleştirilir ve riskin tolere edilip edilemeyeceğine dair Allow/Caution/Block şeklinde net bir karar üretilir.

## Politikalar ve Kesin Sınırlar
- **No Auto-Hedging:** Bu katman hiçbir koşulda otonom olarak riskten kaçınma (de-risking), hedge pozisyonu açma veya açık pozisyonları kapatma işlemi gerçekleştirmez. Amacı yalnızca risk şeffaflığı (visibility) sunmak ve gerektiğinde yeni işlemlere blokaj (caution/block overlay) getirmektir.
- **Dürüst Hesaplama:** Model varsayımları muhafazakâr tutulmalı, bilinmeyen/eksik veri durumunda daima "en kötü senaryo" varsayılmalıdır.
