# Conditional-Go Scope Enforcement ve Activation Guardrails Politikası

## Conditional-Go Board Kararının Korunması
Readiness Board tarafından alınan bir "Conditional-Go" kararı, belirli kısıtlamalar içerir (Örn: "Sadece ETHUSDT" veya "Max 2 saat"). Bu kısıtlamalar sadece bir metin değil, `Activation Intent` içine yazılan hard kısıtlamalardır. Staged Activation Controller bu kısıtlamaların dışına çıkılmasını (Scope Leak) engeller.

## Policy, Capital, Market Truth, Shadow, Lifecycle Guards
Aktivasyon süreci sadece "zaman" geçmesini beklemez. Aktivasyon süresince:
- **Policy Guards:** Temel policy invariant'ların ihlal edilmemesini sağlar.
- **Capital Guards:** Sermaye kısıtlarının aşılmamasını, "no-new-exposure" durumlarında strict blokaj uygulanmasını sağlar.
- **Market Truth Guards:** Fiyat ve orderbook feed'lerinin taze kalmasını şart koşar.
- **Shadow & Lifecycle Guards:** Veri kirliliği ve orphan emir olmamasını güvence altına alır.

## Scope Leak Riskleri
Scope leak, sadece bir sembole izin verilmişken yanlış yapılandırma nedeniyle tüm sembollere işlem açılmasıdır. ScopeEnforcer sınıfı, `allowed_symbols`, `allowed_profiles` gibi listeleri kesiştirerek bu tarz bir aşımı compile (plan oluşturma) aşamasında reddeder.
