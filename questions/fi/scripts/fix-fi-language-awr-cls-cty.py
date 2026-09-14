#!/usr/bin/env python3
"""
Kieliasun korjaukset (lukion 3. luokan oikeinkirjoitustaso) kolmen kansion
monivalintakysymyksiin:

    questions/fi/items/arena-warmup/
    questions/fi/items/classification/
    questions/fi/items/competition-types/

Vain kenttien STEM, OPTION_A, OPTION_B, OPTION_C, OPTION_D ja EXPLANATION
arvoja muutetaan. Muut kentät (ID, PARENT_ID, DOMAIN, ARTICLE, EDITION_REF,
SOURCE_PAGE, TYPE, CORRECT, STATUS, CREATED, VERIFIED_AGAINST_SOURCE) jäävät
koskemattomiksi. Tiedostomuoto "AVAIN: arvo" (yksi kenttä per rivi) säilyy.

Termistö on yhtenäistetty Suomen Ratsastajainliiton Kilpailusäännöt III
-sääntökirjan kanssa (ratsukko, virhepiste, uusinta, arvostelu A/C,
verryttelyalue, sarjaeste, pystyeste, pituuseste, lähtö- ja maalilinja,
ratapiirros, kilpailukutsu, stewardi, tallimies).
"""

from pathlib import Path

ITEMS = Path(__file__).resolve().parents[1] / "items"

EDITABLE = {"STEM", "OPTION_A", "OPTION_B", "OPTION_C", "OPTION_D", "EXPLANATION"}

# filename -> {field: corrected value}
FIXES: dict[str, dict[str, str]] = {}


def add(name: str, **fields: str) -> None:
    FIXES[name] = fields


# --------------------------------------------------------------------------
# arena-warmup
# --------------------------------------------------------------------------

add(
    "arena-warmup/fi-awr-0001-v1.txt",
    STEM="Milloin kilpailualueen kaikki sisään- ja uloskäynnit on kilpailun aikana suljettava fyysisesti?",
    OPTION_A="Vain suorituksen ollessa käynnissä",
    OPTION_B="Aina, kun hevonen on kilpailualueella",
    OPTION_C="Vain palkintojenjakotilaisuudessa",
    OPTION_D="Vasta, kun kelloa on soitettu",
    EXPLANATION="JR:n artikla 329 edellyttää, että kaikki sisään- ja uloskäynnit ovat fyysisesti suljettuina aina, kun hevonen on kilpailun aikana kilpailualueella.",
)

add(
    "arena-warmup/fi-awr-0001-v2.txt",
    STEM="Mitä JR:n artiklassa 241.1.1 edellytetään hevosen ollessa kilpailun aikana kilpailualueella?",
    OPTION_A="Vain hevosen käyttämä sisäänkäynti on suljettava",
    OPTION_B="Kaikkien sisään- ja uloskäyntien on oltava fyysisesti suljettuina",
    OPTION_C="Sisäänkäynnit voivat olla auki, jos paikalla on stewardi",
    OPTION_D="Uloskäynnit on merkittävä, mutta ne voivat olla auki",
    EXPLANATION="Kilpailusääntöjen artikla 329 edellyttää, että kilpailualue on aidattu ja että kaikki sisään- ja uloskäynnit ovat fyysisesti suljettuina hevosen ollessa alueella kilpailun aikana.",
)

add(
    "arena-warmup/fi-awr-0001-v3.txt",
    STEM="Mikä seuraavista kilpailualuetta koskevista väittämistä on oikein JR:n artiklan 241.1.1 nojalla?",
    OPTION_A="Kilpailualuetta ei tarvitse sulkea radan tarkastuksen aikana",
    OPTION_B="Kilpailualueen on oltava aidattu ja sisään- ja uloskäyntien fyysisesti suljettuina hevosen ollessa kilpailun aikana kilpailualueella",
    OPTION_C="Toimihenkilöt voivat jättää portit auki nopeuttaakseen radan uudelleenrakentamista",
    OPTION_D="Sääntö koskee vain ulkokenttiä",
    EXPLANATION="Kilpailusääntöjen artikla 329 edellyttää, että kilpailualue on aidattu ja että kaikki sisään- ja uloskäynnit ovat fyysisesti suljettuina hevosen ollessa alueella kilpailun aikana.",
)

add(
    "arena-warmup/fi-awr-0001.txt",
    STEM="Mikä seuraavista pätee kaikkiin sisään- ja uloskäynteihin hevosen ollessa kilpailualueella?",
    OPTION_A="Niiden on pysyttävä auki tallimiehiä varten",
    OPTION_B="Niiden on oltava fyysisesti suljettuina",
    OPTION_C="Ne voidaan sulkea, jos urheilija ei ole radalla",
    OPTION_D="Stewardin on valvottava niitä",
    EXPLANATION="Kilpailusääntöjen artiklassa 329 todetaan, että hevosen ollessa kilpailun aikana kilpailualueella kaikkien sisään- ja uloskäyntien on oltava fyysisesti suljettuina.",
)

add(
    "arena-warmup/fi-awr-0002-v1.txt",
    STEM="Radalla on 12 estettä. Mikä on radan suurin sallittu pituus?",
    EXPLANATION="JR:n artiklan 329 mukaan radan enimmäispituus on 12 estettä × 60 m = 720 m.",
)

add(
    "arena-warmup/fi-awr-0002-v2.txt",
    STEM="Jos radalla on 10 estettä, sen pituus saa olla enintään:",
    EXPLANATION="JR:n artiklassa 329 radan pituus rajoitetaan esteiden lukumäärään kerrottuna 60:llä: 10 × 60 = 600 m.",
)

add(
    "arena-warmup/fi-awr-0002.txt",
    STEM="Mikä on radan suurin sallittu kokonaispituus suhteessa esteiden lukumäärään?",
    EXPLANATION="JR:n artiklassa 329 määrätään, että radan kokonaispituus metreinä ei saa koskaan ylittää esteiden lukumäärää kerrottuna 60:llä.",
)

add(
    "arena-warmup/fi-awr-0003-v1.txt",
    STEM="JR:n artiklan 241.2.5 mukaan lähtölinjan ja ensimmäisen esteen välinen vähimmäisetäisyys on:",
    EXPLANATION="JR:n artiklan 329 mukaan lähtö- ja maalilinjan on oltava vähintään 6 metrin ja enintään 15 metrin etäisyydellä ensimmäisestä ja viimeisestä esteestä.",
)

add(
    "arena-warmup/fi-awr-0003-v2.txt",
    STEM="Mikä etäisyyspari on JR:n artiklassa 241.2.5 lähtö- ja maalilinjan sijainnille asetettujen rajojen mukainen?",
    OPTION_A="4 m ja 16 m",
    OPTION_B="6 m ja 15 m",
    OPTION_C="3 m ja 14 m",
    OPTION_D="8 m ja 18 m",
    EXPLANATION="JR:n artiklassa 329 sallitaan 6–15 metrin etäisyys ensimmäisestä ja viimeisestä esteestä, joten 6 m ja 15 m ovat täsmälleen sallitut rajat.",
)

add(
    "arena-warmup/fi-awr-0003-v3.txt",
    STEM="Millaiset merkinnät lähtö- ja maalilinjassa on oltava JR:n artiklan 241.2.5 mukaan?",
    OPTION_A="Yksi keltainen lippu vasemmalla",
    OPTION_B="Punainen lippu oikealla ja valkoinen lippu vasemmalla sekä S- ja F-merkit",
    OPTION_C="Sininen lippu kummallakin puolella",
    OPTION_D="Vain numeroidut kartiot",
    EXPLANATION="JR:n artiklassa 329 vaaditaan kokonaan punainen lippu oikealle ja kokonaan valkoinen lippu vasemmalle sekä S-merkki (lähtö) ja F-merkki (maali).",
)

add(
    "arena-warmup/fi-awr-0003.txt",
    STEM="Kuinka kaukana lähtö- ja maalilinjan on oltava ensimmäisestä ja viimeisestä esteestä?",
    EXPLANATION="JR:n artiklassa 329 määrätään, että lähtö- ja maalilinja eivät saa olla yli 15 metrin eivätkä alle kuuden metrin etäisyydellä ensimmäisestä ja viimeisestä esteestä.",
)

