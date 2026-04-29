# Phase 17: Controlled Live Runtime & Rollout Kademeleri

## Neden Controlled Live Runtime?
Testnet ve Paper execution simülasyonları ne kadar iyi olursa olsun, gerçek mainnet'te account balance, margin requirements, gerçek latency, execution reject fırtınaları ve operasyonel baskı (stress) vardır. Bu nedenle, mainnet live execution varsayılan olarak açık olamaz.

Araya `LiveOrchestrator` adında ayrı bir execution runner katmanı ekledik. Bu katman, Strategy/Risk ile Execution Gateway arasında durur ve üretimi korur.

## Rollout Kademeleri

1. **Shadow Only**: Karar mekanizması tam çalışır, gateway'e emir gitmez, her intent sayılır ve local loglanır. Live risk yoktur.
2. **Testnet Exec**: Kararlar gerçek testnet account'una yollanır. Risk kısıtları test edilir ama mainnet parası riske girmez.
3. **Canary Live**: Gerçek mainnet ortamı, çok dar sembol listesi (sadece `BTCUSDT`), çok düşük notional cap ($100), çok kısa seans süresi. İlk canlı üretim denemesidir.
4. **Capped Live**: Canary başarılı olduktan sonra daha geniş ama hâlâ sert limitli moddur. ($1000 notional, $100 daily loss limit).
5. **Full Live Locked**: Tam açık mod. Bu fazda varsayılan olarak **hard-coded yasaktır** (locked). Geçilmesi için Phase 18 operasyon olgunluğu gereklidir.
