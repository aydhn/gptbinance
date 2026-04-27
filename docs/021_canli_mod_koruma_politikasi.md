# Canlı Mod (Live) Koruma Politikası

Uygulamanın en kritik güvenlik mekanizması, gerçek parayla hatalı veya kaza eseri işlem yapılmasını önleyen **Live Guard** sistemidir (`app/core/runtime_guards.py`).

## Canlı Modun Açılabilmesi İçin Gereken Şartlar

`PROFILE=live` ayarlandığında, bootstrap aşamasının başarıyla tamamlanması için aşağıdaki şartların **tamamı** sağlanmalıdır:

1. **Explicit Onay:** `LIVE_CONFIRMATION` çevre değişkeni tam olarak `"I_UNDERSTAND_THE_RISKS_AND_ALLOW_LIVE_TRADING"` değerine sahip olmalıdır. Basit bir `true/1` kabul edilmez.
2. **Execution Şalteri:** `EXECUTION_ENABLED=true` olmalıdır. Mantıken emir göndermeyecek bir sistemin `live` profille çalışması anlamsızdır.
3. **Gerçek Ağ Kullanımı:** `BINANCE_USE_TESTNET=false` olmalıdır.
4. **Kimlik Bilgileri:** `BINANCE_API_KEY` ve `BINANCE_API_SECRET` mutlaka tanımlı olmalıdır.
5. **Risk Yönetimi:** `RISK_HARD_STOPS=true` olmalıdır. Temel risk korumaları kapatılarak canlı işleme izin verilmez.

## Hata Durumu (Fail-Fast)
Eğer yukarıdaki şartlardan herhangi biri sağlanmazsa, uygulama `LiveModeError` fırlatarak anında kapanır. Hata mesajı, eksikliğin ne olduğunu (örn. "Missing Binance API credentials") net bir şekilde belirtir, ancak asla hassas bir bilgiyi ekrana basmaz.

## Gelecek Genişletmeler
Gelecek fazlarda, bu guard içerisine "strateji geçerlilik kontrolü", "minimum bakiye kontrolü" gibi ek güvenlik adımları eklenebilir.