add(
    "arena-warmup/fi-awr-0004-v1.txt",
    STEM="Miten kolmiosainen sarjaeste voidaan merkitä ratapiirrokseen?",
    OPTION_A="7, 8, 9",
    OPTION_B="8A, 8B, 8C",
    OPTION_C="8, 8a, 8b",
    OPTION_D="III",
    EXPLANATION="JR:n artiklassa 241.3.3 annetaan sarjaesteen osille, joilla on yksi yhteinen numero, esimerkkimerkinnät 8A, 8B ja 8C.",
)

add(
    "arena-warmup/fi-awr-0004-v2.txt",
    STEM="Miksi sarjaesteen jokaiseen osaan lisätään erottava kirjain?",
    OPTION_A="Jotta osien järjestys on selvä tuomaristolle ja urheilijoille",
    OPTION_B="Jotta esteiden lukumäärä kasvaa",
    OPTION_C="Jotta ilmenee, mitkä osat ovat vapaaehtoisia",
    OPTION_D="Vain umpinaisten sarjaesteiden merkitsemistä varten",
    EXPLANATION="JR:n artiklassa 329 selitetään, että yksi ainoa numero voidaan toistaa sarjaesteen jokaisessa osassa erottavin kirjaimin, jotta merkintä on selvä tuomaristolle ja urheilijoille.",
)

add(
    "arena-warmup/fi-awr-0004-v3.txt",
    STEM="Mikä seuraavista väittämistä on oikein JR:n artiklan 241.3.3 mukaan?",
    OPTION_A="Sarjaesteillä on erilliset peräkkäiset numerot",
    OPTION_B="Sarjaesteillä on yksi numero, ja osat merkitään kirjaimin",
    OPTION_C="Vain sarjaesteen viimeinen osa numeroidaan",
    OPTION_D="Kirjaimia ei sallita ratapiirroksessa",
    EXPLANATION="JR:n artiklassa 241.3.3 todetaan, että sarjaesteillä on yksi numero ja että jokaiseen osaan lisätään erottava kirjain, esimerkiksi 8A, 8B ja 8C.",
)

add(
    "arena-warmup/fi-awr-0004.txt",
    STEM="Miten sarjaesteet numeroidaan ratapiirroksessa?",
    OPTION_A="Jokainen osa saa erillisen juoksevan numeron",
    OPTION_B="Niillä on vain yksi numero, ja jokainen osa merkitään kirjaimella, esimerkiksi 8A, 8B ja 8C",
    OPTION_C="Vain ensimmäinen osa numeroidaan",
    OPTION_D="Ne numeroidaan roomalaisin numeroin",
    EXPLANATION="JR:n artiklassa 241.3.3 määrätään, että sarjaesteillä on vain yksi numero, joka voidaan toistaa jokaisessa osassa erottavin kirjaimin.",
)

add(
    "arena-warmup/fi-awr-0005-v1.txt",
    STEM="Mitä JR:n artiklassa 241.6.1.2 sanotaan tilanteista, jotka tapahtuvat ennen kuin urheilija ylittää lähtölinjan?",
    OPTION_A="Jokainen kielto ennen lähtöä lasketaan ensimmäiseksi tottelemattomuudeksi",
    OPTION_B="Urheilijan ja/tai hevosen kaatuminen kilpailualueelle tulon jälkeen estää lähdön",
    OPTION_C="45 sekunnin lähtölaskentaa ei saa keskeyttää",
    OPTION_D="Tottelemattomuudesta ennen lähtölinjan ylittämistä ei rangaista",
    EXPLANATION="Lähtömerkin ja lähtölinjan ylityksen välisenä aikana tapahtuvasta tottelemattomuudesta ei rangaista, mutta kilpailualueelle tulon ja lähtölinjan ylityksen välillä tapahtuva kaatuminen estää urheilijan lähdön.",
)

add(
    "arena-warmup/fi-awr-0005-v2.txt",
    STEM="Mitkä lähtömenettelyä koskevat väittämät ovat oikein JR:n artiklan 241.6.1.2 nojalla?",
    OPTION_A="45 sekunnin lähtölaskenta voidaan keskeyttää odottamattomien olosuhteiden vuoksi",
    OPTION_B="Kilpailualueelle tulon jälkeen mutta ennen lähtölinjan ylittämistä tapahtuva kaatuminen estää urheilijan lähdön",
    OPTION_C="Tottelemattomuudesta ennen lähtölinjan ylittämistä rangaistaan aina",
    OPTION_D="Tuomaristo voi peruuttaa lähtömenettelyn ja käynnistää lähtölaskennan uudelleen",
    EXPLANATION="JR:n artiklassa 329 annetaan tuomaristolle oikeus keskeyttää lähtölaskenta odottamattomissa olosuhteissa, määrätään, että kilpailualueelle tulon jälkeen mutta ennen lähtölinjan ylitystä tapahtuva kaatuminen estää lähdön, ja sallitaan tuomariston peruuttaa lähtömenettely ja käynnistää lähtölaskenta uudelleen. Tottelemattomuudesta ennen lähtölinjan ylittämistä ei rangaista.",
)

add(
    "arena-warmup/fi-awr-0005-v3.txt",
    STEM="Mitkä kelloa ja lähtömenettelyä koskevat väittämät ovat oikein JR:n artiklan 241.6.1.2 mukaan?",
    OPTION_A="Kello käynnistää 45 sekunnin lähtölaskennan, joka näkyy ajanottolaitteen tulostaulussa tai muussa kilpailualueen vieressä olevassa näytössä",
    OPTION_B="Urheilijan on ylitettävä lähtölinja oikeaan suuntaan lähtölaskennan aikana",
    OPTION_C="Lähtölaskenta käynnistyy automaattisesti uudelleen, jos se keskeytetään",
    OPTION_D="Tuomaristo voi keskeyttää lähtölaskennan odottamattomissa olosuhteissa",
    EXPLANATION="JR:n artiklassa 241.6.1.2 määrätään, että kello käynnistää 45 sekunnin lähtölaskennan, joka näkyy ajanottolaitteen tulostaulussa tai muussa kilpailualueen vieressä olevassa näytössä. Lähtölaskenta määrää ajan, jonka kuluessa urheilijan on aloitettava suoritus ylittämällä lähtölinja oikeaan suuntaan. Tuomaristo voi keskeyttää lähtölaskennan odottamattomissa olosuhteissa, eikä se käynnisty uudelleen automaattisesti.",
)

add(
    "arena-warmup/fi-awr-0005.txt",
    STEM="Mitkä 45 sekunnin lähtölaskentaa koskevat väittämät ovat oikein?",
    OPTION_A="Se käynnistetään kellolla, ja se näkyy tulostaulussa tai muussa näytössä",
    OPTION_B="Se määrää ajan, jonka kuluessa urheilijan on aloitettava suoritus ylittämällä lähtölinja oikeaan suuntaan",
    OPTION_C="Lähtömerkin ja lähtölinjan ylityksen välillä tapahtuvasta tottelemattomuudesta rangaistaan aina",
    OPTION_D="Kilpailualueelle tulon jälkeen mutta ennen lähtölinjan ylittämistä tapahtuva kaatuminen estää urheilijan lähdön",
    EXPLANATION="JR:n artiklassa 241.6.1.2 määrätään, että kello käynnistää 45 sekunnin lähtölaskennan, joka näkyy ajanottolaitteen tulostaulussa tai muussa kilpailualueen vieressä olevassa näytössä. Lähtölaskenta määrää ajan, jonka kuluessa urheilijan on aloitettava suoritus ylittämällä lähtölinja oikeaan suuntaan. Tottelemattomuudesta ennen lähtölinjan ylittämistä ei rangaista, kun taas kilpailualueelle tulon ja lähtölinjan ylityksen välillä tapahtuva kaatuminen estää ratsukon lähdön.",
)

add(
    "arena-warmup/fi-awr-0006-v1.txt",
    STEM="Käynnissä olevassa kilpailussa esteiden enimmäiskorkeus on 1,35 m. Mikä on verryttelyesteiden enimmäiskorkeus JR:n artiklan 242.4.3 mukaan?",
    EXPLANATION="JR:n artiklan 329 mukaan verryttelyesteet saavat ylittää kilpailun enimmäiskorkeuden 10 senttimetrillä: 1,35 m + 0,10 m = 1,45 m.",
)

