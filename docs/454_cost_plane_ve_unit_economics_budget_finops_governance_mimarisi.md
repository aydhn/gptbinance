# Cost Plane ve Unit-Economics/FinOps Governance Mimarisi

Bu doküman, Phase 89'da kurulan Cost Plane ve FinOps/Unit Economics Yönetişim altyapısının esaslarını tanımlar.

## Temel Felsefe
- **Total Spend != Useful Economics**: Sadece faturanın toplam boyutunu görmek ekonomik sağlığı ölçmeye yetmez. Bütçe aşımı, kaynak kullanım yoğunluğu, model performansı, research replay israfları vb. maliyetin niteliğine odaklanmalıyız.
- **No Hidden Subsidy**: Shared kaynak kullanımının getirdiği gizli sübvansiyonlara ve cost migration’lara karşı önlem alınmalıdır.
- **Cost Governance**: Budget, guardrails, allocations, varyans, forecasting ve trust zincirleme bir analizle ilerler. Capacity/release/activation sistemleri bu entegrasyon sayesinde bir risk veya verimlilik sinyali verebilir.

## Cost Truth
Sabit, değişken, usage bazlı ve vendor ücretlerini ayrı sınıflara (class) ayıran Cost Object modelleri kullanılmaktadır.
