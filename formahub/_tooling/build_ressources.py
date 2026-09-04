#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère ressources-externes.html à partir de la liste complète."""
import html as H

SOLDE = 1353.80
PART_MIN, PART_MAX = 103.20, 150.0

# (titre, organisme, note_organisme, cout_txt, cout_min|None, plafond|None,
#  cpf: "oui"|"non"|"variable", url|None, note|None)
CATS = [
 ("SEO Fondamentaux", "SEO", [
  ("Google Search Central", "Google", "Documentation officielle, mise à jour continue",
   "Gratuit", None, None, "non", "https://developers.google.com/search?hl=fr", None),
  ("Parcours SEO", "OpenClassrooms", "Parcours structuré, environ 10 h",
   "Gratuit (mode libre)", None, None, "non", "https://openclassrooms.com/fr/", None),
  ("Semrush Academy", "Semrush", "Modules courts, tous niveaux",
   "Gratuit", None, None, "non", "https://www.semrush.com/academy/", None),
  ("Accompagnement SEO individuel", "LiveMentor", "RS6710 — mentorat individuel",
   "1 650 à 1 980 €", 1650, 1500, "oui", "https://www.livementor.com/formation/seo/", None),
  ("Formation SEO certifiante", "Skills4All", "RS — vidéos, exercices et projet final, 30 h",
   "≈ 2 000 €", 2000, 1500, "oui", "https://www.skills4all.com/", None),
  ("Formation SEO éligible CPF", "La WAB", "RS7500 — e-learning et visio hebdomadaire, 8 semaines",
   "≈ 1 485 €", 1485, 1500, "oui",
   "https://www.la-wab.fr/formation-seo-eligible-cpf-reconnu-par-l-etat", None),
  ("Formation SEO", "Wemodo (ex-Webmyday)", "RS — modules et coaching de groupe",
   "1 740 à 2 088 €", 1740, 1500, "oui", "https://wemodo.com/formations/web/formation-seo",
   "L'organisme a été renommé : Webmyday est devenu Wemodo."),
  ("Formation SEO", "The Business Legion", "Formation et communauté Discord",
   "≈ 2 000 €", 2000, 1500, "oui", "https://the-business-legion.com/", None),
  ("Formation SEO", "Mantra (ex-GrowthMakers)", "Orientée futurs responsables SEO",
   "≈ 1 990 €", 1990, 1500, "oui", "https://www.mantra.work/", None),
  ("Cours SEO (Guersan)", "Udemy", "9 h 30 de contenu — option petit budget",
   "≈ 22,99 €", None, None, "non", "https://www.udemy.com/", None),
 ]),
 ("Content Marketing", "Content Marketing", [
  ("Content Marketing Certification", "HubSpot Academy", "8 h, certificat gratuit",
   "Gratuit", None, None, "non", "https://academy.hubspot.fr/courses/content-marketing", None),
  ("Content Strategy Course", "HubSpot Academy", "Cours complémentaire",
   "Gratuit", None, None, "non", "https://academy.hubspot.com/courses/content-strategy", None),
  ("Formation marketing digital", "HubSpot Academy", "Vue d'ensemble marketing",
   "Gratuit", None, None, "non", "https://academy.hubspot.fr/", None),
 ]),
 ("IA Générative", "IA Générative", [
  ("Formation IA générative", "SavoirIA", "RS6776 — 16 h, présentiel ou distanciel",
   "Variable", None, 1500, "oui", "https://www.savoiria.fr/", None),
  ("Formation IA générative", "Jedha", "Certification IA générative, 42 h",
   "1 500 €", 1500, 1500, "oui", "https://www.jedha.co/", None),
  ("Prompt Engineer", "Jedha", "RS7234 — certification « Generative AI »",
   "Variable", None, 1500, "oui", "https://www.jedha.co/", None),
  ("Parcours IA — Fondamental et Approfondi", "Skillevos", "RS6776",
   "Variable", None, 1500, "oui", "https://www.skillevos.fr/formation-ia-entreprise/", None),
  ("Formation IA générative", "Perma France", "18 h — annoncée sans reste à charge",
   "≈ 1 490 €", 1490, 1500, "oui", None,
   "Organisme non retrouvé lors de la vérification des liens — à confirmer avant toute inscription."),
  ("Formation IA", "26 Academy", "RNCP / RS — 100 % en ligne, tuteur dédié",
   "Variable", None, 1500, "oui", "https://26academy.com/", None),
  ("Formation IA", "Phoenix Performance", "16 h — prise en charge annoncée jusqu'à 1 500 €",
   "Variable", None, 1500, "oui", "https://www.phoenix-performance.pro/formation-ia", None),
  ("Introduction to Generative AI", "Google Cloud Skills Boost", "Fondamentaux de l'IA générative",
   "Gratuit", None, None, "non", "https://www.cloudskillsboost.google/paths/118", None),
  ("Notions fondamentales — IA générative", "Microsoft Learn", "Parcours guidé",
   "Gratuit", None, None, "non",
   "https://learn.microsoft.com/fr-fr/training/paths/introduction-generative-ai/", None),
 ]),
 ("Gestion de projet", "Gestion de projet", [
  ("Google Project Management Certificate", "Coursera", "Idéal pour débuter",
   "150 à 300 €", None, None, "non", "https://www.coursera.org/", None),
  ("PRINCE2 Foundation", "Skills4All / Oo2 / Cegos", "RS — référence internationale",
   "1 450 à 2 500 €", 1450, 1500, "oui",
   "https://www.skills4all.com/", None),
  ("Préparation PMP", "Cegos / Orsys / Demos", "Certification PMP",
   "2 000 à 3 500 €", 2000, 1500, "oui", "https://www.cegos.fr/", None),
  ("Gestion de projet agile", "26 Academy", "RS5487 / RNCP37091 — Scrum, transformation digitale",
   "Variable", None, 1500, "oui", "https://26academy.com/", None),
  ("CompTIA Project+", "CompTIA", "Pour coordinateurs IT",
   "≈ 350 €", None, None, "non", "https://www.comptia.org/", None),
  ("ITIL 4 Foundation", "Cegos / Orsys", "Gestion des services IT",
   "1 200 à 1 800 €", 1200, 1500, "oui", "https://www.orsys.fr/", None),
 ]),
 ("Management d'équipe", "Management", [
  ("Manager des équipes de proximité", "26 Academy", "RS6626",
   "Variable", None, 1500, "oui", "https://26academy.com/", None),
  ("Management d'équipe", "Walter Learning", "RS6626 — 34 h",
   "Variable", None, 1500, "oui", "https://walter-learning.com/", None),
  ("Certification RS6626", "Organismes référencés MaFormation", "Comparateur multi-organismes",
   "2 110 à 2 850 €", 2110, 1500, "oui", "https://www.maformation.fr/", None),
  ("Certificat de Compétences en Entreprise (CCE)", "CCI Formation", "Certification CCE",
   "Variable", None, 1500, "oui", "https://www.cci.fr/ressources/formation",
   "Le portail national des CCI ; les tarifs et sessions dépendent de la CCI territoriale."),
 ]),
 ("CRM Salesforce", "CRM", [
  ("Trailhead — parcours officiel Salesforce", "Salesforce", "Badges et superbadges officiels, sans certification CPF",
   "Gratuit", None, None, "non", "https://trailhead.salesforce.com/fr", None),
 ]),
 ("Langues", "Langues", [
  ("DELE espagnol (A1 à C2)", "Instituto Cervantes", "Officialise un niveau d'espagnol déjà acquis",
   "500 à 3 000 € selon le niveau", 500, 1500, "oui",
   "https://paris.cervantes.es/fr/examens_espagnol/info_examens_espagnol.htm", None),
  ("TOEIC / DELE / Goethe / CILS", "OpenLang", "RS — organisme certifié Qualiopi",
   "Variable", None, 1500, "oui", "https://openlang.fr/", None),
  ("LILATE / CLOE", "Cercle des Langues", "RS — guide et organismes partenaires",
   "Variable", None, 1500, "oui", "https://www.cercledeslangues.com/", None),
  ("TOEIC / DELE / Goethe / DELF", "Linguaphone", "Certifié Qualiopi",
   "Variable", None, 1500, "oui", "https://www.linguaphone.fr/", None),
  ("TCF / TOEIC / Linguaskill", "ILE International", "Sessions individuelles ou collectives",
   "Variable", None, 1500, "oui", "https://ile-international.com/", None),
 ]),
 ("Transition écologique & RSE", "RSE", [
  ("Responsable RSE", "Nova Formation", "43 h — e-learning avec formateur",
   "2 850 €", 2850, 1500, "oui", "https://www.novaformation.com/formation-rse/",
   "Homonyme : ne pas confondre avec le Nova Formation du secteur funéraire."),
  ("Responsable RSE", "E&H Academy", "RS7389 — sans prérequis, éligible depuis janvier 2026",
   "Variable", None, 1500, "oui", "https://eh-academy.com/fr/formations/responsable-rse/", None),
  ("Transition écologique & RSE", "L'Air des Pichoulis", "Diagnostic, plan d'action, bilan carbone",
   "Variable", None, 1500, "oui", "https://www.lairdespichoulis.fr/formations/", None),
  ("Stratège de la Transformation Durable", "École Polytechnique (Exed)", "RNCP41077BC05 — 68 h",
   "14 400 € TTC", 14400, None, "oui",
   "https://exed.polytechnique.edu/formations/durabilite/stratege-transformation-durable",
   "Hors budget au regard du solde CPF actuel : un financement complémentaire serait nécessaire."),
 ]),
 ("Plateformes transversales", "Transversal", [
  ("Parcours diplômants et cours libres", "OpenClassrooms", "SEO, gestion de projet, marketing, management",
   "Gratuit en mode libre ; ≈ 3 600 € pour un parcours RNCP", 3600, None, "variable",
   "https://openclassrooms.com/fr/",
   "CPF uniquement pour les parcours RNCP — jamais pour le mode libre."),
  ("Cours en mode audit", "Coursera", "IA générative, gestion de projet, management",
   "Gratuit sans certificat", None, None, "non", "https://www.coursera.org/", None),
  ("MOOC universitaires", "Fun-Mooc", "Tous domaines, portage ministériel",
   "Gratuit", None, None, "non", "https://www.fun-mooc.fr/", None),
  ("Catalogue vidéo", "LinkedIn Learning", "Management, marketing, CRM, compétences transverses",
   "1 mois offert, puis ≈ 30 €/mois", None, None, "non", "https://www.linkedin.com/learning/", None),
  ("Ateliers Numériques", "Google", "Marketing digital et SEO",
   "Gratuit", None, None, "non", "https://grow.google/intl/fr_fr/", None),
  ("Bases transversales", "Khan Academy", "Fondamentaux, tous niveaux",
   "Gratuit", None, None, "non", "https://fr.khanacademy.org/", None),
  ("Aide Individuelle à la Formation (AIF)", "France Travail", "Abondement possible en complément du CPF, selon profil",
   "Prise en charge selon profil", None, None, "variable",
   "https://www.francetravail.fr/candidat/en-formation/mes-aides-financieres/laide-individuelle-a-la-formatio.html",
   "Accessible aux demandeurs d'emploi ; se cumule avec le CPF."),
 ]),
]


