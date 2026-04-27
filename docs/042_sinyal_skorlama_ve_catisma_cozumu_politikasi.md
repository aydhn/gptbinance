# Phase 07: Sinyal Skorlama ve Çatışma Çözümü Politikası

## Score Neden Var?
Skorlama katmanı, execution yerine geçmek için değil; aynı anda çok sayıda signal çıktığında önceliklendirme yapabilmek ve kalitesiz/eksik bağlamlı sinyalleri aşağı çekebilmek için tasarlanmıştır.

## Conflict Resolution Nasıl Çalışır?
Aynı sembolda farklı stratejilerden gelen sinyaller veya niyetler (intents) arasında çakışmalar (conflicts) olabilir.
Çözüm politikası sade kurallara dayanır:
- Higher score wins (Yüksek skor önceliklidir).
- Stale signal kaybeder (Bayat sinyal elenir).
- Düşük quality (kalite) sinyal elenir.
Aynı yöndeki niyetler tekleştirilebilir, zıt yönlü niyetler "no clear intent" ile reddedilebilir.

## Aynı Sembolde Çoklu Strateji Davranışı
Çoklu stratejiler birbirini test eden hipotezler gibidir. Aynı anda "Trend Follow" ve "Mean Reversion" sinyal üretebilir. Çatışma çözücü (Conflict Resolver) bu karmaşayı, skor ve tazelik (freshness) kriterlerine göre azaltarak tek (veya en nitelikli) bir intent (niyet) adayı çıkarır.

## Neden Skor Tek Başına Risk Kararı Değildir?
Yüksek skor, sadece o anki strateji hipotezinin güçlü olduğuna işaret eder. Sermayenin mevcut durumu, pozisyon büyüklüğü, genel piyasa drawdown seviyesi gibi risk ölçütlerini içermez. Skor, sadece risk motorunun değerlendireceği *niyetin (intent)* kalitesini gösterir.
