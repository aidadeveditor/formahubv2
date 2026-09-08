#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Génère ressources-externes.html à partir de la liste complète."""
import html as H
import re
import unicodedata
from pathlib import Path

# --- Colonne « Inscription » -------------------------------------------------
# Identifiant stable par ligne : le suivi (statut + date) vit dans le
# localStorage du navigateur, sous la clé formahub-inscriptions, et se
# retrouve d'une régénération à l'autre tant que l'organisme et l'intitulé
# ne changent pas.

def ins_slug(*parts):
    txt = " ".join(p for p in parts if p)
    txt = unicodedata.normalize("NFKD", txt).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^A-Za-z0-9]+", "-", txt).strip("-").lower()[:70]


_INS_SEEN = {}


def ins_id(prefix, *parts):
    base = prefix + "-" + ins_slug(*parts)
    _INS_SEEN[base] = _INS_SEEN.get(base, 0) + 1
    n = _INS_SEEN[base]
    return base if n == 1 else "{}-{}".format(base, n)


INS_CELL = (
    '<td class="ins-cell" data-ins-id="{id}">'
    '<select class="ins-status" aria-label="Statut d&#39;inscription">'
    '<option value="todo">Pas encore</option>'
    '<option value="inscrite">Inscrite</option>'
    '<option value="terminee">Terminée</option>'
    '</select>'
    '<span class="ins-date-label" hidden>Inscrite le</span>'
    '<input type="date" class="ins-date" hidden aria-label="Date d&#39;inscription">'
    '</td>')

INS_FILTER = """    <div class="filter-group">
      <span class="filter-group-label">Inscription</span>
      <div class="filter-bar" id="filter-ins">
        <button class="filter-btn active" data-ins="all">Toutes</button>
        <button class="filter-btn" data-ins="inscrite">Inscrite</button>
        <button class="filter-btn" data-ins="terminee">Terminée</button>
        <button class="filter-btn" data-ins="todo">Pas encore</button>
      </div>
    </div>
"""


