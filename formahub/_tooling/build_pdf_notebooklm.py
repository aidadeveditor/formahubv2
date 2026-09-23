#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Formahub — export d'une formation en PDF pour NotebookLM.

Reprend le contenu réel de chaque module (index.html + quiz.json), le
remet en forme dans un document imprimable propre — sans navigation, sans
boutons, corrigés d'exercices et quiz développés — et l'exporte en PDF
avec la mise en page du site (assets/css/style.css), via Chromium headless
(Playwright). Le PDF obtenu peut être déposé comme source dans un notebook
NotebookLM pour en générer un podcast audio.

Le fichier audio résultant, une fois téléchargé depuis NotebookLM, se
dépose dans `formations/<slug>/module-N/podcast-audio.mp3` (ou .m4a/.wav) :
`assets/js/audio.js` le détecte automatiquement et l'utilise à la place
de la voix de synthèse — voir le README, section « Audio et podcasts ».

Usage :
    python3 _tooling/build_pdf_notebooklm.py seo                  # tous les modules de la formation
    python3 _tooling/build_pdf_notebooklm.py seo/module-3         # un seul module
    python3 _tooling/build_pdf_notebooklm.py seo content-marketing --out /chemin/sortie

Sans --out, les PDF sont écrits dans ../notebooklm-exports/<slug>/
(en dehors de formahub/, donc jamais déployés sur Cloudflare Pages).

Dépendances : pip install beautifulsoup4 playwright && playwright install chromium
"""
import argparse
import json
import os
import sys
from pathlib import Path

from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

SITE_ROOT = Path(__file__).resolve().parent.parent


def find_chromium():
    for p in Path("/opt/pw-browsers").glob("chromium-*/chrome-linux/chrome"):
        return str(p)
    return None  # Playwright utilisera le Chromium qu'il a lui-même installé


def build_quiz_html(quiz):
    if not quiz or not quiz.get("questions"):
        return ""
    parts = ['<section class="quiz-recap"><h2>Quiz d\'auto-évaluation — questions et corrigé</h2>']
    for i, q in enumerate(quiz["questions"], 1):
        parts.append('<div class="method-box">')
        parts.append(f"<h4>Question {i} — {q.get('question', '')}</h4>")
        parts.append("<ul>")
        correct = q.get("correct_answer")
        for choice in q.get("choices", []):
            marker = " ✅ (bonne réponse)" if choice.get("key") == correct else ""
            parts.append(f"<li>{choice.get('key', '').upper()}. {choice.get('text', '')}{marker}</li>")
        parts.append("</ul>")
        if q.get("feedback"):
            parts.append(f"<p><em>Explication : {q['feedback']}</em></p>")
        parts.append("</div>")
    parts.append("</section>")
    return "\n".join(parts)


def extract_module(html_path: Path):
    soup = BeautifulSoup(html_path.read_text(encoding="utf-8"), "html.parser")

    title_el = soup.select_one(".module-header h1")
    titre = title_el.get_text(strip=True) if title_el else html_path.parent.name

    meta_el = soup.select_one(".module-header .module-meta")
    meta_html = str(meta_el) if meta_el else ""

    article = soup.select_one("article.module-content")
    if article is None:
        raise ValueError(f"pas de .module-content dans {html_path}")

    # Développe tous les corrigés (details.solution-box) : ils doivent
    # apparaître dans le PDF sans interaction possible.
    for det in article.select("details"):
        det["open"] = "open"
        summary = det.find("summary")
        if summary:
            summary["style"] = "font-weight:600;"

    return titre, meta_html, str(article)


def render_pdf(titre, meta_html, article_html, quiz_html, css_href, out_pdf: Path):
    doc = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<title>{titre}</title>
<link rel="stylesheet" href="{css_href}">
<style>
  body {{ background:#fff; }}
  .main-container {{ max-width: 820px; margin: 0 auto; padding: 24px 8px; }}
  .print-title {{ margin-bottom: 4px; }}
  .print-meta {{ margin-bottom: 28px; }}
  details > summary {{ cursor: default; }}
  details > summary::-webkit-details-marker {{ display: none; }}
  @page {{ margin: 16mm 14mm; }}
  /* L'export d'impression de Chromium fige les animations sur leur image
     de départ (opacity: 0) : on les désactive pour que tout reste visible. */
  *, *::before, *::after {{ animation: none !important; transition: none !important; opacity: 1 !important; }}
</style>
</head>
<body>
<main class="main-container">
  <h1 class="print-title">{titre}</h1>
  <div class="module-meta print-meta">{meta_html}</div>
  {article_html}
  {quiz_html}
</main>
</body>
</html>"""
    tmp_html = out_pdf.with_suffix(".tmp.html")
    tmp_html.write_text(doc, encoding="utf-8")

    with sync_playwright() as p:
        browser = p.chromium.launch(executable_path=find_chromium())
        page = browser.new_page()
        page.goto(tmp_html.resolve().as_uri())
        page.pdf(path=str(out_pdf), format="A4", print_background=True,
                 margin={"top": "16mm", "bottom": "16mm", "left": "14mm", "right": "14mm"})
        browser.close()
    tmp_html.unlink(missing_ok=True)


def resolve_keys(root: Path, arg: str):
    """« seo » -> tous les modules ; « seo/module-3 » -> un seul module."""
    if "/" in arg:
        return [arg]
    formation_dir = root / "formations" / arg
    if not formation_dir.is_dir():
        raise SystemExit(f"formation inconnue : {arg}")
    modules = sorted(
        (p.name for p in formation_dir.iterdir() if p.is_dir() and p.name.startswith("module-")),
        key=lambda n: int(n.split("-")[1]) if n.split("-")[1].isdigit() else 0,
    )
    return [f"{arg}/{m}" for m in modules]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cibles", nargs="+", help="slug de formation (ex. seo) ou slug/module-N")
    ap.add_argument("--root", default=str(SITE_ROOT), help="racine du site (défaut : dossier parent de _tooling)")
    ap.add_argument("--out", default=None, help="dossier de sortie (défaut : ../notebooklm-exports/<slug>/)")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    css_href = (root / "assets" / "css" / "style.css").resolve().as_uri()

    keys = []
    for cible in args.cibles:
        keys.extend(resolve_keys(root, cible))

    for key in keys:
        slug, mod = key.split("/")
        out_dir = Path(args.out).resolve() if args.out else (root.parent / "notebooklm-exports" / slug)
        out_dir.mkdir(parents=True, exist_ok=True)

        mod_dir = root / "formations" / slug / mod
        html_path = mod_dir / "index.html"
        quiz_path = mod_dir / "quiz.json"
        if not html_path.exists():
            print(f"{key:28} -> ABSENT, ignoré")
            continue

        titre, meta_html, article_html = extract_module(html_path)
        quiz_html = build_quiz_html(json.loads(quiz_path.read_text(encoding="utf-8"))) if quiz_path.exists() else ""

        out_pdf = out_dir / f"{mod}.pdf"
        render_pdf(titre, meta_html, article_html, quiz_html, css_href, out_pdf)
        size_ko = out_pdf.stat().st_size / 1024
        print(f"{key:28} -> {out_pdf}  ({size_ko:.0f} Ko)")


if __name__ == "__main__":
    main()
