const DATA_PATH = "../../data/read_with_chatgpt/ops_math_7_9_S1_S6_matrix.json";

const areaOrder = ["S1", "S2", "S3", "S4", "S5", "S6"];

const applicationFi = {
  "Predicting what happens next": "ennustetaan, mitä tapahtuu seuraavaksi",
  "Choices, schedules, passwords, probability":
    "tehdään valintoja, aikatauluja ja vaihtoehtolaskuja",
  "Central to all mathematics": "perustellaan ratkaisu niin, että se kestää tarkistuksen",
  "Problems, science, finance": "tehtävissä, luonnontieteissä ja rahalaskuissa",
  "Why mathematics gives certainty": "nähdään, miksi tulos on varmasti tosi",
  "Critical reasoning": "arvioidaan väitteitä kriittisesti",
  "Programming and systematic problem-solving":
    "ohjelmoinnissa ja järjestelmällisessä ongelmanratkaisussa",
  "Automation, simulation": "automaatiossa ja simuloinnissa",
  "Real-world mathematics and data": "arkidatan tulkinnassa",
  "Temperature, debt, height relative to sea level":
    "lämpötiloissa, veloissa ja korkeuseroissa",
  "Portions, ratios, probability": "annoksissa, suhteissa ja todennäköisyyksissä",
  "Signed quantities": "etumerkillisissä suureissa",
  "Fractions, algebra": "murtoluvuissa ja algebrassa",
  "Distance/error/deviation": "etäisyyksissä, virheissä ja poikkeamissa",
  "Needed for roots and continuous quantities":
    "juurissa ja jatkuvissa suureissa",
  "Fractions, factors, number theory":
    "murtoluvuissa, tekijöissä ja lukujen rakenteessa",
  "Simplifying fractions, structure of integers":
    "murtolukujen sieventämisessä ja lukujen rakenteessa",
  "Money, measurement": "rahassa ja mittauksissa",
  "Measurement and science": "mittauksissa ja luonnontieteissä",
  "Measurements, estimates": "mittauksissa ja arvioinneissa",
  "Ubiquitous everyday numeracy": "arkisissa prosenttitilanteissa",
  "Surveys, statistics": "kyselyissä ja tilastoissa",
  "VAT, discounts, interest": "alennuksissa, veroissa ja koroissa",
  "Original price, population":
    "alkuperäisen hinnan tai määrän selvittämisessä",
  "Price changes, interest": "hinnanmuutoksissa ja korkolaskuissa",
  "Economics, population, measurements":
    "talousluvuissa, väestötiedoissa ja mittauksissa",
  "Prices, salaries, statistics": "hinnoissa, palkoissa ja tilastoissa",
  "Scale, science, exponential quantities":
    "mittakaavoissa, luonnontieteissä ja kasvumalleissa",
  "Geometry, Pythagoras": "geometriassa ja pituuslaskuissa",
  "Generalising relationships": "riippuvuuksien yleistämisessä",
  "Formulas everywhere": "kaavojen käytössä",
  "Makes algebra manageable": "algebran selkeyttämisessä",
  "Algebra/science": "algebrassa ja luonnontieteissä",
  "Foundation for later algebra": "jatkoalgebran perustana",
  "Algebraic modelling": "tilanteiden mallintamisessa algebralla",
  "Geometry/formulas/later algebra":
    "geometriassa, kaavoissa ja jatko-opinnoissa",
  "Mathematical modelling": "tilanteiden mallintamisessa",
  "Unknown prices, distances, ages":
    "tuntemattomien hintojen, matkojen ja ikien ratkaisuissa",
  Geometry: "geometrian pituus- ja alalaskuissa",
  "Two simultaneous constraints":
    "tilanteissa, joissa kaksi ehtoa on voimassa yhtä aikaa",
  "Budgets/limits": "budjeteissa ja raja-arvoissa",
  "Patterns, growth": "säännönmukaisuuksissa ja kasvussa",
  "Scale, recipes, speed": "mittakaavassa, resepteissä ja nopeuksissa",
  "Nearly all mathematical modelling":
    "melkein kaikessa matemaattisessa mallintamisessa",
  "Data and trends": "datan ja trendien tulkinnassa",
  Modelling: "mallintamisessa",
  "Unit price, constant speed": "yksikköhinnoissa ja vakionopeudessa",
  "Shared work, fixed-distance travel":
    "jaetussa työssä ja vakioetäisyyden matkassa",
  "General model of dependency":
    "tilanteissa, joissa yksi suure riippuu toisesta",
  "Constant rates": "vakionopeuksissa ja tasaisissa muutoksissa",
  "Projectile/area models, later math":
    "kaari-ilmiöissä, pinta-alamalleissa ja jatko-opinnoissa",
  "Speed, €/unit, rate of change":
    "nopeudessa, yksikköhinnoissa ja muutosnopeudessa",
  "Fixed fees + variable cost":
    "kiinteän maksun ja muuttuvan kulun yhdistelmissä",
  "Break-even, crossing points": "nollakohdissa ja leikkauspisteissä",
  "Language of geometry": "geometrian käsitteiden täsmällisessä käytössä",
  Geometry: "geometriassa",
  "Construction, surveying": "rakentamisessa ja mittauksissa",
  "Design, construction": "suunnittelussa ja rakentamisessa",
  "Maps, models, indirect measurement":
    "kartoissa, pienoismalleissa ja epäsuorissa mittauksissa",
  "Geometry/proof": "geometriassa ja perusteluissa",
  "Design, geometric reasoning":
    "suunnittelussa ja geometrisessa päättelyssä",
  "Distance/construction": "etäisyyden laskemisessa ja rakentamisessa",
  "Construction/checking squareness":
    "rakennuslinjojen suorakulmaisuuden tarkistuksessa",
  "Heights/distances/surveying":
    "korkeuksien ja etäisyyksien arvioinnissa",
  "Circle geometry": "ympyrägeometriassa",
  "Fencing/material": "aidan, listan tai muun materiaalin mitoituksessa",
  "Flooring/land": "lattia- ja maa-alueiden mitoituksessa",
  "Wheels, circular objects":
    "renkaiden, kaapelikelojen ja muiden pyöreiden kohteiden mitoissa",
  "Materials/land": "materiaalin menekin ja maa-alan arvioinnissa",
  "Curved paths/components":
    "kaarteissa, radoissa ja pyöreissä osissa",
  "Design, rotating systems": "suunnittelussa ja pyörivissä järjestelmissä",
  "Containers/buildings": "säiliöissä ja rakennusten tiloissa",
  "Balls/tanks": "palloissa ja säiliöissä",
  "Cans/tanks": "purkeissa ja lieriömäisissä säiliöissä",
  "Funnels/conical objects": "suppiloissa ja kartiomaisissa kappaleissa",
  "Essential practical numeracy":
    "jokapäiväisissä mittamuunnoksissa",
  "Surveys/experiments": "kyselyissä ja kokeissa",
  "Any data analysis": "kaikessa datan jäsentämisessä",
  "Science, society, media": "tieteen, yhteiskunnan ja median tulkinnoissa",
  "Grades, measurements": "arvosanoissa ja mittaussarjoissa",
  "Typical category/value": "tyypillisen arvon löytämisessä",
  "Surveys/statistics": "kyselyissä ja tilastoissa",
  "Polling/probability": "mielipidemittauksissa ja todennäköisyyksissä",
  "Income/data with extremes":
    "aineistoissa, joissa ääriarvot voivat hämätä",
  "Weather, measurements, finance": "säässä, mittauksissa ja talousluvuissa",
  "News/media/science":
    "uutisten, median ja tutkimuskuvioiden tulkinnassa",
  Communication: "datan esittämisessä selkeästi muille",
  "Risk, games, prediction":
    "riskeissä, peleissä ja epävarmojen tilanteiden arvioinnissa",
};

