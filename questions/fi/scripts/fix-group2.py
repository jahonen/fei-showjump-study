#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""fix-group2.py

Kieliasun korjaus (lukion 3. luokan oikeinkirjoitustaso) kolmen aihealueen
monivalintakysymyksiin:
  - competitors-horses
  - faults-during-course
  - fines-warnings-elimination-disqualification

Korjataan VAIN kentät STEM, OPTION_A..D ja EXPLANATION. Muut kentat
(ID, PARENT_ID, DOMAIN, ARTICLE, EDITION_REF, SOURCE_PAGE, TYPE, CORRECT,
STATUS, CREATED, VERIFIED_AGAINST_SOURCE) jaavat koskemattomiksi.

Terminologia yhtenaistetty Suomen Ratsastajainliiton Kilpailusaannot III
-teoksen kanssa: hylkaaminen, kilpailusta sulkeminen, tottelemattomuus,
kieltaytyminen, sivuun poikkeaminen, niskurointi, voltti, virhepiste,
enimmaisaika, aikaraja, verryttelyalue, kilpailukutsu, ratsukko, arvostelu A/C.
"""

import os
import sys

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "items")
BASE = os.path.normpath(BASE)

EDITABLE = ("STEM", "OPTION_A", "OPTION_B", "OPTION_C", "OPTION_D", "EXPLANATION")

FIXES = {
# ---------------------------------------------------------------- competitors-horses
"competitors-horses/fi-cah-0071.txt": {
 "EXPLANATION": "Esteratsastussääntöjen artiklan 333 mukaan pohjoisen pallonpuoliskon hevosten virallinen syntymäaika on 1. tammikuuta.",
},
"competitors-horses/fi-cah-0071-v1.txt": {
 "STEM": "Mikä on eteläisen pallonpuoliskon hevosten virallinen syntymäaika JR:n artiklan 202.1.1 mukaan?",
 "EXPLANATION": "Esteratsastussääntöjen artiklan 333 mukaan eteläisen pallonpuoliskon hevosten virallinen syntymäaika on 1. elokuuta.",
},
"competitors-horses/fi-cah-0071-v2.txt": {
 "STEM": "Eteläisellä pallonpuoliskolla syntynyt hevonen kilpailee pohjoisella pallonpuoliskolla. Minkä ikäluokan kilpailuissa sen annetaan yleensä kilpailla?",
 "OPTION_A": "Vuotta vanhempien hevosten luokassa",
 "OPTION_B": "Vuotta nuorempien hevosten luokassa",
 "OPTION_C": "Kaksi vuotta vanhempien hevosten luokassa",
 "OPTION_D": "Samanikäisten hevosten luokassa",
 "EXPLANATION": "Esteratsastussääntöjen artiklan 333 mukaan eteläisellä pallonpuoliskolla syntyneiden hevosten, jotka kilpailevat pohjoisella pallonpuoliskolla, annetaan kilpailla vuotta nuorempien hevosten luokissa.",
},
"competitors-horses/fi-cah-0071-v3.txt": {
 "STEM": "Pohjoisella pallonpuoliskolla syntynyt hevonen kilpailee eteläisellä pallonpuoliskolla. Minkä ikäluokan kilpailuissa se yleensä kilpailee JR:n artiklan 202.1.4 mukaan?",
 "OPTION_A": "Vuotta vanhempien hevosten luokassa",
 "OPTION_B": "Vuotta nuorempien hevosten luokassa",
 "OPTION_C": "Kaksi vuotta nuorempien hevosten luokassa",
 "OPTION_D": "Samanikäisten hevosten luokassa",
 "EXPLANATION": "Esteratsastussääntöjen artiklan 333 mukaan pohjoisella pallonpuoliskolla syntyneiden hevosten, jotka kilpailevat eteläisellä pallonpuoliskolla, annetaan kilpailla vuotta vanhempien hevosten luokissa.",
},
"competitors-horses/fi-cah-0072.txt": {
 "STEM": "Mitkä seuraavista vastaavat hevosten vähimmäisikää olympialaisissa, seniorien mannermestaruuskilpailuissa ja CSI3*–5*-kilpailuissa?",
 "OPTION_A": "Olympialaiset: yhdeksän vuotta",
 "OPTION_B": "Seniorien mannermestaruuskilpailut: kahdeksan vuotta",
 "OPTION_C": "CSI3*–5*: seitsemän vuotta",
 "OPTION_D": "CSI1*–2*: kuusi vuotta",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 202.2 hevosen vähimmäisiäksi määrätään yhdeksän vuotta olympialaisissa, maailmanmestaruuskilpailuissa ja FEI:n esteratsastuksen maailmancupin finaalissa, kahdeksan vuotta mannerkilpailuissa, seniorien mannermestaruuskilpailuissa ja alueellisissa kilpailuissa sekä seitsemän vuotta CSI3*–5*- ja CSIO3*–5*-kilpailuissa, FEI:n esteratsastuksen maailmancupin osakilpailuissa (finaalia lukuun ottamatta) ja nuorten ratsastajien sekä juniorien mannermestaruuskilpailuissa.",
},
"competitors-horses/fi-cah-0072-v1.txt": {
 "STEM": "Minkä ikäinen hevosen on vähintään oltava, jotta se voi kilpailla olympialaisissa JR:n artiklan 202.2 mukaan?",
 "OPTION_A": "Seitsemän vuotta",
 "OPTION_B": "Kahdeksan vuotta",
 "OPTION_C": "Yhdeksän vuotta",
 "OPTION_D": "Kymmenen vuotta",
 "EXPLANATION": "Esteratsastussääntöjen artikla 333 edellyttää, että hevonen on vähintään yhdeksänvuotias olympialaisissa, maailmanmestaruuskilpailuissa ja FEI:n esteratsastuksen maailmancupin finaalissa.",
},
"competitors-horses/fi-cah-0072-v2.txt": {
 "STEM": "Mikä on hevosen vähimmäisikä seniorien mannermestaruuskilpailuissa JR:n artiklan 202.2 mukaan?",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 333 hevosen vähimmäisiäksi seniorien mannermestaruuskilpailuissa määrätään kahdeksan vuotta.",
},
"competitors-horses/fi-cah-0072-v3.txt": {
 "STEM": "Mikä on hevosen vähimmäisikä yleensä CSI1*–2*-, CSIJ/CSIOJ-, CSICh/CSIOCh-, CSIP/CSIOP-, CSIV/CSIOV- ja CSIAm-kilpailuissa sekä poniratsastajien, lasten ja veteraanien mannermestaruuskilpailuissa?",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 202.2 näiden kilpailujen hevosen vähimmäisiäksi määrätään kuusi vuotta, paitsi jos esteiden korkeus on 1,40 metriä tai enemmän, jolloin vähimmäisikä on seitsemän vuotta.",
},
"competitors-horses/fi-cah-0073.txt": {
 "STEM": "Mikä on urheilijaa kohden sallittujen hevosten enimmäismäärä CSI- ja CSIO-kilpailuissa kilpailukutsun mukaan?",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 203.1.1 todetaan, että kilpailukutsussa on määriteltävä urheilijaa kohden sallittujen hevosten lukumäärä CSI- ja CSIO-kilpailuissa ja että hevosia saa olla enintään neljä.",
},
"competitors-horses/fi-cah-0073-v1.txt": {
 "STEM": "Kuinka monta hevosta urheilija saa ilmoittaa luokkaa kohden JR:n artiklan 203.1.1 mukaan, jos samana viikonloppuna järjestetään eri luokkien kilpailuja?",
 "OPTION_D": "Ei rajoitusta",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 203.1.1 määrätään, että jos samana viikonloppuna järjestetään eri luokkien kilpailuja, hevosia saa olla enintään neljä urheilijaa ja luokkaa kohden.",
},
"competitors-horses/fi-cah-0073-v2.txt": {
 "STEM": "Kilpailusääntöjen artiklan 203.1.1 mukaan kilpailukutsussa on määriteltävä urheilijaa kohden sallittujen hevosten lukumäärä, joka saa olla enintään:",
 "OPTION_A": "Kolme",
 "OPTION_B": "Neljä",
 "OPTION_C": "Viisi",
 "OPTION_D": "Kuusi",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 333 urheilijaa kohden sallittujen hevosten enimmäismääräksi CSI- ja CSIO-kilpailuissa määrätään neljä.",
},
"competitors-horses/fi-cah-0073-v3.txt": {
 "STEM": "Kuinka monella hevosella kilpailun järjestäjä voi sallia urheilijan ratsastaa CSIAm-kilpailussa?",
 "OPTION_A": "Vain yhdellä",
 "OPTION_B": "Enintään neljällä",
 "OPTION_C": "Useammalla kuin yhdellä hevosella kaikissa kilpailuissa",
 "OPTION_D": "Ei rajoitusta",
 "EXPLANATION": "Esteratsastussääntöjen artikla 333 ei koske CSIAm-kilpailuja, joissa järjestäjä voi sallia urheilijoiden ratsastaa useammalla kuin yhdellä hevosella kaikissa kilpailuissa.",
},
"competitors-horses/fi-cah-0074.txt": {
 "STEM": "Kuinka monella hevosella urheilija saa ratsastaa CSI- tai CSIO-kilpailun Grand Prix -kilpailussa tai, jos Grand Prix -kilpailua ei ole, kilpailussa, jossa on suurin palkintosumma?",
 "OPTION_A": "Yhdellä",
 "OPTION_B": "Kahdella",
 "OPTION_C": "Kolmella",
 "OPTION_D": "Ei rajoitusta",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 333 määrätään, että CSI- ja CSIO-kilpailuissa jokainen urheilija saa ratsastaa vain yhdellä hevosella Grand Prix -kilpailussa tai, jos Grand Prix -kilpailua ei ole, kilpailussa, jossa on suurin palkintosumma. Derby-kilpailussa urheilija saa ratsastaa useammalla kuin yhdellä hevosella.",
},
"competitors-horses/fi-cah-0074-v1.txt": {
 "STEM": "Missä kilpailussa urheilija saa yhden hevosen säännöstä huolimatta ratsastaa useammalla kuin yhdellä hevosella JR:n artiklan 203.2.1 mukaan?",
 "OPTION_A": "Nations Cup -kilpailussa",
 "OPTION_B": "Grand Prix -kilpailussa",
 "OPTION_C": "Derby-kilpailussa",
 "OPTION_D": "Vaikeutuvassa kilpailussa",
 "EXPLANATION": "Esteratsastussääntöjen artiklan 333 mukaan yhden hevosen sääntöä sovelletaan Grand Prix -kilpailuun tai suurimman palkintosumman kilpailuun, mutta Derby-kilpailussa urheilija saa ratsastaa useammalla kuin yhdellä hevosella.",
},
"competitors-horses/fi-cah-0074-v2.txt": {
 "STEM": "Mihin kilpailuun sovelletaan JR:n artiklan 203.2.1 mukaista sääntöä yhdestä hevosesta urheilijaa kohden, jos Grand Prix -kilpailua ei ole?",
 "OPTION_A": "Ensimmäiseen kilpailuun",
 "OPTION_B": "Kilpailuun, jossa on suurin palkintosumma",
 "OPTION_C": "Nations Cup -kilpailuun",
 "OPTION_D": "Vaikeutuvaan kilpailuun",
 "EXPLANATION": "Esteratsastussääntöjen artiklan 333 mukaan yhden hevosen sääntöä sovelletaan Grand Prix -kilpailuun tai, jos Grand Prix -kilpailua ei ole, kilpailuun, jossa on suurin palkintosumma.",
},
"competitors-horses/fi-cah-0074-v3.txt": {
 "STEM": "Artikla 203.2.2 sallii urheilijan ratsastaa kahdella hevosella CSI1*-, CSI2*- ja CSI3*-kilpailujen Grand Prix -kilpailussa vain, jos:",
 "OPTION_A": "Urheilija on sijoittunut sadan parhaan joukkoon",
 "OPTION_B": "Ilmoittautuneiden lähtijöiden määrä on enintään 50 prosenttia suunnitellusta lähtijämäärästä ja kilpailukutsu sallii tämän",
 "OPTION_C": "Järjestäjä ilmoittaa siitä kilpailun aikana",
 "OPTION_D": "Kyseessä on Nations Cup -kilpailu",
 "EXPLANATION": "Esteratsastussääntöjen artikla 333 sallii kaksi hevosta urheilijaa kohden Grand Prix -kilpailussa vain, jos ilmoittautuneiden lähtijöiden määrä on enintään 50 prosenttia suunnitellusta lähtijämäärästä ja kilpailukutsussa on mainittu tämä mahdollisuus.",
},
"competitors-horses/fi-cah-0075.txt": {
 "STEM": "Missä seuraavista kilpailuista urheilijat eivät saa kilpailla ennen sitä vuotta, jona he täyttävät 18 vuotta?",
 "OPTION_A": "Olympialaisissa",
 "OPTION_B": "CSI3*–CSI5*-kilpailujen Grand Prix -kilpailuissa",
 "OPTION_C": "CSI1*-kilpailussa, jonka esteiden korkeus on enintään 1,20 metriä",
 "OPTION_D": "Longines League of Nations™ -kilpailussa",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 205.1 luetellaan alle 18-vuotiailta urheilijoilta kiellettyinä olympialaiset, manner- ja alueelliset kilpailut, CSI3*–5*- ja CSIO1*–5*-kilpailujen Grand Prix, Nations Cup ja Longines League of Nations™, FEI Jumping World Cup™, voima- ja taitokilpailut, Derby sekä suurimman palkintosumman kilpailut. CSI1*-kilpailuja, joiden esteiden korkeus on 1,20 metriä, ei ole luettelossa.",
},
"competitors-horses/fi-cah-0075-v1.txt": {
 "STEM": "Minkä kilpailuluokkien Grand Prix -kilpailuihin alle 18-vuotiaat urheilijat eivät saa osallistua JR:n artiklan 205.1 mukaan?",
 "OPTION_A": "Vain CSI1*-kilpailujen",
 "OPTION_B": "CSI3*–CSI5*-kilpailujen",
 "OPTION_C": "Vain CSIAm-kilpailujen",
 "OPTION_D": "Kaikkien CSI-kilpailujen",
 "EXPLANATION": "Esteratsastussääntöjen artikla 333 kieltää alle 18-vuotiailta urheilijoilta osallistumisen CSI3*–CSI5*-kilpailujen Grand Prix -kilpailuihin.",
},
"competitors-horses/fi-cah-0075-v2.txt": {
 "STEM": "Mikä seuraavista väittämistä pitää paikkansa JR:n artiklan 205.1 mukaan?",
 "OPTION_A": "Alle 18-vuotiaat urheilijat saavat kilpailla Longines League of Nations™ -kilpailussa",
 "OPTION_B": "Alle 18-vuotiaat urheilijat saavat kilpailla olympialaisissa",
 "OPTION_C": "Alle 18-vuotiaat urheilijat eivät saa kilpailla voima- ja taitokilpailuissa",
 "OPTION_D": "Alle 18-vuotiaat urheilijat saavat kilpailla missä tahansa Nations Cup -kilpailussa",
 "EXPLANATION": "Esteratsastussääntöjen artikla 333 kieltää alle 18-vuotiailta urheilijoilta osallistumisen voima- ja taitokilpailuihin sekä olympialaisiin ja Longines League of Nations™ -kilpailuihin.",
},
"competitors-horses/fi-cah-0075-v3.txt": {
 "STEM": "Artiklassa 205.1 todetaan myös, että urheilijaa ei voida luokitella ammattilaiseksi ennen sitä vuotta, jona hän täyttää:",
 "OPTION_A": "16 vuotta",
 "OPTION_B": "17 vuotta",
 "OPTION_C": "18 vuotta",
 "OPTION_D": "21 vuotta",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 333 todetaan, että urheilijaa ei voida luokitella ammattilaiseksi ennen sitä vuotta, jona hän täyttää 18 vuotta.",
},
"competitors-horses/fi-cah-0076.txt": {
 "STEM": "Siitä vuodesta alkaen, jona urheilija täyttää 12 vuotta, hän voi osallistua CSI- ja CSIO1*–5*-kilpailuihin sekä CSIAm-luokkien A ja B kilpailuihin edellyttäen, että esteiden korkeus ensimmäisellä kierroksella ei ylitä:",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 205.2.2 määrätään, että urheilijat voivat siitä vuodesta alkaen, jona he täyttävät 12 vuotta, kilpailla CSI- ja CSIO1*–5*-kilpailuissa sekä CSIAm-luokkien A ja B kilpailuissa edellyttäen, että ensimmäisen kierroksen esteiden korkeus ei ylitä 1,30 metriä.",
},
"competitors-horses/fi-cah-0076-v1.txt": {
 "STEM": "Artiklan 205.2.3 mukaan urheilijat voivat siitä vuodesta alkaen, jona he täyttävät 14 vuotta, kilpailla kaikissa CSI1*-kilpailuissa sekä niissä CSI2*–CSI5*- ja CSIO1*–5*-kilpailuissa, joissa ensimmäisen kierroksen esteiden korkeus ei ylitä:",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 333 ensimmäisen kierroksen esteiden korkeusrajaksi määrätään 1,40 metriä niille urheilijoille, jotka ovat täyttäneet 14 vuotta.",
},
"competitors-horses/fi-cah-0076-v2.txt": {
 "STEM": "Siitä vuodesta alkaen, jona urheilijat täyttävät 16 vuotta, he voivat artiklan 205.2.4 mukaan kilpailla kaikissa CSI1*–CSI5*- ja CSIO1*–CSIO5*-kilpailuissa. Seniorien alueellisissa kilpailuissa ensimmäisen kierroksen esteiden korkeus ei kuitenkaan saa ylittää:",
 "EXPLANATION": "Esteratsastussääntöjen artikla 333 sallii urheilijoiden kilpailla siitä vuodesta alkaen, jona he täyttävät 16 vuotta, kaikissa CSI1*–5*- ja CSIO1*–5*-kilpailuissa sekä seniorien alueellisissa kilpailuissa edellyttäen, että ensimmäisen kierroksen esteiden korkeus ei ylitä seniorien alueellisissa kilpailuissa 1,45 metriä.",
},
"competitors-horses/fi-cah-0076-v3.txt": {
 "STEM": "Minkä iän täytettyään urheilijat voivat kansallisen liittonsa luvalla kilpailla seniorien kilpailuissa JR:n artiklan 205.2.1 mukaan?",
 "OPTION_A": "10 vuotta",
 "OPTION_B": "12 vuotta",
 "OPTION_C": "14 vuotta",
 "OPTION_D": "16 vuotta",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 205.2.1 todetaan, että urheilijat voivat kansallisen liittonsa nimenomaisella luvalla kilpailla seniorien kilpailuissa siitä vuodesta alkaen, jona he täyttävät 12 vuotta.",
},
"competitors-horses/fi-cah-0077.txt": {
 "STEM": "Urheilija voi kilpailla nuorena ratsastajana sen kalenterivuoden alusta, jona hän täyttää 16 vuotta, sen kalenterivuoden loppuun, jona hän täyttää:",
 "OPTION_A": "18 vuotta",
 "OPTION_B": "21 vuotta",
 "OPTION_C": "25 vuotta",
 "OPTION_D": "16 vuotta",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 205.3.2 todetaan, että urheilijat voivat kilpailla nuorina ratsastajina sen kalenterivuoden alusta, jona he täyttävät 16 vuotta, sen kalenterivuoden loppuun, jona he täyttävät 21 vuotta.",
},
"competitors-horses/fi-cah-0077-v1.txt": {
 "STEM": "Artiklan 205.3.3 mukaan urheilija voi kilpailla juniorina 14 vuoden iästä sen vuoden loppuun, jona hän täyttää:",
 "OPTION_A": "16 vuotta",
 "OPTION_B": "18 vuotta",
 "OPTION_C": "21 vuotta",
 "OPTION_D": "25 vuotta",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 205.3.3 todetaan, että urheilijat voivat kilpailla junioreiden kilpailuissa siitä vuodesta alkaen, jona he täyttävät 14 vuotta, sen vuoden loppuun, jona he täyttävät 18 vuotta.",
},
"competitors-horses/fi-cah-0077-v2.txt": {
 "STEM": "Artiklan 205.3.1 mukaan urheilija voi kilpailla U25-sarjassa 16 vuoden iästä sen vuoden loppuun, jona hän täyttää:",
 "OPTION_A": "21 vuotta",
 "OPTION_B": "23 vuotta",
 "OPTION_C": "25 vuotta",
 "OPTION_D": "30 vuotta",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 333 määrätään, että urheilijat voivat kilpailla U25-sarjassa siitä vuodesta alkaen, jona he täyttävät 16 vuotta, sen vuoden loppuun, jona he täyttävät 25 vuotta.",
},
"competitors-horses/fi-cah-0077-v3.txt": {
 "STEM": "Mikä artiklan 205.3.4 mukainen urheilijaluokka alkaa 45 vuoden iässä?",
 "OPTION_B": "Nuoret ratsastajat",
 "OPTION_C": "Veteraanit",
 "OPTION_D": "Amatöörit",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 333 todetaan, että urheilijat voivat kilpailla veteraanien sarjassa sen vuoden alusta, jona he täyttävät 45 vuotta.",
},
"competitors-horses/fi-cah-0078.txt": {
 "STEM": "Milloin asianmukaisesti kiinnitetyn suojapäähineen käyttö on pakollista?",
 "OPTION_A": "Vain esteitä hypättäessä",
 "OPTION_B": "Aina hevosen selässä ratsastettaessa",
 "OPTION_C": "Vain palkintojenjaon aikana",
 "OPTION_D": "Vain kilpailualueella",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 333 määrätään, että kaikkien on käytettävä asianmukaisesti kiinnitettyä suojapäähinettä aina hevosen selässä ratsastaessaan.",
},
"competitors-horses/fi-cah-0078-v1.txt": {
 "STEM": "Mitä urheilijan on tehtävä JR:n artiklan 207.1.2 mukaan, jos hänen suojapäähineensä leukahihna irtoaa suorituksen aikana?",
 "OPTION_A": "Jatkettava hyppäämistä",
 "OPTION_B": "Kiinnitettävä hihna välittömästi uudelleen",
 "OPTION_C": "Pysähdyttävä ja keskeytettävä suoritus",
 "OPTION_D": "Annettava merkki tuomaristolle",
 "EXPLANATION": "Esteratsastussääntöjen artikla 333 edellyttää, että urheilija kiinnittää leukahihnan välittömästi uudelleen, jos se irtoaa suorituksen aikana.",
},
"competitors-horses/fi-cah-0078-v2.txt": {
 "STEM": "Pysäytetäänkö kello artiklan 207.1.2 mukaan, jos urheilija pysähtyy noutamaan tai kiinnittämään suojapäähineensä?",
 "OPTION_A": "Kyllä",
 "OPTION_B": "Ei",
 "OPTION_C": "Vain pyydettäessä",
 "OPTION_D": "Vain arvostelussa C",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 207.1.2 todetaan, että urheilijaa ei rangaista pysähtymisestä suojapäähineen noutamiseksi tai kiinnittämiseksi, mutta kelloa ei pysäytetä.",
},
"competitors-horses/fi-cah-0078-v3.txt": {
 "STEM": "Senioriurheilijat saavat artiklan 207.1.2 mukaan riisua suojapäähineensä palkintoja vastaanottaessaan, kansallislaulun aikana ja muissa seremonioissa. Mikä tämä määräys on?",
 "OPTION_A": "Kielto",
 "OPTION_B": "Poikkeus yleisestä säännöstä",
 "OPTION_C": "Velvollisuus",
 "OPTION_D": "Vain ulkona voimassa oleva lupa",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 207.1.2 mainitaan nimenomaisesti poikkeus, jonka mukaan senioriurheilijat saavat riisua suojapäähineensä seremonioiden aikana.",
},
"competitors-horses/fi-cah-0079.txt": {
 "STEM": "Minkä värinen urheilijan solmion tai kaulahuivin on oltava kilpailuissa?",
 "OPTION_A": "Musta",
 "OPTION_B": "Valkoinen",
 "OPTION_C": "Kansallisvärien mukainen",
 "OPTION_D": "Mikä tahansa takkiin sopiva väri",
 "EXPLANATION": "Esteratsastussääntöjen artikla 333 edellyttää valkoisen solmion tai kaulahuivin käyttöä kilpailuissa ja palkintojenjaossa.",
},
"competitors-horses/fi-cah-0079-v1.txt": {
 "STEM": "Kilpailusääntöjen artiklan 207.2.3.1 mukaan kilpailutakit voivat olla minkä värisiä tahansa, mutta niiden nappien on osoitettava:",
 "OPTION_A": "Sisäänpäin",
 "OPTION_B": "Ulospäin",
 "OPTION_C": "Mihin suuntaan tahansa",
 "OPTION_D": "Ulospäin vain hihansuissa",
 "EXPLANATION": "Kilpailusääntöjen artiklassa 207.2.3.1 määrätään, että kilpailutakit voivat olla minkä värisiä tahansa ja että niissä on oltava ulospäin osoittavat napit.",
},
"competitors-horses/fi-cah-0079-v2.txt": {
 "STEM": "Tuomaristo voi erittäin lämpimällä säällä sallia artiklan 207.2.3.4 mukaan, että urheilijat ratsastavat ilman takkia. Millaisia paitojen on tällöin oltava?",
 "OPTION_A": "Hihattomia",
 "OPTION_B": "Hihallisia, joko lyhyt- tai pitkähihaisia",
 "OPTION_C": "Vain valkoisia",
 "OPTION_D": "Mustakauluksisia",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 333 todetaan, että jos takkia ei sääolosuhteiden vuoksi käytetä, paidoissa on oltava hihat; sekä lyhyt- että pitkähihaiset paidat ovat sallittuja.",
},
"competitors-horses/fi-cah-0080.txt": {
 "STEM": "Minkä värisiä samanvärisellä kauluksella varustettuja takkeja ei saa rekisteröidä minkään kansallisen liiton viralliseksi takiksi?",
 "OPTION_A": "Mustia, punaisia, tummansinisiä ja vihreitä",
 "OPTION_B": "Valkoisia, keltaisia, pinkkejä ja oransseja",
 "OPTION_C": "Harmaita, ruskeita, violetteja ja sinisiä",
 "OPTION_D": "Kaikkia tummia värejä",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 207.2.4.2 määrätään, että mustia, punaisia, tummansinisiä ja vihreitä takkeja, joissa on samanvärinen kaulus, ei voi rekisteröidä minkään kansallisen liiton viralliseksi takiksi.",
},
"competitors-horses/fi-cah-0080-v1.txt": {
 "STEM": "Minkä suuruisen sakon tuomaristo määrää artiklan 207.2.4.3 mukaan jokaiselle sääntöä rikkovalle urheilijalle, jos joukkueen jäsenten takit eivät ole samanväriset?",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 333 määrätään, että urheilijalle, joka ei noudata joukkueen takin väriä koskevaa sääntöä, tuomaristo määrää 1 000 Sveitsin frangin sakon.",
},
"competitors-horses/fi-cah-0080-v2.txt": {
 "STEM": "Missä kilpailuissa urheilijoiden on käytettävä kansallisen liittonsa virallista kilpailuasua JR:n artiklan 207.2.4.1 mukaan?",
 "OPTION_A": "Kaikissa CSI1*-kilpailuissa",
 "OPTION_B": "CSIO-kilpailujen Nations Cup- ja Longines League of Nations™ -kilpailuissa, kaikissa manner- ja maailmanmestaruuskilpailujen vaiheissa sekä kansallisen olympiakomitean hyväksynnällä olympialaisissa ja alueellisissa kilpailuissa",
 "OPTION_C": "Vain olympialaisissa",
 "OPTION_D": "Vain palkintojenjaossa",
 "EXPLANATION": "Esteratsastussääntöjen artikla 333 edellyttää kansallisen liiton virallisen kilpailuasun käyttöä CSIO-kilpailujen Nations Cup- ja Longines League of Nations™ -kilpailuissa ja kaikissa manner- ja maailmanmestaruuskilpailujen vaiheissa sekä asianomaisen kansallisen olympiakomitean hyväksynnällä olympialaisissa ja alueellisissa kilpailuissa.",
},
"competitors-horses/fi-cah-0080-v3.txt": {
 "STEM": "Kenen ratkaistaviksi kansallisten liittojen virallisten takkien värejä koskevat kiistat annetaan artiklan 207.2.4.4 mukaan?",
 "OPTION_A": "FEI:n puheenjohtajan",
 "OPTION_B": "FEI:n pääsihteerin",
 "OPTION_C": "Tuomariston",
 "OPTION_D": "Joukkueenjohtajan",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 207.2.4.4 todetaan, että värejä koskevat kiistat annetaan FEI:n pääsihteerin ratkaistaviksi ja että hänen päätöksensä on lopullinen.",
},

# ---------------------------------------------------------------- faults-during-course
"faults-during-course/fi-fdc-0019.txt": {
 "STEM": "Mistä seuraavista virheistä tuomitaan artiklan 244.1 mukaan normaalisti virhepisteitä suorituksen aikana?",
 "OPTION_A": "Esteen pudottamisesta",
 "OPTION_B": "Hevosen ja/tai urheilijan kaatumisesta",
 "OPTION_C": "Enintään 45 sekuntia kestävästä voltin tekemisestä sivuun poikkeamisen tai kieltäytymisen jälkeen",
 "OPTION_D": "Enimmäisajan ylittämisestä",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 244.1 luetellaan virhepisteisiin johtavina virheinä esteen pudottaminen, vesihautaan astuminen, tottelemattomuus, väärä tie, kaatuminen, luvaton apu sekä enimmäisajan tai aikarajan ylittäminen. Artiklan 348 mukaan enintään 45 sekuntia kestävä voltin tekeminen sivuun poikkeamisen tai kieltäytymisen jälkeen ei ole tottelemattomuutta eikä siten virhe.",
},
"faults-during-course/fi-fdc-0019-v1.txt": {
 "STEM": "JR:n artiklan 244.1 mukaan vesihautaan astuminen kuuluu niiden virheiden luetteloon, joista:",
 "OPTION_A": "Seuraa aina hylkääminen",
 "OPTION_B": "Tuomitaan virhepisteitä, ellei toisin määrätä",
 "OPTION_C": "Ei tuomita virhepisteitä arvostelussa C",
 "OPTION_D": "Rangaistaan vain ensimmäisellä kierroksella",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 348 vesihautaan astuminen luetellaan niiden virheiden joukossa, joista tuomitaan virhepisteitä, ellei säännöissä toisin määrätä.",
},
"faults-during-course/fi-fdc-0019-v2.txt": {
 "STEM": "Mikä artiklassa 244.1 luetelluista virheistä koskee kilpailualueen ulkopuolelta saatua apua?",
 "OPTION_A": "Väärä tie",
 "OPTION_B": "Luvaton apu",
 "OPTION_C": "Kaatuminen",
 "OPTION_D": "Tottelemattomuus",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 348 luvaton apu mainitaan yhtenä virheenä, josta seuraa rangaistus.",
},
"faults-during-course/fi-fdc-0019-v3.txt": {
 "STEM": "Artiklaa 244.1 sovelletaan, ellei:",
 "OPTION_A": "Tuomaristo päätä toisin",
 "OPTION_B": "Kilpailukutsussa määrätä toisin",
 "OPTION_C": "Säännöissä määrätä toisin",
 "OPTION_D": "Urheilija ole juniori",
 "EXPLANATION": "Esteratsastussääntöjen artikla 348 alkaa sanoilla ”Ellei säännöissä toisin määrätä, seuraavista suorituksen aikana tapahtuvista virheistä tuomitaan virhepisteitä…”",
},
"faults-during-course/fi-fdc-0020.txt": {
 "STEM": "Esteen pudottaminen tapahtuu, kun este tai sen samassa pystytasossa oleva ylin osa putoaa ratsukon virheen vuoksi. Mitä tämä tarkoittaa pystyesteessä, joka koostuu kahdesta samaan pystytasoon asetetusta osasta?",
 "OPTION_A": "Virhe tuomitaan vain ylimmän osan putoamisesta",
 "OPTION_B": "Virhe tuomitaan vain, jos molemmat osat putoavat",
 "OPTION_C": "Alemman osan putoamisesta tuomitaan aina virhe",
 "OPTION_D": "Kumpaakaan osan putoamista ei tuomita pudottamiseksi",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 348 todetaan, että kun esteen osat on asetettu päällekkäin samaan pystytasoon, virhe tuomitaan vain ylimmän osan putoamisesta.",
},
"faults-during-course/fi-fdc-0020-v1.txt": {
 "STEM": "Levitetyssä esteessä on kaksi ylintä osaa, jotka eivät ole samassa pystytasossa. Toinen ylimmistä osista putoaa suorituksen aikana. Kuinka monta virhettä tuomitaan?",
 "OPTION_A": "Yksi",
 "OPTION_B": "Kaksi",
 "OPTION_C": "Yksi jokaisesta pudonneesta osasta",
 "OPTION_D": "Ei yhtään, elleivät molemmat osat putoa",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 348 määrätään, että kun yhdellä hypyllä ylitettävä este koostuu osista, jotka eivät ole samassa pystytasossa, yhden tai useamman ylimmän osan putoamisesta tuomitaan vain yksi virhe riippumatta pudonneiden osien lukumäärästä ja sijainnista.",
},
"faults-during-course/fi-fdc-0020-v2.txt": {
 "STEM": "Artiklan 245.1 mukaan esteen pudottamisesta tuomitaan virhe, kun esteen osan ainakin toinen pää ei enää lepää tuen varassa. Milloin tätä sääntöä sovelletaan?",
 "OPTION_A": "Vain suorituksen aikana",
 "OPTION_B": "Lähtö- ja maalilinjan välillä, viimeistä estettä lukuun ottamatta",
 "OPTION_C": "Vain pystyesteisiin",
 "OPTION_D": "Vain, jos urheilija myöntää virheen",
 "EXPLANATION": "Artiklassa 245.2 määrätään, että esteen pudottaminen tuomitaan virheeksi lähtö- ja maalilinjan välillä; viimeisen esteen osalta virhe tuomitaan myös silloin, kun este putoaa maalilinjan ylittämisen jälkeen mutta ennen kuin ratsukko on poistunut radalta.",
},
"faults-during-course/fi-fdc-0020-v3.txt": {
 "STEM": "Mikä seuraavista tuomitaan artiklan 245.1 mukaan esteen pudottamiseksi?",
 "OPTION_A": "Esteen täytteen kaataminen",
 "OPTION_B": "Umpinaisen sarjaesteen siirtäminen pois paikaltaan",
 "OPTION_C": "Lipun kaataminen hyppäämisen yhteydessä",
 "OPTION_D": "Koko esteen tai sen ylimmän osan kaataminen",
 "EXPLANATION": "Artiklassa 245.1.1 todetaan, että esteen pudottaminen tapahtuu, kun este tai sen samassa pystytasossa oleva ylin osa putoaa ratsukon virheen vuoksi. Artiklan 348 mukaan virhettä ei tuomita esteen täytteen kaatamisesta (245.5.4), umpinaisen sarjaesteen siirtämisestä pois paikaltaan (mistä seuraa hylkääminen) eikä lipun kaatamisesta hypyn aikana (245.5.2).",
},
"faults-during-course/fi-fdc-0021.txt": {
 "STEM": "Mitkä seuraavista katsotaan artiklan 246.1 mukaan tottelemattomuudeksi?",
 "OPTION_A": "Kieltäytyminen",
 "OPTION_B": "Sivuun poikkeaminen",
 "OPTION_C": "Yksi voltti 30 sekunnin ajan uuden hyppy-yrityksen tekemiseksi kieltäytymisen jälkeen",
 "OPTION_D": "Niskurointi",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 348 tottelemattomuudeksi luetellaan kieltäytyminen, sivuun poikkeaminen, niskurointi ja voltin tekeminen. Enintään 45 sekunnin ajan tehdyt voltit sivuun poikkeamisen tai kieltäytymisen jälkeen eivät kuitenkaan ole tottelemattomuutta.",
},
"faults-during-course/fi-fdc-0021-v1.txt": {
 "STEM": "Artiklan 246.1.4 mukaan voltti tai useampi voltti on tottelemattomuutta. Missä tapauksessa sitä ei tuomita tottelemattomuudeksi?",
 "OPTION_A": "Kun voltti tehdään verryttelyalueella",
 "OPTION_B": "Kun voltteja tehdään enintään 45 sekunnin ajan kieltäytymisen tai sivuun poikkeamisen jälkeen",
 "OPTION_C": "Kun urheilija kiertää viimeksi hyppäämänsä esteen",
 "OPTION_D": "Kun voltti tehdään stewardin pyynnöstä",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 348 todetaan, että enintään 45 sekunnin ajan tehdyt voltit sivuun poikkeamisen jälkeen tai uuden hyppy-yrityksen tekemiseksi kieltäytymisen jälkeen eivät ole tottelemattomuutta.",
},
"faults-during-course/fi-fdc-0021-v2.txt": {
 "STEM": "Mitä seuraavista ei luetella artiklassa 246.1 tottelemattomuudeksi?",
 "OPTION_A": "Kieltäytymistä",
 "OPTION_B": "Sivuun poikkeamista",
 "OPTION_C": "Kaatumista",
 "OPTION_D": "Niskurointia",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 348 tottelemattomuudeksi luetellaan kieltäytyminen, sivuun poikkeaminen, niskurointi ja voltin tekeminen. Kaatumista käsitellään erikseen artiklassa 248, eikä se ole tottelemattomuutta.",
},
"faults-during-course/fi-fdc-0021-v3.txt": {
 "STEM": "Artiklan 246.3.1 mukaan sivuun poikkeaminen tapahtuu, kun hevonen:",
 "OPTION_A": "Pysähtyy esteen eteen ja astuu taaksepäin",
 "OPTION_B": "Riistäytyy urheilijan hallinnasta ja sivuuttaa esteen, joka sen on hypättävä",
 "OPTION_C": "Astuu taaksepäin lähtölinjalla",
 "OPTION_D": "Hyppää esteen kahden punaisen lipun välistä",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 348 sivuun poikkeamiseksi määritellään se, että hevonen riistäytyy urheilijan hallinnasta ja sivuuttaa esteen, joka sen on hypättävä, tai pakollisen kääntöpaikan, jonka ohi sen on kuljettava.",
},
"faults-during-course/fi-fdc-0022.txt": {
 "STEM": "Hevonen pysähtyy esteen eteen astumatta taaksepäin ja pudottamatta estettä ja hyppää sitten välittömästi paikaltaan esteen yli. Onko tämä kieltäytyminen?",
 "OPTION_A": "Kyllä, mikä tahansa pysähdys on kieltäytyminen",
 "OPTION_B": "Ei, kyse ei ole kieltäytymisestä, jos hevonen hyppää välittömästi paikaltaan",
 "OPTION_C": "Kyllä, mutta vain arvostelussa A",
 "OPTION_D": "Ei, ellei hevonen astu taaksepäin",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 348 todetaan, ettei kieltäytymisenä pidetä sitä, että hevonen pysähtyy esteen eteen astumatta taaksepäin ja pudottamatta estettä ja hyppää välittömästi sen jälkeen paikaltaan esteen yli.",
},
"faults-during-course/fi-fdc-0022-v1.txt": {
 "STEM": "Milloin esteen eteen pysähtymisestä tulee artiklan 246.2.2 mukaan kieltäytyminen?",
 "OPTION_A": "Jos hevonen astuu taaksepäin, vaikka vain yhden askeleen",
 "OPTION_B": "Jos hevonen laskee päänsä",
 "OPTION_C": "Jos pysähdys kestää yli 10 sekuntia",
 "OPTION_D": "Jos urheilija käyttää raippaa",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 348 määrätään, että jos pysähdys on pitkä tai hevonen astuu taaksepäin joko tahallisesti tai tahattomasti, vaikka vain yhden askeleen, se tuomitaan kieltäytymiseksi.",
},
"faults-during-course/fi-fdc-0022-v2.txt": {
 "STEM": "Hevonen pysähtyy esteen eteen, astuu yhden askeleen taaksepäin ja hyppää sitten esteen yli. Mitä tämä on artiklan 246.2.2 mukaan?",
 "OPTION_A": "Ei virhe",
 "OPTION_B": "Kieltäytyminen",
 "OPTION_C": "Sivuun poikkeaminen",
 "OPTION_D": "Kaatuminen",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 348 todetaan, että jos hevonen astuu taaksepäin, vaikka vain yhden askeleen, pysähdys tuomitaan kieltäytymiseksi.",
},
"faults-during-course/fi-fdc-0022-v3.txt": {
 "STEM": "Mitä on artiklan 246.2.2 mukaan se, että hevonen pysähtyy esteen eteen ja hyppää välittömästi paikaltaan astumatta taaksepäin?",
 "OPTION_A": "Aina kieltäytymisenä tuomittava virhe",
 "OPTION_B": "Ei kieltäytyminen",
 "OPTION_C": "Esteen pudottamisena tuomittava virhe",
 "OPTION_D": "Tuomariston huomiotta jättämä tapaus",
 "EXPLANATION": "Artiklassa 246.2.2 määrätään nimenomaisesti, ettei tällaista tilannetta pidetä kieltäytymisenä.",
},
"faults-during-course/fi-fdc-0023.txt": {
 "STEM": "Hevonen hyppää esteen kahden punaisen lipun välistä. Miten tämä tuomitaan?",
 "OPTION_A": "Esteen pudottamisena",
 "OPTION_B": "Sivuun poikkeamisena, ja este on hypättävä uudelleen oikein",
 "OPTION_C": "Kieltäytymisenä",
 "OPTION_D": "Virhettä ei tuomita",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 348 todetaan, että jos este hypätään kahden punaisen tai kahden valkoisen lipun välistä, estettä ei ole ylitetty oikein; ratsukolle tuomitaan sivuun poikkeaminen ja este on hypättävä uudelleen oikein.",
},
"faults-during-course/fi-fdc-0023-v1.txt": {
 "STEM": "Miten urheilijan on artiklan 246.3.3 mukaan toimittava, jos hevonen hyppää esteen kahden valkoisen lipun välistä?",
 "OPTION_A": "Jatkettava seuraavalle esteelle",
 "OPTION_B": "Palattava takaisin ja hypättävä este oikein",
 "OPTION_C": "Pysähdyttävä 45 sekunniksi",
 "OPTION_D": "Katsottava este hypätyksi",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 348 kahden valkoisen tai kahden punaisen lipun välistä hyppäämistä käsitellään sivuun poikkeamisena, ja este on hypättävä uudelleen oikein.",
},
"faults-during-course/fi-fdc-0023-v2.txt": {
 "STEM": "Hevonen ohittaa hypättävän esteen oletetun jatkeen hyppäämättä estettä. Mitä tämä on artiklan 246.3 mukaan?",
 "OPTION_A": "Kieltäytyminen",
 "OPTION_B": "Sivuun poikkeaminen",
 "OPTION_C": "Kaatuminen",
 "OPTION_D": "Ei virhe",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 348 määrätään, että kyse on sivuun poikkeamisesta, kun hevonen tai mikä tahansa sen osa ohittaa hypättävän esteen oletetun jatkeen.",
},
"faults-during-course/fi-fdc-0023-v3.txt": {
 "STEM": "Minkä värisen lipun on oltava urheilijan oikealla puolella, kun este ylitetään oikein?",
 "OPTION_A": "Valkoisen",
 "OPTION_B": "Punaisen",
 "OPTION_C": "Sinisen",
 "OPTION_D": "Keltaisen",
 "EXPLANATION": "Esteratsastussääntöjen artiklan 348 mukaan ratsukon on ylitettävä este lippujen välistä siten, että punainen lippu on oikealla ja valkoinen lippu vasemmalla. Esteen hyppääminen kahden samanvärisen lipun välistä tuomitaan sivuun poikkeamiseksi.",
},
"faults-during-course/fi-fdc-0024.txt": {
 "STEM": "Mitä seuraa, jos hevonen niskuroi suorituksen aikana 45 sekuntia yhtäjaksoisesti?",
 "OPTION_A": "Ratsukolle tuomitaan 4 virhepistettä",
 "OPTION_B": "Urheilija saa varoituksen",
 "OPTION_C": "Ratsukon suoritus hylätään",
 "OPTION_D": "Kello pysäytetään, mutta suoritus jatkuu",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 348 määrätään, että jos hevonen niskuroi 45 sekuntia yhtäjaksoisesti, ratsukon suoritus hylätään.",
},
"faults-during-course/fi-fdc-0024-v1.txt": {
 "STEM": "Hevonen niskuroi 30 sekuntia ja jatkaa sen jälkeen eteenpäin. Mitä tästä seuraa artiklan 246.4.3 mukaan?",
 "OPTION_A": "Suorituksen hylkääminen",
 "OPTION_B": "Se tuomitaan kieltäytymiseksi",
 "OPTION_C": "Virhettä ei tuomita",
 "OPTION_D": "Urheilija saa varoituksen",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 348 todetaan, että alle 45 sekuntia kestävä niskurointi tuomitaan kieltäytymiseksi.",
},
"faults-during-course/fi-fdc-0024-v2.txt": {
 "STEM": "Miten artiklan 246.4.3 mukainen 45 sekunnin niskurointiaika mitataan?",
 "OPTION_A": "Lähtömerkistä maalilinjalle",
 "OPTION_B": "Yhtäjaksoisesti suorituksen aikana",
 "OPTION_C": "Vain ensimmäisellä esteellä",
 "OPTION_D": "Koko kilpailun ajalta",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 348 tarkoitetaan 45 yhtäjaksoista sekuntia suorituksen aikana, ei yhteen laskettua aikaa.",
},
"faults-during-course/fi-fdc-0025.txt": {
 "STEM": "Mitkä teot katsotaan artiklan 247.1 mukaan vääräksi tieksi?",
 "OPTION_A": "Pakollisen kääntöpaikan ohittamatta jättäminen",
 "OPTION_B": "Esteen hyppääminen väärässä järjestyksessä",
 "OPTION_C": "Esteen hyppääminen väärästä suunnasta",
 "OPTION_D": "Yksi voltti kieltäytymisen jälkeen uuden hyppy-yrityksen tekemiseksi",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 348 vääräksi tieksi katsotaan muun muassa pakollisen kääntöpaikan ohittamatta jättäminen, esteen hyppääminen väärässä järjestyksessä ja esteen hyppääminen väärästä suunnasta. Kieltäytymisen jälkeen tehtyyn volttiin sovelletaan artiklaa 246.1.4.",
},
"faults-during-course/fi-fdc-0025-v2.txt": {
 "STEM": "Mitä seuraa artiklan 247.3 mukaan väärästä tiestä, jota ei ole korjattu, esimerkiksi pakollisen kääntöpaikan ohittamatta jättämisestä?",
 "OPTION_A": "4 virhepistettä",
 "OPTION_B": "Suorituksen hylkääminen",
 "OPTION_C": "Varoitus",
 "OPTION_D": "Ei seurausta",
 "EXPLANATION": "Artiklassa 247.3 todetaan, että korjaamaton väärä tie johtaa suorituksen hylkäämiseen. Myös pakollisen kääntöpaikan ohittamatta jättäminen luetellaan artiklassa 263.4.8 pakollisena hylkäämisperusteena.",
},
"faults-during-course/fi-fdc-0025-v3.txt": {
 "STEM": "Mikä seuraavista ei ole artiklan 247.1 mukaan väärä tie?",
 "OPTION_A": "Pakollisen kääntöpaikan ohittamatta jättäminen",
 "OPTION_B": "Luokkaan kuulumattoman esteen hyppääminen",
 "OPTION_C": "20 sekunnin voltti sivuun poikkeamisen jälkeen",
 "OPTION_D": "Maalilinjan ylittämättä jättäminen lippujen välistä",
 "EXPLANATION": "Esteratsastussääntöjen artiklan 348 mukaan pakollisen kääntöpaikan ohittamatta jättäminen, luokkaan kuulumattoman esteen hyppääminen ja maalilinjan ylittämättä jättäminen lippujen välistä ovat kaikki väärä tie. Enintään 45 sekunnin ajan tehty voltti uuden hyppy-yrityksen tekemiseksi ei sen sijaan ole artiklan 348 mukaan tottelemattomuutta eikä siten väärä tie.",
},
"faults-during-course/fi-fdc-0026.txt": {
 "STEM": "Mitä seuraa artiklan 248.2.2.2 mukaan urheilijan ja/tai hevosen kaatumisesta kilpailusuorituksen aikana?",
 "OPTION_A": "4 virhepistettä",
 "OPTION_B": "6 virhepistettä",
 "OPTION_C": "Suorituksen hylkääminen",
 "OPTION_D": "Varoitus",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 348 todetaan, että kaatuminen kilpailualueella suorituksen aikana johtaa ratsukon suorituksen hylkäämiseen.",
},
"faults-during-course/fi-fdc-0026-v1.txt": {
 "STEM": "Mitä seuraa artiklan 248.2.2.2 mukaan kaatumisesta suorituksen aikana?",
 "OPTION_A": "4 virhepistettä",
 "OPTION_B": "Suorituksen hylkääminen",
 "OPTION_C": "Keltainen kortti",
 "OPTION_D": "Sakko",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 348 todetaan, että kaatuminen kilpailualueella suorituksen aikana johtaa ratsukon suorituksen hylkäämiseen.",
},
"faults-during-course/fi-fdc-0026-v2.txt": {
 "STEM": "Hevonen kaatuu maalilinjan ylittämisen jälkeen. Mitä tästä yleensä seuraa artiklan 248.2 mukaan?",
 "OPTION_A": "Suoritus hylätään silti",
 "OPTION_B": "Suoritusta ei hylätä",
 "OPTION_C": "Ratsukolle tuomitaan 4 virhepistettä",
 "OPTION_D": "Urheilija saa varoituksen",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 348 määrätään, että maalilinjan ylittämisen jälkeen tapahtunut kaatuminen ei johda suorituksen hylkäämiseen.",
},
"faults-during-course/fi-fdc-0027.txt": {
 "STEM": "Mitä pidetään yleensä luvattomana apuna suorituksen aikana?",
 "OPTION_A": "Tuomariston jäsenen antamaa keskeytysmerkkiä",
 "OPTION_B": "Sivullisen fyysistä puuttumista suoritukseen urheilijan tai hänen hevosensa auttamiseksi",
 "OPTION_C": "Valmentajan kilpailualueen ulkopuolelta huutamia ohjeita",
 "OPTION_D": "Kaikkea tuomariston hyväksymää apua",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 348 luvattomalla avulla tarkoitetaan kaikkea sivullisten fyysistä puuttumista suoritukseen lähtölinjan ylittämisen ja maalilinjan välillä urheilijan tai hänen hevosensa auttamiseksi riippumatta siitä, onko apua pyydetty. Luvaton apu suorituksen aikana johtaa suorituksen hylkäämiseen.",
},
"faults-during-course/fi-fdc-0027-v1.txt": {
 "STEM": "Mitä on artiklan 249.2 mukaan apu, jonka tuomaristo on poikkeuksellisissa olosuhteissa sallinut?",
 "OPTION_A": "Luvatonta apua",
 "OPTION_B": "Apua, jota ei pidetä luvattomana",
 "OPTION_C": "Aina hylkäämiseen johtavaa apua",
 "OPTION_D": "Huomiotta jätettävää apua",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 348 määrätään, että tuomaristo voi poikkeustapauksissa antaa urheilijalle luvan tulla kilpailualueelle jalan tai toisen henkilön taluttamana ilman, että tätä pidetään luvattomana apuna.",
},
"faults-during-course/fi-fdc-0027-v2.txt": {
 "STEM": "Mitä luvattomasta avusta yleensä seuraa suorituksen aikana artiklan 249.1 mukaan?",
 "OPTION_A": "4 virhepistettä",
 "OPTION_B": "Suorituksen hylkääminen",
 "OPTION_C": "Sakko",
 "OPTION_D": "Varoitus",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 348 todetaan, että luvattoman avun vastaanottaminen suorituksen aikana johtaa suorituksen hylkäämiseen.",
},

# ------------------------------- fines-warnings-elimination-disqualification
"fines-warnings-elimination-disqualification/fi-fwd-0043.txt": {
 "STEM": "Mikä on hylkäämisen yleinen vaikutus kilpailussa?",
 "OPTION_A": "Urheilija saa jatkaa, mutta hänelle tuomitaan neljä virhepistettä",
 "OPTION_B": "Urheilija ei saa jatkaa kyseisellä hevosella meneillään olevassa kilpailussa",
 "OPTION_C": "Urheilijalle määrätään 1 000 Sveitsin frangin sakko",
 "OPTION_D": "Urheilija sijoittuu viimeiseksi mutta säilyttää oikeuden osallistua myöhempiin kilpailuihin",
 "EXPLANATION": "Artiklassa 263.1 todetaan, että ellei säännöissä toisin määrätä, hylkääminen tarkoittaa, ettei urheilija saa jatkaa kyseisellä hevosella meneillään olevassa kilpailussa.",
},
"fines-warnings-elimination-disqualification/fi-fwd-0043-v1.txt": {
 "STEM": "Millainen hylkääminen voi artiklan 263.1 mukaan myös olla?",
 "OPTION_A": "FEI:n tuomioistuimeen valitettava",
 "OPTION_B": "Takautuva",
 "OPTION_C": "Urheilijan peruutettavissa",
 "OPTION_D": "Sakoksi muunnettava",
 "EXPLANATION": "Artiklassa 263.1 todetaan, että hylkääminen voi olla myös takautuva.",
},
"fines-warnings-elimination-disqualification/fi-fwd-0043-v3.txt": {
 "STEM": "Millä ehdolla urheilija saa hylkäämisen jälkeen hypätä yhden esteen?",
 "OPTION_A": "Este kuuluu meneillään olevan kilpailun rataan eikä hylkääminen johtunut kaatumisesta",
 "OPTION_B": "Tuomaristo antaa siihen suullisen luvan",
 "OPTION_C": "Kyse on vain ensimmäisestä esteestä",
 "OPTION_D": "Urheilija maksaa sakon",
 "EXPLANATION": "Artiklassa 263.3 määrätään, että urheilija saa hylkäämisen jälkeen tehdä yhden hyppy-yrityksen edellyttäen, että este kuuluu meneillään olevan kilpailun rataan eikä hylkääminen johtunut kaatumisesta.",
},
"fines-warnings-elimination-disqualification/fi-fwd-0044.txt": {
 "STEM": "Hevonen on tottelematon toisen kerran samalla suorituksella. Mitä siitä seuraa?",
 "OPTION_A": "Ratsukolle tuomitaan 4 virhepistettä",
 "OPTION_B": "Suorituksen hylkääminen",
 "OPTION_C": "Varoitus",
 "OPTION_D": "Kello pysäytetään 45 sekunniksi",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 346 todetaan, että toinen tottelemattomuus suorituksen aikana johtaa hylkäämiseen.",
},
"fines-warnings-elimination-disqualification/fi-fwd-0044-v1.txt": {
 "STEM": "Mikä tottelemattomuus johtaa artiklan 263.4.25 mukaan pakolliseen hylkäämiseen?",
 "OPTION_A": "Ensimmäinen",
 "OPTION_B": "Toinen",
 "OPTION_C": "Kolmas",
 "OPTION_D": "Neljäs",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 346 todetaan, että toinen tottelemattomuus suorituksen aikana johtaa hylkäämiseen.",
},
"fines-warnings-elimination-disqualification/fi-fwd-0044-v2.txt": {
 "STEM": "Urheilija saa samalla suorituksella ensin kieltäytymisen ja sitten sivuun poikkeamisen. Mitä tästä seuraa artiklan 263.4.25 mukaan?",
 "OPTION_A": "Ei seurausta",
 "OPTION_B": "4 virhepistettä",
 "OPTION_C": "Suorituksen hylkääminen",
 "OPTION_D": "Varoitus",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 346 määrätään, että toinen tottelemattomuus suorituksen aikana johtaa hylkäämiseen; sekä kieltäytyminen että sivuun poikkeaminen ovat tottelemattomuutta.",
},
"fines-warnings-elimination-disqualification/fi-fwd-0045.txt": {
 "STEM": "Hevonen niskuroi suorituksen aikana 45 sekuntia yhtäjaksoisesti. Mitä siitä seuraa?",
 "OPTION_A": "4 virhepistettä",
 "OPTION_B": "Varoitus",
 "OPTION_C": "Suorituksen hylkääminen",
 "OPTION_D": "Urheilijan on jatkettava lyhyen tauon jälkeen",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 346 määrätään, että jos hevonen niskuroi suorituksen aikana 45 sekuntia yhtäjaksoisesti, suoritus hylätään.",
},
"fines-warnings-elimination-disqualification/fi-fwd-0045-v1.txt": {
 "STEM": "Kuinka monta sekuntia yhtäjaksoisesti kestävä niskurointi suorituksen aikana johtaa artiklan 263.4.4 mukaan hylkäämiseen?",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 346 todetaan, että jos hevonen niskuroi suorituksen aikana 45 sekuntia yhtäjaksoisesti, suoritus hylätään.",
},
"fines-warnings-elimination-disqualification/fi-fwd-0045-v3.txt": {
 "STEM": "Hevonen niskuroi 42 sekuntia ja jatkaa sen jälkeen. Miten tämä tuomitaan sääntöjen mukaan?",
 "OPTION_A": "Suoritus hylätään",
 "OPTION_B": "Se tuomitaan kieltäytymiseksi",
 "OPTION_C": "Virhettä ei tuomita",
 "OPTION_D": "Urheilija saa varoituksen",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 346 todetaan, että alle 45 sekuntia kestävä niskurointi tuomitaan kieltäytymiseksi.",
},
"fines-warnings-elimination-disqualification/fi-fwd-0046.txt": {
 "STEM": "Mitä aikarajan ylittämisestä seuraa?",
 "OPTION_A": "Yksi virhepiste jokaisesta ylitetystä sekunnista",
 "OPTION_B": "Varoitus",
 "OPTION_C": "Suorituksen hylkääminen",
 "OPTION_D": "Kilpailusta sulkeminen",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 346 todetaan, että aikarajan ylittäminen johtaa hylkäämiseen.",
},
"fines-warnings-elimination-disqualification/fi-fwd-0046-v1.txt": {
 "STEM": "Mihin aikarajan ylittäminen johtaa artiklan 263.4.13 mukaan?",
 "OPTION_A": "Sakkoon",
 "OPTION_B": "Varoitukseen",
 "OPTION_C": "Hylkäämiseen",
 "OPTION_D": "Keltaiseen korttiin",
 "EXPLANATION": "Artiklassa 263.4.13 aikarajan ylittäminen mainitaan pakollisena hylkäämisperusteena.",
},
"fines-warnings-elimination-disqualification/fi-fwd-0046-v3.txt": {
 "STEM": "Mitä arvostelussa C aikarajan ylittämisestä seuraa?",
 "OPTION_A": "4 virhepistettä",
 "OPTION_B": "Vain aikavirhepisteet",
 "OPTION_C": "Suorituksen hylkääminen",
 "OPTION_D": "Sakko",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 346 määrätään, että arvostelun C aikarajan ylittäminen johtaa hylkäämiseen, ja sama sääntö vahvistetaan yleisesti artiklassa 346.",
},
"fines-warnings-elimination-disqualification/fi-fwd-0047.txt": {
 "STEM": "Mitä varusteita koskevien sääntöjen noudattamatta jättämisestä seuraa?",
 "OPTION_A": "Sakko",
 "OPTION_B": "Suorituksen hylkääminen",
 "OPTION_C": "Varoitus",
 "OPTION_D": "Sulkeminen seuraavasta kilpailusta",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 346 pukeutumista ja varusteita koskevien sääntöjen noudattamatta jättäminen luetellaan pakollisena hylkäämisperusteena.",
},
"fines-warnings-elimination-disqualification/fi-fwd-0047-v1.txt": {
 "STEM": "Urheilija kilpailee kielletyllä kuolaimella. Mitä siitä seuraa artiklan 263.4.22 mukaan?",
 "OPTION_A": "Varoitus",
 "OPTION_B": "Sakko",
 "OPTION_C": "Suorituksen hylkääminen",
 "OPTION_D": "Kilpailusta sulkeminen",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 346 määrätään, että pukeutumista ja varusteita koskevien sääntöjen noudattamatta jättäminen johtaa hylkäämiseen.",
},
"fines-warnings-elimination-disqualification/fi-fwd-0047-v3.txt": {
 "STEM": "Mihin pukeutumista ja varusteita koskevien sääntöjen noudattamatta jättäminen suorituksen aikana johtaa artiklan 263.4.22 mukaan?",
 "OPTION_A": "4 virhepisteeseen",
 "OPTION_B": "Hylkäämiseen",
 "OPTION_C": "Varoitukseen",
 "OPTION_D": "Ei mihinkään seuraukseen",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 346 pukeutumista ja varusteita koskevien sääntöjen noudattamatta jättäminen mainitaan pakollisena hylkäämisperusteena.",
},
"fines-warnings-elimination-disqualification/fi-fwd-0048.txt": {
 "STEM": "Urheilija hyppää esteen suojapäähineen leukahihnan ollessa auki. Mitä siitä seuraa?",
 "OPTION_A": "Virhettä ei tuomita, jos este ylitettiin",
 "OPTION_B": "Hylkääminen, ellei välitön pysähtyminen hihnan kiinnittämiseksi olisi ollut vaarallista",
 "OPTION_C": "500 Sveitsin frangin sakko",
 "OPTION_D": "Varoitus",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 346 todetaan, että esteen hyppääminen tai hyppäämisyritys suojapäähineen leukahihnan ollessa väärin kiinnitettynä tai kiinnittämättä johtaa hylkäämiseen, elleivät olosuhteet tee välitöntä pysähtymistä hihnan kiinnittämiseksi urheilijalle vaaralliseksi.",
},
"fines-warnings-elimination-disqualification/fi-fwd-0048-v1.txt": {
 "STEM": "Milloin urheilijaa ei artiklan 263.4.29 mukaan hylätä kiinnittämättömän leukahihnan vuoksi?",
 "OPTION_A": "Kun hän huomaa asian vasta maalilinjan jälkeen",
 "OPTION_B": "Kun olosuhteet tekisivät välittömän pysähtymisen hihnan kiinnittämiseksi vaaralliseksi",
 "OPTION_C": "Kun hän on juniori",
 "OPTION_D": "Kun tuomaristo ei ole havainnut asiaa",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 346 säädetään poikkeuksesta hylkäämiseen, jos olosuhteiden vuoksi urheilijalle olisi vaarallista pysähtyä välittömästi kiinnittämään leukahihna.",
},
"fines-warnings-elimination-disqualification/fi-fwd-0048-v3.txt": {
 "STEM": "Mitä artiklassa 263.4.29 säädetty hylkäämisperuste koskee nimenomaisesti?",
 "OPTION_A": "Raipan käyttöä",
 "OPTION_B": "Elektronisia laitteita",
 "OPTION_C": "Suojapäähineen leukahihnaa",
 "OPTION_D": "Suojia ja siteitä",
 "EXPLANATION": "Esteratsastussääntöjen artikla 346 koskee esteen hyppäämistä silloin, kun suojapäähineen leukahihna on kiinnitetty väärin tai se on jäänyt kiinnittämättä.",
},
"fines-warnings-elimination-disqualification/fi-fwd-0049.txt": {
 "STEM": "Urheilija käyttää matkapuhelinta kilpailualueella kilpailun aikana. Mitä siitä seuraa?",
 "OPTION_A": "Varoitus",
 "OPTION_B": "1 000 Sveitsin frangin sakko",
 "OPTION_C": "Suorituksen hylkääminen",
 "OPTION_D": "Ei seurausta, jos puhelin on taskussa",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 346 todetaan, että matkapuhelimen, muun elektronisen viestintälaitteen tai kuulokkeiden käyttö kilpailualueella kilpailun aikana johtaa hylkäämiseen.",
},
"fines-warnings-elimination-disqualification/fi-fwd-0049-v1.txt": {
 "STEM": "Minkä elektronisen laitteen käyttö kilpailualueella kilpailun aikana johtaa hylkäämiseen artiklan 263.4.30 mukaan?",
 "OPTION_A": "Matkapuhelimen",
 "OPTION_B": "Sekuntikellon",
 "OPTION_C": "Sykemittarin, jota ei ole yhdistetty urheilijaan",
 "OPTION_D": "Hevosen selkään kiinnitetyn kameran",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 346 mainitaan nimenomaisesti matkapuhelimet, muut elektroniset viestintälaitteet ja kuulokkeet.",
},
"fines-warnings-elimination-disqualification/fi-fwd-0049-v2.txt": {
 "STEM": "Mihin matkapuhelimen käyttö verryttelyalueella kilpailun aikana johtaa artiklan 207.3.1 mukaan?",
 "OPTION_A": "Hylkäämiseen",
 "OPTION_B": "Varoitukseen",
 "OPTION_C": "Sakkoon",
 "OPTION_D": "Ei mihinkään seuraukseen",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 346 todetaan, ettei urheilija saa koskaan käyttää matkapuhelinta verryttelyalueella kilpailun aikana, ja säännön noudattamatta jättämisestä seuraa varoitus.",
},
"fines-warnings-elimination-disqualification/fi-fwd-0050.txt": {
 "STEM": "Mikä on kilpailusta sulkemisen yleinen vaikutus esteratsastussääntöjen mukaan?",
 "OPTION_A": "Urheilija ei saa jatkaa meneillään olevaa suoritusta",
 "OPTION_B": "Urheilija ja/tai hevonen suljetaan kyseisestä kilpailusta tai koko kilpailutapahtumasta",
 "OPTION_C": "Urheilija saa vain virallisen varoituksen",
 "OPTION_D": "Urheilija sijoittuu viimeiseksi meneillään olevassa kilpailussa mutta voi kilpailla myöhemmin",
 "EXPLANATION": "Artiklassa 264.1 todetaan, että kilpailusta sulkeminen tarkoittaa, että urheilija ja/tai hevonen suljetaan kyseisestä kilpailusta tai koko kilpailutapahtumasta, ja se voi olla myös takautuva.",
},
"fines-warnings-elimination-disqualification/fi-fwd-0050-v1.txt": {
 "STEM": "Millainen kilpailusta sulkeminen voi artiklan 264.1 mukaan olla?",
 "OPTION_A": "Sakoksi muunnettava",
 "OPTION_B": "Takautuva",
 "OPTION_C": "Urheilijan peruutettavissa",
 "OPTION_D": "Vain meneillään olevaa suoritusta koskeva",
 "EXPLANATION": "Artiklan 346 mukaan kilpailusta sulkeminen voi olla myös takautuva.",
},
"fines-warnings-elimination-disqualification/fi-fwd-0050-v3.txt": {
 "STEM": "Ketä artiklan 264.1 mukainen kilpailusta sulkeminen voi koskea?",
 "OPTION_A": "Vain urheilijaa",
 "OPTION_B": "Vain hevosta",
 "OPTION_C": "Urheilijaa ja/tai hevosta",
 "OPTION_D": "Vain joukkueenjohtajaa",
 "EXPLANATION": "Artiklassa 264.1 todetaan, että kilpailusta sulkeminen tarkoittaa, että urheilija ja/tai hevonen suljetaan kyseisestä kilpailusta tai koko kilpailutapahtumasta.",
},
"fines-warnings-elimination-disqualification/fi-fwd-0051.txt": {
 "STEM": "Mikä seuraavista on pakollinen kilpailusta sulkemisen peruste?",
 "OPTION_A": "Matkapuhelimen käyttö kilpailualueella",
 "OPTION_B": "Merkit kannusten tai raipan liiallisesta käytöstä missä tahansa hevosen kohdassa",
 "OPTION_C": "Pukeutumissääntöjen rikkominen",
 "OPTION_D": "Kieltäytyminen osallistumasta palkintojenjakoon",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 346 määrätään, että merkit kannusten tai raipan liiallisesta käytöstä missä tahansa hevosen kohdassa johtavat pakolliseen kilpailusta sulkemiseen, ja lisäksi voi seurata artiklojen 265 ja 266 mukaisia seuraamuksia.",
},
"fines-warnings-elimination-disqualification/fi-fwd-0051-v1.txt": {
 "STEM": "Mihin merkit kannusten tai raipan liiallisesta käytöstä johtavat artiklan 264.2.1 mukaan?",
 "OPTION_A": "Hylkäämiseen",
 "OPTION_B": "Sakkoon",
 "OPTION_C": "Kilpailusta sulkemiseen",
 "OPTION_D": "Varoitukseen",
 "EXPLANATION": "Esteratsastussääntöjen artiklan 346 mukaan merkit kannusten tai raipan liiallisesta käytöstä johtavat pakolliseen kilpailusta sulkemiseen.",
},
"fines-warnings-elimination-disqualification/fi-fwd-0051-v2.txt": {
 "STEM": "Mihin muihin artikloihin artiklassa 264.2.1 viitataan mahdollisina lisäseuraamuksina?",
 "OPTION_A": "Artikloihin 259.1 ja 265.2",
 "OPTION_B": "Artikloihin 265 ja 266",
 "OPTION_C": "Artikloihin 261 ja 262",
 "OPTION_D": "Artikloihin 267 ja 268",
 "EXPLANATION": "Artiklassa 264.2.1 määrätään, että merkeistä kannusten tai raipan liiallisesta käytöstä rangaistaan, ja todetaan, että artiklojen 259.1 ja 265.2 nojalla voi seurata lisäseuraamuksia.",
},
"fines-warnings-elimination-disqualification/fi-fwd-0051-v3.txt": {
 "STEM": "Mikä seuraavista ei ole artiklan 264.2 mukaan pakollinen kilpailusta sulkemisen peruste?",
 "OPTION_A": "Merkit kannusten tai raipan liiallisesta käytöstä",
 "OPTION_B": "Luvattomien esteiden hyppääminen kilpailupaikalla",
 "OPTION_C": "Takin käyttämättä jättäminen lämpimällä säällä",
 "OPTION_D": "Hevosen siirtäminen epävirallisiin talleihin ilman lupaa",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 346 luetellaan pakollisina kilpailusta sulkemisen perusteina muun muassa merkit kannusten tai raipan liiallisesta käytöstä, luvattomien esteiden hyppääminen ja hevosen siirtäminen epävirallisiin talleihin. Pukeutumissäännöistä voidaan sen sijaan poiketa lämpimällä säällä.",
},
"fines-warnings-elimination-disqualification/fi-fwd-0052.txt": {
 "STEM": "Mitkä teot voivat olla artiklan 265.1 mukaan hevosen kaltoinkohtelua?",
 "OPTION_A": "Raipan liiallinen käyttö",
 "OPTION_B": "Raipan käyttö tavanomaisena ratsastusapuna",
 "OPTION_C": "Hevosen barraaminen",
 "OPTION_D": "Hevosen kepeä koskettaminen kannuksella suoruuden säilyttämiseksi",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 346 kielletään hevosen barraaminen ja raipan liiallinen käyttö. Raipan käyttöä tavanomaisena ratsastusapuna ja kannusten tavanomaista käyttöä ei sen sijaan pidetä kaltoinkohteluna.",
},
"fines-warnings-elimination-disqualification/fi-fwd-0052-v1.txt": {
 "STEM": "Mitä hevosen barraaminen on artiklan 265.1.1 mukaan?",
 "OPTION_A": "Sallittua",
 "OPTION_B": "Kiellettyä ja hevosen kaltoinkohtelua",
 "OPTION_C": "Sallittua vain verryttelyssä",
 "OPTION_D": "Arvostelumenetelmä",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 346 barraaminen luetellaan niiden kiellettyjen tekojen joukkoon, jotka voivat olla hevosen kaltoinkohtelua.",
},
"fines-warnings-elimination-disqualification/fi-fwd-0052-v3.txt": {
 "STEM": "Mitä raipan liiallinen käyttö on artiklan 265.1.2 mukaan?",
 "OPTION_A": "Sallittua kerran",
 "OPTION_B": "Ehdottomasti kiellettyä",
 "OPTION_C": "Sallittua vain hevosen olkapäähän",
 "OPTION_D": "Huomiotta jätettävää",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 346 raipan liiallinen käyttö kielletään ehdottomasti, ja siitä annetaan esimerkkeinä raipan käyttö hevosen päähän, raipan käyttö useammin kuin kolme kertaa peräkkäin sekä raipan käyttö hylkäämisen jälkeen.",
},
"fines-warnings-elimination-disqualification/fi-fwd-0053.txt": {
 "STEM": "Mihin kilpailuihin osallistuvien hevosten suojien ja siteiden tarkastus on artiklan 266 mukaan pakollinen?",
 "OPTION_A": "Vain Grand Prix -kilpailuun",
 "OPTION_B": "Grand Prix -kilpailuun, korkeimman palkintosumman kilpailuun, Nations Cup- ja Longines League of Nations™ -kilpailuihin sekä Puissance- ja Six Bar -kilpailuihin",
 "OPTION_C": "Kilpailutapahtuman kaikkiin luokkiin",
 "OPTION_D": "Vain Puissance- ja Six Bar -kilpailuihin",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 346 määrätään, että suojien ja siteiden tarkastus on pakollinen kaikille hevosille, jotka osallistuvat Grand Prix -kilpailuun, kilpailutapahtuman korkeimman palkintosumman kilpailuun (jos Grand Prix -kilpailua ei ole), Nations Cup- ja Longines League of Nations™ -kilpailuihin sekä Puissance- ja Six Bar -kilpailuihin; muissa kilpailuissa tarkastusta suositellaan.",
},
"fines-warnings-elimination-disqualification/fi-fwd-0053-v1.txt": {
 "STEM": "Missä kilpailuissa artiklan 266 mukainen suojien ja siteiden tarkastus on pakollinen kaikille osallistuville hevosille?",
 "OPTION_A": "Kilpailutapahtuman kaikissa luokissa",
 "OPTION_B": "Vain Puissance- ja Six Bar -kilpailuissa",
 "OPTION_C": "Grand Prix -kilpailussa, korkeimman palkintosumman kilpailussa, Nations Cup- ja Longines League of Nations™ -kilpailuissa sekä Puissance- ja Six Bar -kilpailuissa",
 "OPTION_D": "Vain Grand Prix -kilpailussa",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 346 määrätään, että suojien ja siteiden tarkastus on pakollinen kaikille hevosille, jotka osallistuvat Grand Prix -kilpailuun, kilpailutapahtuman korkeimman palkintosumman kilpailuun (jos Grand Prix -kilpailua ei ole), Nations Cup- ja Longines League of Nations™ -kilpailuihin sekä Puissance- ja Six Bar -kilpailuihin; muissa kilpailuissa tarkastusta suositellaan.",
},
"fines-warnings-elimination-disqualification/fi-fwd-0053-v3.txt": {
 "STEM": "Mistä artiklassa 266 tarkoitetut suojien ja siteiden tarkastusta koskevat yksityiskohtaiset vaatimukset löytyvät?",
 "OPTION_A": "Vain artiklasta 266 itsestään",
 "OPTION_B": "Veterinaarisäännöistä ja suojien ja siteiden tarkastusta koskevasta ohjeesta",
 "OPTION_C": "Yleisten sääntöjen artiklasta 142",
 "OPTION_D": "Sääntöjen liitteestä VIII",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 346 edellytetään suojien ja siteiden tarkastusta tietyissä kilpailuissa ja todetaan, että tarkemmat tiedot löytyvät säännöistä ja suojien ja siteiden tarkastusta koskevasta ohjeesta, jotka ovat saatavilla FEI:n verkkosivujen Stewards Hub -osiossa.",
},
"fines-warnings-elimination-disqualification/fi-fwd-0054.txt": {
 "STEM": "Kuka voi määrätä sakkoja esteratsastussääntöjen rikkomisesta?",
 "OPTION_A": "Vain FEI:n pääsihteeri",
 "OPTION_B": "Vain tuomariston puheenjohtaja",
 "OPTION_C": "Tuomaristo, päätuomari ja tekninen asiantuntija rikkomuksen mukaan",
 "OPTION_D": "Urheilijan kansallinen liitto",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 346 määrätään, että tuomariston puheenjohtaja voi määrätä sakkoja säännöissä luetelluissa tapauksissa.",
},
"fines-warnings-elimination-disqualification/fi-fwd-0054-v1.txt": {
 "STEM": "Kenelle tuomariston puheenjohtajan määräämät sakot on artiklan 262.2 mukaan maksettava?",
 "OPTION_A": "Kyseiselle urheilijalle",
 "OPTION_B": "Kilpailun järjestäjälle",
 "OPTION_C": "FEI:lle",
 "OPTION_D": "Joukkueenjohtajalle",
 "EXPLANATION": "Artiklassa 346 määrätään, että kaikki tuomariston puheenjohtajan määräämät sakot maksaa kyseisen urheilijan kansallinen liitto FEI:lle.",
},
"fines-warnings-elimination-disqualification/fi-fwd-0054-v3.txt": {
 "STEM": "Joukkueen jäsenen takki ei ole samanvärinen kuin muiden joukkueen jäsenten takit. Minkä suuruinen sakko tästä määrätään artiklan 207.2.4.3 mukaan?",
 "EXPLANATION": "Artiklassa 207.2.4.3 todetaan, että urheilijalle, joka ei noudata joukkueen takin väriä koskevaa sääntöä, tuomaristo määrää 1 000 Sveitsin frangin sakon.",
},
"fines-warnings-elimination-disqualification/fi-fwd-0055.txt": {
 "STEM": "Millä ehdolla hevonen saa artiklan 259 mukaan jatkaa kilpailua kaikissa verenvuototapauksissa?",
 "OPTION_A": "Urheilija pyyhkii veren pois",
 "OPTION_B": "Tuomaristo katsoo eläinlääkäriasiantuntijan kanssa neuvoteltuaan hevosen kilpailukelpoiseksi",
 "OPTION_C": "Joukkueenjohtaja antaa siihen luvan",
 "OPTION_D": "Veri tulee hevosen sieraimesta",
 "EXPLANATION": "Artiklassa 259.3 todetaan, että kaikissa artiklassa 259 mainituissa hevosen verenvuototapauksissa hevonen saa jatkaa kilpailua tai osallistua seuraaviin kilpailuihin vain, jos tuomaristo on eläinlääkäriasiantuntijan kanssa neuvoteltuaan todennut hevosen kilpailukelpoiseksi.",
},
"fines-warnings-elimination-disqualification/fi-fwd-0055-v1.txt": {
 "STEM": "Hevosen kielestä vuotaa verta kilpailun aikana. Millä ehdolla toimihenkilöt voivat artiklan 259.2 mukaan sallia suun huuhtelun tai pyyhkimisen ja antaa ratsukon jatkaa?",
 "OPTION_A": "Urheilija toimittaa eläinlääkärintodistuksen",
 "OPTION_B": "Hevonen katsotaan artiklan 259.3 mukaisesti kilpailukelpoiseksi",
 "OPTION_C": "Verenvuoto tyrehtyy 10 sekunnissa",
 "OPTION_D": "Urheilija pyytää anteeksi",
 "EXPLANATION": "Esteratsastussääntöjen artikla 346 sallii suun huuhtelun tai pyyhkimisen tietyissä verenvuototapauksissa, mutta edellyttää, että tuomaristo katsoo hevosen kilpailukelpoiseksi neuvoteltuaan eläinlääkäriasiantuntijan kanssa.",
},
"fines-warnings-elimination-disqualification/fi-fwd-0055-v3.txt": {
 "STEM": "Kenen kanssa tuomariston on artiklan 259.3 mukaan neuvoteltava, ennen kuin se sallii verta vuotavan hevosen jatkaa kilpailua?",
 "OPTION_A": "Joukkueenjohtajan",
 "OPTION_B": "Ratamestarin",
 "OPTION_C": "Eläinlääkäriasiantuntijan",
 "OPTION_D": "Urheilijan",
 "EXPLANATION": "Esteratsastussääntöjen artiklassa 346 edellytetään, että tuomaristo neuvottelee eläinlääkäriasiantuntijan kanssa, ennen kuin se katsoo hevosen kilpailukelpoiseksi jatkamaan.",
},
}


def main():
    changed = 0
    checked = 0
    problems = []
    for rel, fields in sorted(FIXES.items()):
        path = os.path.join(BASE, rel)
        checked += 1
        if not os.path.exists(path):
            problems.append("PUUTTUU: %s" % rel)
            continue
        with open(path, encoding="utf-8") as fh:
            lines = fh.read().split("\n")
        out = []
        seen = set()
        for line in lines:
            if ": " in line or line.endswith(":"):
                key = line.split(":", 1)[0]
                if key in fields and key in EDITABLE:
                    value = fields[key]
                    if "\n" in value:
                        problems.append("RIVINVAIHTO: %s %s" % (rel, key))
                    out.append("%s: %s" % (key, value))
                    seen.add(key)
                    continue
            out.append(line)
        missing = set(fields) - seen
        if missing:
            problems.append("KENTTÄ EI LÖYTYNYT: %s %s" % (rel, sorted(missing)))
        new = "\n".join(out)
        old = "\n".join(lines)
        if new != old:
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(new)
            changed += 1
    print("Tarkistettu (korjauslistassa): %d, muutettu: %d" % (checked, changed))
    for p in problems:
        print("HUOM:", p)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
