# Shared Service Blast Radius, Global-Local Rule Conflict ve Partner Federation Politikası

- **Shared Services**: "Merkezde sağlıklı" olması, "Tüm tenant'lar güvende" anlamına gelmez. Blast radius net şekilde belgelenmelidir.
- **Global vs Local Rules**: Global rules mandate, local rules impose stricter bounds. Exception'lar sınırlandırılır ve cross-domain conflict'ler çözülmeden işlem yapılamaz.
- **Partner/Vendor Federation**: Siyah kutu yaklaşımlar (black box) reddedilir. Trust staleness uyarısı üretir.
- **Tenant Isolation**: Label-only (sözde) isolation geçerli sayılmaz, execution / data / domain düzeyinde kanıtlanmış isolation aranır.
