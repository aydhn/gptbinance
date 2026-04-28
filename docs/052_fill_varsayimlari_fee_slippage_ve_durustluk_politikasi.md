# 052 - Fill Varsayımları, Fee, Slippage ve Dürüstlük Politikası

Simülasyon sonuçlarının güvenilir olması için fill (emir gerçekleşme) modeli dürüst olmalıdır.

## Fill Politikası
Stratejiler kararlarını bar kapanışında verir (örneğin 15:00-15:15 barının bitiminde). Bu nedenle fill işlemi *asla* aynı barın kapanış fiyatı üzerinden yapılamaz (lookahead bias yaratır). İşlem, bir sonraki barın (15:15) açılış fiyatında (`NEXT_BAR_OPEN`) simüle edilir.

## Fee ve Slippage
*   **Fee (Komisyon):** Binance VIP 0 Taker (örneğin 0.04% USDT-M Futures) temel alınarak işlem hacmi üzerinden hesaplanır ve bakiyeden düşülür.
*   **Slippage (Kayma):** Emrin piyasaya girdiği anki fiyat kayması varsayımıdır (örneğin 0.05%). Fiyat, alım yaparken daha yüksek, satım yaparken daha düşük gösterilerek cezalandırılır.

Bu "kötümser" varsayımlar (pessimistic modeling) sayesinde sistemin "hayal satması" engellenir.