add(
    "arena-warmup/fi-awr-0006-v2.txt",
    STEM="Mikä on verryttelyalueen esteiden korkeusrajoitus JR:n artiklan 242.4.3 mukaan kilpailuissa, joissa estekorkeus on yli 1,40 m?",
    OPTION_D="Sama kuin kilpailun enimmäiskorkeus",
    EXPLANATION="JR:n artiklassa 242.4.3 määrätään, että jos kilpailun esteiden korkeus on yli 1,40 m, verryttelyesteiden korkeus saa olla enintään 1,65 m ja pituus enintään 1,80 m.",
)

add(
    "arena-warmup/fi-awr-0006-v3.txt",
    STEM="Kuinka paljon verryttelyesteet saavat JR:n artiklan 242.4.3 mukaan ylittää käynnissä olevan kilpailun todellisen enimmäispituuden, kun enimmäiskorkeus on 1,30 m?",
    EXPLANATION="JR:n artiklan 329 mukaan verryttelyesteet saavat kilpailuissa, joiden enimmäiskorkeus on 1,40 m tai vähemmän, ylittää kilpailuesteiden todellisen enimmäiskorkeuden ja -pituuden 10 senttimetrillä.",
)

add(
    "arena-warmup/fi-awr-0006.txt",
    STEM="Mikä on verryttelyalueen esteiden suurin sallittu korkeus kilpailussa, jossa esteiden enimmäiskorkeus on 1,40 m tai vähemmän?",
    OPTION_C="10 cm enemmän kuin kilpailun enimmäiskorkeus, enintään 1,50 m",
    EXPLANATION="Kilpailusääntöjen artiklassa 329 määrätään, että kilpailuissa, joissa esteiden enimmäiskorkeus on 1,40 m tai vähemmän, verryttelyesteet saavat ylittää kilpailuesteiden todellisen enimmäiskorkeuden ja -pituuden enintään 10 senttimetrillä. Poniluokat ovat tästä poikkeus.",
)

add(
    "arena-warmup/fi-awr-0007-v1.txt",
    STEM="Minkä seuraavista JR:n artikla 242.4.12 kieltää verryttelyalueella kilpailun verryttelyn aikana?",
    OPTION_A="Pystysuorat verryttelyesteet",
    OPTION_B="Voimistelu- ja harjoitusliikkeet",
    OPTION_C="Yhden pituusesteen",
    OPTION_D="Stewardin",
    EXPLANATION="JR:n artiklassa 329 määrätään, ettei voimistelu- ja harjoitusliikkeitä sallita kilpailun verryttelyn aikana.",
)

add(
    "arena-warmup/fi-awr-0007-v2.txt",
    STEM="Mikä seuraavista on sallittua verryttelyalueella JR:n artiklan 242.4 nojalla?",
    OPTION_A="Voimistelu- ja harjoitusliikkeet",
    OPTION_B="Sarjaesteet kaikissa kilpailuissa",
    OPTION_C="Vähintään yksi pystyeste ja yksi pituuseste",
    OPTION_D="Hevosten kävelyttäminen kuppeihin nostettujen puomien yli",
    EXPLANATION="Vaikka JR:n artiklassa 329 kielletään voimistelu- ja harjoitusliikkeet ja yleisesti myös sarjaesteet, samassa artiklassa vaaditaan verryttelyalueelle vähintään yksi pystyeste ja yksi pituuseste.",
)

add(
    "arena-warmup/fi-awr-0007.txt",
    STEM="Mitä toimintaa kilpailun verryttelyn aikana ei nimenomaisesti sallita?",
    OPTION_A="Maahan asetettujen puomien yli käveleminen",
    OPTION_B="Voimistelu- ja harjoitusliikkeet",
    OPTION_C="Yksittäisen pystyesteen hyppääminen",
    OPTION_D="Ohjauspuomien käyttö",
    EXPLANATION="JR:n artiklassa 329 todetaan nimenomaisesti, ettei voimistelu- ja harjoitusliikkeitä sallita kilpailun verryttelyn aikana.",
)

# --------------------------------------------------------------------------
# classification
# --------------------------------------------------------------------------

add(
    "classification/fi-cls-0064-v1.txt",
    STEM="Mitkä asiakirjat määrittävät urheilijan sijoituksen JR:n artiklan 267.1 mukaan?",
    OPTION_A="Vain FEI:n säännöt",
    OPTION_B="Kilpailukutsu ja mahdolliset ratapiirroksessa mainitut muutokset",
    OPTION_C="Virallinen kilpailukalenteri",
    OPTION_D="Joukkueenjohtajan lausunto",
    EXPLANATION="JR:n artiklan 341 mukaan sijoitus perustuu kilpailun arvosteluun, kilpailukutsun ohjeisiin ja ratapiirroksessa ilmoitettuihin muutoksiin.",
)

add(
    "classification/fi-cls-0064-v2.txt",
    STEM="Arvostelumenetelmän muutos on julkaistu ratapiirroksessa. Mitä tästä muutoksesta seuraa JR:n artiklan 267.1 mukaan?",
    OPTION_A="Se on virheellinen",
    OPTION_B="Se voi vaikuttaa sijoitukseen",
    OPTION_C="Se koskee vain seuraavaa kilpailua",
    OPTION_D="Urheilijoiden on hyväksyttävä se erikseen",
    EXPLANATION="JR:n artiklan 341 mukaan sijoituksen määrittämiseen vaikuttavat myös kaikki ratapiirroksessa mainitut muutokset.",
)

add(
    "classification/fi-cls-0064.txt",
    STEM="Miten yksittäisen urheilijan sijoitus kilpailussa määräytyy?",
    OPTION_A="Urheilijan kansalaisuuden mukaan",
    OPTION_B="Kilpailun arvostelun, kilpailukutsun ja mahdollisten ratapiirroksessa mainittujen muutosten perusteella",
    OPTION_C="Arvonnassa määräytyvän järjestyksen mukaan",
    OPTION_D="Suurimman voitetun palkintorahasumman mukaan",
    EXPLANATION="JR:n artiklassa 267.1 todetaan, että yksittäisen urheilijan sijoitus määräytyy kilpailun arvostelun, kilpailukutsussa olevien ohjeiden ja ratapiirroksessa mainittujen muutosten perusteella.",
)

add(
    "classification/fi-cls-0065-v1.txt",
    STEM="Millä perusteella tuomaristo voi JR:n artiklan 267.2 nojalla myöntää poikkeuksia palkintojenjakoon osallistumisesta?",
    OPTION_A="Kaupallisista syistä",
    OPTION_B="Turvallisuussyistä",
    OPTION_C="Urheilijan kansalaisuuden vuoksi",
    OPTION_D="Palkintosumman suuruuden vuoksi",
    EXPLANATION="JR:n artiklan 341 mukaan tuomaristo voi myöntää palkintojenjakotilaisuuteen osallistumisesta poikkeuksia turvallisuussyistä.",
)

add(
    "classification/fi-cls-0065-v2.txt",
    STEM="Mitä tuomaristo voi tehdä, jos palkinnon voittaja ei osallistu palkintojenjakotilaisuuteen ilman hyväksyttävää syytä?",
    OPTION_A="Sakottaa urheilijaa",
    OPTION_B="Antaa järjestäjälle luvan evätä urheilijan palkinnon tai palkinnot",
    OPTION_C="Hylätä urheilijan suorituksen",
    OPTION_D="Myöntää palkinnon seuraavaksi sijoittuneelle urheilijalle",
    EXPLANATION="JR:n artiklassa 341 määrätään, että jos palkinnon voittaja ei ilman hyväksyttävää syytä osallistu palkintojenjakotilaisuuteen, tuomaristo voi antaa järjestäjälle luvan evätä urheilijan palkinnon tai palkinnot.",
)

add(
    "classification/fi-cls-0065-v3.txt",
    STEM="Kenen kanssa palkinnonsaajien tulee JR:n artiklan 267.2 mukaan osallistua palkintojenjakotilaisuuteen?",
    OPTION_A="Valmentajansa kanssa",
    OPTION_B="Sijoittuneiden hevosten kanssa",
    OPTION_C="Kansallisen liittonsa edustajan kanssa",
    OPTION_D="Sponsorin edustajan kanssa",
    EXPLANATION="JR:n artiklassa 267.2 määrätään, että palkinnonsaajien tulee osallistua palkintojenjakotilaisuuteen sijoittuneiden hevosten kanssa.",
)

