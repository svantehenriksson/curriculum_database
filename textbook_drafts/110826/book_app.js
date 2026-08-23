const grade7Titles = [
  "Lukukäsitys",
  "Laskujärjestys",
  "Murtoluvun merkitys",
  "Murtolukujen yhteen- ja vähennyslasku",
  "Murtolukujen kerto- ja jakolasku",
  "Desimaalilaskut ja pyöristys",
  "Prosentin perusidea",
  "Prosenttiosuus",
  "Suhde ja verrannollisuus",
  "Yksikköhinta",
  "Muuttuja ja tuntematon",
  "Lauseke tekstistä",
  "Lausekkeen arvo",
  "Lausekkeen sievennys",
  "Yhden vaiheen yhtälöt",
  "Kahden vaiheen yhtälöt",
  "Koordinaatisto",
  "Ruudukon etäisyydet",
  "Suorat, janat ja säteet",
  "Kulmien mittaaminen",
  "Kulmasuhteet",
  "Kolmiot",
  "Nelikulmiot",
  "Monikulmion piiri",
  "Peruspinta-alat",
  "Pinta-alayksiköt",
  "Datan keruu",
  "Diagrammien tulkinta",
  "Keskiarvo, mediaani, moodi",
  "Todennäköisyyden perusidea",
  "Ongelmanratkaisun malli",
  "Digitaalinen matematiikkavihko",
  "7. luokan synteesi",
];

const grade8Titles = [
  "Lukusujuvuuden kertaus",
  "Monivaiheiset prosentit",
  "Prosenttimuutos",
  "Suora verrannollisuus",
  "Kääntäen verrannollisuus",
  "Verrannollisuuden kuvaajat",
  "Potenssit",
  "Juuret",
  "Tieteellinen merkintä",
  "Lausekkeet potensseilla",
  "Polynomit",
  "Lineaarinen yhtälö tilanteesta",
  "Yhtälö parametreilla",
  "Epäyhtälöiden perusteet",
  "Suora koordinaatistossa",
  "Funktion käsite",
  "Lineaarisen funktion muodot",
  "Lukujonot",
  "Yhdenmuotoisuus ja mittakaava",
  "Yhtenevyys",
  "Pythagoraan lause",
  "Ympyrä",
  "Yhdistetyt pinta-alat",
  "Kappaleiden pinta-alat",
  "Tasomuunnokset",
  "Tilastot: jakauma ja vaihtelu",
  "Hajontakuvio ja trendi",
  "Yhdistetyt todennäköisyydet",
  "GeoGebra ja taulukkolaskenta",
  "Ohjelmoinnin minilabra",
  "Poikkiaineinen mallinnus",
  "Ratkaisuesitys ja vertaispalaute",
  "8. luokan päätösprojekti",
];

const grade9Titles = [
  "Rationaaliluvut ja tarkistus",
  "Lausekkeiden koonti",
  "Yhtälöperheiden kertaus",
  "Yhtälöryhmä kuvaajalla",
  "Yhtälöryhmä algebrallisesti",
  "Yhtälöryhmän tulkinta",
  "Epäyhtälöt",
  "Yhdistetyt epäyhtälöt",
  "Funktion syventäminen",
  "Funktioiden vertailu",
  "Paloittaiset ja epälineaariset mallit",
  "Kasvumallit",
  "Potenssi- ja juurikoonti",
  "Reaaliluvut malleissa",
  "Koordinaattigeometrian sovellukset",
  "Geometrian perusteleva päättely",
  "Ympyrägeometrian sovellukset",
  "Piiri-pinta-ala-tilavuus",
  "Tilavuus: lieriö, kartio, pallo",
  "Mittausepävarmuus",
  "Otanta ja harha",
  "Tilastollinen vertailu",
  "Todennäköisyysmallit",
  "Talousmatematiikka",
  "Talousmallit taulukkolaskennalla",
  "Simulointiprojekti ohjelmoiden",
  "Optimointitehtävät",
  "Monivaiheinen mallintaminen",
  "Data-analyysi poikkiaineisesti",
  "Koetyyppinen sekasarja A",
  "Koetyyppinen sekasarja B",
  "Portfolioviimeistely",
  "Siirtymä 2. asteelle",
  "9. luokan päätösprojekti",
];

function idFor(grade, index1) {
  return `g${grade}-${String(index1).padStart(2, "0")}`;
}

