# Activation History, Lineage ve Governance Truthfulness Politikası

## Neden Active-Set Lineage Önemlidir?
Geleneksel feature-flag sistemleri "şu an ne açık" sorusunu cevaplar ama "bunu kim, hangi onay ile açtı, daha önce ne açıktı, hangi şartlarda değiştirildi" sorularında yetersiz kalır.

`ActiveSetRegistry` ve `ActivationStorage` kullanılarak:
- Her aktivasyon değişikliği bir `Snapshot` olarak tutulur.
- Değişiklikten önceki aktif kayıt `superseded` olarak işaretlenir.
- Bu sayede geri dönüşlerde (Revert) güvenli şekilde hangi sürüme/yapılandırmaya dönüleceği kesinlikle bilinir.

## Governance and Replay Use
Historical kayıtlar (HistoryTracker), ilerleyen fazlarda simülasyonların "o anki gerçek aktif kurallar (active-set) üzerinden" yapılmasını sağlar. Tekrar eden aktivasyon hataları trend analizine girerek Readiness Board'un bir sonraki kararlarını etkiler.
