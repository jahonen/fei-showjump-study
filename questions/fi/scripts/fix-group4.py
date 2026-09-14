#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""fix-group4.py

Korjaa kolmen aihealueen (penalty-tables, time-speed, vet-medication-passports)
suomenkielisten monivalintakysymysten kieliasun. Muokkaa VAIN kenttiä
STEM, OPTION_A, OPTION_B, OPTION_C, OPTION_D ja EXPLANATION.

Korjaukset on kirjoitettu käsin ID-kohtaiseen sanakirjaan; asiasisältöä ja
oikeaa vastausta ei muuteta. Terminologia on yhtenäistetty Suomen
Ratsastajainliiton Kilpailusäännöt III – Esteratsastus -kirjan kanssa
(arvostelu A / arvostelu C, virhepiste, hylkääminen, enimmäisaika, aikaraja,
ajanotto, ratsukko, tien pituus, lähtömerkki, äänimerkki, valmiusaika,
kilpailukutsu, järjestäjä, hevostarkastus jne.).
"""

import os
import sys

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "items")
EDIT_FIELDS = ("STEM", "OPTION_A", "OPTION_B", "OPTION_C", "OPTION_D", "EXPLANATION")

FIX = {
    # ------------------------------------------------------------------ penalty-tables
    "fi-pte-0036-v1": {
        "STEM": "Kuinka monta virhepistettä arvostelussa A annetaan enimmäisajan ylittämisestä?",
        "OPTION_A": "Yksi virhepiste jokaisesta täydestä sekunnista",
        "OPTION_B": "Yksi virhepiste jokaisesta alkavasta sekunnista",
        "OPTION_C": "Neljä virhepistettä jokaisesta sekunnista",
        "OPTION_D": "Suorituksen hylkääminen",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 342 todetaan, että enimmäisajan ylittämisestä annetaan yksi virhepiste jokaisesta alkavasta sekunnista.",
    },
    "fi-pte-0036-v2": {
        "STEM": "Mikä on seuraus kumoon ratsastamisesta ja/tai satulasta putoamisesta arvostelussa A?",
        "OPTION_A": "4 virhepistettä",
        "OPTION_B": "6 virhepistettä",
        "OPTION_C": "Suorituksen hylkääminen",
        "OPTION_D": "Varoitus",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 217.1.1 kumoon ratsastaminen ja/tai satulasta putoaminen johtaa arvostelussa A suorituksen hylkäämiseen.",
    },
    "fi-pte-0036-v3": {
        "STEM": "Mihin toinen tottelemattomuus samalla suorituksella johtaa arvostelussa A?",
        "OPTION_A": "4 virhepisteeseen",
        "OPTION_B": "6 virhepisteeseen",
        "OPTION_C": "Suorituksen hylkäämiseen",
        "OPTION_D": "Sakkoon",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 217.1.1 toinen tottelemattomuus tai muu kilpailusääntöjen kohdassa 342 mainittu rikkomus johtaa arvostelussa A suorituksen hylkäämiseen.",
    },
    "fi-pte-0036": {
        "STEM": "Mitkä virheet aiheuttavat arvostelussa A neljä virhepistettä ensimmäisellä kerralla?",
        "OPTION_A": "Ensimmäinen tottelemattomuus",
        "OPTION_B": "Esteen pudottaminen",
        "OPTION_C": "Rajaviivan (vedenpinnan) rikkominen vesiesteellä",
        "OPTION_D": "Kumoon ratsastaminen ja/tai satulasta putoaminen",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 342 todetaan, että arvostelussa A ensimmäisestä tottelemattomuudesta, esteen pudottamisesta ja vesiesteellä tehdystä virheestä annetaan kustakin neljä virhepistettä. Kumoon ratsastaminen ja/tai satulasta putoaminen johtaa suorituksen hylkäämiseen.",
    },
    "fi-pte-0037-v1": {
        "STEM": "Kuinka monta virhesekuntia arvostelussa C lisätään suoritusaikaan, jos este pudotetaan ulkokilpailussa?",
        "OPTION_A": "3 sekuntia",
        "OPTION_B": "4 sekuntia",
        "OPTION_C": "5 sekuntia",
        "OPTION_D": "6 sekuntia",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 217.2.1 määrätään, että esteen pudottamisesta tai rajaviivan (vedenpinnan) rikkomisesta lisätään arvostelussa C ulkokilpailuissa 4 sekuntia (kaksivaiheisen kilpailun toisessa vaiheessa ja arvostelua C käyttävässä uusinnassa 3 sekuntia).",
    },
    "fi-pte-0037-v2": {
        "STEM": "Arvostelua C käyttävässä hallikilpailussa este pudotetaan. Kuinka monta virhesekuntia lisätään?",
        "OPTION_A": "2 sekuntia",
        "OPTION_B": "3 sekuntia",
        "OPTION_C": "4 sekuntia",
        "OPTION_D": "6 sekuntia",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 342 määrätään, että esteen pudottamisesta tai rajaviivan (vedenpinnan) rikkomisesta lisätään arvostelua C käyttävissä hallikilpailuissa 3 sekuntia.",
    },
    "fi-pte-0037-v3": {
        "STEM": "Mitä arvostelussa C seuraa ensimmäisestä tottelemattomuudesta, jonka yhteydessä este ei putoa?",
        "OPTION_A": "Suoritusaikaan lisätään 4 sekuntia",
        "OPTION_B": "Suoritusaikaan lisätään 6 sekuntia",
        "OPTION_C": "Virhesekunteja ei anneta",
        "OPTION_D": "Suoritus hylätään",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 342 todetaan, että ensimmäisestä tottelemattomuudesta ei anneta arvostelussa C lainkaan virhesekunteja.",
    },
    "fi-pte-0037": {
        "STEM": "Mitkä arvostelun C virhepisteitä koskevat väittämät ovat oikein?",
        "OPTION_A": "Esteen pudottamisesta lisätään sekunteja ratsukon suoritusaikaan",
        "OPTION_B": "Ensimmäisestä tottelemattomuudesta, jonka yhteydessä este ei putoa, ei lisätä sekunteja",
        "OPTION_C": "Tottelemattomuudesta, jonka yhteydessä este putoaa, lisätään 6 sekuntia",
        "OPTION_D": "Satulasta putoamisesta lisätään 10 sekuntia",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 342 todetaan, että arvostelussa C esteen pudottamisesta tai rajaviivan (vedenpinnan) rikkomisesta lisätään sekunteja, ensimmäisestä tottelemattomuudesta ei lisätä yhtään sekuntia ja tottelemattomuudesta, jonka yhteydessä este putoaa ja/tai siirtyy, lisätään 6 sekuntia. Kumoon ratsastaminen ja satulasta putoaminen johtavat suorituksen hylkäämiseen, eivät aikalisään.",
    },
    "fi-pte-0038-v1": {
        "STEM": "Mikä on arvostelussa C aikaraja, kun tien pituus on 500 m?",
        "OPTION_A": "Yksi minuutti",
        "OPTION_B": "Kaksi minuuttia",
        "OPTION_C": "Kolme minuuttia",
        "OPTION_D": "Neljä minuuttia",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 217.2.3.2 todetaan, että jos tien pituus on alle 600 m, arvostelussa C aikaraja on kaksi minuuttia.",
    },
    "fi-pte-0038-v3": {
        "STEM": "Mihin aikarajan ylittäminen johtaa arvostelussa C?",
        "OPTION_A": "4 virhepisteeseen",
        "OPTION_B": "6 virhepisteeseen",
        "OPTION_C": "Suorituksen hylkäämiseen",
        "OPTION_D": "Pelkkiin aikavirhepisteisiin",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 217.2.4 todetaan, että arvostelussa C aikarajan ylittäminen johtaa suorituksen hylkäämiseen.",
    },
    "fi-pte-0038": {
        "STEM": "Mikä on arvostelussa C suorituksen aikaraja, kun tien pituus on 650 m?",
        "OPTION_A": "Kaksi minuuttia",
        "OPTION_B": "Kolme minuuttia",
        "OPTION_C": "Neljä minuuttia",
        "OPTION_D": "Aikarajaa ei ole",
        "EXPLANATION": "Kilpailusääntöjen kohdan 342 mukaan arvostelussa C aikaraja on kolme minuuttia, jos tien pituus on 600 m tai enemmän.",
    },
    "fi-pte-0039-v1": {
        "STEM": "Ratsukko kieltäytyy arvostelun A mukaisessa kilpailussa esteellä 3 ja myöhemmin samalla suorituksella esteellä 7. Miten tottelemattomuudet tuomitaan?",
        "OPTION_A": "4 virhepistettä eli vain ensimmäisestä tottelemattomuudesta",
        "OPTION_B": "Yhteensä 8 virhepistettä",
        "OPTION_C": "Suoritus hylätään",
        "OPTION_D": "Toisesta tottelemattomuudesta ei anneta virhepisteitä",
        "EXPLANATION": "Arvostelussa A ensimmäisestä tottelemattomuudesta annetaan neljä virhepistettä, ja toinen tottelemattomuus samalla suorituksella johtaa hylkäämiseen (kilpailusääntöjen kohta 342).",
    },
    "fi-pte-0039-v2": {
        "STEM": "Kilpailusääntöjen kohdassa 217.1.5 täsmennetään, että tottelemattomuudesta annettavat virhepisteet kertyvät",
        "OPTION_A": "estekohtaisesti",
        "OPTION_B": "koko suorituksen ajalta",
        "OPTION_C": "koko kilpailun ajalta",
        "OPTION_D": "vain uusinnoissa",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 342 todetaan, että tottelemattomuudesta annettavat virhepisteet kertyvät koko suorituksen ajalta.",
    },
    "fi-pte-0039-v3": {
        "STEM": "Mitä kilpailusääntöjen kohdassa 217.1.5 vahvistetaan kahdesta tottelemattomuudesta, jotka tapahtuvat samalla suorituksella eri esteillä?",
        "OPTION_A": "Kumpikin katsotaan erilliseksi ensimmäiseksi tottelemattomuudeksi",
        "OPTION_B": "Kumpikin lasketaan mukaan koko suorituksen tulokseen",
        "OPTION_C": "Ne kumoavat toisensa",
        "OPTION_D": "Niitä ei oteta arvostelussa A huomioon",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 342 todetaan nimenomaisesti, että tottelemattomuudesta annettavat virhepisteet kertyvät koko suorituksen ajalta, eivät vain samalta esteeltä.",
    },
    "fi-pte-0039": {
        "STEM": "Miten tottelemattomuudesta annettavat virhepisteet kertyvät arvostelussa A?",
        "OPTION_A": "Vain samalta esteeltä",
        "OPTION_B": "Koko suorituksen ajalta",
        "OPTION_C": "Vain radan ensimmäiseltä puoliskolta",
        "OPTION_D": "Vasta kumoon ratsastamisen tai satulasta putoamisen jälkeen",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 342 määrätään, että tottelemattomuudesta annettavat virhepisteet eivät kerry vain samalta esteeltä vaan koko suorituksen ajalta.",
    },
    "fi-pte-0040-v1": {
        "STEM": "Mitä virallisissa tuloksissa on kilpailusääntöjen kohdan 217.1.2 mukaan eriteltävä erikseen?",
        "OPTION_A": "Omistajien nimet",
        "OPTION_B": "Aikavirhepisteet ja muut virhepisteet",
        "OPTION_C": "Palkintorahat",
        "OPTION_D": "Urheilijoiden kansalaisuus",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 342 edellytetään, että virallisissa tuloksissa ilmoitetaan virhepisteiden kokonaismäärä ja eritellään erikseen aikavirhepisteet ja muut virhepisteet.",
    },
    "fi-pte-0040-v2": {
        "STEM": "Missä arvostelussa aikavirhepisteet on eriteltävä tuloksissa erikseen?",
        "OPTION_A": "Vain arvostelussa A",
        "OPTION_B": "Vain arvostelussa C",
        "OPTION_C": "Sekä arvostelussa A että arvostelussa C",
        "OPTION_D": "Ei kummassakaan",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 342 tämä vaatimus koskee arvostelun A mukaan tuomittavia kilpailuja.",
    },
    "fi-pte-0040-v3": {
        "STEM": "Mitä saadaan, kun arvostelussa A annetut virhepisteet lasketaan yhteen?",
        "OPTION_A": "Enimmäisaika",
        "OPTION_B": "Ratsukon suorituksen tulosvirhepisteet",
        "OPTION_C": "Palkintorahat",
        "OPTION_D": "Uusintaan osallistuvien ratsukoiden lukumäärä",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 217.1.2 todetaan, että virhepisteiden yhteenlaskeminen antaa ratsukon suorituksen tulosvirhepisteet.",
    },
    "fi-pte-0040": {
        "STEM": "Mitä tietoja arvostelun A mukaan ratkaistavan kilpailun virallisten tulosten on sisällettävä?",
        "OPTION_A": "Vain virhepisteet yhteensä",
        "OPTION_B": "Virhepisteet yhteensä ja pelkät sijoitukset",
        "OPTION_C": "Virhepisteet yhteensä sekä erikseen aikavirhepisteet ja muut virhepisteet",
        "OPTION_D": "Vain suoritusajan",
        "EXPLANATION": "Kilpailusääntöjen kohdan 342 mukaan virallisissa tuloksissa on ilmoitettava virhepisteiden kokonaismäärä sekä eriteltävä erikseen aikavirhepisteet ja muut suorituksen aikana kertyneet virhepisteet.",
    },
    "fi-pte-0041-v1": {
        "STEM": "Mitä urheilijalle voi seurata, jos hän ei noudata kilpailusääntöjen kohdan 217.3 mukaista harjoituskierroksen ilmoitusvelvollisuutta?",
        "OPTION_A": "Sakko",
        "OPTION_B": "Tuomariston päätös hylätä suoritus",
        "OPTION_C": "Varoitus",
        "OPTION_D": "Sulkeminen koko kilpailusta",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 217.3 todetaan, että tuomaristo voi hylätä sääntöä rikkovan urheilijan suorituksen (ks. kilpailusääntöjen kohta 342).",
    },
    "fi-pte-0041-v2": {
        "STEM": "Mitä arvosteluja harjoituskierrosta koskeva sääntö koskee kilpailusääntöjen kohdan 217.3 mukaan kilpailuissa, joissa aika ratkaisee?",
        "OPTION_A": "Vain arvostelua A",
        "OPTION_B": "Vain arvostelua C",
        "OPTION_C": "Arvostelua A tai arvostelua C",
        "OPTION_D": "Ei kumpaakaan",
        "EXPLANATION": "Kilpailusääntöjen kohta 342 koskee harjoituskierroksia arvostelun A tai arvostelun C mukaisissa kilpailuissa, joissa aika ratkaisee.",
    },
    "fi-pte-0041-v3": {
        "STEM": "Missä vaiheessa urheilijan on ilmoitettava harjoituskierroksesta järjestäjälle kilpailusääntöjen kohdan 217.3 mukaan?",
        "OPTION_A": "Kilpailupaikalle saavuttaessa",
        "OPTION_B": "Ilmoittautumisen yhteydessä",
        "OPTION_C": "Ennen kilpailualueelle tuloa",
        "OPTION_D": "Ensimmäisen suorituksen jälkeen",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 342 edellytetään, että urheilija ilmoittaa asiasta järjestäjälle ilmoittautumisen yhteydessä.",
    },
    "fi-pte-0041": {
        "STEM": "Urheilija haluaa ratsastaa harjoituskierroksen arvostelun A mukaisessa kilpailussa, jossa aika ratkaisee. Mitä hänen on tehtävä?",
        "OPTION_A": "Maksettava lisämaksu",
        "OPTION_B": "Ilmoitettava asiasta järjestäjälle ilmoittautumisen yhteydessä ja lähdettävä ensimmäisenä",
        "OPTION_C": "Pyydettävä tuomaristolta lupa ensimmäisen suorituksen jälkeen",
        "OPTION_D": "Ei mitään, sillä harjoituskierros ei ole sallittu",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 217.3 määrätään, että urheilijan, joka haluaa ratsastaa harjoituskierroksen arvostelun A tai arvostelun C mukaisessa kilpailussa, jossa aika ratkaisee, on ilmoitettava siitä järjestäjälle ilmoittautumisen yhteydessä, ja harjoituskierrosta haluavat lähtevät ensimmäisinä.",
    },
    "fi-pte-0042-v1": {
        "STEM": "Miten tasapisteet yleensä ratkaistaan arvostelun A mukaisessa kilpailussa, jossa aika ei ratkaise?",
        "OPTION_A": "Suoritukseen kuluneen ajan perusteella",
        "OPTION_B": "Pelkästään uusinnalla",
        "OPTION_C": "Kolikonheitolla",
        "OPTION_D": "Jakamalla palkinnot",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 342 esitetään vaihtoehtoja arvostelun A mukaisiin kilpailuihin, joissa aika ei ratkaise. Yhden vaihtoehdon mukaan saman virhepistemäärän saavuttaneet urheilijat ovat millä tahansa sijalla tasaveroisia, jakavat palkinnot eikä uusintaa järjestetä. Jos uusinta järjestetään, uusintaan osallistumattomat urheilijat jakavat silti muut kuin ensimmäisen sijan palkinnot.",
    },
    "fi-pte-0042-v3": {
        "STEM": "Miten tasapisteet voidaan ratkaista arvostelun A mukaisessa kilpailussa, jossa aika ratkaisee?",
        "OPTION_A": "Urheilijan kansalaisuuden perusteella",
        "OPTION_B": "Suoritukseen kuluneen ajan perusteella eli nopeampi suoritus voittaa, jos siitä on maininta kilpailukutsussa",
        "OPTION_C": "Kolikonheitolla",
        "OPTION_D": "Lähtöjärjestyksen arvonnan perusteella",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 342 määrätään, että saman virhepistemäärän saavuttaneiden urheilijoiden tasapisteet voidaan ratkaista suoritukseen kuluneen ajan perusteella kilpailukutsussa esitettyjen ehtojen mukaisesti.",
    },
    "fi-pte-0042": {
        "STEM": "Miten arvostelun A mukaiset kilpailut voidaan määritellä?",
        "OPTION_A": "Vain kilpailuiksi, joissa aika ratkaisee",
        "OPTION_B": "Vain kilpailuiksi, joissa aika ei ratkaise",
        "OPTION_C": "Kilpailuiksi, joissa aika ratkaisee, tai kilpailuiksi, joissa aika ei ratkaise",
        "OPTION_D": "Aina molemmiksi yhtä aikaa",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 217.1.3 määrätään, että arvostelun A mukaan tuomittavat kilpailut voidaan määritellä joko kilpailuiksi, joissa aika ratkaisee, tai kilpailuiksi, joissa aika ei ratkaise.",
    },

    # ------------------------------------------------------------------ time-speed
    "fi-tsp-0028-v1": {
        "STEM": "Mihin enimmäisajan ylittäminen johtaa kilpailusääntöjen kohdan 250.1 mukaan?",
        "OPTION_A": "Suorituksen hylkäämiseen",
        "OPTION_B": "Aikavirhepisteisiin",
        "OPTION_C": "Varoitukseen",
        "OPTION_D": "Ei mihinkään seuraukseen",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 352 määrätään, että enimmäisajan ylittämisestä annetaan aikavirhepisteitä. Aikarajan ylittäminen voi sen sijaan johtaa suorituksen hylkäämiseen (kilpailusääntöjen kohdat 352 ja 263.4.13).",
    },
    "fi-tsp-0028-v2": {
        "STEM": "Missä kilpailutyypissä ei ole enimmäisaikaa mutta on aikaraja?",
        "OPTION_A": "Arvostelu A, jossa aika ratkaisee",
        "OPTION_B": "Arvostelu A, jossa aika ei ratkaise",
        "OPTION_C": "Arvostelu C",
        "OPTION_D": "Voima- ja taitokilpailu",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 217.2.3 todetaan, että arvostelun C mukaisissa kilpailuissa ei ole enimmäisaikaa, mutta niissä on aikaraja.",
    },
    "fi-tsp-0028-v3": {
        "STEM": "Millä perusteella arvostelussa A lasketaan aikavirhepisteet, kun enimmäisaika ylitetään?",
        "OPTION_A": "Yksi virhepiste jokaisesta täydestä sekunnista",
        "OPTION_B": "Yksi virhepiste jokaisesta alkavasta sekunnista",
        "OPTION_C": "Kaksi virhepistettä jokaisesta sekunnista",
        "OPTION_D": "Neljä virhepistettä jokaisesta alkavasta sekunnista",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 352 todetaan, että arvostelussa A enimmäisajan ylittämisestä annetaan yksi virhepiste jokaisesta alkavasta sekunnista.",
    },
    "fi-tsp-0028": {
        "STEM": "Milloin ratsukolle annetaan aikavirhepisteitä kilpailusääntöjen kohdan 250.1 nojalla?",
        "OPTION_A": "Kun ratsukko suorittaa radan enimmäisaikaa nopeammin",
        "OPTION_B": "Kun ratsukko ylittää suoritukselle asetetun enimmäisajan",
        "OPTION_C": "Vain silloin, kun ratsukko ylittää aikarajan",
        "OPTION_D": "Aina kun suorituksen aikana annetaan äänimerkki",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 352 todetaan, että ratsukolle annetaan aikavirhepisteitä, jos se ylittää suoritukselle asetetun enimmäisajan.",
    },
    "fi-tsp-0029-v1": {
        "STEM": "Milloin ajanotto voi kilpailusääntöjen kohdan 251.1.1 mukaan alkaa jo ennen kuin ratsukko ylittää lähtölinjan?",
        "OPTION_A": "Kun urheilija putoaa satulasta ennen lähtöä",
        "OPTION_B": "Kun 45 sekunnin valmiusaika päättyy ennen kuin ratsukko on ylittänyt lähtölinjan oikeasta suunnasta",
        "OPTION_C": "Kun äänimerkki annetaan kahdesti",
        "OPTION_D": "Kun tuomariston jäsenet heiluttavat lippua",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 352 määrätään, että ajanotto alkaa, kun ratsukko ylittää lähtölinjan lähtömerkin jälkeen tai kun 45 sekunnin valmiusaika päättyy, sen mukaan kumpi tapahtuu ensin.",
    },
    "fi-tsp-0029-v2": {
        "STEM": "Milloin ajanotto päättyy kilpailusääntöjen kohdan 251.1.2 mukaan?",
        "OPTION_A": "Kun ratsukko on hypännyt viimeisen esteen",
        "OPTION_B": "Kun ratsukko ylittää maalilinjan oikeasta suunnasta viimeisen esteen hypättyään",
        "OPTION_C": "Kun äänimerkki annetaan",
        "OPTION_D": "Kun ratsukko poistuu kilpailualueelta",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 251.1.2 määrätään, että ajanotto päättyy, kun ratsukko ylittää maalilinjan oikeasta suunnasta viimeisen esteen hypättyään.",
    },
    "fi-tsp-0029-v3": {
        "STEM": "Mikä näyttö on oltava selvästi urheilijan nähtävissä kilpailusääntöjen kohdan 251.1.1 mukaan?",
        "OPTION_A": "Palkintoluettelo",
        "OPTION_B": "45 sekunnin valmiusajan näyttö",
        "OPTION_C": "Aiemmat tulokset näyttävä tulostaulu",
        "OPTION_D": "Verryttelyalueen aikataulu",
        "EXPLANATION": "Kilpailusääntöjen kohdan 352 mukaan 45 sekunnin valmiusaikaa näyttävän taulun on oltava selvästi urheilijan nähtävissä.",
    },
    "fi-tsp-0029": {
        "STEM": "Milloin ajanotto alkaa?",
        "OPTION_A": "Kun äänimerkki annetaan",
        "OPTION_B": "Kun urheilija saapuu kilpailualueelle",
        "OPTION_C": "Kun ratsukko ylittää lähtölinjan oikeasta suunnasta ensimmäisen kerran lähtömerkin jälkeen tai kun 45 sekunnin valmiusaika päättyy, sen mukaan kumpi tapahtuu ensin",
        "OPTION_D": "Kun ratsukko hyppää ensimmäisen esteen",
        "EXPLANATION": "Kilpailusääntöjen kohdan 352 mukaan ajanotto alkaa, kun ratsukko ylittää lähtölinjan oikeasta suunnasta ensimmäisen kerran lähtömerkin jälkeen tai kun 45 sekunnin valmiusaika päättyy, sen mukaan kumpi tapahtuu ensin.",
    },
    "fi-tsp-0030-v2": {
        "STEM": "Mikä on enimmäisaika, kun tien pituus on 400 m ja nopeus 400 m/min?",
        "OPTION_A": "60 sekuntia",
        "OPTION_B": "80 sekuntia",
        "OPTION_C": "90 sekuntia",
        "OPTION_D": "100 sekuntia",
        "EXPLANATION": "Enimmäisaika saadaan jakamalla tien pituus nopeudella: 400 m / 400 m/min = 1 min eli 60 sekuntia.",
    },
    "fi-tsp-0030-v3": {
        "STEM": "Mitä tuomaristo voi muuttaa ennen ensimmäisen ratsukon lähtöä, jos kentän pohja on muuttunut huonoksi?",
        "OPTION_A": "Kilpailukutsussa ilmoitettua nopeutta",
        "OPTION_B": "Esteiden lukumäärää",
        "OPTION_C": "Tien pituutta",
        "OPTION_D": "Palkintorahoja",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 258.2 määrätään, että jos kentän pohja on muuttunut huonoksi, tuomaristo voi muuttaa kilpailukutsussa ilmoitettua nopeutta ennen luokan ensimmäisen ratsukon lähtöä.",
    },
    "fi-tsp-0030": {
        "STEM": "Miten suorituksen enimmäisaika määräytyy?",
        "OPTION_A": "Yksinomaan ratamestarin päätöksellä",
        "OPTION_B": "Kertomalla tien pituus kilpailusääntöjen kohdassa 258 määritellyllä nopeudella",
        "OPTION_C": "Tien pituuden ja kilpailusääntöjen kohdassa 258 määrättyjen nopeuksien perusteella",
        "OPTION_D": "Se on kaikissa kilpailuissa kiinteästi 80 sekuntia",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 252 todetaan, että suorituksen enimmäisaika määräytyy tien pituuden ja kilpailusääntöjen kohdassa 258 määrättyjen nopeuksien perusteella.",
    },
    "fi-tsp-0031-v1": {
        "STEM": "Mikä on aikaraja, jos suorituksen enimmäisaika on 72 sekuntia?",
        "OPTION_A": "108 sekuntia",
        "OPTION_B": "120 sekuntia",
        "OPTION_C": "144 sekuntia",
        "OPTION_D": "180 sekuntia",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 352 määrätään, että aikaraja on kaksinkertainen enimmäisaikaan verrattuna: 72 sekuntia × 2 = 144 sekuntia.",
    },
    "fi-tsp-0031-v2": {
        "STEM": "Mikä on arvostelussa A seuraus aikarajan ylittämisestä?",
        "OPTION_A": "Neljä virhepistettä",
        "OPTION_B": "Pelkät aikavirhepisteet",
        "OPTION_C": "Suorituksen hylkääminen",
        "OPTION_D": "Varoitus",
        "EXPLANATION": "Kilpailusääntöjen kohdan 217.1.1 mukaan arvostelussa A aikarajan ylittäminen johtaa suorituksen hylkäämiseen.",
    },
    "fi-tsp-0031-v3": {
        "STEM": "Missä kilpailussa aikaraja on kilpailusääntöjen kohdan 253 mukaan kaksinkertainen enimmäisaikaan verrattuna?",
        "OPTION_A": "Kilpailussa, jolle on määritelty enimmäisaika",
        "OPTION_B": "Jokaisessa arvostelun C mukaan tuomittavassa kilpailussa",
        "OPTION_C": "Kilpailussa, jossa on alle kahdeksan estettä",
        "OPTION_D": "Jokaisessa hallikilpailussa",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 253 määrätään, että aikaraja on kaksinkertainen enimmäisaikaan verrattuna kilpailussa, jolle on määritelty enimmäisaika.",
    },
    "fi-tsp-0031": {
        "STEM": "Mikä on aikaraja, kun enimmäisaika on määritelty?",
        "OPTION_A": "Yhtä pitkä kuin enimmäisaika",
        "OPTION_B": "Puolitoista kertaa enimmäisaika",
        "OPTION_C": "Kaksinkertainen enimmäisaika",
        "OPTION_D": "Kolminkertainen enimmäisaika",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 253 määrätään, että aikaraja on kaksinkertainen enimmäisaikaan verrattuna kilpailussa, jolle on määritelty enimmäisaika.",
    },
    "fi-tsp-0032-v1": {
        "STEM": "Mitä ratsukko saa tehdä kilpailusääntöjen kohdan 255.1 nojalla, kun ajanotto on pysäytetty?",
        "OPTION_A": "Sen on pysyttävä paikallaan",
        "OPTION_B": "Se saa liikkua vapaasti, kunnes äänimerkki antaa luvan jatkaa suoritusta",
        "OPTION_C": "Se saa poistua kilpailualueelta",
        "OPTION_D": "Sen on hypättävä seuraava este välittömästi",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 255.1 määrätään, että ajanoton ollessa pysäytettynä ratsukko saa liikkua vapaasti, kunnes annetaan äänimerkki, joka antaa luvan jatkaa suoritusta.",
    },
    "fi-tsp-0032-v2": {
        "STEM": "Miten tottelemattomuudet yleensä tuomitaan, kun ajanotto on keskeytetty?",
        "OPTION_A": "Niistä annetaan virhepisteitä kuten tavallisista kieltäytymisistä",
        "OPTION_B": "Niistä ei anneta virhepisteitä, paitsi jos kyseessä on toinen tottelemattomuus sen jälkeen, kun este on pudonnut kieltäytymisen yhteydessä",
        "OPTION_C": "Ne johtavat aina suorituksen hylkäämiseen",
        "OPTION_D": "Ne jätetään kokonaan huomiotta",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 352 todetaan, että ajanoton ollessa keskeytettynä tottelemattomuudesta ei anneta virhepisteitä, lukuun ottamatta toista tottelemattomuutta sen jälkeen, kun este on pudonnut kieltäytymisen yhteydessä.",
    },
    "fi-tsp-0032-v3": {
        "STEM": "Kuka saa käynnistää ja pysäyttää kellon kilpailusääntöjen kohdan 255.3 mukaan?",
        "OPTION_A": "Ajanottaja",
        "OPTION_B": "Ratamestari",
        "OPTION_C": "Kuka tahansa tuomariston jäsen",
        "OPTION_D": "Vain ajanotosta vastaava tuomari",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 255.3 todetaan, että vain ajanotosta vastaava tuomari saa käynnistää ja pysäyttää kellon; ajanottajalle ei voida antaa tätä tehtävää.",
    },
    "fi-tsp-0032": {
        "STEM": "Milloin kello käynnistetään keskeytyksen jälkeen uudelleen kilpailusääntöjen kohdan 255.2 mukaan?",
        "OPTION_A": "Heti kun äänimerkki annetaan",
        "OPTION_B": "Kun ratsukko saapuu radalla siihen kohtaan, jossa ajanotto pysäytettiin",
        "OPTION_C": "Kun ratsukko hyppää seuraavan esteen",
        "OPTION_D": "Kun ratsukko ylittää maalilinjan",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 352 määrätään, että kello käynnistetään uudelleen, kun ratsukko saapuu radalla siihen kohtaan, jossa ajanotto pysäytettiin. Poikkeuksena on tottelemattomuus, jonka yhteydessä este putoaa; siihen sovelletaan kilpailusääntöjen kohtaa 256.",
    },
    "fi-tsp-0033-v1": {
        "STEM": "Este putoaa tottelemattomuuden seurauksena, ja se pystytetään uudelleen. Mitä aikalisää kilpailusääntöjen kohdan 256 nojalla sovelletaan?",
        "OPTION_A": "Aikalisää ei anneta",
        "OPTION_B": "Suoritusaikaan lisätään kuusi sekuntia",
        "OPTION_C": "Aika nollataan",
        "OPTION_D": "Suoritusaikaan lisätään esteen pystyttämiseen kulunut aika",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 352 määrätään, että tottelemattomuuden ja esteen pudottamisen jälkeen ratsukon suoritusaikaan lisätään kuuden sekunnin aikalisä.",
    },
    "fi-tsp-0033-v2": {
        "STEM": "Milloin kello käynnistetään kilpailusääntöjen kohdan 256 mukaan uudelleen sen jälkeen, kun tottelemattomuuden yhteydessä pudonnut este on pystytetty uudelleen?",
        "OPTION_A": "Kun äänimerkki annetaan",
        "OPTION_B": "Kun ratsukko saapuu esteelle",
        "OPTION_C": "Kun hevonen ponnistaa hyppyyn sillä esteellä, jolla kieltäytyminen tapahtui",
        "OPTION_D": "Kun hevonen laskeutuu esteen ylitettyään",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 256 määrätään, että kello käynnistetään uudelleen, kun hevonen ponnistaa hyppyyn sillä esteellä, jolla kieltäytyminen tapahtui. Jos kieltäytyminen tapahtui sarjaesteen toisella tai sitä seuraavalla osalla, kello käynnistetään uudelleen, kun hevonen ponnistaa hyppyyn sarjan ensimmäisellä osalla.",
    },
    "fi-tsp-0033-v3": {
        "STEM": "Mitä tapahtuu kilpailusääntöjen kohdan 256 mukaan sen jälkeen, kun tottelemattomuuden yhteydessä pudonnut este on pystytetty uudelleen?",
        "OPTION_A": "Ratsukon suoritus hylätään automaattisesti",
        "OPTION_B": "Annetaan äänimerkki merkiksi siitä, että rata on valmis ja ratsukko voi jatkaa",
        "OPTION_C": "Enimmäisaika lasketaan uudelleen",
        "OPTION_D": "Suoritus aloitetaan uudelleen lähtölinjalta",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 256 määrätään, että kun este on pystytetty uudelleen, annetaan äänimerkki merkiksi siitä, että rata on valmis ja ratsukko voi jatkaa suoritustaan.",
    },
    "fi-tsp-0033": {
        "STEM": "Milloin ratsukon suoritusaikaan lisätään kuuden sekunnin aikalisä kilpailusääntöjen kohdan 256 mukaan?",
        "OPTION_A": "Aina kun este putoaa",
        "OPTION_B": "Kun tottelemattomuus siirtää tai pudottaa esteen tai sen rajoittimen kohdassa määritellyissä olosuhteissa",
        "OPTION_C": "Aina kun urheilija pyytää ajanoton pysäyttämistä",
        "OPTION_D": "Jokaisen tottelemattomuuden jälkeen",
        "EXPLANATION": "Kilpailusääntöjen kohdan 352 mukaan suoritusaikaan lisätään kuuden sekunnin aikalisä, kun ratsukko tottelemattomuuden seurauksena siirtää tai pudottaa esteen tai sen rajoittimen kohdassa määritellyissä olosuhteissa.",
    },
    "fi-tsp-0034-v1": {
        "STEM": "Mikä on suurin sallittu nopeus tavallisessa kilpailussa kilpailusääntöjen kohdan 258.1.1 mukaan?",
        "OPTION_A": "350 m/min",
        "OPTION_B": "375 m/min",
        "OPTION_C": "400 m/min",
        "OPTION_D": "425 m/min",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 352 enimmäisnopeudeksi on asetettu 400 m/min.",
    },
    "fi-tsp-0034-v2": {
        "STEM": "Mikä nopeus vaaditaan kilpailusääntöjen kohdan 258.1.2 mukaan ulkona ratsastettavissa viiden tähden Nations Cup -kilpailuissa?",
        "OPTION_A": "350 m/min",
        "OPTION_B": "375 m/min",
        "OPTION_C": "400 m/min",
        "OPTION_D": "425 m/min",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 258.1.2 määrätään, että CSIO 5* Nations Cup- ja Longines League of Nations™ -kilpailuissa nopeus on ulkona 400 m/min.",
    },
    "fi-tsp-0034-v3": {
        "STEM": "Mikä on vähimmäisnopeus nuorten hevosten luokissa?",
        "OPTION_A": "300 m/min",
        "OPTION_B": "325 m/min",
        "OPTION_C": "350 m/min",
        "OPTION_D": "375 m/min",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 258.1.3 määrätään, että nuorten hevosten luokissa vähimmäisnopeus on 325 m/min.",
    },
    "fi-tsp-0034": {
        "STEM": "Mikä on kilpailuissa yleisesti sallittu nopeusalue?",
        "OPTION_A": "300–375 m/min",
        "OPTION_B": "325–400 m/min",
        "OPTION_C": "350–425 m/min",
        "OPTION_D": "375–450 m/min",
        "EXPLANATION": "Kilpailusääntöjen kohdan 352 mukaan yleinen nopeusalue on vähintään 325 m/min ja enintään 400 m/min.",
    },
    "fi-tsp-0035-v1": {
        "STEM": "Missä kilpailutyypissä ei ole vähimmäisnopeusvaatimusta kilpailusääntöjen kohdan 258.1.6 nojalla?",
        "OPTION_A": "Arvostelu A, jossa aika ratkaisee",
        "OPTION_B": "Nations Cup",
        "OPTION_C": "Voima- ja taitokilpailu",
        "OPTION_D": "Nuorten hevosten luokka",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 352 määrätään nimenomaisesti, ettei voima- ja taitokilpailuissa vaadita vähimmäisnopeutta.",
    },
    "fi-tsp-0035-v2": {
        "STEM": "Missä kilpailutyypissä aika ei koskaan ratkaise kilpailusääntöjen kohdan 230.1.4 mukaan?",
        "OPTION_A": "Arvostelun A mukaisessa Grand Prix -luokassa",
        "OPTION_B": "Voima- ja taitokilpailussa",
        "OPTION_C": "Nations Cupissa",
        "OPTION_D": "Arvostelun C mukaisessa nopeuskilpailussa",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 352 todetaan, että aika ei koskaan ratkaise voima- ja taitokilpailuissa; niissä ei ole enimmäisaikaa eikä aikarajaa.",
    },
    "fi-tsp-0035": {
        "STEM": "Mitä nopeusvaatimuksia sovelletaan voima- ja taitokilpailuissa?",
        "OPTION_A": "Vähintään 325 m/min",
        "OPTION_B": "Vähintään 350 m/min",
        "OPTION_C": "Vähimmäisnopeutta ei vaadita",
        "OPTION_D": "Enintään 400 m/min",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 258.1.6 todetaan, ettei voima- ja taitokilpailuissa ole vähimmäisnopeusvaatimusta.",
    },

    # ------------------------------------------------------ vet-medication-passports
    "fi-vmp-0093-v1": {
        "STEM": "Kuka voi kilpailusääntöjen kohdan 275.1.3.1 nojalla sopia hevostensa tarkastusajankohdasta?",
        "OPTION_A": "Tuomaristo",
        "OPTION_B": "Joukkueenjohtajat ja/tai vastuuhenkilöt",
        "OPTION_C": "Tekninen edustaja",
        "OPTION_D": "Järjestäjän puheenjohtaja",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 275.1.3.1 määrätään, että joukkueenjohtajien ja/tai vastuuhenkilöiden on sovittava hevostensa tarkastukselle tietty ajankohta kilpailukutsussa mainitun ajan puitteissa.",
    },
    "fi-vmp-0093-v2": {
        "STEM": "Missä kilpailuissa vaaditaan kilpailusääntöjen kohdan 275.1.3.2 mukaan toinen hevostarkastus ennen yksilökilpailua?",
        "OPTION_A": "Kaikissa CSI-kilpailuissa",
        "OPTION_B": "Olympialaisissa ja mannerkisoissa, FEI:n esteratsastuksen maailmancupin™ finaaleissa sekä kaikkien luokkien maailman- ja mannermestaruuskilpailuissa",
        "OPTION_C": "Vain Nations Cupin finaaleissa",
        "OPTION_D": "Vain ulkona järjestettävissä CSIO-kilpailuissa",
        "EXPLANATION": "Kilpailusääntöjen kohta 321 edellyttää toista hevostarkastusta olympialaisissa ja mannerkisoissa, FEI:n esteratsastuksen maailmancupin finaaleissa sekä kaikkien luokkien maailman- ja mannermestaruuskilpailuissa.",
    },
    "fi-vmp-0093-v3": {
        "STEM": "Kuka voi kilpailusääntöjen kohdan 275.1.3.1 mukaan sallia toisen tarkastuksen myöhemmin, jos hevoset eivät ole voineet olla läsnä ensimmäisessä tarkastuksessa poikkeuksellisten ja odottamattomien olosuhteiden vuoksi?",
        "OPTION_A": "Joukkueenjohtaja",
        "OPTION_B": "Järjestäjä",
        "OPTION_C": "Tuomaristo eläinlääkäriedustajaa kuultuaan",
        "OPTION_D": "Tekninen edustaja yksin",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 321 määrätään, että tuomaristo voi eläinlääkäriedustajaa kuultuaan harkintansa mukaan sallia myöhemmin toisen hevostarkastuksen niille hevosille, jotka eivät ole voineet olla läsnä poikkeuksellisten ja odottamattomien olosuhteiden vuoksi.",
    },
    "fi-vmp-0093": {
        "STEM": "Milloin hevostarkastus on suoritettava ennen ensimmäisen kilpailun alkua?",
        "OPTION_A": "12 tunnin kuluessa",
        "OPTION_B": "24 tunnin kuluessa",
        "OPTION_C": "48 tunnin kuluessa",
        "OPTION_D": "Milloin tahansa ennen ensimmäistä kilpailua",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 275.1.3.1 määrätään, että hevostarkastus on suoritettava 24 tunnin kuluessa ennen ensimmäisen kilpailun alkamista.",
    },
    "fi-vmp-0094-v1": {
        "STEM": "Mitkä varusteet on kilpailusääntöjen kohdan 275.1.3.3 mukaan poistettava, kun hevonen esitetään hevostarkastuksessa?",
        "OPTION_A": "Vain loimet",
        "OPTION_B": "Loimet, pintelit ja muut valjaat tai varusteet",
        "OPTION_C": "Vain pintelit",
        "OPTION_D": "Ei mitään, vaan hevonen esitetään sellaisena kuin se on tallissa",
        "EXPLANATION": "Kilpailusääntöjen kohta 321 edellyttää, että loimet, pintelit ja muut valjaat tai varusteet poistetaan.",
    },
    "fi-vmp-0094-v2": {
        "STEM": "Hevonen esitetään tarkastuksessa hackamorella nivel- tai kankisuitsien sijasta. Miten tätä on kilpailusääntöjen kohdan 275.1.3.3 mukaan arvioitava?",
        "OPTION_A": "Se on sallittua",
        "OPTION_B": "Se on sääntöjen vastaista",
        "OPTION_C": "Se on sallittua eläinlääkäriedustajan luvalla",
        "OPTION_D": "Se on sallittua vain nuorille hevosille",
        "EXPLANATION": "Kilpailusääntöjen kohta 321 edellyttää, että hevonen esitetään joko nivel- tai kankisuitsitettuna; hackamorea ei sallita.",
    },
    "fi-vmp-0094-v3": {
        "STEM": "Kilpailusääntöjen kohdassa 275.1.3.3 todetaan, ettei suitsia ja varusteita koskevasta säännöstä voi poiketa. Onko väite oikein?",
        "OPTION_A": "Ei, sillä poikkeukset ovat tuomariston harkinnassa",
        "OPTION_B": "Kyllä, sillä poikkeuksia ei sallita",
        "OPTION_C": "Se pätee vain poneihin",
        "OPTION_D": "Se pätee vain huonolla säällä",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 275.1.3.3 todetaan nimenomaisesti, ettei säännöstä voi poiketa.",
    },
    "fi-vmp-0094": {
        "STEM": "Jokainen hevonen on esitettävä tarkastuksessa. Millä suitsilla hevonen esitetään ja mitkä varusteet on poistettava?",
        "OPTION_A": "Nivelsuitsilla, mutta loimet saavat jäädä paikoilleen",
        "OPTION_B": "Nivel- tai kankisuitsilla, ja loimet, pintelit ja muut varusteet on poistettava",
        "OPTION_C": "Pelkällä kuolaimella, eikä muita rajoituksia ole",
        "OPTION_D": "Kankisuitsilla, mutta suojien on jäätävä paikoilleen",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 275.1.3.3 määrätään, että jokainen hevonen on esitettävä joko nivel- tai kankisuitsitettuna ja että kaikki muut valjaat ja varusteet, kuten loimet ja pintelit, on poistettava. Poikkeuksia ei sallita.",
    },
    "fi-vmp-0095-v2": {
        "STEM": "Hevosen tuntomerkit on peitetty väriaineella. Miten tätä on kilpailusääntöjen kohdan 275.1.3.4 mukaan arvioitava?",
        "OPTION_A": "Se on sallittua",
        "OPTION_B": "Se on sääntöjen vastaista",
        "OPTION_C": "Se on sallittua eläinlääkäriedustajan luvalla",
        "OPTION_D": "Se on sallittua vain CSI1*-kilpailuissa",
        "EXPLANATION": "Kilpailusääntöjen kohta 321 kieltää hevosen tuntomerkkien peittämisen millään tavalla maalilla tai väriaineella.",
    },
    "fi-vmp-0095-v3": {
        "STEM": "Mitä hevostarkastuksessa tuntomerkkien peittämistä koskevalla kiellolla pyritään varmistamaan?",
        "OPTION_A": "Hevosen luotettava tunnistaminen",
        "OPTION_B": "Yhtenäinen väritys",
        "OPTION_C": "Sponsorien näkyvyys",
        "OPTION_D": "Lämmönsäätely",
        "EXPLANATION": "Kilpailusääntöjen kohta 321 on osa passin- ja tunnistustarkastusta, jolla varmistetaan, että esitetty hevonen vastaa virallisia tunnistetietojaan.",
    },
    "fi-vmp-0095": {
        "STEM": "Millaisena hevosta ei saa esittää tarkastuksessa kilpailusääntöjen kohdan 275.1.3.4 nojalla?",
        "OPTION_A": "Harja letitettynä",
        "OPTION_B": "Tuntomerkit maalilla tai väriaineella peitettyinä",
        "OPTION_C": "Valkoiset merkit näkyvissä",
        "OPTION_D": "Urheilijan ratsastamana",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 321 todetaan, ettei hevosta, jonka tuntomerkit on peitetty millään tavalla maalilla tai väriaineella, saa esittää tarkastuksessa.",
    },
    "fi-vmp-0096-v1": {
        "STEM": "Kuinka monta parhaiten sijoittunutta hevosta otetaan yksilökilpailuissa yleensä testattavaksi kilpailusääntöjen kohdan 275.1.4.2 mukaan?",
        "OPTION_A": "Yksi",
        "OPTION_B": "Kaksi",
        "OPTION_C": "Kolme",
        "OPTION_D": "Viisi",
        "EXPLANATION": "Kilpailusääntöjen kohdan 321 a-alakohdassa todetaan, että yksilökilpailujen finaaleissa testataan yleensä kolme parhaiten sijoittunutta hevosta.",
    },
    "fi-vmp-0096-v2": {
        "STEM": "Kuinka monta hevosta kustakin kolmesta parhaiten sijoittuneesta joukkueesta otetaan yleensä testattavaksi joukkuekilpailun finaalissa kilpailusääntöjen kohdan 275.1.4.2 mukaan?",
        "OPTION_A": "Kaikki joukkueen hevoset",
        "OPTION_B": "Kaksi",
        "OPTION_C": "Yksi",
        "OPTION_D": "Ei yhtään",
        "EXPLANATION": "Kilpailusääntöjen kohdan 321 b-alakohdan mukaan näyte otetaan yleensä yhdestä hevosesta kustakin kolmesta parhaiten sijoittuneesta joukkueesta.",
    },
    "fi-vmp-0096": {
        "STEM": "Mitkä hevoset testataan yleensä EADCM-testeissä olympialaisissa ja mannerkisoissa, FEI:n esteratsastuksen maailmancupin™ finaaleissa, Longines League of Nations™ -finaaleissa sekä maailman- ja mannermestaruuskilpailuissa?",
        "OPTION_A": "Kolme parhaiten sijoittunutta hevosta yksilökilpailujen finaaleissa",
        "OPTION_B": "Yksi hevonen kustakin kolmesta parhaiten sijoittuneesta joukkueesta joukkuekilpailujen finaaleissa",
        "OPTION_C": "Jokainen hevonen jokaisessa kilpailussa",
        "OPTION_D": "Vain ne hevoset, jotka kieltäytyvät tarkastuksesta",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 275.1.4.2 todetaan, että näytteitä on otettava riittävältä määrältä hevosia sen varmistamiseksi, että a) yksilökilpailujen finaaleissa näyte otetaan kolmesta parhaiten sijoittuneesta hevosesta ja b) joukkuekilpailujen finaaleissa yhdestä hevosesta kustakin kolmesta parhaiten sijoittuneesta joukkueesta.",
    },
    "fi-vmp-0097-v1": {
        "STEM": "Mitkä määräykset koskevat nimenomaan hevosten antidopingia ja valvottua lääkitystä?",
        "OPTION_A": "FEI:n säännöt",
        "OPTION_B": "FEI:n hevosten antidoping- ja valvotun lääkityksen määräykset",
        "OPTION_C": "Vain FEI:n yleiset säännöt",
        "OPTION_D": "Vain esteratsastuksen kilpailusäännöt",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 275.2 viitataan hevosten antidoping- ja valvotun lääkityksen määräyksiin osana lääkitysvalvonnan säännöstöä.",
    },
    "fi-vmp-0097-v2": {
        "STEM": "Minkä sääntöjen mukaisesti hevosten lääkitysvalvonta suoritetaan esteratsastuskilpailuissa kilpailusääntöjen kohdan 275.2 mukaan?",
        "OPTION_A": "Vain esteratsastuksen kilpailusääntöjen",
        "OPTION_B": "Vain yleisten sääntöjen ja eläinlääkintämääräysten",
        "OPTION_C": "Yleisten sääntöjen, eläinlääkintämääräysten, hevosten antidoping- ja valvotun lääkityksen määräysten sekä muiden sovellettavien FEI:n sääntöjen ja määräysten",
        "OPTION_D": "Vain kilpailukutsun",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 275.2 todetaan, että lääkitysvalvonta on suoritettava yleisten sääntöjen, eläinlääkintämääräysten, hevosten antidoping- ja valvotun lääkityksen määräysten sekä muiden sovellettavien FEI:n sääntöjen ja määräysten mukaisesti.",
    },
    "fi-vmp-0097": {
        "STEM": "Minkä määräysten mukaisesti hevosten lääkitysvalvonta on suoritettava kilpailusääntöjen kohdan 275.2 mukaan?",
        "OPTION_A": "Vain esteratsastuksen kilpailusääntöjen",
        "OPTION_B": "Yleisten sääntöjen, eläinlääkintämääräysten, hevosten antidoping- ja valvotun lääkityksen määräysten sekä muiden sovellettavien FEI:n sääntöjen ja määräysten",
        "OPTION_C": "Vain eläinlääkintämääräysten",
        "OPTION_D": "Vain hevosten antidopingmääräysten",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 275.2 todetaan, että hevosten lääkitysvalvonta on suoritettava yleisten sääntöjen, eläinlääkintämääräysten, hevosten antidoping- ja valvotun lääkityksen määräysten sekä muiden sovellettavien FEI:n sääntöjen ja määräysten mukaisesti.",
    },
    "fi-vmp-0098-v1": {
        "STEM": "Mitä kilpailusääntöjen kohdan 275.3.2 mukaan seuraa ensimmäisellä kerralla siitä, ettei hevosen tunnistenumero ole selvästi näkyvillä?",
        "OPTION_A": "Suorituksen hylkääminen",
        "OPTION_B": "Varoitus",
        "OPTION_C": "Sakko",
        "OPTION_D": "Kilpailusta sulkeminen",
        "EXPLANATION": "Kilpailusääntöjen kohdan 321 mukaan tunnistenumeron esilläpidon laiminlyönnistä annetaan ensin varoitus, ja toistuvasta rikkomuksesta tuomaristo voi määrätä sakon.",
    },
    "fi-vmp-0098-v2": {
        "STEM": "Kuka antaa hevoselle tunnistenumeron, jota sen on kilpailusääntöjen kohdan 275.3.2 mukaan käytettävä poistuessaan talleilta?",
        "OPTION_A": "Urheilija",
        "OPTION_B": "Joukkueenjohtaja",
        "OPTION_C": "Järjestäjä",
        "OPTION_D": "FEI",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 275.3.2 todetaan, että järjestäjä antaa jokaiselle hevoselle tunnistenumeron.",
    },
    "fi-vmp-0098-v3": {
        "STEM": "Mitä kilpailusääntöjen kohdan 275.3.2 mukaan voi seurata siitä, ettei hevosen tunnistenumeroa toistuvasti pidetä selvästi näkyvillä?",
        "OPTION_A": "Pelkkä varoitus",
        "OPTION_B": "Sakko",
        "OPTION_C": "Suorituksen hylkääminen",
        "OPTION_D": "Kilpailusta sulkeminen",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 321 määrätään, että ensimmäisestä rikkomuksesta annetaan varoitus ja että toistuvasta rikkomuksesta tuomaristo voi määrätä urheilijalle sakon.",
    },
    "fi-vmp-0098": {
        "STEM": "Milloin hevosella on oltava järjestäjän antama tunnistenumero?",
        "OPTION_A": "Vain kilpailusuorituksen aikana",
        "OPTION_B": "Aina kun se poistuu talleilta, koko kilpailun ajan",
        "OPTION_C": "Vain palkintojenjaon aikana",
        "OPTION_D": "Vain hevostarkastuksissa",
        "EXPLANATION": "Kilpailusääntöjen kohdassa 275.3.2 määrätään, että urheilijan on huolehdittava siitä, että hevosella on aina sama numero sen poistuessa talleilta koko kilpailun ajan.",
    },
}


def process(path):
    with open(path, "r", encoding="utf-8") as fh:
        lines = fh.read().split("\n")

    item_id = None
    for line in lines:
        if line.startswith("ID: "):
            item_id = line[4:].strip()
            break
    if item_id is None:
        return None, "ID puuttuu"
    if item_id not in FIX:
        return False, "ei korjauksia sanakirjassa"

    fixes = dict(FIX[item_id])
    out = []
    changed = False
    for line in lines:
        if ":" in line:
            key = line.split(":", 1)[0]
            if key in EDIT_FIELDS and key in fixes:
                new_line = "%s: %s" % (key, fixes.pop(key))
                if new_line != line:
                    changed = True
                out.append(new_line)
                continue
        out.append(line)

    if fixes:
        return None, "kentät puuttuvat tiedostosta: %s" % ", ".join(sorted(fixes))

    if changed:
        with open(path, "w", encoding="utf-8") as fh:
            fh.write("\n".join(out))
    return changed, item_id


def main():
    domains = ("penalty-tables", "time-speed", "vet-medication-passports")
    checked = modified = 0
    problems = []
    for domain in domains:
        folder = os.path.normpath(os.path.join(ROOT, domain))
        for name in sorted(os.listdir(folder)):
            if not name.endswith(".txt"):
                continue
            checked += 1
            status, info = process(os.path.join(folder, name))
            if status is None:
                problems.append("%s/%s: %s" % (domain, name, info))
            elif status:
                modified += 1
            else:
                problems.append("%s/%s: %s" % (domain, name, info))
    print("Tarkistettu: %d tiedostoa" % checked)
    print("Muutettu:    %d tiedostoa" % modified)
    for p in problems:
        print("HUOM: %s" % p)
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
