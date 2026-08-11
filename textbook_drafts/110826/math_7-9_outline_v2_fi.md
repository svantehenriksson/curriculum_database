# Matematiikka 7-9 Runko (v2, FI)

<!--
PERUSTELU:
- Tämä versio pohjautuu paikallisten OPS-aineistojen passi-3.1 -signaaliin.
- Painotukset on johdettu erityisesti näistä tuotoksista:
  - data/derived/math_grade_7_9_first_pass.md
  - data/derived/math_topic_candidates_7_9_pass2.jsonl
  - data/derived/math_topic_consensus_7_9_pass3.md
  - data/derived/math_topic_consensus_matrix_7_9_pass3.jsonl
- Menetelmäputki, jolla signaalit tuotettiin:
  - scripts/extract_math_7_9.py
  - scripts/extract_math_topic_candidates.py
  - scripts/cluster_math_topics_pass3.py
- Tulkinta:
  - 7. lk: vahva peruslaskenta + lausekkeet/muuttujat + geometrian peruskieli
  - 8. lk: algebra laajenee, verrannollisuus ja prosentit korostuvat
  - 9. lk: funktiot, yhtälöryhmät/epäyhtälöt, mallintaminen ja 2. asteen valmiudet
- Läpileikkaavat taidot (digitaalisuus, päättely, viestintä, itseohjautuvuus) toistuvat, koska ne näkyvät paikallisissa tavoitteissa eksplisiittisesti.
-->

## 7. luokka (33 aihetta)

<!-- Muotoilu: paikallinen signaali painottaa murtolukuja, desimaaleja, lausekkeita ja kulma/suora-geometriaa. -->

1. Lukukäsitys: kokonaisluvut, suuruusluokka, arviointi.  
   Taitolanka: päättely ja päässälaskun tarkistus.
2. Laskujärjestys kokonais- ja desimaaliluvuilla.  
   Taitolanka: matemaattinen viestintä (vaiheiden näkyvä kirjaus).
3. Murtoluvut määrinä, operaattoreina ja suhteina.  
   Taitolanka: esitystapojen vaihto (symboli-kuvio-sana).  
   Pelillinen idea: React-"murtoliukuri" nopeilla visuaalisilla palautteilla.
4. Murtolukujen yhteen- ja vähennyslasku eri nimittäjillä.  
   Taitolanka: virheanalyysi.
5. Murtolukujen kerto- ja jakolasku.  
   Taitolanka: menetelmän valinta.
6. Desimaalilaskut ja pyöristäminen kontekstissa.  
   Taitolanka: järkevyysarvio.
7. Prosentti "sadasta osasta"; yhteys murtolukuihin ja desimaaleihin.  
   Taitolanka: käsitteiden linkitys.
8. Prosenttiosuuden laskeminen (1-vaiheiset tehtävät).  
   Taitolanka: arjen mallintaminen.
9. Suhteen kieli ja verrannolliset suhteet.  
   Taitolanka: verrannollisuusajattelun perusta.
10. Yksikköhinta ja vertailutehtävät.  
    Taitolanka: datasta perusteleminen.
11. Muuttuja ja tuntematon: merkitys ja merkintä.  
    Taitolanka: symbolinen sujuvuus.
12. Lausekkeen muodostaminen tekstistä.  
    Taitolanka: matemaattinen viestintä.
13. Lausekkeen arvon laskeminen sijoittamalla.  
    Taitolanka: laskennallinen tarkkuus.
14. Lausekkeiden sieventäminen (samanmuotoiset termit).  
    Taitolanka: rakenteen tunnistaminen.
15. Yhden vaiheen yhtälöt tasapainomallilla.  
    Taitolanka: käänteisoperaatioiden päättely.
16. Kahden vaiheen yhtälöt ja ratkaisun tarkistus.  
    Taitolanka: itseohjautuvuus (aina tarkistus).
17. Koordinaatisto: neljännekset ja pisteiden kuvaaminen.  
    Taitolanka: digityökalut (kuvaajat).  
    Pelillinen idea: React-"koordinaattien valtaus" -ruutupeli.
