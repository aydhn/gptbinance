# Phase 21: Research Factory Mimari ve Refresh Orchestration Politikası

Bu doküman, Phase 21 kapsamında kurulan "Research Factory" ve "Refresh Orchestration" katmanının mantığını açıklar.

## Amaç
Bir trading sistemi ilk kurulduğu haliyle kalırsa zamanla bozulur. Ancak yeni veri geldikçe modelleri ve stratejileri otomatik ve sessizce değiştirmek çok daha risklidir. Bu katman, yenileme (refresh), aday üretme (candidate assembly) ve değerlendirme (promotion readiness) süreçlerini kontrollü ve denetlenebilir bir pipeline'a bağlar.

## Refresh Süreci
- **Trigger**: Zaman bazlı, veri bazlı, drift bazlı veya manuel tetiklenir.
- **Planlar**: Fast, Research, Deep olmak üzere 3 temel plan vardır. Planlar hangi bileşenlerin (veri, feature, model vb.) yenileneceğini belirler.
- **Sonuç**: Otomatik live geçiş yapılmaz. Aday paketler (candidate bundles) üretilir.

## Sessiz Değişim Neden Yasak?
- Sistem güvenliği ve hesap verebilirlik esastır.
- Herhangi bir state değişikliği "Candidate -> Reviewed -> Approved -> Active" yaşam döngüsünden geçmek zorundadır.