add(
    "classification/fi-cls-0065.txt",
    STEM="Mitä palkinnonsaajilta edellytetään palkintojenjakotilaisuudessa?",
    OPTION_A="Heidän on myytävä palkinnot takaisin järjestäjälle",
    OPTION_B="Heidän on osallistuttava palkintojenjakotilaisuuteen, yleensä sijoittuneiden hevosten kanssa",
    OPTION_C="Vain johtavan urheilijan on osallistuttava",
    OPTION_D="Osallistuminen on vapaaehtoista, jos palkintosumma ylittää 1 000 Sveitsin frangia",
    EXPLANATION="JR:n artiklassa 267.2 määrätään, että palkinnonsaajien on osallistuttava palkintojenjakotilaisuuteen ja että heidän tulee tehdä se sijoittuneiden hevosten kanssa. Tuomaristo voi kuitenkin myöntää poikkeuksia turvallisuussyistä.",
)

add(
    "classification/fi-cls-0066-v1.txt",
    STEM="Mihin JR:n artiklan 218.3.1 mukainen luvallinen vetäytyminen toiselta kierrokselta sijoittaa urheilijan?",
    OPTION_A="Ensimmäiselle sijalle",
    OPTION_B="Jaetulle viimeiselle sijalle suorituksen päättäneiden jälkeen",
    OPTION_C="Ensimmäisen kierroksen ajan mukaiselle sijalle",
    OPTION_D="Ei mihinkään sijalle, eli urheilija jää sijoittumatta",
    EXPLANATION="JR:n artikla 341 koskee uusintoja, toisia kierroksia ja voittokierroksia. Keskeyttäneet, hylätyt ja luvalla vetäytyneet urheilijat sijoittuvat jaetulle viimeiselle sijalle suorituksen päättäneiden jälkeen.",
)

add(
    "classification/fi-cls-0066-v2.txt",
    STEM="Joukkue vetäytyy Nations Cupin toiselta kierrokselta. Miten se sijoitetaan JR:n artiklan 218.3.1 nojalla?",
    OPTION_A="Jaetulle viimeiselle sijalle toisella kierroksella",
    OPTION_B="Ensimmäisen kierroksen virhepisteiden mukaan",
    OPTION_C="Ilman oikeutta palkintorahaan, mutta sijoitus määräytyy ensimmäisen kierroksen virhepisteiden perusteella",
    OPTION_D="Joukkue hylätään",
    EXPLANATION="JR:n artiklassa 341 todetaan, että Nations Cupin toiselta kierrokselta vetäytyvät joukkueet eivät ole oikeutettuja palkintorahaan ja että ne sijoittuvat ensimmäisellä kierroksella saamiensa virhepisteiden mukaan.",
)

add(
    "classification/fi-cls-0066.txt",
    STEM="Mihin uusinnan keskeyttävä urheilija sijoittuu?",
    OPTION_A="Tasoihin kaikkien hylättyjen urheilijoiden kanssa",
    OPTION_B="Jaetulle viimeiselle sijalle uusinnassa kaikkien suorituksen päättäneiden urheilijoiden jälkeen",
    OPTION_C="Vain peruskierroksen sijoituksensa mukaiselle sijalle",
    OPTION_D="Ei mihinkään sijalle, eli hän jää sijoittumatta",
    EXPLANATION="JR:n artiklassa 341 todetaan, että urheilija, joka keskeyttää, hylätään tai vetäytyy uusinnasta luvalla, sijoittuu uusinnassa jaetulle viimeiselle sijalle kaikkien suorituksen päättäneiden urheilijoiden jälkeen.",
)

add(
    "classification/fi-cls-0067-v1.txt",
    STEM="Kuka voi JR:n artiklan 267.4 nojalla sallia loimien käytön palkintojenjakotilaisuudessa erityisissä olosuhteissa?",
    OPTION_A="Järjestäjä",
    OPTION_B="Tuomaristo",
    OPTION_C="Joukkueenjohtaja",
    OPTION_D="Sponsori",
    EXPLANATION="JR:n artiklassa 341 määrätään, että tuomaristo voi erityisissä olosuhteissa sopia toisin.",
)

add(
    "classification/fi-cls-0067-v2.txt",
    STEM="Millainen loimi on aina poikkeus JR:n artiklan 267.4 mukaisesta yleisestä loimien käyttökiellosta palkintojenjaossa?",
    OPTION_A="Mikä tahansa talliloimi",
    OPTION_B="Kilpailun sponsorien lahjoittamat loimet",
    OPTION_C="Vain FEI:n merkillä varustetut loimet",
    OPTION_D="Loimet mestaruuskilpailuissa",
    EXPLANATION="Kilpailun sponsorien lahjoittamat loimet on JR:n artiklan 341 nojalla vapautettu yleisestä kiellosta.",
)

add(
    "classification/fi-cls-0067-v3.txt",
    STEM="Mitä palkintojenjakotilaisuuden vaatimusta JR:n artikla 267.4 koskee?",
    OPTION_A="Kansallislaulua",
    OPTION_B="Urheilijoiden kilpailuasua",
    OPTION_C="Hevosten loimien käyttöä palkintojenjaossa",
    OPTION_D="Palkintojen jakojärjestystä",
    EXPLANATION="JR:n artiklassa 341 säädellään sitä, saavatko hevoset käyttää loimia palkintojenjakotilaisuudessa.",
)

add(
    "classification/fi-cls-0067.txt",
    STEM="Mikä on yleinen sääntö hevosten loimien käytöstä palkintojenjakotilaisuudessa?",
    OPTION_A="Loimet ovat pakollisia",
    OPTION_B="Loimia ei saa käyttää lukuun ottamatta kilpailun sponsorien lahjoittamia loimia",
    OPTION_C="Loimia saa käyttää vain kylmällä säällä",
    OPTION_D="Vain villaloimet ovat sallittuja",
    EXPLANATION="JR:n artiklassa 267.4 todetaan, että ellei tuomariston kanssa erityisissä olosuhteissa toisin sovita, hevoset eivät saa käyttää palkintojenjakotilaisuudessa loimia lukuun ottamatta kilpailun sponsorien lahjoittamia loimia.",
)

add(
    "classification/fi-cls-0068-v1.txt",
    STEM="Mitä JR:n artiklan 267.7 mukaan tapahtuu urheilijalle, joka on selviytynyt finaaliin mutta kieltäytyy osallistumasta siihen?",
    OPTION_A="Hän menettää kaikki karsintakilpailussa voittamansa palkinnot",
    OPTION_B="Hän säilyttää jo voittamansa palkinnot",
    OPTION_C="Häntä sakotetaan",
    OPTION_D="Hänen suorituksensa hylätään automaattisesti",
    EXPLANATION="JR:n artiklan 341 mukaan urheilija säilyttää karsintakilpailussa voittamansa palkinnot, vaikka hän kieltäytyisi osallistumasta finaaliin.",
)

add(
    "classification/fi-cls-0068-v3.txt",
    STEM="Urheilija voittaa karsintakilpailun, mutta ei halua osallistua finaaliin. Mitä hänen karsinnassa voittamilleen palkinnoille tapahtuu?",
    OPTION_A="Ne palautetaan",
    OPTION_B="Ne säilyvät hänellä",
    OPTION_C="Ne lahjoitetaan edelleen",
    OPTION_D="Ne mitätöidään",
    EXPLANATION="JR:n artiklan 341 mukaan palkinnonsaajat säilyttävät karsintakilpailuissa voittamansa palkinnot, vaikka he kieltäytyisivät osallistumasta finaaliin.",
)

add(
    "classification/fi-cls-0068.txt",
    STEM="Mitä tapahtuu karsintakilpailussa voitetuille palkinnoille, jos urheilija kieltäytyy osallistumasta loppukilpailuun, johon hän on karsinnassa ansainnut paikan?",
    OPTION_A="Hänen on palautettava palkinnot",
    OPTION_B="Hän säilyttää voittamansa palkinnot",
    OPTION_C="Palkinnot siirtyvät järjestäjälle",
    OPTION_D="Palkinnot annetaan seuraavalle karsinnassa sijoittuneelle urheilijalle",
    EXPLANATION="JR:n artiklassa 267.7 todetaan, että karsintakilpailujen voittajat säilyttävät voittamansa palkinnot, vaikka he kieltäytyisivät osallistumasta loppukilpailuun, johon he ovat ansainneet paikan.",
)

