# Phase 21: Promotion, Activation ve Rollback Hazırlık Politikası

Bu doküman bir adayın nasıl desteklendiğini, aktive edildiğini ve gerektiğinde nasıl geri alındığını açıklar.

## Promotion Readiness
- Adayın canlı ortama geçmeye hazır olup olmadığı değerlendirilir.
- Blocker yoksa (örneğin rollback referansının var olması), uygun stage (örn. paper) önerilir.

## Rollback Referansı
- **Zorunlu Kural**: Aktif sisteme geçecek her yeni bundle, önceki "last-known-good" bundle referansını barındırmak ZORUNDADIR.
- Eğer bir sorun çıkarsa sistem hızla bu güvenli noktaya döner.

## Activation
- Activation, aktif olanı aniden değiştirmek yerine "Activation Readiness" raporu ile onay arar.
- Shadow, Paper, Testnet, Live için ayrı onay gate'leri vardır.
