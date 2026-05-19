# Learning Plane ve Institutional Adaptation Governance Mimarisi

## Temel Felsefe
Bir sistemde başarısızlık (incident, miss, failure) kaçınılmazdır. Ancak asıl problem, aynı başarısızlığın farklı yüzeylerde (replay, paper, probation, live) tekrar etmesi ve organizasyonun bundan "öğrendiğini" varsaymasıdır. Bir postmortem belgesinin yazılması veya bir aksiyon listesinin oluşturulması "öğrenme" (learning) değildir. Öğrenme, sistemin anayasasının (constitution), kurallarının (policy), state guard'larının veya süreçlerinin kalıcı ve doğrulanabilir şekilde değişmesi (hardening) anlamına gelir.

Learning Plane, bu adaptasyon sürecini rastgele bir insan eylemi olmaktan çıkarıp, typed, audit edilebilir ve kanıta dayalı bir governance loop'una dönüştürür.

## Signals -> Findings -> Lessons -> Updates -> Validation -> Trust Akışı

1. **Signals & Origins**: Her öğrenme süreci somut bir sinyalle başlar. Bu bir explicit failure, near-miss, avoided-failure veya weak anomaly olabilir.
2. **Findings & Causes**: Sinyaller analiz edilir ve findings'e dönüştürülür. Hypotheses test edilir ve yalnızca evidence-backed olanlar Validated Causes olarak kabul edilir.
3. **Lessons & Scopes**: Nedenlerden dersler (lessons) çıkarılır. "Root-cause theater"a izin verilmez. Her dersin uygulanabilir olduğu bir scope vardır.
4. **Update Targets & Hardening**: Dersler, havada asılı kalamaz. Belirli hedefleri (update targets - policy, constitution, state, contract) güncellemeli ve sistemde bir katılaşma (hardening action) yaratmalıdır.
5. **Adoption & Validation**: Alınan aksiyonlar dokümante edilmekle kalmamalı, benimsenmeli (adoption) ve tekrarı önlediği doğrulanmalıdır (anti-recurrence validation).
6. **Trust & Recurrence Control**: Tüm bu süreç, o öğrenme nesnesinin güvenilirliğini (Trust Verdict) belirler. Eğer aynı hata tekrar ediyorsa, önceki öğrenme trust verdict'ini kaybeder ve sistemin ilerlemesini bloke eder.

## Why Postmortem != Institutional Learning
Postmortem sadece bir analiz dokümanıdır. Gerçekte, bir incident closure'ı, sistemde bir guard değişmeden, bir policy güncellenmeden veya bir test eklenmeden gerçekleşiyorsa, sistem hiçbir şey öğrenmemiştir. Postmortem, learning plane'in girdisidir (origin), çıktısı değil.

## No Buried Lessons
Learning Plane, "öğrenilen derslerin" gömülmesine veya aksiyon mezarlıklarında (action graveyard) unutulmasına izin vermez. Her ders bir hardening action'a bağlanmak, her eylem de doğrulanmak zorundadır. Orphans (sahipsiz dersler) Learning Debt (Öğrenme Borcu) olarak kaydedilir ve sistem sağlığını aşağı çeker.