def euro(v):
    return f"{v:,.0f}".replace(",", " ") + " €"


def reste(cout_min, plafond):
    """Reste après mobilisation du CPF, hors participation obligatoire."""
    if cout_min is None:
        return None
    pris = min(SOLDE, plafond) if plafond else SOLDE
    r = cout_min - pris
    return max(r, 0.0)


rows, n_cpf, n_free = [], 0, 0
for cat, short, items in CATS:
    for (titre, orga, note_o, cout, cmin, plaf, cpf, url, note) in items:
        gratuit = cout.lower().startswith("gratuit")
        if cpf == "oui":
            n_cpf += 1
        if gratuit:
            n_free += 1

        if gratuit:
            rac = '<strong>0 €</strong>'
        elif cpf == "non":
            rac = f'<strong>{H.escape(cout)}</strong><br><span class="rac-note">non finançable</span>'
        else:
            r = reste(cmin, plaf)
            if r is None:
                rac = '<span class="rac-note">à chiffrer auprès de l\'organisme</span>'
            elif r == 0:
                rac = ('<strong>0 €</strong><br>'
                       '<span class="rac-note">+ participation obligatoire</span>')
            else:
                if " à " in cout:
                    approx = "à partir de "
                elif cout.startswith("≈"):
                    approx = "environ "
                else:
                    approx = ""
                rac = (f'<strong>{approx}{euro(r)}</strong><br>'
                       f'<span class="rac-note">+ participation obligatoire</span>')

        if cpf == "oui":
            badge = '<span class="badge badge-success">Éligible CPF</span>'
        elif cpf == "variable":
            badge = '<span class="badge badge-warning">Sous conditions</span>'
        else:
            badge = '<span class="badge badge-neutral">Non éligible</span>'

        if url:
            lien = (f'<a href="{url}" target="_blank" rel="noopener" class="btn btn-outline" '
                    f'style="padding:4px 10px;font-size:0.85rem;white-space:nowrap;">Consulter ↗</a>')
        else:
            lien = '<span class="rac-note">lien non vérifié</span>'

        note_html = (f'<br><span class="row-note">⚠️ {H.escape(note)}</span>') if note else ""

        rows.append(f"""          <tr data-category="{short}" data-cpf="{cpf}" data-free="{'oui' if gratuit else 'non'}">
            <td><strong>{H.escape(titre)}</strong><br><span class="orga">{H.escape(orga)} — {H.escape(note_o)}</span>{note_html}</td>
            <td><span class="badge badge-neutral">{H.escape(cat)}</span></td>
            <td>{H.escape(cout)}</td>
            <td>{badge}</td>
            <td>{rac}</td>
            <td>{lien}</td>
          </tr>""")