const detailedChapterBodies = {
  "g7-01": `
    <p class="meta">7. luokka • Luku 1 • Taitolanka: paattely ja paassalaskun tarkistus</p>
    <h3>Mika on lukukasitys?</h3>
    <p>
      Lukukasitys tarkoittaa, etta ymmarrat lukujen suuruusluokan, osaat vertailla lukuja
      ja tunnistat nopeasti, onko vastaus suurin piirtein järkevä. Tama luku rakentaa
      perustan koko ylakoulun matematiikalle.
    </p>
    <div class="note">
      Tavoite: oppilas osaa arvioida vastauksia ennen tarkkaa laskua, ei vain "laskea nappia painamalla".
    </div>

    <h3>Keskeiset ideat</h3>
    <ul>
      <li>Kokonaisluvut, negatiiviset luvut ja niiden paikka lukusuoralla.</li>
      <li>Suuruusluokan arviointi (esim. 398 x 52 on lahella 400 x 50).</li>
      <li>Vertaaminen: kumpi on suurempi ja miksi?</li>
      <li>Jarkevyystarkistus: onko vastaus liian pieni tai liian suuri tilanteeseen nähden?</li>
    </ul>

    <div class="image-idea">[KUVITUSIDEA: Lukusuora, jossa korostetaan negatiiviset luvut, nolla ja positiiviset luvut eri vareilla.]</div>
    <div class="image-idea">[KUVITUSIDEA: Arviointipuu: "Pyorista -> Laske karkeasti -> Vertaa tarkkaan vastaukseen".]</div>

    <h3>Ratkaistu esimerkki</h3>
    <p><strong>Tehtava:</strong> Arvioi ensin, laske sitten tarkasti: 198 + 304 - 97.</p>
    <p>
      Arvio: 200 + 300 - 100 = 400. Tarkka lasku: 198 + 304 = 502, 502 - 97 = 405.
      Tulos 405 on lahella arviota 400, joten vastaus on uskottava.
    </p>

    <h3>Harjoituksia</h3>
    <div class="exercise"><strong>1.</strong> Jarjesta luvut pienimmasta suurimpaan: -12, 0, -3, 8, -1, 5.</div>
    <div class="exercise"><strong>2.</strong> Arvioi ensin, laske sitten: 49 x 21.</div>
    <div class="exercise"><strong>3.</strong> Onko 27 + 18 = 65 mahdollinen? Perustele ilman tarkkaa laskua.</div>
    <div class="exercise"><strong>4.</strong> Keksi oma "liian suuri/liian pieni" -esimerkki ja korjaa se.</div>
    <div class="exercise"><strong>5.</strong> Piirra lukusuora valilla -10...10 ja merkitse luvut -7, -2, 0, 4, 9.</div>
  `,
  "g7-02": `
    <p class="meta">7. luokka • Luku 2 • Taitolanka: matemaattinen viestinta (vaiheiden kirjoittaminen)</p>
    <h3>Laskujarjestyksen idea</h3>
    <p>
      Laskujarjestys tekee laskuista yksiselitteisia. Kun kaikki noudattavat samoja saantoja,
      sama lauseke antaa saman tuloksen riippumatta laskijasta.
    </p>
    <ul>
      <li>1) Sulut</li>
      <li>2) Kerto- ja jakolaskut vasemmalta oikealle</li>
      <li>3) Yhteen- ja vahennyslaskut vasemmalta oikealle</li>
    </ul>
    <div class="image-idea">[KUVITUSIDEA: "Laskujarjestyksen liikennevalo": punainen=sulut, keltainen=kerto/jako, vihrea=plus/miinus.]</div>

    <h3>Ratkaistu esimerkki</h3>
    <p><strong>Tehtava:</strong> Laske 4 + 3 x (10 - 6).</p>
    <p>
      Ensin sulut: (10 - 6) = 4. Sitten kertolasku: 3 x 4 = 12.
      Lopuksi yhteenlasku: 4 + 12 = 16.
    </p>

    <h3>Tyypillinen virhe</h3>
    <p>
      Jos lasketaan vasemmalta oikealle ilman saantoja: 4 + 3 = 7, 7 x 4 = 28.
      Tama on vaarin, koska kertolasku piti tehda ennen yhteenlaskua.
    </p>

    <h3>Harjoituksia</h3>
    <div class="exercise"><strong>1.</strong> Laske: 5 + 2 x 9.</div>
    <div class="exercise"><strong>2.</strong> Laske: (12 - 4) x 3 + 1.</div>
    <div class="exercise"><strong>3.</strong> Kirjoita kaksi eri lauseketta, jotka antavat tuloksen 18.</div>
    <div class="exercise"><strong>4.</strong> Korjaa virhe: (8 + 2) x 5 = 8 + 10 = 18.</div>
    <div class="exercise"><strong>5.</strong> Selita sanoin, miksi 3 + 4 x 2 != (3 + 4) x 2.</div>
  `,
  "g7-03": `
    <p class="meta">7. luokka • Luku 3 • Taitolanka: esitystapojen vaihto (kuva-sana-symboli)</p>
    <h3>Murtoluku kolmella tavalla</h3>
    <p>
      Murtoluku voidaan tulkita (1) osana kokonaisuutta, (2) jakolaskuna ja (3) suhteena.
      Sama symboli voi tarkoittaa eri tilanteissa eri asiaa.
    </p>

    <h3>Keskeiset kasitteet</h3>
    <ul>
      <li>Osoittaja kertoo montako osaa otetaan.</li>
      <li>Nimittaja kertoo monenko osan kokoisesta jaosta puhutaan.</li>
      <li>Samanarvoiset murtoluvut kuvaavat samaa maarää eri muodossa.</li>
    </ul>

    <div class="image-idea">[KUVITUSIDEA: Sama 3/4 esitettyna pizzana, janalla ja jakolaskuna 3 : 4.]</div>
    <div class="note">
      Opettajan huomio: yhdista murtoluku heti lukusuoraan, jotta murtoluku ei jaa vain "piirakka-ajatteluksi".
    </div>

    <h3>Ratkaistu esimerkki</h3>
    <p><strong>Tehtava:</strong> Ovatko 2/3 ja 4/6 samanarvoiset?</p>
    <p>Kyllä, koska 2/3 x 2/2 = 4/6. Molemmat kuvaavat samaa kohtaa lukusuoralla.</p>

    <h3>Harjoituksia</h3>
    <div class="exercise"><strong>1.</strong> Merkitse lukusuoralle 1/2, 3/4 ja 5/4.</div>
    <div class="exercise"><strong>2.</strong> Kirjoita murtoluvulle 3/5 kaksi samanarvoista muotoa.</div>
    <div class="exercise"><strong>3.</strong> Selita, mita 7/3 tarkoittaa jakolaskuna.</div>
    <div class="exercise"><strong>4.</strong> Kumpi on suurempi: 2/7 vai 3/7? Perustele.</div>
    <div class="exercise"><strong>5.</strong> Keksi arjen esimerkki murtoluvusta suhteena.</div>
  `,
  "g7-04": `
    <p class="meta">7. luokka • Luku 4 • Taitolanka: virheanalyysi</p>
    <h3>Yhteen- ja vahennyslasku murtoluvuilla</h3>
    <p>
      Murtolukuja voi laskea yhteen tai vahentaa vasta, kun nimittajat ovat samat.
      Siksi etsitään ensin yhteinen nimittäjä.
    </p>

    <h3>Toimintamalli</h3>
    <ol>
      <li>Etsi yhteinen nimittaja.</li>
      <li>Muunna murtoluvut saman nimittajan murtoluvuiksi.</li>
      <li>Laske osoittajat yhteen tai vahenna.</li>
      <li>Sievenna tarvittaessa.</li>
    </ol>

    <div class="image-idea">[KUVITUSIDEA: Yhteisen nimittajan "tikas": 1/3 -> 2/6, 1/2 -> 3/6.]</div>

    <h3>Ratkaistu esimerkki</h3>
    <p><strong>Tehtava:</strong> Laske 1/3 + 1/2.</p>
    <p>Yhteinen nimittaja 6. Muunnetaan: 1/3 = 2/6, 1/2 = 3/6. Siis 2/6 + 3/6 = 5/6.</p>

    <h3>Tyypillinen virhe</h3>
    <p>Virhe: 1/3 + 1/2 = 2/5. Nimittajia ei saa laskea suoraan yhteen.</p>

    <h3>Harjoituksia</h3>
    <div class="exercise"><strong>1.</strong> Laske: 3/8 + 1/4.</div>
    <div class="exercise"><strong>2.</strong> Laske: 5/6 - 1/3.</div>
    <div class="exercise"><strong>3.</strong> Laske: 7/10 + 9/20.</div>
    <div class="exercise"><strong>4.</strong> Etsi virhe ja korjaa: 2/5 + 1/3 = 3/8.</div>
    <div class="exercise"><strong>5.</strong> Muodosta oma tehtava, jossa vastaus on 11/12.</div>
  `,
  "g7-05": `
    <p class="meta">7. luokka • Luku 5 • Taitolanka: menetelman valinta</p>
    <h3>Murtolukujen kerto- ja jakolasku</h3>
    <p>
      Kertolaskussa kerrotaan osoittajat keskenaan ja nimittajat keskenaan.
      Jakolaskussa kerrotaan jakoluvun kaanteisluvulla.
    </p>

    <h3>Saannot</h3>
    <ul>
      <li>(a/b) x (c/d) = (ac)/(bd)</li>
      <li>(a/b) : (c/d) = (a/b) x (d/c), kun c != 0</li>
      <li>Ristiinsupistus kannattaa tehda ennen kertolaskua.</li>
    </ul>

    <div class="image-idea">[KUVITUSIDEA: "Kaanteisluku-kortit", joissa oppilas parittaa luvun ja sen kaanteisluvun.]</div>
    <div class="note">
      Edullinen fyysinen idea: kaanteisluku- ja supistuskortit pareittain ratkaistaviin "nopeuskierroksiin".
    </div>

    <h3>Ratkaistu esimerkki</h3>
    <p><strong>Tehtava:</strong> Laske (3/4) : (2/5).</p>
    <p>
      Muutetaan jakolasku kertolaskuksi: (3/4) x (5/2) = 15/8 = 1 7/8.
    </p>

    <h3>Harjoituksia</h3>
    <div class="exercise"><strong>1.</strong> Laske: (2/3) x (9/10).</div>
    <div class="exercise"><strong>2.</strong> Laske: (5/6) : (1/4).</div>
    <div class="exercise"><strong>3.</strong> Laske: (7/8) x (4/21) mahdollisimman paljon supistaen.</div>
    <div class="exercise"><strong>4.</strong> Selita sanoin, miksi kaanteisluku toimii jakolaskussa.</div>
    <div class="exercise"><strong>5.</strong> Muodosta oma tarinatehtava, jossa kaytetaan murtolukujen jakolaskua.</div>
  `,
};

