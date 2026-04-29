# 082 Pretrade Validation, Idempotency ve Duplicate Order Koruma Politikası

## Pre-Trade Validation
Emirler ağa çıkmadan önce `PretradeValidator` ile kontrol edilir:
- Min quantity
- Tick size
- Min notional
Bu, borsadan reject alarak API limitlerini tüketmeyi engeller.

## Idempotency ve C-ID
`ClientOrderIdGenerator`, oturum, sembol ve niyet kimliğini kullanarak benzersiz ve tekrar edilebilir ID'ler üretir. Bu, ağ sorunları nedeniyle aynı emrin iki kez gönderilmesini (duplicate order) önler.
