#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
fix-group3.py

Korjaa suomenkielisten monivalintakysymysten kieliasun kansioissa
  questions/fi/items/jump-offs/
  questions/fi/items/obstacles/

Muutetaan VAIN kentät STEM, OPTION_A..OPTION_D ja EXPLANATION.
Muut kentät (ID, PARENT_ID, DOMAIN, ARTICLE, EDITION_REF, SOURCE_PAGE, TYPE,
CORRECT, STATUS, CREATED, VERIFIED_AGAINST_SOURCE) säilyvät ennallaan.

Terminologia yhtenäistetty lähteeseen:
  questions/fi/source/extracted-text.txt
  (SRL, Kilpailusäännöt III - Esteratsastus, voimassa 1.2.2026)
"""

import os
import sys

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "items")
BASE = os.path.normpath(BASE)

EDITABLE = {"STEM", "OPTION_A", "OPTION_B", "OPTION_C", "OPTION_D", "EXPLANATION"}

FIXES = {}

# ---------------------------------------------------------------- jump-offs

FIXES["jump-offs/fi-jof-0056-v1.txt"] = {
    "STEM": "Jos kilpailukutsussa ei ole määritelty, järjestetäänkö luokassa uusinta, mikä on artiklan 218.1.2 mukainen oletus?",
    "OPTION_A": "Uusinta järjestetään",
    "OPTION_B": "Uusintaa ei järjestetä",
    "OPTION_C": "Järjestäjä päättää asiasta kilpailupäivänä",
    "OPTION_D": "Tuomaristo päättää asiasta",
    "EXPLANATION": "Kilpailusääntöjen artiklan 344 mukaan luokan katsotaan olevan ilman uusintaa, ellei kilpailukutsussa ole toisin määrätty.",
}

FIXES["jump-offs/fi-jof-0056-v2.txt"] = {
    "STEM": "Missä asiakirjassa on ilmoitettava, järjestetäänkö luokassa uusinta?",
    "OPTION_A": "FEI:n kilpailukalenterissa",
    "OPTION_B": "Kilpailukutsussa",
    "OPTION_C": "Palkintojenjako-ohjelmassa",
    "OPTION_D": "Verryttelyalueen säännöissä",
    "EXPLANATION": "Kilpailusääntöjen artiklan 344 mukaan kilpailukutsussa on määriteltävä, järjestetäänkö luokassa uusinta.",
}

FIXES["jump-offs/fi-jof-0056-v3.txt"] = {
    "STEM": "Kilpailukutsussa ei mainita uusintaa. Miten urheilijoiden tulee varautua tilanteeseen?",
    "OPTION_A": "Oletetaan, että uusinta järjestetään",
    "OPTION_B": "Oletetaan, ettei uusintaa järjestetä",
    "OPTION_C": "Pyydetään teknistä edustajaa lisäämään uusinta",
    "OPTION_D": "Päätellään asia palkintorahojen perusteella",
    "EXPLANATION": "Kilpailusääntöjen artiklassa 218.1.2 todetaan, että ellei kilpailukutsussa ole toisin määrätty, luokan katsotaan olevan ilman uusintaa.",
}

FIXES["jump-offs/fi-jof-0056.txt"] = {
    "STEM": "Missä on mainittava, järjestetäänkö luokassa uusinta?",
    "OPTION_A": "Palkintoluettelossa",
    "OPTION_B": "Kilpailukutsussa",
    "OPTION_C": "Vain ratapiirroksessa",
    "OPTION_D": "Ei missään, sillä uusinta oletetaan, ellei toisin mainita",
    "EXPLANATION": "Kilpailusääntöjen artiklassa 218.1.2 määrätään, että kilpailukutsussa on mainittava, järjestetäänkö luokassa uusinta. Jos asiaa ei mainita, luokan katsotaan olevan ilman uusintaa.",
}

FIXES["jump-offs/fi-jof-0057-v1.txt"] = {
    "STEM": "Millä sijoilla mestaruuskilpailuissa voidaan järjestää uusinta tasatuloksen ratkaisemiseksi?",
    "OPTION_A": "Vain ensimmäisellä sijalla",
    "OPTION_B": "Palkintokorokesijoilla",
    "OPTION_C": "Kaikilla palkintosijoilla",
    "OPTION_D": "Viimeisellä sijalla",
    "EXPLANATION": "Kilpailusääntöjen artikla 344 sallii uusinnan, kun ratsukot ovat tasatuloksessa palkintokorokesijoilla mestaruuskilpailuissa tai arvokilpailuissa.",
}

FIXES["jump-offs/fi-jof-0057-v2.txt"] = {
    "STEM": "Kilpailusääntöjen artiklan 218.1.3 mukaan uusinta voidaan järjestää, kun vähintään kaksi ratsukkoa suorittaa perusradan seuraavasti:",
    "OPTION_A": "nopeimmalla ajalla",
    "OPTION_B": "ilman virhepisteitä",
    "OPTION_C": "tasan neljällä virhepisteellä",
    "OPTION_D": "niin, että suoritus hylätään",
    "EXPLANATION": "Kilpailusääntöjen artikla 344 sallii uusinnan, kun useampi kuin yksi ratsukko on suorittanut perusradan ilman virhepisteitä.",
}

FIXES["jump-offs/fi-jof-0057-v3.txt"] = {
    "STEM": "Mikä seuraavista EI ole kilpailusääntöjen artiklan 218.1.3 mukainen peruste uusinnan järjestämiselle?",
    "OPTION_A": "Tasatulos ensimmäisellä sijalla perusradan jälkeen",
    "OPTION_B": "Tasatulos palkintokorokesijoilla mestaruus- tai arvokilpailuissa",
    "OPTION_C": "Useampi kuin yksi ratsukko on suorittanut perusradan ilman virhepisteitä",
    "OPTION_D": "Tasatulos pelkästään ajassa ilman muita perusteita",
    "EXPLANATION": "Kilpailusääntöjen artiklassa 344 luetellaan uusinnan perusteiksi tasatulos virhepisteissä ensimmäisellä sijalla tai palkintokorokesijoilla mestaruus- ja arvokilpailuissa sekä useampi kuin yksi virhepisteetön suoritus. Pelkkä tasatulos ajassa ei ole peruste uusinnalle.",
}

FIXES["jump-offs/fi-jof-0057.txt"] = {
    "STEM": "Milloin kilpailusääntöjen artiklan 218.1.3 mukaan uusinta voidaan järjestää?",
    "OPTION_A": "Kun useampi kuin yksi ratsukko on suorittanut perusradan ilman virhepisteitä",
    "OPTION_B": "Kun ratsukot ovat tasatuloksessa ensimmäisellä sijalla perusradan jälkeen",
    "OPTION_C": "Kun ratsukot ovat tasatuloksessa palkintokorokesijoilla mestaruus- tai arvokilpailuissa",
    "OPTION_D": "Aina kun kilpailukutsussa mainitaan sana uusinta",
    "EXPLANATION": "Kilpailusääntöjen artiklassa 344 määritellään kolme tilannetta, joissa uusinta voidaan järjestää: virhepisteettömät suoritukset, tasatulos ensimmäisellä sijalla sekä tasatulos palkintokorokesijoilla mestaruus- tai arvokilpailuissa.",
}

FIXES["jump-offs/fi-jof-0058-v1.txt"] = {
    "STEM": "Millä edellytyksellä arvostelun A mukaan ratsastetun luokan uusinta voidaan arvostella arvostelun C mukaan?",
    "OPTION_A": "Tuomaristo ilmoittaa siitä kilpailun aikana",
    "OPTION_B": "Siitä on määrätty kilpailukutsussa",
    "OPTION_C": "Kaikki urheilijat suostuvat siihen",
    "OPTION_D": "Kyseessä on Nations Cup -kilpailu",
    "EXPLANATION": "Kilpailusääntöjen artikla 344 sallii arvostelun A mukaan ratsastetun luokan uusinnan arvostelemisen arvostelun C mukaan vain, jos siitä on mainittu kilpailukutsussa.",
}

FIXES["jump-offs/fi-jof-0058-v2.txt"] = {
    "STEM": "Onko kilpailusääntöjen artiklan 218.1.7 mukaan uusinnassa käytettävä samaa hevosta kuin perusradalla?",
    "OPTION_A": "Ei, uusinnassa saa käyttää mitä tahansa ilmoitettua hevosta",
    "OPTION_B": "Kyllä, urheilijan on lähdettävä uusintaan samalla hevosella",
    "OPTION_C": "Vain jos kilpailukutsussa niin määrätään",
    "OPTION_D": "Vain mestaruuskilpailuissa",
    "EXPLANATION": "Kilpailusääntöjen artiklassa 218.1.7 määrätään, että urheilijan on lähdettävä uusintaan samalla hevosella, jolla hän on suorittanut perusradan.",
}

FIXES["jump-offs/fi-jof-0058.txt"] = {
    "STEM": "Uusinta on pääsääntöisesti ratsastettava samojen sääntöjen ja saman arvostelun mukaan kuin perusrata. Mikä poikkeus on sallittu?",
    "OPTION_A": "Arvostelun A mukaan ratsastetun luokan uusinta voidaan arvostella arvostelun C mukaan, jos kilpailukutsussa niin määrätään",
    "OPTION_B": "Vauhti voidaan kaksinkertaistaa",
    "OPTION_C": "Esteet voidaan rakentaa eri materiaaleista",
    "OPTION_D": "Urheilija saa vaihtaa hevosta",
    "EXPLANATION": "Kilpailusääntöjen artiklassa 218.1.6 todetaan, että uusinta on lähtökohtaisesti ratsastettava samojen sääntöjen ja saman arvostelun mukaan kuin perusrata, mutta arvostelun A mukaan ratsastetun luokan uusinta voidaan arvostella arvostelun C mukaan, jos kilpailukutsussa niin määrätään.",
}

FIXES["jump-offs/fi-jof-0059-v1.txt"] = {
    "STEM": "Miten sarjaesteet otetaan kilpailusääntöjen artiklan 218.2.3 mukaan huomioon, kun lasketaan uusinnan esteiden vähimmäismäärää?",
    "OPTION_A": "Jokainen osaeste lasketaan erikseen",
    "OPTION_B": "Sarjaeste lasketaan yhdeksi esteeksi",
    "OPTION_C": "Sarjaesteitä ei lasketa lainkaan",
    "OPTION_D": "Sarjaeste lasketaan kahdeksi esteeksi",
    "EXPLANATION": "Kilpailusääntöjen artiklassa 344 todetaan nimenomaisesti, että sarjaeste lasketaan yhdeksi esteeksi, kun esteiden vähimmäismäärää lasketaan.",
}

FIXES["jump-offs/fi-jof-0059-v3.txt"] = {
    "STEM": "Kilpailusääntöjen artiklan 218.2.3 mukaan uusintarataa voidaan lyhentää siten, että esteitä on vähintään:",
    "OPTION_A": "neljä",
    "OPTION_B": "viisi",
    "OPTION_C": "kuusi",
    "OPTION_D": "seitsemän",
    "EXPLANATION": "Kilpailusääntöjen artikla 344 sallii esteiden määrän vähentämisen uusinnassa kuuteen esteeseen.",
}

FIXES["jump-offs/fi-jof-0059.txt"] = {
    "STEM": "Mikä on uusinnan esteiden pienin sallittu määrä?",
    "OPTION_A": "Neljä",
    "OPTION_B": "Viisi",
    "OPTION_C": "Kuusi",
    "OPTION_D": "Kahdeksan",
    "EXPLANATION": "Kilpailusääntöjen artiklassa 218.2.3 määrätään, että uusinnan esteiden määrää voidaan vähentää kuuteen esteeseen, ja sarjaeste lasketaan tällöin yhdeksi esteeksi.",
}

FIXES["jump-offs/fi-jof-0060-v1.txt"] = {
    "STEM": "Mitä sarjaesteen ominaisuutta EI saa muuttaa uusintaan kilpailusääntöjen artiklan 218.2.6 mukaan?",
    "OPTION_A": "Korkeutta",
    "OPTION_B": "Yksittäisten osaesteiden leveyttä",
    "OPTION_C": "Osaesteiden välistä etäisyyttä",
    "OPTION_D": "Väriä",
    "EXPLANATION": "Kilpailusääntöjen artikla 344 kieltää nimenomaisesti sarjaesteen osaesteiden välisen etäisyyden muuttamisen uusinnassa.",
}

FIXES["jump-offs/fi-jof-0060-v2.txt"] = {
    "STEM": "Mitä uusinnassa saa kilpailusääntöjen artiklan 218.2.5 mukaan muuttaa perusrataan verrattuna?",
    "OPTION_A": "Sarjaesteen osaesteiden välistä etäisyyttä",
    "OPTION_B": "Esteiden järjestystä",
    "OPTION_C": "Esteiden tyyppiä, esimerkiksi pystyestettä okseriksi",
    "OPTION_D": "Sallittujen hyppy-yritysten määrää",
    "EXPLANATION": "Kilpailusääntöjen artikla 344 sallii esteiden järjestyksen muuttamisen uusinnassa perusrataan verrattuna.",
}

FIXES["jump-offs/fi-jof-0060-v3.txt"] = {
    "STEM": "Kilpailusääntöjen artikla 218.2.4 sallii sarjaesteen osaesteiden poistamisen uusinnassa. Mitä osaestettä kolmois- tai nelisarjasta EI kuitenkaan saa poistaa?",
    "OPTION_A": "Ensimmäistä osaestettä",
    "OPTION_B": "Viimeistä osaestettä",
    "OPTION_C": "Keskimmäistä osaestettä tai keskimmäisiä osaesteitä",
    "OPTION_D": "Mitä tahansa reunimmaista osaestettä",
    "EXPLANATION": "Kilpailusääntöjen artiklassa 218.2.4 määrätään, että kolmois- tai nelisarjasta ei saa poistaa keskimmäistä osaestettä eikä keskimmäisiä osaesteitä.",
}

FIXES["jump-offs/fi-jof-0060.txt"] = {
    "STEM": "Miten sarjaesteen osaesteiden välistä etäisyyttä saa muuttaa uusinnassa?",
    "OPTION_A": "Sitä saa kasvattaa, jotta uusinnasta tulee vaativampi",
    "OPTION_B": "Sitä saa pienentää tilan säästämiseksi",
    "OPTION_C": "Sitä ei saa koskaan muuttaa",
    "OPTION_D": "Sitä saa muuttaa vain, jos kaikki urheilijat suostuvat siihen",
    "EXPLANATION": "Kilpailusääntöjen artikla 344 määrää, ettei sarjaesteen osaesteiden välistä etäisyyttä saa koskaan muuttaa uusinnassa.",
}

FIXES["jump-offs/fi-jof-0061-v1.txt"] = {
    "STEM": "Millaisia ovat ne kaksi lisäestettä, jotka kilpailusääntöjen artiklan 218.2.7 mukaan saa lisätä uusintaan?",
    "OPTION_A": "Vain pystyesteitä",
    "OPTION_B": "Kaksi pituusestettä, kaksi pystyestettä tai yksi kumpaakin",
    "OPTION_C": "Vain vesihautoja",
    "OPTION_D": "Vain sarjaesteitä",
    "EXPLANATION": "Kilpailusääntöjen artiklassa 218.2.7.1 määrätään, että kaksi lisäestettä voivat olla joko kaksi pituusestettä, kaksi pystyestettä tai yksi pituuseste ja yksi pystyeste.",
}

FIXES["jump-offs/fi-jof-0061-v2.txt"] = {
    "STEM": "Jos edelliseen kierrokseen kuulunut pystyeste hypätään uusinnassa vastakkaisesta suunnasta, miten se otetaan huomioon kilpailusääntöjen artiklan 218.2.7.1 mukaan?",
    "OPTION_A": "Sitä ei lasketa esteeksi",
    "OPTION_B": "Se lasketaan yhdeksi kahdesta sallitusta lisäesteestä",
    "OPTION_C": "Se lasketaan sarjaesteeksi",
    "OPTION_D": "Sen hyppääminen ei ole sallittua",
    "EXPLANATION": "Kilpailusääntöjen artiklan 344 mukaan este, joka on kuulunut edelliseen kierrokseen tai edellisiin kierroksiin ja joka hypätään uusinnassa vastakkaisesta suunnasta, lasketaan yhdeksi kahdesta sallitusta lisäesteestä.",
}

FIXES["jump-offs/fi-jof-0061.txt"] = {
    "STEM": "Kuinka monta lisäestettä uusintaradalle saa lisätä?",
    "OPTION_A": "Yhden",
    "OPTION_B": "Kaksi",
    "OPTION_C": "Kolme",
    "OPTION_D": "Ei yhtään",
    "EXPLANATION": "Kilpailusääntöjen artikla 344 määrää, että uusintaradalle saa lisätä enintään kaksi lisäestettä.",
}

FIXES["jump-offs/fi-jof-0062-v1.txt"] = {
    "STEM": "Miten sijoittuu urheilija, jonka suoritus uusinnassa hylätään, kilpailusääntöjen artiklan 218.3.1 mukaan?",
    "OPTION_A": "Ensimmäiseksi",
    "OPTION_B": "Tasan viimeiseksi kaikkien uusinnan suorittaneiden jälkeen",
    "OPTION_C": "Perusradalla saavuttamansa ajan mukaan",
    "OPTION_D": "Häntä ei sijoiteta lainkaan",
    "EXPLANATION": "Kilpailusääntöjen artikla 344 määrää, että hylkääminen, keskeyttäminen tai luvallinen luopuminen sijoittaa urheilijan kyseisellä kierroksella tasan viimeiseksi kaikkien kierroksen suorittaneiden jälkeen.",
}

FIXES["jump-offs/fi-jof-0062-v2.txt"] = {
    "STEM": "Urheilija keskeyttää uusinnan ilman tuomariston lupaa. Mihin hänet sijoitetaan kilpailusääntöjen artiklan 218.3.2 mukaan?",
    "OPTION_A": "Tasan ensimmäiseksi",
    "OPTION_B": "Niiden urheilijoiden jälkeen, jotka ovat luopuneet luvallisesti, keskeyttäneet tai tulleet hylätyiksi",
    "OPTION_C": "Häntä ei sijoiteta lainkaan",
    "OPTION_D": "Tasan toiseksi viimeiseksi keskeyttäneiden joukossa",
    "EXPLANATION": "Kilpailusääntöjen artiklassa 218.3.2 todetaan, että ilman lupaa keskeyttänyt urheilija sijoittuu niiden urheilijoiden jälkeen, jotka ovat luopuneet luvallisesti, keskeyttäneet tai tulleet hylätyiksi uusinnassa.",
}

FIXES["jump-offs/fi-jof-0062-v3.txt"] = {
    "STEM": "Miten Nations Cup -kilpailussa toiselta kierrokselta luopuva joukkue sijoittuu?",
    "OPTION_A": "Tasan viimeiseksi toisella kierroksella",
    "OPTION_B": "Ensimmäisellä kierroksella saamiensa virhepisteiden mukaan",
    "OPTION_C": "Kolikonheiton perusteella",
    "OPTION_D": "Alustavan sijoituksensa mukaan",
    "EXPLANATION": "Kilpailusääntöjen artiklan 344 mukaan joukkue, joka luopuu Nations Cup -kilpailun toiselta kierrokselta, sijoittuu ensimmäisellä kierroksella saamiensa virhepisteiden mukaan.",
}

FIXES["jump-offs/fi-jof-0062.txt"] = {
    "STEM": "Urheilija keskeyttää uusinnan tuomariston luvalla. Mihin hänet sijoitetaan?",
    "OPTION_A": "Tasan samalle sijalle kaikkien muiden keskeyttäneiden kanssa",
    "OPTION_B": "Tasan viimeiseksi uusinnassa kaikkien kierroksen suorittaneiden urheilijoiden jälkeen",
    "OPTION_C": "Hän säilyttää perusradan sijoituksensa",
    "OPTION_D": "Hänet suljetaan kilpailusta",
    "EXPLANATION": "Kilpailusääntöjen artiklan 344 mukaan urheilija, joka keskeyttää, tulee hylätyksi tai luopuu luvallisesti uusinnasta, toiselta kierrokselta tai voittokierrokselta, sijoittuu kyseisellä kierroksella tasan viimeiseksi kaikkien kierroksen suorittaneiden urheilijoiden jälkeen.",
}

FIXES["jump-offs/fi-jof-0063-v1.txt"] = {
    "STEM": "Miten Longines Ranking -kilpailun uusinnan lähtöjärjestys voidaan kilpailusääntöjen artiklan 218.1.9 mukaan määrätä?",
    "OPTION_A": "Aakkosjärjestykseen urheilijoiden sukunimen mukaan",
    "OPTION_B": "Edellisen kierroksen aikojen käänteiseen järjestykseen",
    "OPTION_C": "Arvonnalla",
    "OPTION_D": "Kansalaisuuden mukaan",
    "EXPLANATION": "Kilpailusääntöjen artikla 344 sallii sen, että Longines Ranking -kilpailun uusinnan lähtöjärjestys määräytyy urheilijoiden edellisen kierroksen aikojen käänteisessä järjestyksessä, jos kilpailukutsussa on niin määrätty.",
}

FIXES["jump-offs/fi-jof-0063-v2.txt"] = {
    "STEM": "Jos Longines Ranking -kilpailun kilpailukutsussa ei mainita uusinnan lähtöjärjestystä, mitä kilpailusääntöjen artiklan 218.1.9 mukaan sovelletaan?",
    "OPTION_A": "Aikojen käänteistä järjestystä",
    "OPTION_B": "Samaa järjestystä kuin edellisellä kierroksella",
    "OPTION_C": "Kilpailupäivänä suoritettavaa arvontaa",
    "OPTION_D": "Järjestystä, jossa nopein lähtee viimeisenä",
    "EXPLANATION": "Kilpailusääntöjen artiklassa 218.1.9 todetaan, että ellei kilpailukutsussa ole toisin määrätty, lähtöjärjestys on sama kuin edellisellä kierroksella.",
}

FIXES["jump-offs/fi-jof-0063.txt"] = {
    "STEM": "Mikä on uusinnan oletusarvoinen lähtöjärjestys?",
    "OPTION_A": "Perusradan sijoitusten käänteinen järjestys",
    "OPTION_B": "Sama kuin edellisen kierroksen lähtöjärjestys",
    "OPTION_C": "Arvonnalla määräytyvä järjestys",
    "OPTION_D": "Järjestys, jossa perusradan nopein lähtee ensimmäisenä",
    "EXPLANATION": "Kilpailusääntöjen artiklassa 218.1.8 määrätään, että uusinnan lähtöjärjestyksen on pysyttävä samana kuin edellisellä kierroksella, ellei kilpailukutsussa tai kilpailusäännöissä ole toisin määrätty.",
}

# ---------------------------------------------------------------- obstacles

FIXES["obstacles/fi-obs-0008-v1.txt"] = {
    "STEM": "Puomin kannattimen vähimmäissyvyys on:",
    "EXPLANATION": "Kilpailusääntöjen artiklan 301 mukaan kannattimen syvyyden on oltava vähintään 18 mm.",
}

FIXES["obstacles/fi-obs-0008-v2.txt"] = {
    "STEM": "Mikä on puomin kannattimen suurin sallittu syvyys kilpailusääntöjen artiklan 232.3 mukaan?",
    "EXPLANATION": "Kilpailusääntöjen artiklassa 301 kannattimen enimmäissyvyydeksi määrätään 20 mm.",
}

FIXES["obstacles/fi-obs-0008-v3.txt"] = {
    "STEM": "Mikä seuraavista kannattimia koskevista väittämistä on oikein kilpailusääntöjen artiklan 232.3 mukaan?",
    "OPTION_A": "Kannattimet on kiinnitettävä niin, etteivät puomit pääse vierimään",
    "OPTION_B": "Kannattimen on sallittava puomin vieriminen, ja sen syvyyden on oltava 18–20 mm",
    "OPTION_C": "Syvyysrajoitukset eivät koske turvakannattimia",
    "OPTION_D": "Kannattimen syvyys mitataan esteen pylvään ulkopuolelta",
    "EXPLANATION": "Kilpailusääntöjen artikla 301 edellyttää, että puomi pääsee vierimään kannattimellaan, ja määrää kannattimen syvyydeksi vähintään 18 mm ja enintään 20 mm.",
}

FIXES["obstacles/fi-obs-0008.txt"] = {
    "STEM": "Mikä on puomeja ja muita esteen osia kannattavien kannattimien sallittu syvyys?",
    "EXPLANATION": "Kilpailusääntöjen artiklan 301 mukaan kannattimen syvyyden on oltava vähintään 18 mm ja enintään 20 mm.",
}

FIXES["obstacles/fi-obs-0009-v1.txt"] = {
    "STEM": "Mikä on esteiden suurin sallittu korkeus sisäkilpailuissa kilpailusääntöjen artiklan 233.1 mukaan?",
    "EXPLANATION": "Kilpailusääntöjen artikla 301 määrää, ettei esteiden korkeus sisäkilpailuissa saa koskaan ylittää 1,65 metriä lukuun ottamatta kuuden esteen kilpailuja ja Puissance-kilpailuja.",
}

FIXES["obstacles/fi-obs-0009-v2.txt"] = {
    "STEM": "Mikä on trippelin suurin sallittu leveys kilpailusääntöjen artiklan 233.1 mukaan?",
    "EXPLANATION": "Kilpailusääntöjen artikla 301 sallii trippelille 2,20 metrin enimmäisleveyden.",
}

FIXES["obstacles/fi-obs-0009-v3.txt"] = {
    "STEM": "Missä kilpailumuodoissa esteet saavat ylittää 1,70 metrin enimmäiskorkeuden?",
    "OPTION_A": "Derby-kilpailuissa",
    "OPTION_B": "Kuuden esteen kilpailuissa ja Puissance-kilpailuissa",
    "OPTION_C": "Nations Cup -kilpailuissa",
    "OPTION_D": "Vaikeutuvassa ratsastuksessa",
    "EXPLANATION": "Kilpailusääntöjen artikla 301 määrää, ettei mikään este saa ylittää 1,70 metriä lukuun ottamatta kuuden esteen kilpailuja ja Puissance-kilpailuja.",
}

FIXES["obstacles/fi-obs-0009.txt"] = {
    "STEM": "Mikä on esteiden enimmäiskorkeus tavallisissa ulkokilpailuissa?",
    "EXPLANATION": "Kilpailusääntöjen artikla 301 määrää, ettei esteen korkeus saa missään olosuhteissa ylittää 1,70 metriä lukuun ottamatta kuuden esteen kilpailuja ja Puissance-kilpailuja.",
}

FIXES["obstacles/fi-obs-0010-v1.txt"] = {
    "STEM": "Kilpailukutsussa esteiden enimmäiskorkeudeksi on ilmoitettu 1,50 m. Kuinka korkean esteen radalle saa kilpailusääntöjen artiklan 233.2.2 mukaan todellisuudessa rakentaa?",
    "EXPLANATION": "Kilpailusääntöjen artikla 301 sallii enintään 3 cm:n ylityksen suunnitellusta korkeudesta, kun kyseinen korkeus on vähintään 1,45 m: 1,50 m + 0,03 m = 1,53 m.",
}

FIXES["obstacles/fi-obs-0010-v2.txt"] = {
    "STEM": "Kilpailusääntöjen artiklan 233.2.2 mukainen oikeus ylittää suunniteltu korkeus enintään 3 cm:llä koskee vain luokkia, joiden suunniteltu enimmäiskorkeus on vähintään:",
    "EXPLANATION": "Kilpailusääntöjen artiklan 301 mukaan 3 cm:n ylitys on sallittu vain kilpailuissa, joiden kilpailukutsussa ilmoitettu enimmäiskorkeus on vähintään 1,45 m.",
}

FIXES["obstacles/fi-obs-0010-v3.txt"] = {
    "STEM": "Kuka toimihenkilö voi päättää suunnitellun estekorkeuden ylittämisestä enintään 3 cm:llä luokassa, jonka enimmäiskorkeus on vähintään 1,45 m?",
    "OPTION_A": "Tuomariston puheenjohtaja",
    "OPTION_B": "Ratamestari",
    "OPTION_C": "Tekninen edustaja",
    "OPTION_D": "Joukkueenjohtaja",
    "EXPLANATION": "Kilpailusääntöjen artiklassa 233.2.2 määrätään, että korkeus voi ratamestarin harkinnan mukaan ylittää suunnitellun korkeuden enintään 3 cm:llä.",
}

FIXES["obstacles/fi-obs-0010.txt"] = {
    "STEM": "Kuinka paljon ratamestari saa ylittää suunnitellun korkeuden luokassa, jonka enimmäiskorkeus on vähintään 1,45 m?",
    "EXPLANATION": "Kilpailusääntöjen artikla 301 sallii luokissa, joiden suunniteltu enimmäiskorkeus on vähintään 1,45 m, esteiden korkeuden ylittää suunnitellun korkeuden ratamestarin harkinnan mukaan enintään 3 cm:llä.",
}

FIXES["obstacles/fi-obs-0011-v1.txt"] = {
    "STEM": "Kilpailusääntöjen artiklan 233.1 mukaan trippelin suurin sallittu leveys on:",
    "EXPLANATION": "Kilpailusääntöjen artikla 301 sallii trippelin enimmäisleveydeksi 2,20 m, kun taas muiden pituusesteiden enimmäisleveys on 2,00 m.",
}

FIXES["obstacles/fi-obs-0011-v2.txt"] = {
    "STEM": "Mikä on vesihaudan suurin sallittu leveys ponnahduselementti mukaan luettuna?",
    "EXPLANATION": "Kilpailusääntöjen artikla 301 määrää, ettei vesihaudan leveys saa ylittää 4,00 metriä ponnahduselementti mukaan luettuna.",
}

FIXES["obstacles/fi-obs-0011-v3.txt"] = {
    "STEM": "Tavallinen pituuseste rakennetaan 2,10 metrin levyiseksi. Onko tämä kilpailusääntöjen artiklan 233.1 mukaan sallittua?",
    "OPTION_A": "Kyllä, sillä kaikki enintään 2,20 metrin levyiset esteet ovat sallittuja",
    "OPTION_B": "Ei, sillä tavallisen pituusesteen enimmäisleveys on 2,00 metriä",
    "OPTION_C": "Kyllä, jos ratamestari hyväksyy sen",
    "OPTION_D": "Ei, sillä raja on 1,80 metriä",
    "EXPLANATION": "Kilpailusääntöjen artikla 301 rajoittaa esteiden leveyden 2,00 metriin lukuun ottamatta trippeleitä, joiden leveys saa olla enintään 2,20 metriä.",
}

FIXES["obstacles/fi-obs-0011.txt"] = {
    "STEM": "Mikä on suurin sallittu leveys esteellä, jonka ylittämiseen tarvitaan vain yksi hyppy?",
    "EXPLANATION": "Kilpailusääntöjen artiklan 301 mukaan esteen leveys saa olla enintään 2,00 m lukuun ottamatta trippeleitä, joiden leveys saa olla enintään 2,20 m.",
}

FIXES["obstacles/fi-obs-0012-v1.txt"] = {
    "STEM": "Kilpailusääntöjen artiklan 236.1.1 mukaan vesihaudassa on oltava ponnahduselementti, jonka vähimmäiskorkeus on:",
    "EXPLANATION": "Kilpailusääntöjen artikla 301 edellyttää ponnahduselementtiä, esimerkiksi risulaatikkoa tai pientä muuria, jonka korkeus on vähintään 40 cm ja enintään 50 cm.",
}

FIXES["obstacles/fi-obs-0012-v2.txt"] = {
    "STEM": "Mitä vaatimuksia vesihaudan pohjalle asetetaan, jos se on tehty betonista tai muusta kovasta materiaalista?",
    "OPTION_A": "Se on maalattava valkoiseksi",
    "OPTION_B": "Se on peitettävä pehmeämmällä ja liukumattomalla materiaalilla",
    "OPTION_C": "Sen on pysyttävä paljaana",
    "OPTION_D": "Sen on oltava vähintään 30 cm syvä",
    "EXPLANATION": "Kilpailusääntöjen artiklan 301 mukaan betonista tai muusta kovasta materiaalista tehty vesihaudan pohja on peitettävä pehmeämmällä ja liukumattomalla materiaalilla, esimerkiksi kookos- tai kumimatolla.",
}

FIXES["obstacles/fi-obs-0012-v3.txt"] = {
    "STEM": "Kuinka paljon vesihaudan etureunan leveyden on vähintään oltava haudan pituutta suurempi?",
    "EXPLANATION": "Kilpailusääntöjen artiklan 301 mukaan vesihaudan etureunan leveyden on oltava vähintään 30 prosenttia suurempi kuin haudan pituus.",
}

FIXES["obstacles/fi-obs-0012.txt"] = {
    "STEM": "Kuinka leveä esteen on vähintään oltava, jotta sitä voidaan kutsua vesiesteeksi?",
    "OPTION_D": "Yli 2,00 metriä",
    "EXPLANATION": "Kilpailusääntöjen artikla 301 määrää, että vesihaudan veden leveyden on oltava vähintään 2,00 metriä.",
}

FIXES["obstacles/fi-obs-0013-v1.txt"] = {
    "STEM": "Mitkä seuraavista ovat kilpailusääntöjen artiklan 236.1.3 mukaisia virheitä vesihaudalla?",
    "OPTION_A": "Jalka tai kenkä koskettaa rimaa ja jättää siihen jäljen",
    "OPTION_B": "Vuohisnivel jättää rimaan jäljen",
    "OPTION_C": "Hevonen koskettaa vettä yhdellä jalalla",
    "OPTION_D": "Ponnahduspuolen risulaatikko siirtyy paikaltaan",
    "EXPLANATION": "Kilpailusääntöjen artiklan 301 mukaan virhe syntyy, kun hevosen jalka tai kenkä koskettaa rimaa ja jättää siihen jäljen tai kun hevonen koskettaa vettä yhdellä tai useammalla jalalla. Vuohisnivelen tai suojan jättämä jälki ei ole virhe, eikä risulaatikon siirtyminen paikaltaan aiheuta virhettä.",
}

FIXES["obstacles/fi-obs-0013-v2.txt"] = {
    "STEM": "Mikä seuraavista EI ole kilpailusääntöjen artiklan 236.1.3 mukainen virhe vesihaudalla?",
    "OPTION_A": "Hevonen koskettaa vettä takajalallaan",
    "OPTION_B": "Vuohisnivel jättää rimaan jäljen",
    "OPTION_C": "Kenkä jättää rimaan jäljen",
    "OPTION_D": "Jalka koskettaa vettä",
    "EXPLANATION": "Kilpailusääntöjen artiklassa 301 todetaan nimenomaisesti, ettei vuohisnivelen tai suojan jättämä jälki ole virhe.",
}

FIXES["obstacles/fi-obs-0013-v3.txt"] = {
    "STEM": "Mitkä seuraavista lasketaan virheiksi vesihaudalla kilpailusääntöjen artiklan 236.1.3 mukaan?",
    "OPTION_A": "Riman koskettaminen jalalla tai kengällä siten, että siihen jää jälki",
    "OPTION_B": "Veden koskettaminen yhdellä tai useammalla jalalla",
    "OPTION_C": "Risulaatikon siirtyminen paikaltaan",
    "OPTION_D": "Lipun kaataminen",
    "EXPLANATION": "Kilpailusääntöjen artiklassa 301 luetellaan virheiksi ainoastaan riman koskettaminen niin, että siihen jää jälki, sekä veden koskettaminen. Risulaatikon siirtyminen paikaltaan (kohta 236.1.4) ja lipun kaataminen eivät ole tässä yhteydessä vesihaudan virheitä.",
}

FIXES["obstacles/fi-obs-0013.txt"] = {
    "STEM": "Milloin vesihaudalla syntyy virhe?",
    "OPTION_A": "Hevosen jalka koskettaa rimaa ja jättää siihen jäljen",
    "OPTION_B": "Vuohisnivel jättää rimaan jäljen",
    "OPTION_C": "Hevonen koskettaa vettä yhdellä tai useammalla jalalla",
    "OPTION_D": "Hevonen osuu ponnahduspuolen risulaatikkoon",
    "EXPLANATION": "Kilpailusääntöjen artikla 301 määrää, että virhe syntyy, kun jalka tai kenkä koskettaa rimaa ja jättää siihen jäljen tai kun hevonen koskettaa vettä yhdellä tai useammalla jalalla. Vuohisnivelen tai suojan jättämä jälki ei ole virhe, eikä risulaatikkoon osuminen aiheuta virhettä.",
}

FIXES["obstacles/fi-obs-0014-v1.txt"] = {
    "STEM": "Kuinka pitkiä puomeja vesihaudan ylle sijoitetussa pystyesteessä on kilpailusääntöjen artiklan 236.2 mukaan vähintään käytettävä?",
    "EXPLANATION": "Kilpailusääntöjen artiklan 301 mukaan vesihaudan ylle sijoitetussa pystyesteessä saa käyttää vain vähintään 3,50 metrin pituisia puomeja.",
}

FIXES["obstacles/fi-obs-0014-v2.txt"] = {
    "STEM": "Millaisena esteenä arvostellaan vesihaudan päälle sijoitettu pystyeste?",
    "OPTION_A": "Vesihautana",
    "OPTION_B": "Pystyesteenä",
    "OPTION_C": "Liverpool-esteenä",
    "OPTION_D": "Pituusesteenä",
    "EXPLANATION": "Kilpailusääntöjen artiklassa 301 todetaan nimenomaisesti, että vesihaudan päälle sijoitettu pystyeste arvostellaan pystyesteenä eikä vesihautana.",
}

FIXES["obstacles/fi-obs-0014-v3.txt"] = {
    "STEM": "Mikä on vesihaudan päälle sijoitetun pystyesteen ylimmän puomin kannattimen syvyys kilpailusääntöjen artiklan 236.2 mukaan?",
    "EXPLANATION": "Kilpailusääntöjen artiklassa 301 pystyesteen ylimmän puomin turvakannattimien syvyydeksi määrätään 18 mm.",
}

FIXES["obstacles/fi-obs-0014.txt"] = {
    "STEM": "Jos vesihauta ei täytä liitteen IV vaatimuksia, mitä sen päälle on sijoitettava?",
    "OPTION_A": "Pituuseste",
    "OPTION_B": "Enintään 1,50 metriä korkea pystyeste",
    "OPTION_C": "Trippeli",
    "OPTION_D": "Ei mitään, vaan vesi poistetaan",
    "EXPLANATION": "Kilpailusääntöjen artikla 301 edellyttää, että vesihaudan päälle sijoitetaan enintään 1,50 metriä korkea pystyeste, jos vesihauta ei täytä liitteen IV vaatimuksia.",
}

FIXES["obstacles/fi-obs-0015-v1.txt"] = {
    "STEM": "Miten sarjaesteen osaesteiden välinen etäisyys mitataan kilpailusääntöjen artiklan 237.1 mukaan?",
    "OPTION_A": "Esteen keskeltä seuraavan esteen keskelle",
    "OPTION_B": "Edellisen esteen alastulopuolen tyveltä seuraavan esteen ponnahduspuolen tyvelle",
    "OPTION_C": "Ensimmäisen esteen etureunasta toisen esteen etureunaan",
    "OPTION_D": "Kummankin esteen korkeimmasta kohdasta",
    "EXPLANATION": "Kilpailusääntöjen artiklassa 237.1 todetaan, että etäisyys mitataan edellisen esteen alastulopuolen tyveltä seuraavan esteen ponnahduspuolen tyvelle.",
}

FIXES["obstacles/fi-obs-0015-v2.txt"] = {
    "STEM": "Missä tilanteessa sarjaesteen osaesteiden välinen etäisyys saa olla alle seitsemän metriä?",
    "OPTION_A": "Arvostelun C mukaan ratsastettavissa nopeus- ja taitokilpailuissa",
    "OPTION_B": "Kaikissa sisäkilpailuissa",
    "OPTION_C": "Kun tuomaristo hyväksyy sen",
    "OPTION_D": "Puissance-kilpailuissa",
    "EXPLANATION": "Kilpailusääntöjen artiklassa 301 tehdään poikkeus arvostelun C mukaan ratsastettaviin nopeus- ja taitokilpailuihin sekä pysyviin kiinteisiin esteisiin, jotka edellyttävät kahta tai useampaa peräkkäistä hyppyä.",
}

FIXES["obstacles/fi-obs-0015-v3.txt"] = {
    "STEM": "Kaksoissarja rakennetaan siten, että sen osaesteiden välinen etäisyys on 6,5 metriä. Millainen etäisyys tämä on kilpailusääntöjen artiklan 237.1 mukaan?",
    "OPTION_A": "Sallittu",
    "OPTION_B": "Liian lyhyt",
    "OPTION_C": "Liian pitkä",
    "OPTION_D": "Sallittu vain sisäkilpailuissa",
    "EXPLANATION": "Kilpailusääntöjen artikla 301 edellyttää sarjaesteen osaesteiden väliltä vähintään seitsemän metrin etäisyyttä, joten 6,5 metriä on liian lyhyt.",
}

FIXES["obstacles/fi-obs-0015.txt"] = {
    "STEM": "Mikä on sarjaesteen osaesteiden välinen sallittu etäisyys?",
    "EXPLANATION": "Kilpailusääntöjen artiklassa 237.1 todetaan, että sarjaeste muodostuu kahdesta tai useammasta esteestä, joiden välinen etäisyys on vähintään seitsemän ja enintään 12 metriä.",
}

FIXES["obstacles/fi-obs-0016-v1.txt"] = {
    "STEM": "Ratsukko tekee ohituksen tavallisen avoimen kaksoissarjan toisella osaesteellä. Mitä sen on tehtävä?",
    "OPTION_A": "Hypättävä uudelleen vain toinen osaeste",
    "OPTION_B": "Hypättävä uudelleen molemmat osaesteet",
    "OPTION_C": "Hypättävä toisen osaesteen yli ja jatkettava matkaa",
    "OPTION_D": "Suoritus hylätään",
    "EXPLANATION": "Kilpailusääntöjen artikla 301 edellyttää, että ratsukko hyppää kiellon tai ohituksen jälkeen uudelleen kaikki sarjaesteen osaesteet.",
}

FIXES["obstacles/fi-obs-0016-v2.txt"] = {
    "STEM": "Millaisessa sarjaesteessä kaikkia osaesteitä ei tarvitse hypätä uudelleen kiellon tai ohituksen jälkeen?",
    "OPTION_A": "Avoimessa sarjaesteessä",
    "OPTION_B": "Umpinaisessa sarjaesteessä",
    "OPTION_C": "Kolmoissarjassa",
    "OPTION_D": "Kaksoissarjassa",
    "EXPLANATION": "Kilpailusääntöjen artikla 301 vapauttaa umpinaiset ja osittain umpinaiset sarjaesteet vaatimuksesta hypätä kaikki osaesteet uudelleen kiellon tai ohituksen jälkeen.",
}

FIXES["obstacles/fi-obs-0016-v3.txt"] = {
    "STEM": "Mitä ratsukon on tehtävä kuuden esteen kilpailussa kiellon jälkeen?",
    "OPTION_A": "Jatkettava rataa siltä esteeltä, jolla virhe tapahtui",
    "OPTION_B": "Hypättävä kaikki kuusi estettä uudelleen",
    "OPTION_C": "Ohitettava kyseinen este ja jatkettava matkaa",
    "OPTION_D": "Poistuttava kilpailualueelta",
    "EXPLANATION": "Kilpailusääntöjen artikla 301 edellyttää, että ratsukko jatkaa kuuden esteen kilpailussa kiellon tai ohituksen jälkeen rataa siltä esteeltä, jolla virhe tapahtui.",
}

FIXES["obstacles/fi-obs-0016.txt"] = {
    "STEM": "Mitä ratsukon on pääsäännön mukaan tehtävä, jos se tekee sarjaesteellä kiellon tai ohituksen?",
    "OPTION_A": "Hypättävä uudelleen vain se osaeste, jolla virhe tapahtui",
    "OPTION_B": "Hypättävä uudelleen kaikki sarjaesteen osaesteet",
    "OPTION_C": "Jatkettava seuraavalle esteelle",
    "OPTION_D": "Ratsastettava yksi ympyrä ja jatkettava seuraavasta osaesteestä",
    "EXPLANATION": "Kilpailusääntöjen artiklassa 237.3 määrätään, että kiellon tai ohituksen sattuessa ratsukon on hypättävä uudelleen kaikki sarjaesteen osaesteet, ellei kyseessä ole umpinainen tai osittain umpinainen sarjaeste tai kuuden esteen kilpailu.",
}

FIXES["obstacles/fi-obs-0017-v1.txt"] = {
    "STEM": "Mitä seuraa siitä, että ratsukko poistuu umpinaisesta sarjaesteestä väärään suuntaan tai siirtää sitä?",
    "OPTION_A": "Neljä virhepistettä",
    "OPTION_B": "Kuusi virhepistettä",
    "OPTION_C": "Suorituksen hylkääminen",
    "OPTION_D": "Varoitus",
    "EXPLANATION": "Kilpailusääntöjen artikla 301 määrää, että umpinaisesta sarjaesteestä poistuminen väärään suuntaan tai sarjaesteen siirtäminen johtaa suorituksen hylkäämiseen.",
}

FIXES["obstacles/fi-obs-0017-v2.txt"] = {
    "STEM": "Mikä erottaa umpinaisen sarjaesteen osittain umpinaisesta sarjaesteestä?",
    "OPTION_A": "Osaesteiden lukumäärä",
    "OPTION_B": "Se, onko sarjaeste kokonaan sellaisten sivujen ympäröimä, jotka voi ylittää vain hyppäämällä, vai onko vain yksi sivu suljettu",
    "OPTION_C": "Osaesteiden välinen etäisyys",
    "OPTION_D": "Vesihaudan käyttäminen sarjaesteessä",
    "EXPLANATION": "Kilpailusääntöjen artiklassa 301 täysin umpinaiseksi sarjaesteeksi määritellään sarjaeste, jonka ympäröivät sivut voi ylittää vain hyppäämällä, kun taas osittain umpinaisessa sarjaesteessä on yksi suljettu ja yksi avoin sivu.",
}

FIXES["obstacles/fi-obs-0017-v3.txt"] = {
    "STEM": "Mikä on umpinaisen sarjaesteen tunnusmerkki kilpailusääntöjen artiklan 238.1 mukaan?",
    "OPTION_A": "Siinä on vähintään kolme osaestettä",
    "OPTION_B": "Sen sivut voi ylittää vain hyppäämällä",
    "OPTION_C": "Sen jokainen osaeste on merkitty punaisella ja valkoisella lipulla",
    "OPTION_D": "Ratsukko voi palata radalle viimeisen osaesteen lippujen välistä",
    "EXPLANATION": "Kilpailusääntöjen artiklassa 301 umpinaiseksi sarjaesteeksi määritellään sarjaeste, jonka sivut voi ylittää vain hyppäämällä.",
}

FIXES["obstacles/fi-obs-0017.txt"] = {
    "STEM": "Millainen on umpinainen sarjaeste?",
    "OPTION_A": "Sarjaeste, jossa on liput vain ensimmäisellä ja viimeisellä osaesteellä",
    "OPTION_B": "Sarjaeste, jonka ympäröivät sivut voi ylittää vain hyppäämällä",
    "OPTION_C": "Sarjaeste, jonka osaesteet ovat niin lähellä toisiaan, että ne muodostavat yhden kokonaisuuden",
    "OPTION_D": "Sarjaeste, jossa saa olla enintään kaksi osaestettä",
    "EXPLANATION": "Kilpailusääntöjen artiklassa 301 täysin umpinaiseksi sarjaesteeksi määritellään sarjaeste, jonka ympäröivät sivut voi ylittää vain hyppäämällä. Tällaisia ovat esimerkiksi in and out -este, karsina sekä neliön tai kuusikulmion muotoinen este.",
}

FIXES["obstacles/fi-obs-0018-v1.txt"] = {
    "STEM": "Mikä vaikutus jokeriesteen hyppäämisellä on vaikeutuvassa ratsastuksessa?",
    "OPTION_A": "Se vähentää aikavirhepisteitä",
    "OPTION_B": "Siitä saa enemmän pisteitä kuin vaihtoehtoisesta tavallisesta esteestä",
    "OPTION_C": "Se poistaa aiemmat virheet",
    "OPTION_D": "Se oikeuttaa välittömään uusintasuoritukseen",
    "EXPLANATION": "Kilpailusääntöjen artiklassa 240.3 todetaan, että ratsukko saa enemmän pisteitä, jos se hyppää jokeriesteen vaihtoehtoisen tavallisen esteen sijasta.",
}

FIXES["obstacles/fi-obs-0018-v2.txt"] = {
    "STEM": "Mikä seuraavista jokeriestettä koskevista väittämistä on oikein kilpailusääntöjen artiklan 240.3 mukaan?",
    "OPTION_A": "Se on pakollinen kaikissa erikoisluokissa",
    "OPTION_B": "Sen on aina oltava radan ensimmäinen este",
    "OPTION_C": "Se on vapaaehtoinen, ja sitä saa käyttää vain vaikeutuvassa ratsastuksessa",
    "OPTION_D": "Se on eräänlainen vesieste",
    "EXPLANATION": "Kilpailusääntöjen artiklassa 301 jokerieste määritellään vaikeaksi vapaaehtoiseksi esteeksi, joka on sallittu vain vaikeutuvassa ratsastuksessa.",
}

FIXES["obstacles/fi-obs-0018-v3.txt"] = {
    "STEM": "Millä periaatteella jokeriesteet on suunniteltava kilpailusääntöjen artiklan 240.3 mukaan?",
    "OPTION_A": "Niin korkeiksi kuin teknisesti on mahdollista",
    "OPTION_B": "Hevosystävällisyyttä ja reiluutta noudattaen",
    "OPTION_C": "Täysin muiden esteiden kaltaisiksi",
    "OPTION_D": "Ilman lippuja",
    "EXPLANATION": "Kilpailusääntöjen artiklassa 301 todetaan, että jokeriesteet on suunniteltava hevosystävällisyyttä ja reilun kilpailun periaatetta noudattaen.",
}

FIXES["obstacles/fi-obs-0018.txt"] = {
    "STEM": "Millaisessa kilpailussa jokeriestettä saa käyttää?",
    "OPTION_A": "Kaikissa Grand Prix -kilpailuissa",
    "OPTION_B": "Vain vaikeutuvassa ratsastuksessa",
    "OPTION_C": "Nations Cup -kilpailussa",
    "OPTION_D": "Puissance-kilpailussa",
    "EXPLANATION": "Kilpailusääntöjen artiklassa 240.3 todetaan, että jokerieste on vaikea vapaaehtoinen este, jota saa käyttää vain vaikeutuvassa ratsastuksessa.",
}


def main():
    checked = 0
    changed = 0
    problems = []

    for rel, fields in sorted(FIXES.items()):
        path = os.path.join(BASE, rel)
        if not os.path.exists(path):
            problems.append("PUUTTUU: %s" % rel)
            continue
        with open(path, "r", encoding="utf-8") as fh:
            lines = fh.read().split("\n")

        checked += 1
        out = []
        seen = set()
        file_changed = False
        for line in lines:
            if ": " in line or line.endswith(":"):
                key = line.split(":", 1)[0]
            else:
                key = None
            if key in fields:
                if key not in EDITABLE:
                    problems.append("EI-SALLITTU KENTTA: %s / %s" % (rel, key))
                    out.append(line)
                    continue
                seen.add(key)
                new_line = "%s: %s" % (key, fields[key])
                if new_line != line:
                    file_changed = True
                out.append(new_line)
            else:
                out.append(line)

        missing = set(fields) - seen
        if missing:
            problems.append("KENTTIA EI LOYTYNYT: %s -> %s" % (rel, sorted(missing)))

        if file_changed:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write("\n".join(out))
            changed += 1

    print("Tarkistettu: %d tiedostoa" % checked)
    print("Muutettu:    %d tiedostoa" % changed)
    for p in problems:
        print("HUOM: %s" % p)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
