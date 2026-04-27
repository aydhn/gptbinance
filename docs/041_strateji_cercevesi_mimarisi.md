# Phase 07: Strateji Çerçevesi Mimarisi

## Neden Strategy Framework Gerekiyor?
Bir trading sisteminde "Feature üreten bir sistem ile trade eden bir sistem arasında, kuralları açık, açıklanabilir, geriye dönük incelenebilir ve daha sonra risk/portfolio/execution katmanına bağlanabilir bir karar katmanı yoksa proje kısa sürede karmakarışık olur."
Bu nedenle; feature'ları işleyip, kurallı olarak değerlendiren ve execution'a geçmeden önce niyeti (intent) ortaya koyan ara bir "karar adayı" (signal candidate) katmanına ihtiyaç vardır.

## Feature -> Signal -> Intent Zinciri
1. **Feature:** Ham piyasa verilerinden üretilmiş, belli bir pazar karakteristiğini ölçen özellik (örn. SMA, RSI).
2. **Signal (Signal Candidate):** "Bu zaman noktasında stratejik açıdan dikkat çekici bir durum oluştu." (örn. RSI aşırı satımdan döndü). Henüz trade yapılması gerektiği anlamına gelmez.
3. **Intent (Entry/Exit Intent Candidate):** "Risk ve execution katmanına iletilebilecek potansiyel giriş/çıkış niyeti var." Signal'in filtrelenmiş, skorlanmış ve onanmış halidir.

## Execution'dan Neden Ayrıldığı?
Bu fazda herhangi bir execution (emir gönderme, paper fill, pozisyon yönetimi) yapılmaz.
Ayrımın temel sebepleri:
- Stratejilerin görevi fırsatları tespit etmektir, sermayeyi nasıl yöneteceğine karar vermek değil.
- Execution kararı, risk yönetimi ve mevcut portföy durumu ile birlikte verilir. Strateji katmanı bu bağlamdan izole çalışmalıdır.
- "Sadece karar adayları üreten, execution'dan tamamen ayrı bir katman" mimari temizliği ve modülerliği sağlar.

## Explainability'nin Rolü
Her signal ve intent açıklanabilir olmalıdır. "Black box" stratejilerden kaçınılmalıdır.
Telegram bildirimleri, günlük raporlar, geriye dönük testler (backtesting) ve hata ayıklama (debugging) için; bir sinyalin hangi kuralları geçtiği, neden o skoru aldığı ve neden elenmediği bilinmelidir.
