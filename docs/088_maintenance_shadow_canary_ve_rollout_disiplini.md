# Maintenance, Shadow, Canary ve Rollout Disiplini

Sistemin bakım süreleri önceden kaydedilir ve bu süreçlerde yeni emir gönderilmez (gerekirse reduce-only). Shadow modu, canlı veri ile çalışırken log sink kullanır. Canary, dar kapsamlı limitlerle sistemi test eder. Gerçek order submission ancak go-live kapıları geçilirse açılabilir (bu fazda default kapalıdır).
