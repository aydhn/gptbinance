# 081 Execution Gateway Mimarisi ve Testnet-First Politikası

## Amaç
Execution gateway, risk motoru tarafından onaylanmış işlem niyetlerini (intent) gerçek borsa emirlerine dönüştüren son katmandır.

## Testnet-First Yaklaşımı
Gerçek fonlarla işlem yapmadan önce, Binance testnet üzerinde emir gönderimi, partial fill senaryoları, stream/REST senkronizasyon hataları gibi gerçek dünya problemleri sınanmalıdır. Bu nedenle varsayılan execution ortamı `TESTNET` olarak ayarlanmıştır. Mainnet erişimi sert bir güvenlik kapısı (`MainnetDisarmedGate`) arkasındadır.

## Mimari Bileşenler
- **Intent -> Execution Request**: Stratejiden gelen sinyaller risk motorunda `ExecutionIntent`'e dönüşür, execution gateway bunu `ExecutionRequest` olarak alır.
- **Order Router**: Validasyon ve ID üretiminden sonra emri yönlendirir.
- **State Store**: Olası stream/REST kopmalarına karşı lokalde emir durumunu tutar.
