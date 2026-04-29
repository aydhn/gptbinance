# 084 Mainnet Safety Gates ve Arm/Disarm Politikası

## Neden Default Kapalı?
Production kazalarını engellemek için mainnet emir gönderimi "silahlandırılmadığı" (armed) sürece yasaktır.

## Safety Gates
- `MainnetDisarmedGate`: `config.mainnet_armed` false ise işlemi reddeder.
- `SessionReadinessGate`: Oturum hazır değilse emri bloklar.

## CLI Entegrasyonu
Mainnet'i aktif etmek için açıkça bir CLI argümanı (örn. `--arm-mainnet-execution`) verilmelidir. Bu, yanlışlıkla gerçek emir gönderilmesini engeller.