filters = "\n".join(
    f'      <button class="filter-btn" data-filter="{s}">{H.escape(s)}</button>'
    for _, s, _ in CATS)

PAGE = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Formahub — Ressources externes &amp; formations suggérées</title>
  <link rel="stylesheet" href="assets/css/style.css">
  <style>
    .orga {{ color: var(--text-muted); font-size: 0.85rem; }}
    .rac-note {{ color: var(--text-muted); font-size: 0.78rem; }}
    .row-note {{ display: block; margin-top: 6px; color: var(--text-muted);
                 font-size: 0.78rem; line-height: 1.45; }}
    .filter-group {{ margin-bottom: 10px; }}
    .filter-group-label {{ display: block; font-size: 0.78rem; text-transform: uppercase;
                           letter-spacing: 0.05em; color: var(--text-muted); margin-bottom: 6px; }}
    #result-count {{ color: var(--text-muted); font-size: 0.9rem; margin: 4px 0 18px; }}
    #ressources-table td:first-child {{ min-width: 240px; }}
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
      <a href="ressources-externes.html" class="nav-link active">Ressources externes</a>
      <button class="theme-toggle" type="button">🌙 Mode Sombre</button>
    </nav>
  </header>

  <main class="main-container">
    <div class="hero-banner">
      <h1>Ressources externes &amp; formations suggérées</h1>
      <p>{len(rows)} ressources pour prolonger les six parcours Formahub : documentations officielles gratuites, cours en accès libre et formations certifiantes éligibles au CPF.</p>
      <div style="margin-top: 16px; display: flex; gap: 12px; flex-wrap: wrap;">
        <span class="badge badge-progress">Solde CPF de référence : 1 353,80 €</span>
        <span class="badge badge-success">{n_cpf} formations éligibles CPF</span>
        <span class="badge badge-neutral">{n_free} ressources gratuites</span>
      </div>
    </div>

    <div class="intro-box">
      <h3>📌 Comment lire la colonne « reste à charge »</h3>
      <p><strong>Reste à charge = coût de la formation − min(solde CPF ; plafond réglementaire applicable) + participation obligatoire.</strong></p>
      <p>Les plafonds 2026 retenus : <strong>1 500 €</strong> pour une certification du Répertoire spécifique hors CléA, <strong>1 600 €</strong> pour un bilan de compétences, <strong>900 €</strong> pour le permis B. Les titres RNCP, la VAE et CléA ne sont pas plafonnés.</p>
      <p>Quand un coût est annoncé sous forme de fourchette, le reste à charge affiché part du <em>tarif le plus bas</em> — considérez-le comme un plancher, pas comme un devis.</p>
    </div>

    <div class="pitfall-box">
      <h4>⚠️ Deux points à vérifier avant de vous engager</h4>
      <p><strong>Le montant de la participation obligatoire.</strong> Les sources consultées l'annoncent entre <strong>103,20 €</strong> et <strong>150 €</strong>. Elle n'est donc pas intégrée aux montants du tableau, qui indiquent seulement « + participation obligatoire ». Le montant exact s'affiche au moment de l'inscription sur moncompteformation.gouv.fr.</p>
      <p><strong>Le solde CPF réellement disponible.</strong> Les cinq dernières années travaillées en Espagne n'alimentent pas le CPF français : le solde de référence utilisé ici est à confirmer sur <a href="https://www.moncompteformation.gouv.fr/" target="_blank" rel="noopener">moncompteformation.gouv.fr</a> avant tout arbitrage. Tous les calculs de cette page en dépendent.</p>
      <p>Enfin, le CPF ne finance que les formations menant à une certification RNCP ou RS. Une attestation de suivi, même délivrée par un organisme sérieux, n'ouvre aucun droit.</p>
    </div>

    <div class="filter-group">
      <span class="filter-group-label">Thématique</span>
      <div class="filter-bar" id="filter-theme">
        <button class="filter-btn active" data-filter="all">Toutes</button>
{filters}
      </div>
    </div>

    <div class="filter-group">
      <span class="filter-group-label">Financement</span>
      <div class="filter-bar" id="filter-money">
        <button class="filter-btn active" data-money="all">Tous</button>
        <button class="filter-btn" data-money="cpf">Éligible CPF</button>
        <button class="filter-btn" data-money="free">Gratuit</button>
      </div>
    </div>

    <p id="result-count"></p>

    <div class="table-responsive">
      <table id="ressources-table">
        <thead>
          <tr>
            <th>Intitulé &amp; organisme</th>
            <th>Thématique</th>
            <th>Coût annoncé</th>
            <th>CPF</th>
            <th>Reste à charge estimé</th>
            <th>Lien</th>
          </tr>
        </thead>
        <tbody>
{chr(10).join(rows)}
        </tbody>
      </table>
    </div>

    <div class="takeaway-box">
      <h3>✅ Méthode de mise à jour</h3>
      <ul>
        <li>Revalider cette liste tous les trois mois : les tarifs et l'éligibilité CPF évoluent vite.</li>
        <li>Retirer un lien mort plutôt que de le laisser en ligne — une ressource introuvable coûte plus de temps qu'elle n'en fait gagner.</li>
        <li>Vérifier le code RNCP ou RS sur <a href="https://www.francecompetences.fr/recherche_certificationprofessionnelle/" target="_blank" rel="noopener">France Compétences</a> avant de retenir une formation : c'est la seule source qui fasse foi sur l'éligibilité.</li>
        <li>Comparer au moins deux organismes pour une même certification — les écarts de prix sur un même code RS dépassent souvent 50 %.</li>
      </ul>
    </div>
  </main>

  <script src="assets/js/progress.js"></script>
  <script>
    (function () {{
      var theme = 'all', money = 'all';
      var rows = Array.prototype.slice.call(
        document.querySelectorAll('#ressources-table tbody tr'));
      var count = document.getElementById('result-count');

      function apply() {{
        var shown = 0;
        rows.forEach(function (row) {{
          var okTheme = (theme === 'all') || (row.dataset.category === theme);
          var okMoney = (money === 'all')
            || (money === 'cpf' && row.dataset.cpf === 'oui')
            || (money === 'free' && row.dataset.free === 'oui');
          var visible = okTheme && okMoney;
          row.style.display = visible ? '' : 'none';
          if (visible) shown++;
        }});
        count.textContent = shown === 0
          ? 'Aucune ressource ne correspond à ces filtres.'
          : shown + (shown > 1 ? ' ressources affichées' : ' ressource affichée')
            + ' sur ' + rows.length + '.';
      }}

      function wire(barId, handler) {{
        var bar = document.getElementById(barId);
        bar.addEventListener('click', function (e) {{
          var btn = e.target.closest('.filter-btn');
          if (!btn) return;
          bar.querySelectorAll('.filter-btn').forEach(function (b) {{
            b.classList.remove('active');
          }});
          btn.classList.add('active');
          handler(btn);
          apply();
        }});
      }}

      wire('filter-theme', function (b) {{ theme = b.dataset.filter; }});
      wire('filter-money', function (b) {{ money = b.dataset.money; }});
      apply();
    }})();
  </script>
</body>
</html>
"""

open("/tmp/ressources-externes.html", "w", encoding="utf-8").write(PAGE)
print(f"{len(rows)} ressources | {n_cpf} CPF | {n_free} gratuites | {len(PAGE)} octets")