add(
    "classification/fi-cls-0069-v2.txt",
    STEM="Mikä on JR:n artiklan 267.6 mukainen yleinen sääntö niiden urheilijoiden palkinnoista, jotka eivät pysty suorittamaan kilpailun ensimmäistä kierrosta loppuun?",
    OPTION_A="He saavat aina palkinnon",
    OPTION_B="He eivät saa palkintoja muutoin kuin tietyissä erikoiskilpailuissa",
    OPTION_C="He saavat puolet palkintorahasta",
    OPTION_D="He menettävät kaikki tulevat osallistumismaksut",
    EXPLANATION="JR:n artiklassa 341 todetaan, että urheilijat, jotka eivät pysty suorittamaan kilpailun ensimmäistä kierrosta loppuun, eivät saa palkintoja muutoin kuin tietyissä erikoiskilpailuissa.",
)

add(
    "classification/fi-cls-0069-v3.txt",
    STEM="Mitä JR:n artiklan 267.6 mukainen tiettyjä erikoiskilpailuja koskeva poikkeus tarkoittaa urheilijoille, jotka eivät pysty suorittamaan ensimmäistä kierrosta loppuun?",
    OPTION_A="He saavat täyden palkinnon tilanteesta riippumatta",
    OPTION_B="He voivat saada palkinnon, vaikka eivät olisi suorittaneet ensimmäistä kierrosta loppuun",
    OPTION_C="Heidät hylätään automaattisesti",
    OPTION_D="Heidän on aloitettava ensimmäinen kierros uudelleen",
    EXPLANATION="JR:n artiklassa 341 määrätään, että urheilijat, jotka eivät pysty suorittamaan ensimmäistä kierrosta loppuun, eivät saa palkintoja muutoin kuin tietyissä erikoiskilpailuissa. Tämä tarkoittaa, että näissä erikoiskilpailuissa palkinto voidaan myöntää, vaikka kierros jäisi kesken.",
)

add(
    "classification/fi-cls-0069.txt",
    STEM="Minkä palkinnon saavat JR:n artiklan 267.6 mukaan urheilijat, jotka eivät pysty suorittamaan kilpailun ensimmäistä kierrosta loppuun?",
    OPTION_A="He saavat lohdutuspalkinnon",
    OPTION_B="He eivät saa palkintoja muutoin kuin tietyissä erikoiskilpailuissa",
    OPTION_C="He saavat puolet palkintorahasta",
    OPTION_D="He saavat palkinnon, jos he ovat suorittaneet vähintään puolet radasta",
    EXPLANATION="JR:n artiklassa 341 todetaan, että urheilijat, jotka eivät pysty suorittamaan kilpailun ensimmäistä kierrosta loppuun, eivät saa palkintoja muutoin kuin tietyissä erikoiskilpailuissa.",
)

add(
    "classification/fi-cls-0070-v2.txt",
    STEM="Missä JR:n luvussa FEI:n kunniamerkit mainitaan?",
    EXPLANATION="JR:n artikla 341 sisältyy lukuun X ”Sijoitukset ja kunnianosoitukset”.",
)

add(
    "classification/fi-cls-0070-v3.txt",
    STEM="Mistä seuraavista FEI:n esteratsastuksen kunniamerkit myönnetään JR:n artiklan 268.1 mukaan?",
    OPTION_A="Minkä tahansa CSI1*-kilpailun voittamisesta",
    OPTION_B="Määrättyjen mestaruuskilpailujen ensimmäisen kierroksen suorittamisesta keskeyttämättä tai putoamatta",
    OPTION_C="FEI:n toimihenkilönä toimimisesta",
    OPTION_D="Grand Prix -kilpailussa kilpailevan hevosen omistamisesta",
    EXPLANATION="JR:n artiklassa 268.1 määrätään, että FEI:n esteratsastuksen kunniamerkit myönnetään urheilijoille, jotka suorittavat tiettyjen kilpailujen, kuten olympialaisten ja maailmanmestaruuskilpailujen, ensimmäisen kierroksen keskeyttämättä tai putoamatta, edellyttäen että kulta-, hopea- ja pronssimerkkien vaatimukset täyttyvät.",
)

add(
    "classification/fi-cls-0070.txt",
    STEM="Mistä FEI:n esteratsastuksen kunniamerkit myönnetään JR:n artiklan 268.1 mukaan?",
    OPTION_A="Yhden CSI5*-kilpailun voittamisesta",
    OPTION_B="Tiettyjen joukkue- ja yksilömestaruuskilpailujen ensimmäisen kierroksen suorittamisesta keskeyttämättä tai putoamatta",
    OPTION_C="Täydellisestä läsnäolosta kilpailuissa",
    OPTION_D="Toimihenkilönä toimimisesta",
    EXPLANATION="JR:n artiklassa 268.1 määrätään, että FEI:n esteratsastuksen kunniamerkit myönnetään urheilijoille, jotka ovat suorittaneet ensimmäisen kierroksen keskeyttämättä tai putoamatta seniorien CSIO-kilpailun Nations Cupissa tai Longines League of Nations™ -kilpailussa, olympialaisten joukkue- ja/tai yksilökilpailussa sekä seniorien maailman- ja mannermestaruuskilpailujen joukkue- ja/tai yksilökilpailussa.",
)

# --------------------------------------------------------------------------
# competition-types
# --------------------------------------------------------------------------

add(
    "competition-types/fi-cty-0081-v1.txt",
    STEM="Milloin arvostelu A:n mukaisessa kilpailussa, jota ei ratsasteta aikaa vastaan, voidaan JR:n artiklan 220.1.1.2 nojalla järjestää uusinta ensimmäisestä sijasta?",
    OPTION_A="Aina",
    OPTION_B="Vain, jos siitä on mainittu kilpailukutsussa",
    OPTION_C="Ei koskaan",
    OPTION_D="Automaattisesti, jos täsmälleen kaksi urheilijaa on tasapisteissä",
    EXPLANATION="JR:n artiklassa 354 määrätään, että uusinta ilman ajanottoa voidaan järjestää, jos ensimmäisellä sijalla on tasapisteet, edellyttäen että tämä vaihtoehto on mainittu kilpailukutsussa.",
)

add(
    "competition-types/fi-cty-0081-v2.txt",
    STEM="JR:n artiklan 220.1.1.3 mukaan arvostelu A:n kilpailussa, jota ei ratsasteta aikaa vastaan, voidaan järjestää aikaa vastaan ratsastettava uusinta, jos kilpailukutsussa niin määrätään. Minkä perusteella muut urheilijat sijoittuvat?",
    OPTION_A="Uusinnassa saavuttamansa ajan perusteella",
    OPTION_B="Ensimmäisellä kierroksella saamiensa virhepisteiden perusteella",
    OPTION_C="Tasapisteasemansa perusteella",
    OPTION_D="Voittamansa palkintorahan perusteella",
    EXPLANATION="JR:n artiklassa 220.1.1.3 todetaan, että muut urheilijat sijoittuvat ensimmäisellä kierroksella saamiensa virhepisteiden mukaan ja että samat virhepisteet johtavat jaettuihin palkintoihin.",
)

add(
    "competition-types/fi-cty-0081.txt",
    STEM="Mitä tapahtuu, jos urheilijoilla on millä tahansa sijalla samat virhepisteet arvostelu A:n mukaisessa kilpailussa, jota ei ratsasteta aikaa vastaan?",
    OPTION_A="Heille järjestetään aina uusinta",
    OPTION_B="He jakavat palkinnot, eikä uusintaa järjestetä, ellei kilpailukutsussa ole määrätty ensimmäisen sijan uusinnasta",
    OPTION_C="Nopeampi suoritus voittaa",
    OPTION_D="Heidät sijoitetaan jaetulle ensimmäiselle sijalle",
    EXPLANATION="JR:n artiklassa 220.1.1.1 todetaan, että arvostelu A:n mukaisessa kilpailussa, jota ei ratsasteta aikaa vastaan, samat virhepisteet millä tahansa sijalla saaneet urheilijat jakavat palkinnot eikä uusintaa järjestetä.",
)