function makePlaceholderBody(grade, index, title) {
  return `
    <p class="meta">${grade}. luokka • Luku ${index}</p>
    <p class="placeholder">
      Tama luku on toistaiseksi placeholder-versio. Se taydennetaan seuraavassa sisaltopassissa
      samalla rakenteella kuin luvut 1-5: selitys, kuvitusideat, ratkaistut esimerkit ja harjoitukset.
    </p>
    <div class="image-idea">[KUVITUSIDEA: lisataan seuraavassa versiossa aiheeseen sopiva kaavio tai tilannekuva.]</div>
    <h3>Tavoite (placeholder)</h3>
    <ul>
      <li>Keskeinen kasite 1: ${title}</li>
      <li>Keskeinen kasite 2: soveltava tehtavatyyppi</li>
      <li>Keskeinen kasite 3: taitolanka + itsearviointi</li>
    </ul>
  `;
}

function buildChapterList() {
  const chapters = [];

  grade7Titles.forEach((title, idx) => {
    const n = idx + 1;
    const id = idFor(7, n);
    chapters.push({
      id,
      grade: 7,
      index: n,
      title,
      full: n <= 5,
      body:
        detailedChapterBodies[id] ||
        makePlaceholderBody(7, n, title),
    });
  });

  grade8Titles.forEach((title, idx) => {
    const n = idx + 1;
    chapters.push({
      id: idFor(8, n),
      grade: 8,
      index: n,
      title,
      full: false,
      body: makePlaceholderBody(8, n, title),
    });
  });

  grade9Titles.forEach((title, idx) => {
    const n = idx + 1;
    chapters.push({
      id: idFor(9, n),
      grade: 9,
      index: n,
      title,
      full: false,
      body: makePlaceholderBody(9, n, title),
    });
  });

  return chapters;
}

