# Telegram Operasyon Bildirimleri ve Spam Kontrolü

## Amaç
Telegram botu, operatörün sistemi 7/24 takip etmesine olanak tanır. Ancak, loglama mantığıyla spam mesaj göndermek yerine sadece operasyonel, kritik ve özet verileri iletir.

## Rate Limiting ve Severity
`PaperNotifierBridge` üzerinden giden mesajlarda olay bazlı soğuma süreleri (cooldown) vardır:
- **Stream Degraded:** En az 5 dakikada bir uyarı gider.
- **Risk Veto Storm:** Peş peşe gelen risk redlerinde 5 dakikada bir özet uyarı gider.
- **Drawdown Warning:** Drawdown limitini aştığında en az 15 dakikada bir uyarı gider.
- **Kill Switch:** Kritik olduğu için rate limit'e takılmaz, anında iletilir.
- **Session Start/Stop:** Session açıldığında ve kapandığında özet bilgi olarak gider.

## Şablonlar
`app/telegram/templates.py` içinde standartlaştırılmış HTML tabanlı mesaj formatları bulunur. Bu formatlarda:
- Run ID
- Sembol ve zaman
- Konu özeti (PnL, Drawdown, Health vb.)
- Detaylar ve nedenler (Rejection reason, lag time, vb.)
bulunur.
