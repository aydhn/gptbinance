# Phase 48: Block Reason Taxonomy ve Decision Friction Politikası

Sistemin reddettiği her trade fırsatı, spesifik bir nedenle açıklanabilmelidir. Block nedenlerinin dağınık veya serbest metin formatında olması, analizi ve attribution'ı zorlaştırır. Bu yüzden standart bir taksonomi kullanılır.

## Canonical Block Reason IDs
Her reddedilen fırsat, aşağıdaki kategorilerden en az bir `primary reason`'a sahiptir:
- `market_truth_stale` / `market_truth_broken_sequence`
- `event_risk_block`
- `stress_budget_block`
- `capital_no_new_exposure` / `capital_freeze`
- `policy_hard_block` / `policy_block`
- `universe_ineligible`
- `cross_book_conflict`
- `shadow_truthfulness_poor`
- `lifecycle_ambiguous`
- `account_mode_mismatch`
- `qualification_stale`
- `workspace_boundary`
- `symbol_quarantined`
- `execution_not_submitted`
- `manual_skip_or_suppression`

## Friction Sources ve Attribution
Karar funnel'ında "sürtünme" (friction) kaynakları netleştirilir. Sürtünme kaynakları şunlardır:
- Strategy Issue
- Risk Filter
- Capital Constraint
- Event-Risk Restriction
- Policy Hard-block
- Market-Truth Degradation
- Lifecycle/Execution Issue
- Cross-book Conflict

## Funnel Drop-off Yorumlama
Bir sinyalin intent aşamasına gelip compile edilmemesi ile lifecycle aşamasında fill olmaması farklı sürtünme tipleridir. Bu düşüşlerin nerede yoğunlaştığını görmek, sistem darboğazlarını belirler.

## Repeated Blocker Clusters
Sürekli aynı blok nedeni tarafından kesilen sinyaller "cluster" oluşturur. Örneğin; `market_truth_stale` kaynaklı sürekli düşüş, verinin kronik bir sorunu olduğunu gösterir. Bu cluster'lar uyarı üretir ve knowledge base'e ders olarak çıkarılır, ancak ASLA kuralları otomatik esnetmez.
