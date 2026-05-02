# Break-Glass ve Emergency Override Politikası

## Break-Glass Ne Zaman Kullanılabilir?
Normal onay süreçlerinin işlemediği (örneğin diğer onaycılara ulaşılamadığı) veya sistemin acil kurtarma (incident recovery, system down) gerektirdiği aşırı kritik durumlarda kullanılır.

## Neden Ayrı Audit ve Review Gerektirir?
Break-glass bir "kolay kaçış" veya günlük hızlandırıcı değildir. Bu yol kullanıldığında sistem "kırmızı alarm" verir. Break-glass yetkilendirmesi, sonrasında zorunlu bir olay sonrası inceleme (post-incident review) ve artırılmış audit kaydı oluşturulmasına neden olur.

## Hangi Scope'larda Yasak / İzinli?
Break-glass sadece sistemi güvenli hale getirecek (örneğin `FLATTEN_LIVE_SESSION` veya `ROLLBACK_LIVE_SESSION`) aksiyonlar için kullanılabilir.
Riskli ve kalıcı etkileri olan aksiyonlarda (örneğin `APPLY_RESTORE` veya `DESTRUCTIVE_RETENTION_CLEANUP`) break-glass kullanılması kesinlikle yasaktır. Bu tür aksiyonların listesi `ActionRegistry` içinde "allow_break_glass=False" olarak belirlenmiştir.

## Post-Incident Review Zorunluluğu
Break-glass kullanan bir operatörün aksiyonu, Command Journal'a "Break-Glass" bayrağı ile kaydedilir ve derhal Telegram/Observability üzerinden yöneticilere raporlanır. Kullanım sonrası süreç, operasyon ekiplerinin olayı gözden geçirmesini şart koşar.
