# Phase 17: Account Sync, Live PnL ve Capital Cap Politikası

## Account Sync
Live session başladığında, Exchange'den gerçek account balance (`USDT` free ve locked) fetch edilerek `LiveAccountSnapshot` oluşturulur. Execution devam ettikçe balance drift takip edilir. Lokal pozisyon defteri (`LivePositionBook`) gelen execution fill'lerle güncellenir.

## Live PnL ve Equity
Gerçek fill'ler geldikçe realized PnL hesaplanır, account fee'ler düşülür. Unrealized PnL o anki last_price ve average entry price üzerinden hesaplanır. Max equity seen hesaplanıp anlık drawdown yüzdesi çıkarılır.

## Capital Cap Politikası Neden Risk Engine Üstündedir?
Risk Engine stratejik olarak pozisyon büyüklüğünü onaylayabilir. Ancak operasyonel üretim güvenliği (Capital Cap), strategy mantığından bağımsızdır. `max_session_notional`, `max_daily_loss` ve `allowlist` kontrolleri, Live Runtime Orchestrator içerisinde intent'ler gateway'e basılmadan bir milisaniye önce son kez kontrol edilir. İhlal durumunda anında `HALT` veya `REJECT` verilir.
