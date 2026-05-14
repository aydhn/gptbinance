# Supply Chain Plane

## Amaç
Bu modül, yazılımdaki artifact'lerin (source, dependency, build input, package, release, runtime object) birbirleriyle olan ilişkisini, "provenance" (kaynak kökeni), "SBOM" ve "trust" boyutlarını disiplin altına alan canonical bir katmandır.

## Source -> Deps -> Build -> Package -> Release -> Runtime -> Trust Akışı
- Component ve Origin: Bir şey içeriden mi dışarıdan mı geldi?
- Dependencies: Neye bağlı (direct, transitive)?
- Build: Hangi tarif (recipe) ile yapıldı?
- Provenance: Build'in inputları ve outputları kanıtlanabilir mi?
- Package: Versiyon ile hash (digest) aynı şeyi mi gösteriyor?
- Release ve Runtime: Çalışan şeyin release ile aynı olduğu teyit edilebilir mi?
- Trust Verdict: Her şeyin sonunda bu bileşen güvenilir mi?

## Neden Version != Digest != Provenance != Runtime Match
Çünkü versiyon bir etikettir. Aynı etiket altında artifact değişebilir (digest). Artifact aynı kalsa da nasıl yapıldığı ve nereden geldiği bilinemezse güvenilmezdir (provenance). Runtime'da başka bir şey çalıştırılabilir. Bütün bu kavramları ayırmak şarttır.

## Sınırlar
Bu faz, dependency download/upload aracı değildir. Zaten var olan component, package ve SBOM datalarını governance, policy ve audit kapsamında anlamlandırma ve bir güven matriksine oturtma aracıdır.
