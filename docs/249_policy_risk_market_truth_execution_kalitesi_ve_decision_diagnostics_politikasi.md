# Phase 48: Policy, Risk, Market Truth, Execution Kalitesi ve Decision Diagnostics Politikası

Bu sistem, kalitenin sadece sinyal kalitesi olmadığının, tüm yardımcı bileşenlerin (policy, risk, capital, event vb.) sürtünme veya fayda üretebileceğinin farkındadır.

## Frictions Katmanları ve Yorumları
- **Risk Frictions:** Limitler veya stress bütçeleri kaynaklı engeller. (Güvenliği sağlar ama fazla agresif olabilir).
- **Policy Frictions:** Genel kurallar ve invariant'ların ürettiği bloklar. Hangi policy kuralının (örn. no_short_during_event) en çok drop-off yarattığını gösterir.
- **Market Truth Frictions:** Fiyatın bayat, verinin sorunlu olduğu durumlar yüzünden bastırılan fırsatlar.
- **Execution Frictions:** Sinyal var, order var ama slippage, timeout veya kısmi dolum kaynaklı kalite düşüşleri.

## Attribution Mantığı
Kötü gerçekleşen bir işlemde kabahat tek bir modülde olmayabilir. Sistem, zararın / düşük performansın kaynağını attribution ile böler: "Strategy Signal'ı iyiydi, ancak Execution slippage yüzünden PnL etkilendi" ya da "Market Truth sequence hatalı olduğu için yanlış fiyatla girildi".

## Decision Quality Evidence
Verilen her kalite tanısı kanıtlara (evidence) dayanır. Bir `blocked_and_likely_saved_loss` kararı, funnel lineage'ine, risk değerlendirme blok kanıtlarına ve subsequent price excursion datasına referans verir.

## Governance ve Qualification İlişkisi
- **Qualification:** Sistemin profil kalifikasyonu artık funnel degradation analizini içerir. Sistem funnel sağlığı (örneğin sürekli market_truth block olması) kötüleşirse readiness caution verir.
- **Governance:** Terfi (promotion) için bir kod grubunun (bundle) sadece backtest performansı değil, "Decision Funnel Health" metrikleri de incelenir. "Teknik olarak güvenli ama funnel tamamen tıkalı" durumlar terfi için bir alarmdır.