const chapters = buildChapterList();
const chapterById = Object.fromEntries(chapters.map((c) => [c.id, c]));

function renderNav() {
  const nav = document.getElementById("chapter-nav");
  const byGrade = { 7: [], 8: [], 9: [] };
  chapters.forEach((c) => byGrade[c.grade].push(c));

  const gradeNames = {
    7: "7. luokka",
    8: "8. luokka",
    9: "9. luokka",
  };

  nav.innerHTML = "";
  [7, 8, 9].forEach((grade) => {
    const block = document.createElement("div");
    block.className = "grade-block";

    const title = document.createElement("h3");
    title.className = "grade-title";
    title.textContent = `${gradeNames[grade]} (${byGrade[grade].length} lukua)`;
    block.appendChild(title);

    byGrade[grade].forEach((chapter) => {
      const a = document.createElement("a");
      a.href = `#${chapter.id}`;
      a.className = "chapter-link";
      a.dataset.chapterId = chapter.id;
      a.textContent = `${chapter.index}. ${chapter.title}${chapter.full ? "" : " [placeholder]"}`;
      block.appendChild(a);
    });

    nav.appendChild(block);
  });
}

function renderChapter(chapterId) {
  const chapter = chapterById[chapterId] || chapters[0];
  const view = document.getElementById("chapter-view");
  view.innerHTML = `
    <h2>${chapter.grade}. luokka, luku ${chapter.index}: ${chapter.title}</h2>
    ${chapter.body}
  `;

  document.querySelectorAll(".chapter-link").forEach((el) => {
    el.classList.toggle("active", el.dataset.chapterId === chapter.id);
  });
}

function currentChapterIdFromHash() {
  const id = location.hash.replace("#", "").trim();
  if (id && chapterById[id]) {
    return id;
  }
  return chapters[0].id;
}

function init() {
  renderNav();
  renderChapter(currentChapterIdFromHash());
}

window.addEventListener("hashchange", () => {
  renderChapter(currentChapterIdFromHash());
});

init();
