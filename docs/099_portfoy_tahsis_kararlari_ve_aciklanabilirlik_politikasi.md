# Phase 18: Portföy Tahsis Kararları ve Açıklanabilirlik

Neden bir işlem kabul edildi, diğeri küçültüldü veya reddedildi? Ops operasyonunda izlenebilirlik her şeydir.

## PortfolioVerdict Kararları
- **APPROVE:** Bütçe ve sleeve kısıtlarında sorun yok, aday onaylandı.
- **REDUCE:** Fırsat onaylandı ancak (sleeve kısıtlarına takılmamak veya reserve nakdi bitirmemek adına) büyüklüğü küçültüldü.
- **DEFER:** Sistem bu cycle'da (döngü) yeterince tahsis yaptı (`max_new_allocations_per_cycle`), bu fırsat bekletilecek.
- **REJECT:** Bütçe yok, concentration limiti aşılıyor veya overlap nedeniyle sıralamada dibe düştü.

## Açıklanabilirlik (Explainability)
`ExplainabilityEngine` üretilen `PortfolioDecisionBatch`'i insan dostu bir metne dönüştürür.
- Tüm `blocking_reasons`, `allocation_ratio` ve `ranking_rationale` değerleri kaydedilir.
- Bu raporlar DB'ye (portfolio.sqlite) kaydedilir ve CLI (`--show-portfolio-decisions`) ile istenildiği an okunabilir.
