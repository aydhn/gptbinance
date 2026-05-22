# Phase 110 - Adversarial Plane ve Gaming / Manipulation / Abuse / Deception Governance Mimarisi

Bu dokuman, sistemdeki Adversarial Plane mimarisini ve gaming, evasion, deception risklerinin nasil yonetilecegini aciklar.

## Actors/Incentives -> Surfaces/Exploits -> Resistance/Detectability -> Confirmation/Trust Akisi

Sistem, yalnizca dogrudan saldirilari degil, ayni zamanda oyunlanan surecleri de yonetmelidir. Bu yuzden aktorler (insan, ajan, vendor) ve onlarin tesvikleri (hiz, gizlilik, metrik iyilesmesi) saldiri yuzeyleriyle (onaylar, esikler) eslenir.
Exploit'ler bu yuzeyleri hedefler; sistemin direnci ve tespit edilebilirligi test edilir. En sonunda suphelerin kanitlanmasi veya curutulmesiyle guven (trust) belirlenir.

## Why Good Score != Non-Gamed System
Bir metrik cok iyi gorunuyor olabilir, ancak bu onun "oyunlanmadigi" anlamina gelmez. Metric gaming, gercek bir iyilesme yerine sadece skorun yukseltilmesini hedefler. Sistem bu yuzden "iyi skor"un arkasindaki oyunlanabilirligi sorgular.

## Why No Review Theater
Sadece "gozden gecirildi" kutusunun isaretlenmesi yeterli degildir. Review evasion ve approval laundering gibi taktikler bu kutuyu isaretleyip gercek incelemeyi atlayabilir. Sistem, review surecinin kalitesini ve direncini olcer.

## Adversarial Governance Mantigi
Bu katman, witch-hunt yapmaz; sadece abuse surface'leri, evasion path'leri ve metric gaming risklerini explicit ve canonical hale getirir. Paranoia theater yaratmadan, yonetilebilir bir abuse direnc agi kurar.
