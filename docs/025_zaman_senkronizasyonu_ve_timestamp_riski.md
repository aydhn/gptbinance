# Zaman Senkronizasyonu ve Timestamp Riski

## Neden Ölçüyoruz?
Binance API'sine imzalı (authenticated) bir istek gönderirken, isteğin içinde bir `timestamp` değeri bulunmak zorundadır. Binance, sunucu zamanı ile gelen isteğin timestamp'i arasındaki fark belirli bir toleransı (recvWindow, varsayılan 5000ms) aşarsa isteği `Timestamp for this request is outside of the recvWindow` hatasıyla reddeder.

## Local Clock Drift
Kendi sunucumuzun saati (local clock) zamanla geri kalabilir veya ileri gidebilir. Bu drift (sapma) ölçülmez ve tolere edilmezse, emirler sürekli olarak reject yiyebilir.

## Drift Hesaplama Yöntemi
`TimeService`, `/api/v3/time` endpointine istek atarak Round-Trip Time (RTT) hesaplar.
1. `start_time` = İstek başlar.
2. `server_time` = Binance'ten gelen zaman.
3. `end_time` = İstek biter.
4. `RTT` = `end_time` - `start_time`
5. Binance'in isteği işlediği yaklaşık local an: `approx_local_time_at_server = start_time + (rtt / 2)`
6. `Drift` = `approx_local_time_at_server - server_time`

## Stale State Riski
Eğer local saat ile borsa arasında ciddi ve değişken bir latency (örn: 2000ms üzeri) varsa, botun fiyatlara dair gördüğü "anlık" durum aslında geçersiz (stale) olabilir. `HealthService` bu latency değerini ölçerek `POOR` durumu fırlatır, bu da ileride risk mekanizmalarını tetikleyebilir ve trading'i durdurabilir.