const theoryFi = {
  "Pattern, dependency, variable": "sääntö, riippuvuus ja muuttuja",
  "Systematic listing/tree principle":
    "järjestelmällinen luettelu ja puukaavio",
  "Implication, counterexample, logical reasoning":
    "johtopäätös, vastaesimerkki ja looginen päättely",
  "Mathematical notation/language": "matemaattinen merkintätapa",
  "Assumptions → logical steps → conclusion":
    "oletus, loogiset askeleet ja johtopäätös",
  "True/false, counterexample": "tosi/epätosi ja vastaesimerkki",
  "Algorithm, sequence, condition, repetition":
    "algoritmi, askeljärjestys, ehto ja toisto",
  "Variables, loops, conditions": "muuttujat, toistot ja ehdot",
  "Depends on task": "tehtävän mukaan valittu työväline",
  "Number line, signs": "lukusuora ja etumerkit",
  "Equivalent fractions, reciprocal":
    "samanarvoiset murtoluvut ja käänteisluku",
  "Number line": "lukusuora",
  "Multiplicative inverse": "käänteisluku",
  "Natural, integer, rational, irrational, real":
    "luonnolliset luvut, kokonaisluvut, rationaaliluvut, irrationaaliluvut ja reaaliluvut",
  "Divisor/multiple": "tekijä ja monikerta",
  "Prime numbers": "alkuluvut",
  "Place value": "paikka-arvo",
  Precision: "tarkkuus",
  "Place value/significant precision":
    "paikka-arvo ja pyöristystarkkuus",
  "Ratio to 100": "suhde sataan",
  "Part/whole": "osa ja kokonaisuus",
  "Multiplication by decimal factor":
    "kertominen desimaalikertoimella",
  "Inverse operation": "käänteinen laskutoimitus",
  "1 ± p/100": "muutoskerroin 1 +/- p/100",
  "Change/original": "muutos ja alkuarvo",
  "Reference quantity matters": "vertailukohdan valinta ratkaisee",
  "Base/exponent, negative exponent":
    "kantaluku, eksponentti ja negatiivinen eksponentti",
  "x²=a": "toisen asteen yhteys x^2 = a",
  "Variable vs unknown": "muuttuja ja tuntematon",
  "Substitution, operation order":
    "sijoittaminen ja laskujärjestys",
  "Terms, coefficients": "termit ja kertoimet",
  "Exponent rules": "potenssisäännöt",
  "Term, coefficient, degree": "termi, kerroin ja aste",
  "Like terms": "samanmuotoiset termit",
  "Distributive law": "osittelulaki",
  "Variables and operations": "muuttujat ja laskutoimitukset",
  "Equality and inverse operations":
    "yhtäsuuruus ja käänteiset laskutoimitukset",
  "Squares/roots/factoring as applicable":
    "neliöt, juuret tai tekijöihin jako tilanteen mukaan",
  "Intersection/substitution/elimination":
    "leikkauspiste, sijoitusmenetelmä ja yhteenlaskumenetelmä",
  "Inequality signs, number line":
    "epäyhtälömerkit ja lukusuora",
  "Term/index/rule": "lukujonon jäsen, järjestysnumero ja sääntö",
  "Equivalent ratios": "samanarvoiset suhteet",
  Variables: "muuttujat",
  "Axes, coordinates, scale":
    "akselit, koordinaatit ja mittakaava",
  "Variables/formula": "muuttujat ja kaava",
  "Proportionality constant": "verrannollisuuskerroin",
  "Constant product": "vakio tulo",
  "Input/output": "syöte ja tulos",
  Coordinates: "koordinaatisto",
  "y=ax²+… concept": "paraabelin perusidea y = ax^2 + ...",
  "Δy/Δx": "muutosnopeus delta y / delta x",
  "Linear equation": "lineaarisen funktion yhtälö",
  "Direction along x-axis": "suunnan muutos x-akselilla",
  "f(x)=0": "nollakohta määrittyy ehdosta f(x)=0",
  Definitions: "täsmälliset määritelmät",
  "Parallel/perpendicular, angle relations":
    "yhdensuuntaisuus, kohtisuoruus ja kulmasuhteet",
  "Sides, vertices, angles": "sivut, kärjet ja kulmat",
  "Corresponding sides/angles": "vastaavat sivut ja kulmat",
  Correspondence: "vastaavuus",
  "Bisectors etc.": "puolittajat ja peruskonstruktiot",
  "a²+b²=c²": "Pythagoraan lause a^2 + b^2 = c^2",
  "Converse logic": "käänteinen päättely",
  "sin, cos, tan": "trigonometriset funktiot sin, cos ja tan",
  "Arc and angle relationship": "kaaren ja kulman välinen yhteys",
  "Semicircle geometry": "puoliympyrän geometria",
  "Side lengths": "sivunpituuksien summa",
  "Area formulas/decomposition": "pinta-alakaavat ja pilkkominen",
  "π, radius, diameter": "pii, säde ja halkaisija",
  "πr²": "ympyrän pinta-ala A = pii * r^2",
  "Fraction of full angle": "osuus täydestä kulmasta",
  "Fraction of circle": "osuus koko ympyrästä",
  "Faces/surfaces/sections": "tahkot, pinnat ja leikkaukset",
  "Sphere formulas": "pallon pinta-ala- ja tilavuuskaavat",
  "Base × height etc.": "pohjan pinta-ala kertaa korkeus",
  "Cone formulas": "kartion pinta-ala- ja tilavuuskaavat",
  "Powers of conversion factors":
    "muunnoskertoimet ja niiden potenssit",
  "Population/sample/measurement basics":
    "perusjoukko, otos ja mittaamisen perusteet",
  "Variables/categories": "muuttujat ja luokat",
  "Summary statistics/comparison":
    "yhteenvetoluvut ja aineistojen vertailu",
  "Sum/count": "summa ja havaintojen lukumäärä",
  Frequency: "frekvenssi eli lukumäärä",
  "Counting/categories": "laskeminen ja luokittelu",
  "Ratio/percentage": "suhde ja prosentti",
  Ordering: "järjestäminen",
  "Central value vs spread": "keskitaso ja vaihtelu",
  "Axes/scales/categories": "akselit, mittakaava ja luokat",
  "Chart choice/scales": "diagrammityypin valinta ja mittakaava",
  "Favourable/all outcomes":
    "suotuisten tapausten määrä ja kaikkien tapausten määrä",
};

