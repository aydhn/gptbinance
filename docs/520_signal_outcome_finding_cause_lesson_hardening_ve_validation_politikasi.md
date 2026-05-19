# Signal, Finding, Cause, Lesson, Hardening ve Validation Politikası

## 1. Signal Discipline
Hiçbir öğrenme (learning) objesi kaynaksız var olamaz. Bir learning object oluşturulurken mutlaka bir sinyale (`LearningSignalRecord`) ve bir kaynağa (`LearningOriginRecord`) bağlanmalıdır.
- **Desteklenen Sinyaller**: Explicit failure, near-miss, weak anomaly, avoided failure, repeated workaround.
- Sinyal olmadan üretilen "dersler", kanıtsız felsefe olarak değerlendirilir ve reddedilir.

## 2. Findings and Causes
Olayın analizi (finding) ve nedensellik (causality) birbirinden ayrılır.
- **Findings**: Doğrudan gözlemlenen anomaliler, sistemik bulgular veya recurrence (tekrarlama) bulgularıdır.
- **Hypotheses vs. Validated Causes**: Ortaya atılan her neden bir hipotezdir (`CausalHypothesisRecord`). Sadece kanıtlarla desteklenen hipotezler `ValidatedCauseRecord` seviyesine yükselebilir.

## 3. Lessons
Öğrenilen ders (`LessonRecord`), spesifik ve hedeflenmiş olmalıdır.
- "Daha dikkatli olmalıyız" bir ders değildir.
- "Deployment öncesi X konfigürasyonunun Y ile uyuşmazlığı tespit edilmelidir" geçerli bir derstir.
- Dersler operasyonel, anayasal, teknik veya süreç odaklı sınıflara ayrılır.

## 4. Hardening Actions
Bir dersin somut eyleme dönüşmüş haline Hardening Action denir.
- Hardening, bir doküman yazmak değil, sistemi değiştirmektir (örneğin, bir guardrail eklemek, bir workflow'u değiştirmek).
- Aksiyon ile Öğrenme eşanlamlı değildir (`Why Action != Learning`). Aksiyon alınabilir ama öğrenme gerçekleşmemiş olabilir.

## 5. Anti-Recurrence Validation
En kritik kural: **Kapanış, Doğrulama Olmadan Yapılamaz.**
- Bir öğrenmenin gerçekten işe yaradığını kanıtlamak için anti-recurrence validation (tekrar-önleme doğrulaması) şarttır.
- Alınan aksiyonun, aynı sınıf hatanın (failure class) tekrar etmesini zorlaştırdığına veya engellediğine dair kanıt sunulmalıdır.
