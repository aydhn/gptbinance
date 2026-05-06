# Decision Lineage, Case File Assembly ve Audit Traceability Politikası

Bu doküman, bir kararın hangi kanıtlara dayandığını belgeleyen izlenebilirlik (traceability) kurallarını belirler.

## Decision Lineage
Her karar, ona yol açan kanıtların bir soy ağacına (lineage) sahip olmalıdır. `LineageEngine`, geçmişe doğru (backward) tarama yaparak kararın köklerini, geleceğe doğru (forward) tarama yaparak kararın etkilediği diğer çıktıları tespit eder. Bağlantılar (relations) tipli ve tek yönlüdür.

## Case File Assembly
Dağınık raporlar yerine, bir olay veya karar etrafındaki tüm kanıtlar `CaseFileAssembler` tarafından bir vaka dosyası (Case File) olarak derlenir.
- Vaka dosyaları bir "Anchor Artefact" etrafında şekillenir.
- Spekülasyon veya otomatik çıkarım yapılamaz; yalnızca graf üzerindeki mevcut kanıtlar ve bunların "Kabul Edilen" (Accepted) veya "Reddedilen" (Rejected) statüleri gösterilir.

## Audit Traceability
Hiçbir artefact veya ilişki iz bırakmadan silinemez veya değiştirilemez. Güncellemeler her zaman eski kaydı `superseded` olarak işaretleyip yenisini ekleme yoluyla yapılır. Eksik veya kopuk bağlantılar (Graph Gaps), sistem uyarıları üreterek denetim ekibine (audit) bildirilir.
