#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère formations-espagne.html — dispositifs de formation gratuits
accessibles depuis Valence (Comunitat Valenciana).

Usage : python3 build_formations_espagne.py > ../formations-espagne.html

Pendant de build_ressources.py, mais sur l'autre système : ici le CPF
n'existe pas, tout est à 0 €, et la colonne qui discrimine est la
condition d'accès. Relevé du 4 septembre 2026 — à revalider tous les
trois mois comme la page Ressources externes.
"""

# --- Accès : la colonne structurante de cette page -------------------------
# libre        : ouvert à tous, tout de suite, sans convocatoria ni statut
# labora       : réservé aux inscrits Espai LABORA, priorité aux desempleados
# convocatoria : dépend d'un appel national ouvert et du statut (voir public)

EFUNDAE = "https://www.efundae.es/course/view.php?id={}"
PUNT = "https://puntlabora.gva.es/ofsrvfor/consultar?lang=es"

# (titre, organisme/précision, thématique, accès, modalité, lien)
ROWS = []

def add(titre, orga, theme, acces, modalite, lien, note=""):
    ROWS.append({"titre": titre, "orga": orga, "theme": theme,
                 "acces": acces, "modalite": modalite, "lien": lien,
                 "note": note})

# --- 1. eFundae — durabilité et RSE, accès libre ---------------------------
EFUNDAE_RSE = [
    ("Cálculo de la Huella de Carbono", 1167),
    ("Cálculo de la huella de carbono de Alcance 3", 1168),
    ("Evaluación de doble materialidad en el contexto de las NEIS", 995),
    ("Objetivos de Desarrollo Sostenible y criterios ESG", 998),
    ("Taxonomía Europea de actividades sostenibles aplicada a las pymes", 1166),
    ("Cómo realizar informes de sostenibilidad en las pymes", 992),
    ("Informes de sostenibilidad para pymes que cotizan en bolsa", 999),
    ("Comunicación de la sostenibilidad", 993),
    ("Impacto de la sostenibilidad empresarial", 994),
    ("Economía circular", 997),
    ("Las 9R de la Economía Circular", 1157),
    ("Proyectos sostenibles y circulares", 1190),
    ("Sostenibilidad, economía circular y otros conceptos clave", 1000),
    ("Análisis del ciclo de vida", 1158),
    ("Logística inversa", 1003),
    ("Gestión de recursos y de residuos en las pymes", 1162),
    ("Transición energética", 996),
    ("Autoconsumo con energías renovables", 1192),
    ("Electromovilidad", 1161),
    ("Biodiversidad", 1191),
    ("Pymes y cambio climático", 1163),
    ("Digitalización y tecnologías sostenibles", 1160),
    ("Gestión de proyectos de innovación en sostenibilidad", 1159),
    ("Subvenciones y ayudas para sostenibilidad en pymes", 1001),
    ("Fiscalidad sostenible para pymes", 1002),
]
for titre, cid in EFUNDAE_RSE:
    add(titre, "eFundae (Fundae) — Sensibilización Medioambiental",
        "Durabilité &amp; RSE", "libre", "En ligne, à son rythme",
        EFUNDAE.format(cid))

# --- 2. eFundae — itinéraires numériques (4 niveaux DigComp) ---------------
EFUNDAE_ITI = [
    ("Plan de marketing y estrategia digital", 432, "Numérique &amp; marketing"),
    ("Business Analytics — Odisea Data", 253, "Numérique &amp; marketing"),
    ("Community Manager", 431, "Numérique &amp; marketing"),
    ("Comercio electrónico", 529, "Numérique &amp; marketing"),
    ("Programación", 232, "Numérique &amp; marketing"),
]
for titre, cid, theme in EFUNDAE_ITI:
    add(titre, "eFundae (Fundae) — itinéraire de 4 niveaux progressifs",
        theme, "libre", "En ligne, ~150 h",
        "https://www.efundae.es/course/index.php?categoryid={}".format(cid))

# --- 3. Campus virtuel LABORA — en ligne, tutoré ---------------------------
LABORA_ONLINE = [
    ("Excel — básico", "Competencias digitales I", "Numérique &amp; marketing"),
    ("Excel — avanzado", "Competencias digitales I", "Numérique &amp; marketing"),
    ("Microsoft Word — medio", "Competencias digitales I", "Transversal"),
    ("Microsoft Word — avanzado", "Competencias digitales I", "Transversal"),
    ("PowerPoint — avanzado", "Competencias digitales I", "Transversal"),
    ("Metodología de gestión de proyectos de software con SCRUM",
     "Competencias digitales I — IFCD048PO", "Numérique &amp; marketing"),
    ("Gestión de proyectos con metodologías ágiles y enfoque Lean",
     "Competencias digitales I", "Numérique &amp; marketing"),
    ("Técnicas y habilidades de comunicación",
     "Competencias transversales", "Transversal"),
    ("Liderazgo. Dirección de equipos de trabajo",
     "Competencias transversales", "Transversal"),
    ("Pensamiento positivo — optimismo y entusiasmo",
     "Competencias transversales", "Transversal"),
]
for titre, bloc, theme in LABORA_ONLINE:
    add(titre, "Campus Virtual LABORA Formació — " + bloc, theme, "labora",
        "En ligne, tutoré, jusqu'à 30 h",
        "https://labora.gva.es/es/aula-virtual",
        note="Édition affichée : millésime 2025. Diploma de aprovechamiento.")

# --- 4. Plan LABORA 2026 — Valence et l'Horta, présentiel ------------------
LABORA_FPE = [
    ("22085", "Gestión de marketing y comunicación", "Valencia", "Numérique &amp; marketing"),
    ("22117", "CMS y e-commerce", "Valencia", "Numérique &amp; marketing"),
    ("22179", "Procedimientos básicos en la atención al cliente y ecommerce", "Valencia", "Numérique &amp; marketing"),
    ("22177", "Procedimientos básicos en el marketing digital y redes sociales", "Valencia", "Numérique &amp; marketing"),
    ("22190", "Digitalización y RRSS como estrategia corporativa", "Valencia", "Numérique &amp; marketing"),
    ("22258", "Entorno y estrategia en la transformación digital", "Valencia", "Numérique &amp; marketing"),
    ("22162", "Inteligencia artificial (IA) aplicada a marketing digital", "Valencia", "Numérique &amp; marketing"),
    ("22194", "Inteligencia artificial aplicada a la empresa", "Valencia", "Numérique &amp; marketing"),
    ("22188", "Especialista en inteligencia artificial", "L'Horta Nord", "Numérique &amp; marketing"),
    ("22246", "Habilitación para la docencia en grados A, B y C del sistema de FP", "Valencia", "Transversal"),
    ("21912", "Gestión administrativa y financiera del comercio internacional", "L'Horta Sud", "Transversal"),
    ("22109", "Actividades de gestión del pequeño comercio", "Valencia", "Transversal"),
    ("21963", "Operaciones básicas en montaje y mantenimiento de instalaciones de energías renovables", "Valencia", "Durabilité &amp; RSE"),
    ("22339", "Eficiència energètica d'edificis", "L'Horta Sud", "Durabilité &amp; RSE"),
    ("22323", "Confección y publicación de páginas web", "L'Horta Nord", "Métiers techniques"),
    ("22048", "Programación de sistemas informáticos", "Valencia", "Métiers techniques"),
    ("22043", "Seguridad informática", "L'Horta Sud", "Métiers techniques"),
    ("22350", "Inglés B2", "L'Horta Sud", "Langues"),
    ("22326", "Inglés B2", "L'Horta Nord", "Langues"),
    ("22349", "Inglés B1", "L'Horta Sud", "Langues"),
    ("22325", "Inglés B1", "L'Horta Nord", "Langues"),
    ("22353", "Inglés A2", "L'Horta Sud", "Langues"),
    ("22351", "Francés A1", "L'Horta Sud", "Langues"),
]
for code, titre, comarque, theme in LABORA_FPE:
    add(titre,
        "LABORA — plan 2026, code {} · {}".format(code, comarque),
        theme, "labora", "Présentiel — préinscription ouverte", PUNT)

# --- 5. Convocatoria estatal — en ligne ------------------------------------
ESTATAL = [
    ("Sistemas de gestión ambiental", "150 h", True,
     "https://www.cursosfemxa.es/sistemas-gestion-ambiental-gratuito-titulos-oficiales-curso",
     "Durabilité &amp; RSE"),
    ("Gestión integral de residuos", "200 h", False,
     "https://www.cursosfemxa.es/gestion-integral-residuos-online-gratuito-estatal-femxa-curso",
     "Durabilité &amp; RSE"),
    ("Impacto ambiental y su auditoría", "30 h", False,
     "https://www.cursosfemxa.es/impacto-ambiental-auditoria-gratuito-online-estatal-femxa-curso",
     "Durabilité &amp; RSE"),
    ("Conducción económica y ecológica", "50 h", False,
     "https://www.cursosfemxa.es/conduccion-economica-ecologica-gratuito-online-curso",
     "Durabilité &amp; RSE"),
    ("Gestión de compras informatizada", "40 h", False,
     "https://www.cursosfemxa.es/gestion-compras-informatizada-gratuito-online-curso",
     "Transversal"),
    ("Personal shopper", "40 h", True,
     "https://www.cursosfemxa.es/personal-shopper-gratuito-online-curso",
     "Transversal"),
    ("Básico de prevención de riesgos laborales", "30 h", False,
     "https://www.cursosfemxa.es/basico-prl-gratuito-online-estatal-femxa-curso",
     "Transversal"),
]
for titre, heures, desempleados, url, theme in ESTATAL:
    public = "Desempleados, trabajadores y autónomos" if desempleados \
        else "Trabajadores y autónomos uniquement"
    add(titre, "Convocatoria estatal (SEPE / Fundae) — " + public,
        theme, "convocatoria", "En ligne, " + heures, url,
        note="" if desempleados
        else "Fermé tant que le statut est celui de demandeuse d'emploi.")

# --- 6. Plateformes permanentes -------------------------------------------
PLATEFORMES = [
    ("Conecta Empleo", "Fundación Telefónica — numérique, data, cybersécurité, développement",
     "Numérique &amp; marketing", "En ligne et présentiel, avec certificat",
     "https://www.fundaciontelefonica.com/empleabilidad/conecta-empleo/"),
    ("Grow with Google", "Google — ce qui subsiste de Google Actívate : marketing, e-commerce, cloud, IA",
     "Numérique &amp; marketing", "En ligne, cours d'initiation",
     "https://grow.google/intl/es/courses-and-tools/"),
    ("Formación Abierta", "EOI — école publique du ministère de l'Industrie, MOOC gratuits",
     "Durabilité &amp; RSE", "En ligne, accès libre",
     "https://www.eoi.es/es/formacionabierta"),
    ("Mi Competencia Digital", "Fundae — test DigComp, environ 20 minutes",
     "Transversal", "En ligne, auto-évaluation",
     "https://micompetenciadigital.fundae.es/"),
    ("Buscador de formación subvencionada", "Fundae — moteur officiel, toutes convocatorias",
     "Transversal", "Recherche par territoire et modalité",
     "https://experienciafundae.es/buscador"),
]
for titre, orga, theme, modalite, url in PLATEFORMES:
    add(titre, orga, theme, "libre", modalite, url)


# --- Rendu -----------------------------------------------------------------
ACCES_BADGE = {
    "libre": ('badge-success', 'Accès libre'),
    "labora": ('badge-progress', 'Espai LABORA'),
    "convocatoria": ('badge-warning', 'Convocatoria'),
}
THEMES = ["Durabilité &amp; RSE", "Numérique &amp; marketing", "Langues",
          "Transversal", "Métiers techniques"]

def esc(s):
    return s.replace("'", "&#x27;")

def render():
    n_libre = sum(1 for r in ROWS if r["acces"] == "libre")
    n_labora = sum(1 for r in ROWS if r["acces"] == "labora")
    n_conv = sum(1 for r in ROWS if r["acces"] == "convocatoria")

    theme_btns = "\n".join(
        '        <button class="filter-btn" data-filter="{0}">{0}</button>'.format(t)
        for t in THEMES)

    rows_html = []
    for r in ROWS:
        cls, label = ACCES_BADGE[r["acces"]]
        note = ('<br><span class="row-note">{}</span>'.format(esc(r["note"]))
                if r["note"] else "")
        rows_html.append(
            '          <tr data-category="{cat}" data-acces="{acces}">\n'
            '            <td><strong>{titre}</strong><br>'
            '<span class="orga">{orga}</span>{note}</td>\n'
            '            <td><span class="badge badge-neutral">{cat}</span></td>\n'
            '            <td><span class="badge {cls}">{label}</span></td>\n'
            '            <td class="modalite">{modalite}</td>\n'
            '            <td><a href="{lien}" target="_blank" rel="noopener" '
            'class="btn btn-outline" style="padding:4px 10px;font-size:0.85rem;'
            'white-space:nowrap;">Consulter &#8599;</a></td>\n'
            '          </tr>'.format(
                cat=r["theme"], acces=r["acces"], titre=esc(r["titre"]),
                orga=esc(r["orga"]), note=note, cls=cls, label=label,
                modalite=esc(r["modalite"]), lien=r["lien"]))

    return TEMPLATE.format(
        total=len(ROWS), n_libre=n_libre, n_labora=n_labora, n_conv=n_conv,
        theme_btns=theme_btns, rows="\n".join(rows_html))


TEMPLATE = """<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="Formahub — dispositifs de formation gratuits accessibles depuis Valence : eFundae, LABORA, convocatorias nationales.">
  <meta name="color-scheme" content="light dark">
  <title>Formahub &mdash; Formations Espagne</title>
  <link rel="stylesheet" href="assets/css/style.css">
  <style>
    .orga {{ color: var(--text-muted); font-size: 0.85rem; }}
    .row-note {{ display: block; margin-top: 6px; color: var(--text-muted);
                 font-size: 0.78rem; line-height: 1.45; }}
    .modalite {{ font-size: 0.85rem; color: var(--text-muted); }}
    .filter-group {{ margin-bottom: 10px; }}
    .filter-group-label {{ display: block; font-size: 0.78rem; text-transform: uppercase;
                           letter-spacing: 0.05em; color: var(--text-muted); margin-bottom: 6px; }}
    #result-count {{ color: var(--text-muted); font-size: 0.9rem; margin: 4px 0 18px; }}
    #espagne-table td:first-child {{ min-width: 260px; }}
  </style>
