# Event-Risk Intelligence

Bu modül, scheduled macro event'ler (CPI, FOMC vb.), borsa bakımları ve sistem içi/manual planlı olayları takip ederek trade güvenliğini sağlar.

## Katmanlar
- **Sources**: Dış verileri (API, mock vb.) çeker (HTML scraping KESINLIKLE yasak).
- **Normalization**: Gelen event'leri standart formata çevirir.
- **Windows**: Event öncesi ve sonrası cool-down / risk zaman dilimlerini belirler.
- **Overlay**: Aktif window'lara ve profile'a göre risk kararı üretir (Allow, Caution, Block, Reduce vb.).
- **Gating**: Bu kararı strategy, portfolio, execution gibi modüllere advisory ya da blocking olarak sunar.