const specialBlocks = {
  Muutosprosentti: `
    <p>
      Hinta nousee 50 eurosta 60 euroon. Muutos on 10 euroa. Pelkkä 10 euroa ei vielä kerro,
      oliko muutos suuri. Sama 10 euroa näyttää ihan eri asialta, jos lähtöhinta on 500 euroa.
    </p>
    <p>
      Siksi vertaamme muutosta siihen, mistä lähdettiin: 10 / 50 = 0,2 = 20 %.
      Nyt tulkinta on selkeä: 50 euroa -> 60 euroa on 20 prosentin nousu.
    </p>
    <p class="rule">
      Vasta tämän jälkeen yleinen sääntö:
      <strong>muutosprosentti = (muutos / alkuarvo) * 100 %</strong>
    </p>
  `,
  Pyöristäminen: `
    <p>
      Mittauksessa saadaan pituudeksi 18,476 m, mutta työohje pyytää tuloksen
      0,1 metrin tarkkuudella.
    </p>
    <p>
      Katsotaan kymmenesosaa (4) ja seuraavaa numeroa (7). Koska 7 on vähintään 5,
      pyöristetään ylöspäin: 18,476 m ≈ 18,5 m.
    </p>
    <p class="rule">
      Sääntö: jos seuraava numero on 0-4, pidä ennallaan. Jos se on 5-9, nosta yhdellä.
    </p>
  `,
  Prosenttiarvo: `
    <p>
      Tuotteen hinta on 80 euroa ja alennus 15 %. Kuinka monta euroa alennus on?
    </p>
    <p>
      Muunnetaan prosentti desimaaliksi: 15 % = 0,15. Lasketaan 0,15 * 80 = 12.
      Alennus on siis 12 euroa.
    </p>
    <p class="rule">
      Yleinen sääntö: <strong>p % luvusta x = (p / 100) * x</strong>.
    </p>
  `,
  Perusarvo: `
    <p>
      Tiedetään, että 24 euroa on 30 % alkuperäisestä hinnasta. Mikä oli 100 %?
    </p>
    <p>
      Jos 30 % vastaa 24 euroa, niin 1 % vastaa 24 / 30 = 0,8 euroa.
      Siksi 100 % on 0,8 * 100 = 80 euroa.
    </p>
    <p class="rule">
      Yleinen malli: <strong>alkuarvo = osa / (prosentti desimaalina)</strong>.
    </p>
  `,
};