SOLDE = 1353.80
PARTICIPATION = 150.0  # décret n° 2026-234 du 30 mars 2026 (publié le 1er avril),
# applicable aux demandes déposées à compter du 2 avril 2026 ; non due par les demandeurs d'emploi

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
  ("Accompagnement SEO individuel", "LiveMentor", "Mentorat individuel, 3 mois — 1 650 €",
   "1 650 €", 1650, 1500, "variable", "https://www.livementor.com/formation/seo/",
   "Le RS6710 affiché par l'organisme a expiré le 19/07/2026 ; il est remplacé par le RS7589, "
   "intitulé « Entreprendre et développer sa clientèle grâce au marketing digital » — pas une "
   "certification SEO. Faire confirmer le code réellement mobilisable avant inscription."),
  ("Formation SEO certifiante", "Skills4All", "RS — vidéos, exercices et projet final, 30 h",
   "≈ 2 000 €", 2000, 1500, "oui", "https://www.skills4all.com/", None),
  ("Formation SEO éligible CPF", "La WAB", "RS7500 — e-learning et visio hebdomadaire, 8 semaines",
   "≈ 1 485 €", 1485, 1500, "oui",
   "https://www.la-wab.fr/formation-seo-eligible-cpf-reconnu-par-l-etat", None),
  ("Formation SEO", "Wemodo (ex-Webmyday)", "RS — modules et coaching de groupe",
   "1 640 €", 1640, 1500, "oui", "https://wemodo.com/formations/web/formation-seo",
   "L'organisme a été renommé : Webmyday est devenu Wemodo. Tarif relevé sur la page : 1 640 € "
   "pour la formule certifiante, 42 h sur 3 mois, certification RS7500."),
  ("Formation SEO", "The Business Legion", "Formation et communauté Discord",
   "≈ 2 000 €", 2000, 1500, "oui", "https://the-business-legion.com/",
   "Site injoignable lors du contrôle de septembre 2026 (erreur serveur). "
   "À revérifier avant toute démarche."),
  ("Formation SEO", "Mantra (ex-GrowthMakers)", "Orientée futurs responsables SEO",
   "Variable", None, 1500, "oui", "https://www.mantra.work/",
   "Renommage GrowthMakers → Mantra confirmé (2023). Aucun tarif public sur le site : "
   "le prix de 1 990 € parfois cité n'a pas pu être vérifié, demander un devis."),
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
  ("Prompt Engineer", "Jedha", "Certification à confirmer auprès de l'organisme",
   "Variable", None, 1500, "variable", "https://www.jedha.co/",
   "Le code RS7234 ne correspond pas à cette formation : il est enregistré au nom de LION "
   "pour « Intégrer l'utilisation des outils numériques et de l'IA dans la gestion de projet ». "
   "Demander à Jedha le code exact mobilisable au CPF."),
  ("Parcours IA — Fondamental et Approfondi", "Skillevos", "Formats de 3 h à 1 journée",
   "1 300 à 2 300 €", 1300, 1500, "variable", "https://www.skillevos.fr/formation-ia-entreprise/",
   "L'organisme indique lui-même être « en cours d'agrément EDOF » pour l'éligibilité CPF : "
   "à ce stade le financement passe par l'OPCO, pas par le CPF individuel."),
  ("Formation IA", "26 Academy", "RNCP / RS — 100 % en ligne, tuteur dédié",
   "Variable", None, 1500, "oui", "https://26academy.com/", None),
  ("Formation IA", "Phoenix Performance", "RS6776 — 16 h en synchrone",
   "1 650 €", 1650, 1500, "oui", "https://www.phoenix-performance.pro/formation-ia",
   "Tarif construit pour tomber juste : 1 500 € de CPF + 150 € de participation obligatoire."),
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
  ("Gestion de projet agile", "26 Academy", "Codes à faire confirmer par l'organisme",
   "Variable", None, 1500, "variable", "https://26academy.com/",
   "Le RS5487 « Gérer un projet en mobilisant les méthodes agiles » (Simplon.co) est inactif "
   "depuis le 08/07/2026. Le RNCP37091 est actif mais correspond au titre « Manager d'unité "
   "opérationnelle » de niveau 7 (Montpellier BS), pas à une formation agile courte."),
  ("CompTIA Project+", "CompTIA", "Pour coordinateurs IT",
   "≈ 350 €", None, None, "non", "https://www.comptia.org/", None),
  ("ITIL 4 Foundation", "Cegos / Orsys", "Gestion des services IT",
   "1 200 à 1 800 €", 1200, 1500, "oui", "https://www.orsys.fr/", None),
 ]),
 ("Management d'équipe", "Management", [
  ("Manager des équipes et piloter l'efficacité collective", "26 Academy",
   "RS6626 — certificateur SCYFCO, actif jusqu'au 31/05/2027",
   "Variable", None, 1500, "oui", "https://26academy.com/", None),
  ("Manager des équipes et piloter l'efficacité collective", "Walter Learning",
   "RS6626 — 34 h, certificateur SCYFCO",
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
   "Examen seul : de l'ordre de 100 à 250 € selon le niveau", None, None, "variable",
   "https://paris.cervantes.es/fr/diplomes_espagnol/tarifs_inscription_dele.htm",
   "Ne pas confondre les deux prix : l'inscription à l'examen DELE coûte quelques centaines "
   "d'euros au plus ; les 500 à 3 000 € parfois cités correspondent à une formation de "
   "préparation vendue par un organisme tiers. Vérifier le tarif exact du niveau visé sur la "
   "page tarifs, et l'éligibilité CPF du passage de l'examen seul."),
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
  ("Responsable RSE", "Nova Formation", "E-learning avec formateur — durée à confirmer",
   "Variable", None, 1500, "oui", "https://www.novaformation.com/formation-rse/",
   "Homonyme : ne pas confondre avec le Nova Formation du secteur funéraire. La page annonce "
   "une « Formation RSE opérationnelle » de 204 h, pas 43 h, et n'affiche aucun tarif : "
   "les 2 850 € précédemment indiqués n'ont pas pu être vérifiés."),
  ("Responsable RSE", "E&H Academy", "RS7389 — 56 h sur 8 jours, sans prérequis",
   "4 000 € HT", 4000, 1500, "oui", "https://eh-academy.com/fr/formations/responsable-rse/",
   "RS7389 « Définir et déployer une stratégie de durabilité en entreprise », certificateur "
   "Des Enjeux et Des Hommes, enregistré le 27/11/2025 et actif jusqu'au 27/11/2028. "
   "Aucune session n'était ouverte lors du contrôle de septembre 2026."),
  ("Transition écologique & RSE", "L'Air des Pichoulis", "RSE, bilan carbone méthode ADEME",
   "Variable", None, 1500, "variable", "https://www.lairdespichoulis.fr/formations/",
   "Organisme Qualiopi confirmé (NDA 32 59 09711 59). L'éligibilité CPF est affirmée par "
   "l'organisme lui-même sans code RS ou RNCP publié : à faire confirmer."),
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
        ins_td = INS_CELL.format(id=ins_id("fr", orga, titre))

        rows.append(f"""          <tr data-category="{short}" data-cpf="{cpf}" data-free="{'oui' if gratuit else 'non'}">
            <td><strong>{H.escape(titre)}</strong><br><span class="orga">{H.escape(orga)} — {H.escape(note_o)}</span>{note_html}</td>
            <td><span class="badge badge-neutral">{H.escape(cat)}</span></td>
            <td>{H.escape(cout)}</td>
            <td>{badge}</td>
            <td>{rac}</td>
            <td>{lien}</td>
            {ins_td}
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
        <span class="badge badge-progress" id="ins-summary"></span>
      </div>
    </div>

    <div class="intro-box">
      <h3>📌 Comment lire la colonne « reste à charge »</h3>
      <p><strong>Reste à charge = coût de la formation − min(solde CPF ; plafond réglementaire applicable) + participation obligatoire.</strong></p>
      <p>Les plafonds 2026 retenus : <strong>1 500 €</strong> pour une certification du Répertoire spécifique hors CléA, <strong>1 600 €</strong> pour un bilan de compétences, <strong>900 €</strong> pour le permis B. Les titres RNCP, la VAE et CléA ne sont pas plafonnés.</p>
      <p>Quand un coût est annoncé sous forme de fourchette, le reste à charge affiché part du <em>tarif le plus bas</em> — considérez-le comme un plancher, pas comme un devis.</p>
      <p><strong>La colonne « Inscription »</strong> suit où vous en êtes sur chaque ligne : « Pas encore », « Inscrite » — la date du jour se remplit alors toute seule et reste modifiable — puis « Terminée ». Le suivi est enregistré dans ce navigateur, comme la progression des modules, et se filtre avec les boutons ci-dessous.</p>
    </div>

    <div class="pitfall-box">
      <h4>⚠️ Trois points à vérifier avant de vous engager</h4>
      <p><strong>La participation obligatoire est de 150 €.</strong> Fixée par le décret n° 2026-234 du 30 mars 2026, elle s'applique à toute demande d'inscription déposée <strong>à compter du 2 avril 2026</strong> (elle était de 100 € depuis mai 2024, puis de 103,20 € au 1er janvier 2026). Elle est due une fois par dossier, quel que soit le coût de la formation. <strong>Deux cas d'exonération</strong> : les demandeurs d'emploi n'en sont pas redevables, et elle est neutralisée lorsque l'employeur ou un opérateur de compétences abonde le dossier. Elle n'est donc pas intégrée aux montants du tableau — le montant réellement dû s'affiche à l'inscription sur moncompteformation.gouv.fr.</p>
      <p><strong>Le code de certification annoncé.</strong> Un code RS ou RNCP se périme : plusieurs organismes affichent encore un code expiré, ou un code qui ne correspond pas à la formation vendue. Avant de payer, cherchez le code sur <a href="https://www.francecompetences.fr/" target="_blank" rel="noopener">francecompetences.fr</a> et vérifiez trois choses : qu'il est actif, que son intitulé correspond bien à ce que vous allez apprendre, et que l'organisme est le certificateur ou un partenaire déclaré. Les lignes concernées de ce tableau portent un avertissement.</p>
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

{INS_FILTER}
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
            <th>Inscription</th>
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
      var theme = 'all', money = 'all', ins = 'all';
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
          var okIns = (ins === 'all') || ((row.dataset.ins || 'todo') === ins);
          var visible = okTheme && okMoney && okIns;
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
      wire('filter-ins', function (b) {{ ins = b.dataset.ins; }});

      window.formahubApplyFilters = apply;
      apply();
    }})();
  </script>
</body>
</html>
"""

# La page est écrite à côté des autres, quel que soit le dossier courant.
OUT = Path(__file__).resolve().parent.parent / "ressources-externes.html"
OUT.write_text(PAGE, encoding="utf-8")
print(f"{len(rows)} ressources | {n_cpf} CPF | {n_free} gratuites | "
      f"{len(PAGE)} octets → {OUT}")
