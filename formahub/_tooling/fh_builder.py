#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Formahub — générateur de modules de formation complets (gabarit V5).
Blocs supportés : mise en situation, sous-sections, méthode pas à pas,
erreur fréquente, exemple, tableau, étude de cas, checklist,
exercices gradués avec corrigés, glossaire, à retenir, ressources."""
import os, re, json

OUT = "/tmp/out_v2"

def set_out(p):
    global OUT
    OUT = p

PAGE = """<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="color-scheme" content="light dark">
  <title>Formahub — {formation} : {titre}</title>
  <link rel="stylesheet" href="../../../assets/css/style.css">
</head>
<body>
  <a class="skip-link" href="#contenu">Aller au contenu</a>
  <header class="site-header">
    <a href="../../../index.html" class="brand">
      <div class="brand-icon">F</div>
      <span>Formahub</span>
    </a>
    <nav class="nav-links">
      <a href="../../../index.html" class="nav-link">Mes formations</a>
      <a href="../../../ressources-externes.html" class="nav-link">Ressources externes</a>
      <a href="../../../formations-espagne.html" class="nav-link">Formations Espagne</a>
      <button class="theme-toggle" type="button">🌙 Mode sombre</button>
    </nav>
  </header>

  <main class="main-container">
    <div class="module-header">
      <div class="breadcrumb">
        <a href="../../../index.html">Accueil</a> &gt;
        <span>{formation}</span> &gt;
        <strong>Module {num}</strong>
      </div>
      <h1>Module {num} : {titre}</h1>
      <div class="module-meta">
        <span class="badge badge-progress">⏱️ {duree}</span>
        <span class="badge badge-neutral">Module {num} sur {total}</span>
        <span class="badge badge-neutral">Niveau : {niveau}</span>
        <span class="badge badge-neutral">{nbmots} mots</span>
      </div>
    </div>

    <article class="module-content" id="contenu">
      <div class="intro-box">
        <h3>📍 Mise en situation</h3>
{situation}
      </div>

      <div class="objectives-box">
        <h3>🎯 À l'issue de ce module, vous saurez</h3>
        <ul>
{objectifs}
        </ul>
      </div>

{sections}
{etude_cas}
{checklist}
      <div class="glossary-box">
        <h3>📖 Glossaire du module</h3>
        <dl>
{glossaire}
        </dl>
      </div>

      <div class="takeaway-box">
        <h3>✅ À retenir</h3>
        <ul>
{retenir}
        </ul>
      </div>

{exercices}
      <div class="resources-box">
        <h3>🔗 Pour aller plus loin</h3>
        <ul>
{ressources}
        </ul>
      </div>
    </article>

    <section class="quiz-section">
      <h2>🧠 Quiz d'auto-évaluation</h2>
      <p style="color:var(--text-muted);margin-bottom:20px;">Sélectionnez la bonne réponse pour valider vos acquis. Le feedback immédiat vous expliquera les concepts clés.</p>
      <div id="quiz-container">
        <!-- Quiz chargé dynamiquement par quiz-engine.js -->
      </div>
      <div style="margin-top: 24px; text-align: center;">
        <button id="btn-mark-complete" data-module-id="{module_id}" class="btn btn-primary">
          Marquer le module comme terminé ✓
        </button>
      </div>
    </section>

    <nav class="module-nav">
      <a href="{prev_href}" class="btn btn-outline">{prev_label}</a>
      <a href="{next_href}" class="btn btn-primary">{next_label}</a>
    </nav>
  </main>

  <script src="../../../assets/js/progress.js"></script>
  <script src="../../../assets/js/quiz-engine.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', () => {{
      loadQuiz('quiz.json', 'quiz-container');
    }});
  </script>