add(
    "competition-types/fi-cty-0082-v1.txt",
    STEM="Milloin aikaa vastaan ratsastettavan arvostelu A:n kilpailun uusinta voidaan JR:n artiklan 220.2.1.3 mukaan arvostella arvostelu C:n mukaan?",
    OPTION_A="Kun kaikki urheilijat ovat siitä samaa mieltä",
    OPTION_B="Kun kilpailussa ei jaeta Longines Ranking -pisteitä ja tästä on määrätty kilpailukutsussa",
    OPTION_C="Kun kyseessä on Grand Prix -kilpailu",
    OPTION_D="Kun kilpailu järjestetään sisätiloissa",
    EXPLANATION="JR:n artiklassa 220.2.1.3 todetaan, että arvostelu C:n mukainen uusinta on sallittu vain kilpailuissa, joissa ei jaeta Longines Ranking -pisteitä, ja että siitä on mainittava kilpailukutsussa.",
)

add(
    "competition-types/fi-cty-0082-v2.txt",
    STEM="Aikaa vastaan ratsastettavassa arvostelu A:n kilpailussa ensimmäisestä sijasta tasapisteissä olevat urheilijat voivat ratsastaa uusinnan. Minkä arvostelun mukaan tämä uusinta arvostellaan JR:n artiklan 220.2.1.2 mukaan?",
    OPTION_A="Arvostelu C:n mukaan",
    OPTION_B="Arvostelu A:n mukaan",
    OPTION_C="Ilman arvostelua, pelkän ajan perusteella",
    OPTION_D="Joukkueenjohtajan päätöksen mukaan",
    EXPLANATION="JR:n artiklassa 354 määrätään, että virhepisteiden ollessa tasan uusinta ratsastetaan arvostelu A:n mukaan aikaa vastaan.",
)

add(
    "competition-types/fi-cty-0082.txt",
    STEM="Mitkä tasapisteitä ja uusintoja koskevat väittämät ovat oikein aikaa vastaan ratsastettavassa arvostelu A:n kilpailussa?",
    OPTION_A="Tasapisteet millä tahansa sijalla voidaan ratkaista ajan perusteella ilman uusintaa",
    OPTION_B="Virhepisteiden tasatilanne voidaan ratkaista arvostelu A:n mukaisella, aikaa vastaan ratsastettavalla uusinnalla",
    OPTION_C="Ensimmäisen sijan tasapisteet voidaan ratkaista arvostelu C:n mukaisella uusinnalla, jos siitä on määrätty eikä Longines Ranking -pisteitä jaeta",
    OPTION_D="Virhepisteiden ja ajan tasatilanne ensimmäisellä sijalla johtaa aina uuteen uusintaan",
    EXPLANATION="JR:n artiklassa 354 luetellaan aikaa vastaan ratsastettavien arvostelu A:n kilpailujen vaihtoehdot: tasapisteet ratkaistaan ajan perusteella ilman uusintaa (kohta 220.2.1.1), uusinta ratsastetaan arvostelu A:n mukaan (kohta 220.2.1.2) tai uusinta ratsastetaan arvostelu C:n mukaan kilpailuissa, joissa ei jaeta Longines Ranking -pisteitä, jos kilpailukutsussa niin määrätään (kohta 220.2.1.3). Lisäuusinta on mahdollinen, jos virhepisteet ja aika ovat tasan, mutta sitä ei järjestetä aina.",
)

add(
    "competition-types/fi-cty-0083-v1.txt",
    STEM="Mitä JR:n artiklan 221.1 mukaan tapahtuu urheilijoille, jotka putoavat tai keskeyttävät kahden kierroksen kilpailun ensimmäisellä kierroksella?",
    OPTION_A="He saavat osallistua toiselle kierrokselle",
    OPTION_B="He eivät saa osallistua toiselle kierrokselle eivätkä he saa sijoitusta",
    OPTION_C="He saavat osallistua toiselle kierrokselle toisella hevosella",
    OPTION_D="Heidät sijoitetaan automaattisesti viimeiseksi",
    EXPLANATION="JR:n artiklassa 221.1 todetaan, että urheilijat, jotka ovat pudonneet tai keskeyttäneet ensimmäisellä kierroksella, eivät saa osallistua toiselle kierrokselle eivätkä he saa sijoitusta.",
)

add(
    "competition-types/fi-cty-0083-v2.txt",
    STEM="Minkä suhteen kahden kierroksen kilpailun radat voivat JR:n artiklan 221.1 nojalla poiketa toisistaan?",
    OPTION_A="Vain esteiden lukumäärän suhteen",
    OPTION_B="Radan, esteiden lukumäärän tai esteiden mittojen suhteen",
    OPTION_C="Vain nopeuden suhteen",
    OPTION_D="Ratojen on oltava täysin samanlaiset",
    EXPLANATION="JR:n artiklassa 354 määrätään, että radat voivat olla samanlaiset tai poiketa toisistaan radan, esteiden lukumäärän tai esteiden mittojen suhteen, mutta nopeuden on oltava sama.",
)

add(
    "competition-types/fi-cty-0083.txt",
    STEM="Onko jokaisen urheilijan ratsastettava kahden kierroksen kilpailussa samalla hevosella molemmilla kierroksilla?",
    OPTION_A="Ei, urheilija voi vaihtaa hevosta kierrosten välillä",
    OPTION_B="Kyllä, jokaisen urheilijan on osallistuttava molemmille kierroksille samalla hevosella",
    OPTION_C="Vain, jos kilpailukutsussa niin määrätään",
    OPTION_D="Vain Grand Prix -kilpailuissa",
    EXPLANATION="JR:n artiklassa 354 määrätään, että kahden kierroksen kilpailussa jokaisen urheilijan on osallistuttava molemmille kierroksille samalla hevosella.",
)

add(
    "competition-types/fi-cty-0084-v1.txt",
    STEM="Ketkä urheilijat palaavat Grand Prix -kilpailussa toiselle kierrokselle JR:n artiklan 221.2.2 mukaan, vaikka heidän lukumääränsä ylittäisi kilpailukutsussa mainitun prosenttiosuuden?",
    OPTION_A="Parhaat 25 prosenttia",
    OPTION_B="Kaikki urheilijat, jotka ovat ensimmäisellä kierroksella virhepisteittä",
    OPTION_C="Vain jaetulla ensimmäisellä sijalla olevat",
    OPTION_D="Nopeimmat 50 prosenttia",
    EXPLANATION="JR:n artiklassa 221.2.2 määrätään, että kaikissa Grand Prix -kilpailuissa kaikki virhepisteittä suorittaneet urheilijat palaavat toiselle kierrokselle, vaikka heidän lukumääränsä olisi suurempi kuin kilpailukutsussa vahvistettu prosenttiosuus.",
)

add(
    "competition-types/fi-cty-0084-v2.txt",
    STEM="Mihin kierrokseen kaikkien urheilijoiden on JR:n artiklan 221.2 mukaan osallistuttava kahden kierroksen kilpailussa?",
    OPTION_A="Vain ensimmäiseen kierrokseen",
    OPTION_B="Vasta toiseen kierrokseen",
    OPTION_C="Ensimmäiseen kierrokseen",
    OPTION_D="Uusintaan",
    EXPLANATION="JR:n artiklassa 221.2 määrätään, että kaikkien urheilijoiden on osallistuttava ensimmäiseen kierrokseen.",
)

add(
    "competition-types/fi-cty-0084.txt",
    STEM="Kahden kierroksen kilpailussa kilpailukutsussa on määrättävä, ketkä urheilijat jatkavat toiselle kierrokselle. Mikä on pienin sallittu prosenttiosuus urheilijoista, joka voidaan valita jatkoon?",
    EXPLANATION="JR:n artiklassa 221.2.2 määrätään, että toiselle kierrokselle osallistuvien urheilijoiden määrää voidaan rajoittaa kilpailukutsussa määrätyllä tavalla, kuitenkin niin, että jatkoon pääsee vähintään 25 prosenttia urheilijoista.",
)

add(
    "competition-types/fi-cty-0085-v1.txt",
    STEM="JR:n artiklan 222.1.2 mukaan tavallisen kahden vaiheen kilpailun toinen vaihe saa sisältää enintään:",
    OPTION_A="Yhden sarjaesteen",
    OPTION_B="Kaksi sarjaestettä",
    OPTION_C="Kolme sarjaestettä",
    OPTION_D="Ei yhtään sarjaestettä, sillä ne ovat kiellettyjä",
    EXPLANATION="JR:n artiklassa 222.1.2 määrätään, että toinen vaihe ratsastetaan neljän–kuuden esteen radalla, johon saa sisältyä enintään yksi sarjaeste.",
)

