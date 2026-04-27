# Konfigürasyon Şeması Referansı

Uygulamanın ayarları, güçlü bir şekilde tiplendirilmiş Pydantic modelleri (`app.config.models.AppConfig`) kullanılarak yönetilir. Ayarlar, öncelikli olarak çevre değişkenlerinden (Environment Variables / `.env`) okunur.

## Bölümler

### 1. General (`general`)
- `PROFILE` (Enum): Çalışma profili (`dev`, `paper`, `testnet`, `live`). *Varsayılan: dev*

### 2. Logging (`logging`)
- `LOG_LEVEL` (Enum): Log seviyesi (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`). *Varsayılan: INFO*

### 3. Binance (`binance`)
- `BINANCE_API_KEY` (SecretStr): Borsa API anahtarı. Loglarda maskelenir.
- `BINANCE_API_SECRET` (SecretStr): Borsa API gizli anahtarı. Loglarda maskelenir.
- `BINANCE_USE_TESTNET` (bool): Test ağının kullanılıp kullanılmayacağı. `live` profilinde kesinlikle `false` olmalıdır.

### 4. Execution & Risk (`execution`, `risk`)
- `EXECUTION_ENABLED` (bool): Emir gönderme yeteneğinin genel şalteri.
- `RISK_HARD_STOPS` (bool): Katı risk kurallarının (örn. günlük zarar limiti) açık olup olmadığı. `live` modda zorunludur.

### 5. Telegram (`telegram`)
- `TELEGRAM_ENABLED` (bool): Telegram bildirimlerinin açık olup olmadığı.
- `TELEGRAM_BOT_TOKEN` (SecretStr): Bot tokeni. Maskelenir.
- `TELEGRAM_CHAT_ID` (SecretStr): Hedef chat ID. Maskelenir.

### 6. Live Guard (`live_guard`)
- `LIVE_CONFIRMATION` (str): Canlı moda geçiş için gereken tam eşleşmeli onay metni. Sadece `live` profilinde anlamlıdır ve zorunludur.

## Etkili Konfigürasyon (Effective Config)
Çalışma anında hangi ayarların geçerli olduğunu görmek için şu komut kullanılabilir:
```bash
python -m app.main --print-effective-config
```
Bu komut, tüm secret değerleri (`***REDACTED***` vb. şeklinde) maskeleyerek güvenli bir JSON çıktısı üretir.
