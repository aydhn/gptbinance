# Workspace & Profile İzolasyon Mimarisi ve Context Politikası

Sistem tek bir profil varsayımıyla çalışmaktan çıkarak, çoklu çalışma alanlarını (workspace) ve bunların altındaki izolasyon sınırlarını (profile) tanımlar.

## Temel Ayrımlar
- **Workspace**: Ana proje / repo mantıksal kökü.
- **Profile**: Çalışma alanının altındaki operasyonel bağlam.
- **Context**: O an aktif olan Workspace + Profile ikilisi.

## Politikalar
- Context her zaman açıkça belirtilmelidir (explicit). "Son kullanılanı hatırla ve kritik işlem yap" mantığı yasaktır.
- Ortak yazılabilir (shared mutable) path'ler tehlikelidir ve Contamination Checker tarafından işaretlenir.
- Local-first mimari korunur, bu yapı kurumsal bir IAM veya web-SaaS multi-tenant modeli değildir.