18. Pisteiden lukeminen, etäisyys ja yksinkertaiset reitit ruudukossa.  
    Taitolanka: avaruudellinen hahmotus.
19. Suorat, janat, säteet ja kulmasanasto.  
    Taitolanka: täsmällinen terminologia.
20. Kulmien mittaaminen ja konstruktiot.  
    Taitolanka: välineosaaminen (viivain/harppi/astelevy).  
    Edullinen fyysinen idea: astelevyt + minitaulut.
21. Kulmasuhteet (vastinkulmat, oikokulmapari, komplementti).  
    Taitolanka: perustelun kieli.
22. Kolmiot: luokittelu ja kulmasumma.  
    Taitolanka: ominaisuuksista päättely.
23. Nelikulmiot: perheet ja ominaisuudet.  
    Taitolanka: määritelmien vertailu.
24. Monikulmioiden piiri käytännön tehtävissä.  
    Taitolanka: mallintaminen.
25. Suorakulmion, kolmion ja suunnikkaan pinta-ala.  
    Taitolanka: yksikköajattelu.
26. Pinta-alayksiköiden muunnokset (perus).  
    Taitolanka: yksikkötarkkuus.
27. Datan keruu ja selkeä taulukointi.  
    Taitolanka: datalukutaito.
28. Pylväs- ja viivadiagrammien tulkinta.  
    Taitolanka: kriittinen lukeminen.
29. Keskiarvo, mediaani, moodi pienissä aineistoissa.  
    Taitolanka: sopivan tunnusluvun valinta.
30. Todennäköisyyden perusidea (tasatodennäköiset tapaukset).  
    Taitolanka: koe vs odotusarvo.  
    Edullinen fyysinen idea: noppa- ja korttiasemat.
31. Ongelmanratkaisun perusprotokolla: ymmärrä-suunnittele-ratkaise-tarkista.  
    Taitolanka: itseohjautuvuus.
32. Digitaalinen matematiikkavihko (vaiheet + kuvakaappaukset).  
    Taitolanka: digitaalinen työskentely ja organisointi.
33. 7. luokan synteesiprojekti: "Matematiikka omassa viikossa".  
    Taitolanka: mallintaminen + viestintä.

## 8. luokka (33 aihetta)

<!-- Muotoilu: passi-3.1 nostaa vahvasti esiin lausekkeet, prosentit, verrannollisuuden ja geometrian jatkon; ohjelmointi/digityökalut säilyvät näkyvinä. -->

1. Kokonais- ja murtolukujen sujuvuuden kertaus.  
   Taitolanka: tehokas strategian valinta.
2. Monivaiheiset prosenttitehtävät (alennus, vero, korotus).  
   Taitolanka: mallintaminen.
3. Prosenttimuutos ja vertailuprosentti.  
   Taitolanka: tulkinta ja viestintä.
4. Suora verrannollisuus ja skaalaus.  
   Taitolanka: funktionaalinen ajattelu.
5. Kääntäen verrannollisuus käytännössä.  
   Taitolanka: mallin kriittinen arviointi.
6. Verrannollisuuden kuvaajat ja kulmakertoimen intuitio.  
   Taitolanka: digitaalinen kuvaajatulkinta.
7. Potenssit ja potenssisäännöt (kokonaiseksponentit).  
   Taitolanka: symbolinen rakenne.
8. Juuret ja neliöjuuren arviointi.  
   Taitolanka: järkevyysarvio.
9. Tieteellinen merkintä ja suuruusluokkavertailu.  
   Taitolanka: esitystapojen sujuvuus.
10. Lausekkeiden sieventäminen potensseilla.  
    Taitolanka: algebrallinen tarkkuus.
11. Polynomit: yhteen-, vähennys- ja peruskertolasku.  
    Taitolanka: rakenteen tunnistaminen.
12. Lineaariset yhtälöt taulukoista ja tilanteista.  
    Taitolanka: mallin rakentaminen.
13. Yhtälöiden ratkaiseminen parametreilla ja ehdoilla.  
    Taitolanka: päättely + validointi.