add(
    "competition-types/fi-cty-0085-v2.txt",
    STEM="Kuinka monta estettä tavallisen kahden vaiheen kilpailun toisessa vaiheessa saa JR:n artiklan 222.1.2 mukaan olla?",
    OPTION_A="Neljästä kuuteen",
    OPTION_B="Neljästä kuuteen",
    OPTION_C="Kuudesta kahdeksaan",
    OPTION_D="Seitsemästä yhdeksään",
    EXPLANATION="JR:n artiklassa 222.1.2 todetaan, että toinen vaihe ratsastetaan neljän–kuuden esteen radalla.",
)

add(
    "competition-types/fi-cty-0085.txt",
    STEM="Kuinka monta estettä tavallisen kahden vaiheen kilpailun ensimmäisessä vaiheessa saa olla?",
    OPTION_A="Neljästä kuuteen",
    OPTION_B="Seitsemästä yhdeksään",
    OPTION_C="Kymmenestä kahteentoista",
    OPTION_D="Ei enimmäismäärää",
    EXPLANATION="JR:n artiklassa 222.1.2 määrätään, että tavallisen kahden vaiheen kilpailun ensimmäinen vaihe on seitsemän–yhdeksän esteen rata, jolla voi olla sarjaesteitä tai olla olematta.",
)

add(
    "competition-types/fi-cty-0086-v1.txt",
    STEM="Missä kohdassa pysäytetään urheilijat, jotka ovat saaneet virhepisteitä tavallisen kahden vaiheen kilpailun ensimmäisessä vaiheessa, JR:n artiklan 222.1.3 nojalla?",
    OPTION_A="Ennen ensimmäisen vaiheen viimeisen esteen hyppäämistä",
    OPTION_B="Ensimmäisen vaiheen viimeisen esteen hyppäämisen jälkeen tai maalilinjan ylittämisen jälkeen, jos sallittu aika on ylitetty",
    OPTION_C="Toisen vaiheen lähtölinjalla",
    OPTION_D="Toisen maalilinjan ylittämisen jälkeen",
    EXPLANATION="JR:n artiklassa 222.1.3 määrätään, että urheilijat, jotka ovat saaneet virhepisteitä ensimmäisessä vaiheessa, pysäytetään kellon äänimerkillä sen jälkeen, kun he ovat hypänneet ensimmäisen vaiheen viimeisen esteen tai, jos ensimmäisen vaiheen aika on ylitetty, ylittäneet ensimmäisen vaiheen maalilinjan. Näiden urheilijoiden on pysähdyttävä ylitettyään ensimmäisen maalilinjan, eivätkä he saa jatkaa toiseen vaiheeseen.",
)

add(
    "competition-types/fi-cty-0086-v2.txt",
    STEM="Missä kohdassa tavallisen kahden vaiheen kilpailun ensimmäisessä vaiheessa virhepisteitä saaneet urheilijat pysäytetään JR:n artiklan 222.1.3 nojalla?",
    OPTION_A="Välittömästi sen esteen kohdalla, josta virhepisteet tulivat",
    OPTION_B="Ensimmäisen vaiheen viimeisen esteen hyppäämisen jälkeen tai ensimmäisen maalilinjan ylittämisen jälkeen, jos ensimmäisen vaiheen sallittu aika on ylitetty",
    OPTION_C="Toisen vaiheen alussa",
    OPTION_D="Toisen vaiheen maalilinjalla",
    EXPLANATION="JR:n artiklassa 354 määritetään tarkka kohta, jossa ensimmäisessä vaiheessa virhepisteitä saaneet urheilijat pysäytetään.",
)

add(
    "competition-types/fi-cty-0086.txt",
    STEM="Mitä tapahtuu urheilijoille, jotka ovat saaneet virhepisteitä tavallisen kahden vaiheen kilpailun ensimmäisessä vaiheessa?",
    OPTION_A="He jatkavat toiseen vaiheeseen, mutta virhepisteet siirtyvät mukana",
    OPTION_B="Heidät pysäytetään ensimmäisen vaiheen viimeisen esteen jälkeen tai ensimmäisen maalilinjan ylittämisen jälkeen, jos ensimmäisen vaiheen sallittu aika on ylitetty, eivätkä he jatka toiseen vaiheeseen",
    OPTION_C="He jatkavat toiseen vaiheeseen, mutta eivät voi enää voittaa",
    OPTION_D="Heidät hylätään",
    EXPLANATION="JR:n artiklassa 354 todetaan, että urheilijat, jotka ovat saaneet virhepisteitä ensimmäisessä vaiheessa, pysäytetään sen jälkeen, kun he ovat hypänneet ensimmäisen vaiheen viimeisen esteen tai, jos ensimmäisen vaiheen aika on ylitetty, ylittäneet ensimmäisen vaiheen maalilinjan. Heidän on pysähdyttävä, eivätkä he saa jatkaa toiseen vaiheeseen.",
)

add(
    "competition-types/fi-cty-0088-v1.txt",
    STEM="Millaisessa kilpailutapahtumassa Nations Cup saadaan JR:n artiklan 226.1.1 mukaan järjestää?",
    OPTION_A="CSI-kilpailussa",
    OPTION_B="CSIO-kilpailussa",
    OPTION_C="Mestaruuskilpailussa",
    OPTION_D="Missä tahansa FEI-kilpailussa",
    EXPLANATION="JR:n artiklassa 354 todetaan, että Nations Cup saadaan järjestää vain CSIO-kilpailussa.",
)

add(
    "competition-types/fi-cty-0088-v2.txt",
    STEM="JR:n artiklassa 226.1.4 todetaan, että Nations Cup on ainoa kilpailu, jossa:",
    OPTION_A="jaetaan yksilöpalkintorahaa",
    OPTION_B="viralliset joukkueet edustavat kansallisia liittoja",
    OPTION_C="ulkomaiset tuomarit toimivat tuomaristossa",
    OPTION_D="nuoret urheilijat kilpailevat",
    EXPLANATION="JR:n artiklassa 226.1.4 todetaan, että Nations Cup on ainoa kilpailu, jossa viralliset joukkueet edustavat kansallisia liittoja.",
)

add(
    "competition-types/fi-cty-0088-v3.txt",
    STEM="Mitä sijoituksia Nations Cupissa on JR:n artiklan 226.1.4 mukaan?",
    OPTION_A="Yksilösijoitukset",
    OPTION_B="Ei yksilösijoituksia",
    OPTION_C="Erillinen yksilökilpailu",
    OPTION_D="Sekä joukkue- että yksilösijoitukset",
    EXPLANATION="JR:n artiklassa 354 määrätään, ettei Nations Cupissa saa olla yksilösijoituksia, jotta kilpailun erityisluonne säilyy.",
)

add(
    "competition-types/fi-cty-0088.txt",
    STEM="Kuinka monen kansallisen liiton on vähintään osallistuttava, jotta kilpailu voidaan tunnustaa Nations Cupiksi?",
    EXPLANATION="JR:n artiklassa 226.1.2 todetaan, että kilpailuun on osallistuttava vähintään kolme kansallista liittoa, jotta se voidaan tunnustaa Nations Cupiksi.",
)

add(
    "competition-types/fi-cty-0089-v1.txt",
    STEM="Mikä on esteiden vähimmäis- ja enimmäiskorkeus JR:n artiklan 226.3.1 mukaan neljän tähden Nations Cupissa ulkokentällä?",
    EXPLANATION="JR:n artiklan 354 taulukossa neljän tähden Nations Cupin vähimmäis- ja enimmäiskorkeudeksi ulkokentällä on ilmoitettu 1,40/1,55 m.",
)

add(
    "competition-types/fi-cty-0089-v2.txt",
    STEM="Mikä on trippelin suurin sallittu pituus viiden tähden Nations Cupissa JR:n artiklan 226.3.1 nojalla?",
    EXPLANATION="JR:n artiklan 354 taulukon mukaan trippelin enimmäispituus viiden tähden Nations Cupissa on 2,20 m.",
)

