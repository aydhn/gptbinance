# Event Risk Intelligence Mimarisi

Bu belge, planlı olaylar (scheduled events), bakım pencereleri (maintenance windows) ve karar kısıtlamalarını (event-aware trading) yöneten modülün mimarisini açıklar.

## 1. Neden Event Risk Intelligence Katmanı?
Teknik, operasyonel ve finansal katmanlar ne kadar olgun olursa olsun, dış dünyadaki makro olaylar (ör. CPI, FOMC) veya platform bakımları likiditeyi ve fiyatları anormal şekilde etkileyebilir. Bu riskleri sistematik, denetlenebilir ve otomatize edilebilir bir yolla ele almak için Event-Risk katmanı kurulmuştur.

## 2. Scraping Neden Yasak?
Kararların stabil, öngörülebilir ve güvenilir kaynaklara dayanması gerekir. HTML scraping hem kırılgan hem de belirsizdir. Bu sistem sadece API destekli, yapısal (structured) ve ücretsiz/meşru ekonomik takvim veya resmi borsa duyurularıyla çalışır.

## 3. Akış Mimarisi
1. **Sources**: `app/events/sources.py` - Kaynaklardan verileri alır.
2. **Normalization**: `app/events/normalization.py` - Verileri standart EventRecord nesnesine çevirir.
3. **Windows**: `app/events/windows.py` - Olay bazlı zaman pencereleri ve birleşmeleri (merge) hesaplar.
4. **Overlay**: `app/events/overlay.py` - Profile ve severity'e göre Allow/Caution/Block gibi kararlar üretir.
5. **Gating**: Üretilen kararlar execution, portfolio ve strategy katmanlarına yönlendirilir.