14. Epäyhtälöiden perusteet ja ratkaisun tulkinta.  
    Taitolanka: joukkojen täsmällinen ilmaisu.
15. Koordinaattigeometria: suora, kulmakerroin, vakiotermi.  
    Taitolanka: kuvaajien viestintä.
16. Funktion käsite: syöte-lähtö, määrittelyjoukko, merkintä.  
    Taitolanka: abstrahointi.
17. Lineaarisen funktion esitysmuodot.  
    Taitolanka: muunnos muodosta toiseen.
18. Lukujonot: rekursiivinen ja eksplisiittinen esitys.  
    Taitolanka: säännön yleistys.
19. Yhdenmuotoisuus, mittakaava ja karttatehtävät.  
    Taitolanka: verrannollisuusajattelu.
20. Yhtenevyys ja geometrian perustelut.  
    Taitolanka: todistusvalmius.
21. Pythagoraan lause sovelluksissa.  
    Taitolanka: strateginen ongelmanratkaisu.  
    Pelillinen idea: React-"Pythagoras-palapeli".
22. Ympyrä: kehän pituus ja pinta-ala.  
    Taitolanka: kaavapäättely.
23. Yhdistetyt pinta-alat ja osiin pilkkominen.  
    Taitolanka: ratkaisun suunnittelu.
24. Kappaleiden pinta-alan perusteet (esim. särmiö/lieriö).  
    Taitolanka: verkon hahmotus.
25. Tasomuunnokset (siirto, kierto, peilaus).  
    Taitolanka: geometrian viestintä.
26. Tilastot: jakauma, vaihtelu, poikkeavat havainnot.  
    Taitolanka: kriittinen dataluku.
27. Kahden muuttujan data: hajontakuvio ja trendi.  
    Taitolanka: väitteet evidenssillä.
28. Todennäköisyys: yhdistetyt tapahtumat (intro).  
    Taitolanka: epävarmuuspäättely.
29. GeoGebra/taulukkolaskenta algebra- ja tilastotutkimuksissa.  
    Taitolanka: digityökalut.  
    Edullinen idea: QR-tehtäväpolku + laitevaunu.
30. Ohjelmoinnin minilabra: matemaattisen säännön generoija.  
    Taitolanka: algoritminen ajattelu.
31. Poikkiaineinen mallinnustehtävä (esim. luonnontiede/talous).  
    Taitolanka: osaamisen siirto.
32. Oppilaiden ratkaisuesitykset + vertaispalaute.  
    Taitolanka: matemaattinen viestintä.
33. 8. luokan päätösprojekti: "Mallinna, testaa, perustele".  
    Taitolanka: kokonainen ongelmanratkaisusykli.

## 9. luokka (34 aihetta)

<!-- Muotoilu: passi-3.1 näyttää vahvemman myöhäisvaiheen funktionäkymän, mukana epäyhtälöt/yhtälöryhmät, tilavuus ja jatko-opintovalmius. -->

1. Rationaalilukujen sujuvuus ja robusti tarkistus.  
   Taitolanka: systemaattinen itsekorjaus.
2. Lausekkeiden koonti: sievennä, avaa, tekijöihinjako (perus).  
   Taitolanka: rakenteellinen joustavuus.
3. Yhtälöperheiden kertaus (lineaarinen, rationaalinen, 2. asteen intro).  
   Taitolanka: menetelmän valinta.
4. Yhtälöryhmät kuvaajamenetelmällä.  
   Taitolanka: esitystapojen vertailu.
5. Yhtälöryhmät sijoitus- ja eliminointimenetelmällä.  
   Taitolanka: algoritminen sujuvuus.
6. Yhtälöryhmien tulkinta kontekstissa.  
   Taitolanka: mallin merkitystulkinta.
7. Epäyhtälöt ja väli-/joukkomerkintä.  
   Taitolanka: täsmällinen ilmaisu.
8. Yhdistetyt epäyhtälöt ja rajoitteet.  
   Taitolanka: looginen päättely.
