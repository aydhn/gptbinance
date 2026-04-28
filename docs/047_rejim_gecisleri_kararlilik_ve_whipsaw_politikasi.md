# Rejim Geçişleri, Kararlılık ve Whipsaw Politikası

Piyasada rejimler statik değildir. Geçiş dönemleri, stratejiler için en tehlikeli zamanlardır.

## Transition (Geçiş) Kavramı
Rejim motoru her değerlendirmede sadece anlık durumu değil, bir önceki duruma göre değişimi de (`RegimeTransition`) takip eder.

## Whipsaw ve Kararsız Rejimler
Fiyatın belirli eşiklerde git-gel yapması durumunda rejim sürekli değişebilir (örn. Güçlü Trend -> Yönsüz -> Zayıf Trend -> Yönsüz). Bu tür durumlar Whipsaw (testere) olarak adlandırılır. Whipsaw ortamları, çoğu strateji için risklidir.

## Kalite Notlarının Önemi
Rejim motoru sadece bir etiket üretmez, aynı zamanda bu etiketin ne kadar güvenilir olduğunu ve geçiş kararlılığını ölçen kalite notları (`ContextQuality`, `stability_score`) üretir. Düşük stabilite skorları, stratejilere risk yönetimi kurallarını sıkılaştırma veya işlemden kaçınma sinyali verir.
