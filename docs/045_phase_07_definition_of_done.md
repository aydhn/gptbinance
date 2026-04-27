# Phase 07: Definition of Done

## Tamamlanma Ölçütleri
- `Strategy` registry ve engine mekanizmaları başarıyla çalışıyorsa.
- Kural (rule), filtre (filter), skor (score), conflict ve cooldown zinciri eksiksiz kurulmuşsa.
- **Signal Candidate** ile **Intent Candidate** ayrımı koda net olarak yansımışsa.
- Her sinyal için açıklanabilirlik (explainability / rationale) sağlanmışsa.
- En az dört örnek strategy family (Trend, Mean Reversion, Breakout, Structure) implemente edilmişse.
- CLI üzerinden (yeni `--evaluate-strategies` vb. flag'lerle) strateji değerlendirmesi, özetler ve açıklamalar (rationale) alınabiliyorsa.
- Framework'ü doğrulayan tüm birim testler yazılmışsa ve başarıyla geçiyorsa.
- Hiçbir execution, gerçek trade mantığı, paper fill simülasyonu eklenmemişse (risk layer bypass edilmiyorsa).

## Bilerek Ertelenenler
- Gerçek order gönderimi, paper fill motoru.
- Portfolio management, PnL hesaplama.
- Stop-loss / take-profit mekanizmaları, risk sizing.
- Canlı state (live trading state) ile tam cooldown entegrasyonu (şu an sadece stateless/memory temelli varsayımlar veya basit in-memory tasarımlar olacak).

## Sonraki Faza Geçiş Şartları
Yukarıdaki tüm tamamlanma ölçütlerinin testlerle doğrulanması ve `app/strategies/` altındaki yapının risk/execution katmanına bağlanmaya hazır temiz bir API (SignalCandidate / EntryIntentCandidate / ExitIntentCandidate listeleri) dönmesi şarttır.