9. Funktion syventäminen: kulmakerroin ja vakiotermi merkityksinä.  
   Taitolanka: käsitteellinen tulkinta.
10. Funktioiden vertailu ja mallin valinta.  
    Taitolanka: kriittinen arviointi.
11. Paloittaiset ja epälineaariset mallit (intro).  
    Taitolanka: abstrahointi.
12. Jonot ja kasvumallit (lineaarinen vs epälineaarinen).  
    Taitolanka: säännön päättely.
13. Potenssi- ja juurilaskennan koonti algebraan.  
    Taitolanka: symbolinen sujuvuus.
14. Reaalilukuoperaatiot monivaiheisissa malleissa.  
    Taitolanka: laskennallinen luotettavuus.
15. Koordinaattigeometria ja etäisyyssovellukset.  
    Taitolanka: algebra-geometria -linkki.
16. Geometrian suhteet ja perusteleva päättely.  
    Taitolanka: deduktiivinen argumentointi.
17. Ympyrägeometrian sovellukset.  
    Taitolanka: strateginen pilkkominen.
18. Piiri-pinta-ala-tilavuus integroituina tehtävinä.  
    Taitolanka: yksikkökurinalaisuus.
19. Lieriö, kartio, pallo: tilavuus ja pinta-ala kontekstissa.  
    Taitolanka: kaavojen mallintava käyttö.
20. Mittausepävarmuus ja pyöristyksen tarkoituksenmukaisuus.  
    Taitolanka: kriittinen arviointi.
21. Tilastot: otanta, harha, luotettavuus.  
    Taitolanka: datalukutaito.
22. Tilastollinen vertailu ja väitteiden laatu.  
    Taitolanka: evidenssiperusteinen argumentti.
23. Todennäköisyysmallit ja simuloinnin tarkistus.  
    Taitolanka: kokeellinen suunnittelu.
24. Talousmatematiikka: korko, maksuerät, vertailu.  
    Taitolanka: päätöksentekotaito.  
    Pelillinen idea: React-"budjettipeli" (laina/alennusvalinnat).
25. Taulukkolaskenta talousskenaarioiden mallinnuksessa.  
    Taitolanka: digityökalut.
26. Ohjelmoinnin miniprojekti: toistokokeiden simulointi.  
    Taitolanka: ohjelmointi + todennäköisyys.
27. Optimointityyppiset kontekstitehtävät.  
    Taitolanka: strategia + rajoitteet.
28. Monivaiheinen mallinnus eksplisiittisillä oletuksilla.  
    Taitolanka: mallin läpinäkyvyys.
29. Poikkiaineinen projekti: energia/ilmastoaineiston mallinnus.  
    Taitolanka: tulkinta ja siirtovaikutus.
30. Koetyyppinen sekasarja A (ydinosaaminen).  
    Taitolanka: ajankäyttö ja itseohjautuvuus.
31. Koetyyppinen sekasarja B (haaste ja laajennus).  
    Taitolanka: sinnikkyys ja reflektio.
32. Portfolioviimeistely: yhden vaativan ratkaisun esitys.  
    Taitolanka: matemaattinen viestintä.
33. Siirtymämoduuli: valmiudet 2. asteelle.  
    Taitolanka: tavoitteenasettelu ja opiskelustrategia.
34. 9. luokan päätösprojekti: "Datasta päätökseen".  
    Taitolanka: integroitu mallintaminen + kritiikki.

---

## Pelillistämisen konservatiivinen käyttö

<!--
Linjan perustelu:
- Paikalliset tavoitteet painottavat päättelyä, täsmällistä ilmaisua ja vastuullista työskentelyä.
- Siksi pelillistäminen pidetään kevyenä tukikeinona, ei rungon kantavana ideana.
-->

- Suositus: kevyt pelillistys noin 1/6-1/8 aiheessa.
- Käytä lyhyitä syklejä:
  - React-minityökalu/haaste (5-10 min)
  - nopea fyysinen asema edullisilla välineillä
- Pisteet toissijaisia; ratkaisun perustelu ensisijainen.