let chapters = [];
let chapterIndexById = new Map();
let currentIndex = 0;

function escapeHtml(text) {
  return String(text || "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}

function toFiApplication(text) {
  return applicationFi[text] || text.toLowerCase();
}

function toFiTheory(text) {
  return theoryFi[text] || text.toLowerCase();
}

function toFiExample(example) {
  return String(example || "")
    .replace("→", "->")
    .replace("opposite of", "vastaluku luvusta")
    .replace("reciprocal of", "käänteisluku luvusta")
    .replace("mean of", "keskiarvo luvuista")
    .replace("mode of", "tyyppiarvo aineistossa")
    .replace("median of", "mediaani luvuista")
    .replace("Is ", "Onko ")
    .replace("How much larger is", "Kuinka paljon suurempi on")
    .replace("Program that", "Ohjelma, joka")
    .replace("Procedure for", "Menettely, jolla");
}

function buildWhyWords(row) {
  const app = toFiApplication(row.application);
  return `
    <p>
      <strong>${escapeHtml(row.ops_item)}</strong> on hyödyllinen silloin, kun ${escapeHtml(
        app
      )}.
    </p>
    <p>
      Tämän luvun ydin on yksi ajatus: ennen kaavaa pitää ymmärtää, mitä verrataan,
      mitä etsitään ja miksi juuri tämä tapa toimii.
    </p>
  `;
}

function buildIllustration(row) {
  const app = toFiApplication(row.application);
  return `[Illustration: Tilannekuva aiheesta "${row.ops_item}". Näytä ensin arkitilanne (${app}), sitten sama idea numeroina tai kuviona, ja korosta yksi ratkaiseva askel.]`;
}

function buildGenericConcrete(row) {
  const theory = toFiTheory(row.theory);
  const example = toFiExample(row.example);
  return `
    <p>
      Otetaan konkreettinen lähtötilanne aiheesta. Tehtävän matemaattinen muoto voi olla esimerkiksi:
      <strong>${escapeHtml(example)}</strong>.
    </p>
    <p>
      Ratkaisussa edetään rauhallisesti: tunnista mitä tiedetään, päätä mitä pitää löytää,
      ja tee lasku tai päättely vaihe kerrallaan.
    </p>
    <p class="rule">
      Yleistys vasta lopuksi: tässä luvussa tarvittava teoria on
      <strong>${escapeHtml(theory)}</strong>.
    </p>
  `;
}

function buildWrongTurn(row) {
  if (row.ops_item === "Muutosprosentti") {
    return `
      <p>
        Helppo harhapolku: jakaa muutos loppuarvolla. Se tuntuu loogiselta, mutta kysymys on
        "kuinka suuri muutos oli lähtötilanteeseen verrattuna". Siksi jakaja on aina alkuarvo.
      </p>
    `;
  }

  if (row.ops_item === "Murtolukulaskenta") {
    return `
      <p>
        Helppo harhapolku: laskea murtolukujen nimittäjät suoraan yhteen tai vähennykseen.
        Ensin pitää tehdä nimittäjistä samat, vasta sitten yhdistää osoittajat.
      </p>
    `;
  }

  return `
    <p>
      Helppo harhapolku: hypätä suoraan merkintöihin ilman että pysähtyy miettimään,
      mitä luvut tai symbolit tarkoittavat tilanteessa. Kun merkitys on selvä,
      sääntö on paljon helpompi käyttää oikein.
    </p>
  `;
}

function buildChapterHtml(row, index, total) {
  const special = specialBlocks[row.ops_item];
  const concrete = special || buildGenericConcrete(row);

  return `
    <p class="meta">
      ${escapeHtml(row.content_area)} • ${escapeHtml(row.content_area_name)} •
      ${index + 1}/${total}
    </p>

    <section>
      <h3>Miksi / Sanat</h3>
      ${buildWhyWords(row)}
    </section>

    <section>
      <h3>Kuvitus</h3>
      <div class="illustration">${escapeHtml(buildIllustration(row))}</div>
    </section>

    <section>
      <h3>Konkreettinen esimerkki -> teoria</h3>
      ${concrete}
    </section>

    <section>
      <h3>Helppo harhapolku</h3>
      ${buildWrongTurn(row)}
    </section>
  `;
}

function buildChapters(data) {
  return data.map((row, idx) => ({
    id: `${row.content_area.toLowerCase()}-${String(idx + 1).padStart(2, "0")}`,
    index: idx,
    title: row.ops_item,
    area: row.content_area,
    areaName: row.content_area_name,
    html: buildChapterHtml(row, idx, data.length),
  }));
}

function renderNav() {
  const nav = document.getElementById("chapter-nav");
  nav.innerHTML = "";

  for (const area of areaOrder) {
    const items = chapters.filter((c) => c.area === area);
    if (!items.length) continue;

    const block = document.createElement("section");
    block.className = "area-block";

    const heading = document.createElement("h3");
    heading.className = "area-heading";
    heading.textContent = `${area} - ${items[0].areaName}`;
    block.appendChild(heading);

    const list = document.createElement("div");
    list.className = "chapter-list";

    for (const chapter of items) {
      const link = document.createElement("a");
      link.href = `#${chapter.id}`;
      link.className = "chapter-link";
      link.dataset.chapterId = chapter.id;
      link.textContent = chapter.title;
      list.appendChild(link);
    }

    block.appendChild(list);
    nav.appendChild(block);
  }
}

function renderChapterByIndex(index) {
  currentIndex = Math.max(0, Math.min(index, chapters.length - 1));
  const chapter = chapters[currentIndex];
  const view = document.getElementById("chapter-view");

  view.innerHTML = `
    <h2>${escapeHtml(chapter.title)}</h2>
    ${chapter.html}
  `;

  document.getElementById("chapter-position").textContent = `${currentIndex + 1} / ${chapters.length}`;
  document.getElementById("prev-btn").disabled = currentIndex === 0;
  document.getElementById("next-btn").disabled = currentIndex === chapters.length - 1;

  for (const link of document.querySelectorAll(".chapter-link")) {
    link.classList.toggle("active", link.dataset.chapterId === chapter.id);
  }

  if (location.hash !== `#${chapter.id}`) {
    history.replaceState(null, "", `#${chapter.id}`);
  }
}

function renderChapterById(id) {
  if (!chapterIndexById.has(id)) {
    renderChapterByIndex(0);
    return;
  }
  renderChapterByIndex(chapterIndexById.get(id));
}

function setupControls() {
  document.getElementById("prev-btn").addEventListener("click", () => {
    renderChapterByIndex(currentIndex - 1);
  });

  document.getElementById("next-btn").addEventListener("click", () => {
    renderChapterByIndex(currentIndex + 1);
  });

  window.addEventListener("hashchange", () => {
    const id = location.hash.replace("#", "");
    renderChapterById(id);
  });
}

async function init() {
  try {
    let data = null;

    // Toimii myös file://-avauksessa ilman paikallista web-palvelinta.
    if (Array.isArray(window.BOOK_DATA) && window.BOOK_DATA.length > 0) {
      data = window.BOOK_DATA;
    } else {
      const response = await fetch(DATA_PATH);
      if (!response.ok) {
        throw new Error(`JSON-lataus epäonnistui: ${response.status}`);
      }
      data = await response.json();
    }

    chapters = buildChapters(data);
    chapterIndexById = new Map(chapters.map((c, idx) => [c.id, idx]));

    renderNav();
    setupControls();

    const startId = location.hash.replace("#", "");
    renderChapterById(startId || chapters[0].id);
  } catch (error) {
    const view = document.getElementById("chapter-view");
    view.innerHTML = `
      <h2>Virhe</h2>
      <p>Oppikirjaa ei voitu ladata.</p>
      <pre>${escapeHtml(error.message)}</pre>
    `;
  }
}

init();