add(
    "competition-types/fi-cty-0089-v3.txt",
    STEM="Kuinka monta estettä radalla on kaikilla JR:n artiklassa 226.3.1 luetelluilla Nations Cupin tähtitasoilla?",
    OPTION_A="10",
    OPTION_B="11",
    OPTION_C="12",
    OPTION_D="Lukumäärä riippuu tähtitasosta",
    EXPLANATION="JR:n artiklan 354 taulukossa esteiden lukumääräksi on merkitty 12 sekä 5*-, 4*-, 3*-, 2*- että 1*-tason Nations Cup -kilpailuissa.",
)

add(
    "competition-types/fi-cty-0089.txt",
    STEM="Mitä teknisiä vaatimuksia sovelletaan JR:n artiklan 226.3.1 nojalla viiden tähden Nations Cup -kilpailuihin ulkokentällä?",
    OPTION_A="Esteiden lukumäärä 12",
    OPTION_B="Vähimmäis- ja enimmäiskorkeus 1,45/1,60 m",
    OPTION_C="Nopeus 400 m/min",
    OPTION_D="Esteen enimmäispituus 2,00 m",
    EXPLANATION="JR:n artiklan 354 taulukossa viiden tähden Nations Cupin ulkoradalle määrätään 12 estettä, vähimmäis- ja enimmäiskorkeus 1,45/1,60 m, nopeus 400 m/min ja esteen enimmäispituus 2,00 m.",
)

add(
    "competition-types/fi-cty-0090-v1.txt",
    STEM="Minkä estetyypin on JR:n artiklan 230.2.1 mukaan oltava Puissance-kilpailun ensimmäisellä kierroksella?",
    OPTION_A="Vesiesteen",
    OPTION_B="Pystyesteen",
    OPTION_C="Trippelin",
    OPTION_D="Sarjaesteen",
    EXPLANATION="JR:n artiklassa 354 vaaditaan, että Puissance-kilpailun ensimmäisen kierroksen neljästä–kuudesta yksittäisestä esteestä vähintään yhden on oltava pystyeste.",
)

add(
    "competition-types/fi-cty-0090-v2.txt",
    STEM="Mitä estetyyppejä Puissance-kilpailussa ei JR:n artiklan 230.2.1 nojalla sallita?",
    OPTION_A="Pystyesteitä ja muureja",
    OPTION_B="Sarjaesteitä, vesiesteitä, ojia ja luonnonesteitä",
    OPTION_C="Pituusesteitä",
    OPTION_D="Yksittäisesteitä",
    EXPLANATION="JR:n artiklassa 354 kielletään sarjaesteet, vesiesteet, ojat ja luonnonesteet Puissance-kilpailuissa.",
)

add(
    "competition-types/fi-cty-0090-v3.txt",
    STEM="Kuinka korkea ensimmäisen esteen on vähintään oltava Puissance-kilpailun ensimmäisellä kierroksella?",
    EXPLANATION="JR:n artiklassa 230.2.1 määrätään, että ensimmäisen esteen on oltava vähintään 1,40 metriä korkea.",
)

add(
    "competition-types/fi-cty-0090.txt",
    STEM="Kuinka monta yksittäistä estettä Puissance-kilpailun ensimmäisen kierroksen on sisällettävä?",
    OPTION_A="Kahdesta neljään",
    OPTION_B="Neljästä kuuteen",
    OPTION_C="Kuudesta kahdeksaan",
    OPTION_D="Kahdeksasta kymmeneen",
    EXPLANATION="JR:n artiklan 354 mukaan Puissance-kilpailun ensimmäisen kierroksen on koostuttava neljästä–kuudesta yksittäisestä esteestä, joista vähintään yhden on oltava pystyeste.",
)

add(
    "competition-types/fi-cty-0091-v1.txt",
    STEM="Mihin lukumäärään Six Bar -kilpailun esteiden määrää voidaan JR:n artiklan 230.3.1 mukaan enintään vähentää?",
    EXPLANATION="JR:n artiklassa 230.3.1 todetaan, että esteiden lukumäärää voidaan vähentää neljään, jos kilpailualueen koko sitä edellyttää.",
)

add(
    "competition-types/fi-cty-0091-v2.txt",
    STEM="JR:n artiklan 230.3.2 mukaan Six Bar -kilpailussa puomeja kannattavien kuppien enimmäissyvyys on:",
    EXPLANATION="JR:n artiklassa 354 määrätään, että Six Bar -kilpailussa puomeja kannattavien kuppien enimmäissyvyys on 20 mm.",
)

add(
    "competition-types/fi-cty-0091-v3.txt",
    STEM="Mistä esteestä urheilijan on JR:n artiklan 230.3.4 mukaan jatkettava rataa Six Bar -kilpailussa kiellon tai ohituksen jälkeen?",
    OPTION_A="Ensimmäisestä esteestä",
    OPTION_B="Siitä esteestä, jolla virhe tapahtui",
    OPTION_C="Viimeisestä esteestä",
    OPTION_D="Tuomariston harkinnan mukaan määrätystä esteestä",
    EXPLANATION="JR:n artiklassa 354 todetaan, että kiellon tai ohituksen sattuessa urheilijan on jatkettava rataa siitä esteestä, jolla virhe tapahtui.",
)

add(
    "competition-types/fi-cty-0091.txt",
    STEM="Kuinka monta pystyestettä asetetaan Six Bar -kilpailussa suoraan linjaan noin 11 metrin etäisyydelle toisistaan?",
    EXPLANATION="JR:n artiklassa 354 todetaan, että Six Bar -kilpailussa kuusi pystyestettä asetetaan suoraan linjaan noin 11 metrin etäisyydelle toisistaan.",
)

add(
    "competition-types/fi-cty-0092-v1.txt",
    STEM="Minkä kilpailutyypin radalla jokeriestettä saa käyttää?",
    OPTION_A="Derbyn",
    OPTION_B="Pisteidenkeräilykilpailun",
    OPTION_C="Voima ja taito -kilpailun",
    OPTION_D="Nations Cupin",
    EXPLANATION="JR:n artiklassa 354 jokeriesteen käyttö rajataan pisteidenkeräilykilpailuihin.",
)

add(
    "competition-types/fi-cty-0092-v3.txt",
    STEM="Mitä jokeriesteen hyppäämisestä yleensä seuraa pisteidenkeräilykilpailussa?",
    OPTION_A="Se vähentää aikavirhepisteitä",
    OPTION_B="Siitä saa enemmän pisteitä kuin tavallisesta esteestä",
    OPTION_C="Se aiheuttaa urheilijan hylkäämisen",
    OPTION_D="Se nollaa pisteet",
    EXPLANATION="JR:n artiklassa 240.3 todetaan, että ratsukko kerää enemmän pisteitä, jos se hyppää jokeriesteen vaihtoehtoisen tavallisen esteen sijasta.",
)

add(
    "competition-types/fi-cty-0092.txt",
    STEM="Missä kilpailutyypissä jokerieste voi olla vaikea, vapaaehtoinen este?",
    OPTION_A="Puissance-kilpailussa",
    OPTION_B="Pisteidenkeräilykilpailussa",
    OPTION_C="Nations Cupissa",
    OPTION_D="Six Bar -kilpailussa",
    EXPLANATION="JR:n artiklassa 354 todetaan, että jokerieste on vaikea, vapaaehtoinen este, jota saa käyttää vain pisteidenkeräilykilpailussa. Samassa artiklassa säädellään pisteidenkeräilykilpailuja.",
)


def main() -> None:
    changed = 0
    checked = 0
    for rel, fields in sorted(FIXES.items()):
        path = ITEMS / rel
        checked += 1
        if not path.exists():
            raise SystemExit(f"Tiedostoa ei löydy: {path}")
        lines = path.read_text(encoding="utf-8").split("\n")
        out = []
        seen = set()
        for line in lines:
            if ": " in line or line.endswith(":"):
                key = line.split(":", 1)[0]
                if key in EDITABLE and key in fields:
                    new = fields[key]
                    assert "\n" not in new
                    out.append(f"{key}: {new}")
                    seen.add(key)
                    continue
            out.append(line)
        missing = set(fields) - seen
        if missing:
            raise SystemExit(f"{rel}: kenttiä ei löytynyt: {sorted(missing)}")
        new_text = "\n".join(out)
        if new_text != path.read_text(encoding="utf-8"):
            path.write_text(new_text, encoding="utf-8")
            changed += 1
    print(f"Tarkistettu (muutoslistalla): {checked}, muutettu: {changed}")


if __name__ == "__main__":
    main()