</body>
</html>
"""

def P(ps, ind=6):
    return "\n".join(" " * ind + f"<p>{p}</p>" for p in ps)

def block(b, ind=6):
    s = " " * ind
    t = b["type"]
    if t == "h3":
        out = [f"{s}<h3>{b['titre']}</h3>", P(b["paras"], ind)]
        return "\n".join(x for x in out if x)
    if t == "html":
        return s + b["html"].strip()
    if t == "exemple":
        return (f'{s}<div class="example-box">\n{s}  <h4>📌 Exemple — {b["titre"]}</h4>\n'
                + P(b["paras"], ind + 2) + f"\n{s}</div>")
    if t == "method":
        steps = "\n".join(f"{s}    <li>{x}</li>" for x in b["steps"])
        intro = P(b.get("paras", []), ind + 2)
        return (f'{s}<div class="method-box">\n{s}  <h4>⚙️ Méthode — {b["titre"]}</h4>\n'
                + (intro + "\n" if intro else "")
                + f"{s}  <ol>\n{steps}\n{s}  </ol>" + f"\n{s}</div>")
    if t == "pitfall":
        return (f'{s}<div class="pitfall-box">\n{s}  <h4>⚠️ Erreur fréquente — {b["titre"]}</h4>\n'
                + P(b["paras"], ind + 2) + f"\n{s}</div>")
    raise ValueError(t)

def render_sections(sections):
    out = []
    for i, sec in enumerate(sections, 1):
        out.append(f"      <h2>{i}. {sec['titre']}</h2>")
        if sec.get("paras"):
            out.append(P(sec["paras"]))
        for b in sec.get("blocks", []):
            out.append(block(b))
        out.append("")
    return "\n".join(out)

def render_exercices(exs):
    out = ['      <h2 class="exercises-title">Exercices d\'application</h2>']
    for i, e in enumerate(exs, 1):
        out.append('      <div class="exercise-box">')
        out.append(f'        <h3>🛠️ Exercice {i} — {e["titre"]} <span class="badge badge-neutral">{e["niveau"]}</span></h3>')
        out.append(P(e["enonce"], 8))
        out.append('        <details class="solution-box">')
        out.append('          <summary>Afficher le corrigé commenté</summary>')
        out.append('          <div class="solution-content">')
        out.append("\n".join("            " + l for l in e["corrige"].strip().split("\n")))
        out.append("          </div>")
        out.append("        </details>")
        out.append("      </div>")
    return "\n".join(out)

def build(key, m):
    slug, mod = key.split("/")
    n, total = m["num"], m["total"]
    prev = ("../../../index.html", "← Retour catalogue") if n == 1 else (f"../module-{n-1}/index.html", f"← Module {n-1}")
    nxt = ("../../../index.html", "Terminer la formation ✓") if n == total else (f"../module-{n+1}/index.html", f"Module {n+1} →")

    sections_html = render_sections(m["sections"])
    words = len(re.sub(r"<[^>]+>", " ", sections_html).split())

    etude = ""
    if m.get("etude_cas"):
        e = m["etude_cas"]
        etude = ('      <div class="case-box">\n'
                 f'        <h3>🔍 Étude de cas — {e["titre"]}</h3>\n'
                 + "\n".join("        " + l for l in e["html"].strip().split("\n")) + "\n      </div>\n")
    check = ""
    if m.get("checklist"):
        items = "\n".join(f"          <li>{c}</li>" for c in m["checklist"]["items"])
        check = ('      <div class="checklist-box">\n'
                 f'        <h3>📋 {m["checklist"]["titre"]}</h3>\n'
                 f'        <ul class="checklist">\n{items}\n        </ul>\n      </div>\n')

    total_words = words + len(re.sub(r"<[^>]+>", " ", etude + check).split())

    html = PAGE.format(
        formation=m["formation"], titre=m["titre"], num=n, total=total,
        duree=m["duree"], niveau=m["niveau"], module_id=m["module_id"],
        nbmots=f"~{round(total_words, -2):.0f}".replace(".0", ""),
        situation=P(m["situation"], 8),
        objectifs="\n".join(f"          <li>{o}</li>" for o in m["objectifs"]),
        sections=sections_html, etude_cas=etude, checklist=check,
        glossaire="\n".join(f"          <dt>{t}</dt>\n          <dd>{d}</dd>" for t, d in m["glossaire"]),
        retenir="\n".join(f"          <li>{r}</li>" for r in m["retenir"]),
        exercices=render_exercices(m["exercices"]),
        ressources="\n".join(f"          <li>{r}</li>" for r in m["ressources"]),
        prev_href=prev[0], prev_label=prev[1], next_href=nxt[0], next_label=nxt[1],
    )
    path = os.path.join(OUT, slug, mod)
    os.makedirs(path, exist_ok=True)
    open(os.path.join(path, "index.html"), "w", encoding="utf-8").write(html)
    full = len(re.sub(r"<[^>]+>", " ", html).split())
    return total_words, full