</head>
<body>
  <header class="site-header">
    <a href="index.html" class="brand">
      <div class="brand-icon">F</div>
      <span>Formahub</span>
    </a>
    <nav class="nav-links">
      <a href="index.html" class="nav-link">Mes formations</a>
      <a href="ressources-externes.html" class="nav-link">Ressources externes</a>
      <a href="formations-espagne.html" class="nav-link active">Formations Espagne</a>
      <button class="theme-toggle" type="button">&#127769; Mode sombre</button>
    </nav>
  </header>

  <main class="main-container">
    <div class="hero-banner">
      <h1>Formations gratuites en Espagne</h1>
      <p>{total} dispositifs accessibles depuis Valence, tous gratuits. La page Ressources externes couvre le système français et le CPF ; celle-ci couvre le système espagnol, où le financement ne se pose pas et où la vraie question est la condition d&#x27;accès.</p>
      <div style="margin-top: 16px; display: flex; gap: 12px; flex-wrap: wrap;">
        <span class="badge badge-success">{n_libre} en accès libre</span>
        <span class="badge badge-progress">{n_labora} via Espai LABORA</span>
        <span class="badge badge-warning">{n_conv} soumis à convocatoria</span>
      </div>
    </div>

    <div class="intro-box">
      <h3>&#128204; Comment lire la colonne &laquo;&nbsp;accès&nbsp;&raquo;</h3>
      <p>Ici, le coût ne trie rien : tout est à 0 &euro;. Ce qui trie, c&#x27;est la porte d&#x27;entrée, et il y en a trois.</p>
      <p><strong>Accès libre.</strong> Ouvert à tous, immédiatement, avec une simple pièce d&#x27;identité : ni convocatoria, ni statut, ni date. C&#x27;est le seul bloc qui peut commencer aujourd&#x27;hui.</p>
      <p><strong>Espai LABORA.</strong> Réservé aux personnes inscrites comme demandeuses d&#x27;emploi auprès de la Generalitat Valenciana, avec priorité donnée aux desempleados. Avant toute préinscription : corriger ses données dans Punt LABORA (autoentrevista, puis &laquo;&nbsp;guardar y finalizar&nbsp;&raquo;) &mdash; les erreurs de coordonnées sont la première cause d&#x27;exclusion citée par l&#x27;organisme.</p>
      <p><strong>Convocatoria.</strong> Appels nationaux SEPE / Fundae, ouverts par vagues et par public. La mention du public compte plus que l&#x27;intitulé : une bonne part du catalogue est réservée aux <em>trabajadores y autónomos</em> et se ferme avec le statut de demandeuse d&#x27;emploi.</p>
    </div>

    <div class="pitfall-box">
      <h4>&#9888;&#65039; Trois points à vérifier avant de s&#x27;engager</h4>
      <p><strong>Les éditions LABORA en ligne affichent encore le millésime 2025</strong> (matriculation 17/09 &ndash; 07/10, accès 15/10 &ndash; 04/11). La page n&#x27;a pas basculé sur 2026, et les blocs <em>Competencias digitales II</em> et <em>Idiomas</em> n&#x27;ont aucune édition publiée. Les intitulés restent valables d&#x27;une édition à l&#x27;autre ; les dates, non.</p>
      <p><strong>Aucun cours en &laquo;&nbsp;plazo de inscripción abierto&nbsp;&raquo; pour Valence au 4 septembre 2026.</strong> Les 23 codes du plan 2026 listés ici sont en phase <em>planificados</em> : la préinscription est possible dès maintenant et déclenche un courriel à l&#x27;ouverture du délai. C&#x27;est la seule façon de ne pas rater la fenêtre.</p>
      <p><strong>Le moteur Punt LABORA plafonne à 200 résultats affichés</strong> sur les 350 cours planifiés de la province. Filtrer par comarque pour voir la totalité d&#x27;un territoire.</p>
    </div>

    <div class="filter-group">
      <span class="filter-group-label">Thématique</span>
      <div class="filter-bar" id="filter-theme">
        <button class="filter-btn active" data-filter="all">Toutes</button>
{theme_btns}
      </div>
    </div>

    <div class="filter-group">
      <span class="filter-group-label">Accès</span>
      <div class="filter-bar" id="filter-acces">
        <button class="filter-btn active" data-acces="all">Tous</button>
        <button class="filter-btn" data-acces="libre">Accès libre</button>
        <button class="filter-btn" data-acces="labora">Espai LABORA</button>
        <button class="filter-btn" data-acces="convocatoria">Convocatoria</button>
      </div>
    </div>

    <p id="result-count"></p>

    <div class="table-responsive">
      <table id="espagne-table">
        <thead>
          <tr>
            <th>Intitulé &amp; organisme</th>
            <th>Thématique</th>
            <th>Accès</th>
            <th>Modalité</th>
            <th>Lien</th>
          </tr>
        </thead>
        <tbody>
{rows}
        </tbody>
      </table>
    </div>

    <div class="takeaway-box">
      <h3>&#9989; Méthode de mise à jour</h3>
      <ul>
        <li>Revalider cette liste tous les trois mois, comme la page Ressources externes : les convocatorias ouvrent et se ferment par vagues.</li>
        <li>Retirer un lien mort plutôt que de le laisser en ligne &mdash; une ressource introuvable coûte plus de temps qu&#x27;elle n&#x27;en fait gagner.</li>
        <li>Vérifier une offre annoncée &laquo;&nbsp;SEPE&nbsp;&raquo; par un site privé sur le <a href="https://experienciafundae.es/buscador" target="_blank" rel="noopener">buscador de Fundae</a> : c&#x27;est le seul moteur qui fasse foi.</li>
        <li>Reprendre les codes du plan LABORA à chaque revalidation : ils changent d&#x27;une programmation à l&#x27;autre, contrairement aux intitulés.</li>
        <li>Relire la colonne accès après tout changement de statut : un contrat rouvre les cours <em>ocupados</em> et fait perdre la priorité LABORA.</li>
      </ul>
    </div>
  </main>

  <script src="assets/js/progress.js"></script>
  <script>
    (function () {{
      var theme = 'all', acces = 'all';
      var rows = Array.prototype.slice.call(
        document.querySelectorAll('#espagne-table tbody tr'));
      var count = document.getElementById('result-count');

      function apply() {{
        var shown = 0;
        rows.forEach(function (row) {{
          var okTheme = (theme === 'all') || (row.dataset.category === theme);
          var okAcces = (acces === 'all') || (row.dataset.acces === acces);
          var visible = okTheme && okAcces;
          row.style.display = visible ? '' : 'none';
          if (visible) shown++;
        }});
        count.textContent = shown === 0
          ? 'Aucun dispositif ne correspond à ces filtres.'
          : shown + (shown > 1 ? ' dispositifs affichés' : ' dispositif affiché')
            + ' sur ' + rows.length + '.';
      }}

      function wire(barId, attr, setter) {{
        var bar = document.getElementById(barId);
        bar.addEventListener('click', function (e) {{
          var btn = e.target.closest('.filter-btn');
          if (!btn) return;
          bar.querySelectorAll('.filter-btn').forEach(function (b) {{
            b.classList.remove('active');
          }});
          btn.classList.add('active');
          setter(btn);
          apply();
        }});
      }}

      wire('filter-theme', 'filter', function (b) {{ theme = b.dataset.filter; }});
      wire('filter-acces', 'acces', function (b) {{ acces = b.dataset.acces; }});
      apply();
    }})();
  </script>
</body>
</html>
"""

if __name__ == "__main__":
    import sys
    sys.stdout.write(render())
