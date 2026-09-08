#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Harnais de validation Formahub V7.

Usage : FH_OUT=<dossier des modules> FH_CSS=<chemin style.css> \\
            python3 validate.py <slug-formation> <nb-modules>
Sortie : une ligne par module, VALIDÉ ou ÉCHEC pour la formation.
"""
import json, os, re, sys
from html.parser import HTMLParser

OUT = os.environ.get("FH_OUT", "/tmp/out_v2")
VOID = {"area","base","br","col","embed","hr","img","input","link","meta",
        "param","source","track","wbr"}
ALLOWED = set("🌙🎯📌📖✅🛠️🧠⏱️→←✓✗📍⚙️⚠️🔍📋🔗")

CSS = open(os.environ.get("FH_CSS", "/tmp/style.css"), encoding="utf-8").read()
CSS_CLASSES = set(re.findall(r"\.([a-zA-Z][\w-]*)", CSS))

class Balance(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack = []
        self.errors = []
    def handle_starttag(self, tag, attrs):
        if tag not in VOID:
            self.stack.append(tag)
    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack:
            self.errors.append(f"</{tag}> sans ouvrant")
        elif self.stack[-1] != tag:
            self.errors.append(f"</{tag}> alors que <{self.stack[-1]}> est ouvert")
            if tag in self.stack:
                while self.stack and self.stack.pop() != tag:
                    pass
        else:
            self.stack.pop()

REQUIRED = ["intro-box", "module-meta", "example-box", "takeaway-box",
            "glossary-box", "solution-box", "checklist-box", "resources-box"]

def check(slug, n, total):
    d = f"{OUT}/{slug}/module-{n}"
    path = f"{d}/index.html"
    errs, warns = [], []
    html = open(path, encoding="utf-8").read()

    # 1. équilibre des balises
    b = Balance(); b.feed(html)
    errs += [f"balise: {e}" for e in b.errors]
    if b.stack:
        errs.append(f"balises non fermées: {b.stack}")

    # 2. caractères parasites
    for i, ch in enumerate(html):
        o = ord(ch)
        if o < 128 or ch in ALLOWED:
            continue
        if 0x00C0 <= o <= 0x017F or ch in "“”‘’—–…«»°€·×≤≥≈≠±ᵉ⁻¹²³½¼¾":
            continue
        errs.append(f"caractère suspect {ch!r} (U+{o:04X}) pos {i}: "
                    f"...{html[max(0,i-40):i+40]}...")

    # 3. blocs pédagogiques requis
    for cls in REQUIRED:
        if f'class="{cls}"' not in html and f'"{cls}' not in html:
            errs.append(f"bloc manquant: .{cls}")

    # 4. classes CSS couvertes
    used = set()
    for m in re.findall(r'class="([^"]+)"', html):
        used.update(m.split())
    missing = sorted(c for c in used if c not in CSS_CLASSES)
    if missing:
        errs.append(f"classes sans CSS: {missing}")

    # 5. quiz
    qp = f"{d}/quiz.json"
    if not os.path.exists(qp):
        errs.append("quiz.json absent")
    else:
        q = json.load(open(qp, encoding="utf-8"))
        mid_html = re.search(r'data-module-id="([^"]+)"', html)
        mid_html = mid_html.group(1) if mid_html else None
        if q.get("module_id") != mid_html:
            errs.append(f"module_id quiz={q.get('module_id')} vs html={mid_html}")
        for i, qq in enumerate(q.get("questions", []), 1):
            keys = [c["key"] for c in qq.get("choices", [])]
            if qq.get("correct_answer") not in keys:
                errs.append(f"Q{i}: correct_answer {qq.get('correct_answer')!r} "
                            f"absent des choix {keys}")
            if len(set(keys)) != len(keys):
                errs.append(f"Q{i}: clés de choix dupliquées {keys}")
            if not qq.get("feedback"):
                warns.append(f"Q{i}: feedback vide")
            for c in qq.get("choices", []):
                if re.search(r"<(?!/?(strong|em|code|br)\b)[a-zA-Z]", c["text"]):
                    errs.append(f"Q{i}: HTML brut dans un choix: {c['text'][:60]}")
        if len(q.get("questions", [])) < 3:
            warns.append(f"quiz seulement {len(q.get('questions', []))} questions")

    # 6. scripts de la V7 (audio, hors ligne, sauvegarde)
    for js in ("progress.js", "quiz-engine.js", "sync.js", "offline.js", "audio.js"):
        if f"assets/js/{js}" not in html:
            errs.append(f"script manquant: {js}")
    if html.index("assets/js/audio.js") < html.index("assets/js/progress.js"):
        errs.append("audio.js doit être chargé APRÈS progress.js (il lit les volets qu'il construit)")

    # 7. podcast du module, s'il existe
    pp = f"{d}/podcast.json"
    if not os.path.exists(pp):
        warns.append("pas de podcast.json (le lecteur affichera « à venir »)")
    else:
        pod = json.load(open(pp, encoding="utf-8"))
        mid_html2 = re.search(r'data-module-id="([^"]+)"', html)
        mid_html2 = mid_html2.group(1) if mid_html2 else None
        if pod.get("module_id") != mid_html2:
            errs.append(f"module_id podcast={pod.get('module_id')} vs html={mid_html2}")
        lignes = pod.get("lignes", [])
        if len(lignes) < 12:
            errs.append(f"podcast: {len(lignes)} répliques seulement")
        voix = {l.get("v") for l in lignes}
        if not voix <= {"a", "b"} or len(voix) < 2:
            errs.append(f"podcast: voix attendues a et b, trouvé {sorted(voix)}")
        for i, l in enumerate(lignes, 1):
            t = l.get("t", "")
            if re.search(r"<[a-zA-Z/]", t):
                errs.append(f"podcast réplique {i}: HTML dans le texte parlé")
            if not t.strip():
                errs.append(f"podcast réplique {i}: vide")
        pmots = sum(len(re.findall(r"\w+", l.get("t", ""))) for l in lignes)
        if pmots < 900:
            warns.append(f"podcast court: {pmots} mots (~{max(1, round(pmots / 155))} min)")

    # 8. navigation
    prev = f"../module-{n-1}/" if n > 1 else None
    nxt = f"../module-{n+1}/" if n < total else None
    for link, label in ((prev, "précédent"), (nxt, "suivant")):
        if link and link not in html:
            errs.append(f"lien {label} manquant ({link})")

    words = len(re.findall(r"\w+", re.sub(r"<[^>]+>", " ", html)))
    return errs, warns, words


def run(slug, total):
    print(f"\n=== {slug} ===")
    ok = True
    for n in range(1, total + 1):
        errs, warns, words = check(slug, n, total)
        status = "OK " if not errs else "KO "
        print(f"  module-{n}: {status} {words} mots"
              + (f" | {len(warns)} avert." if warns else ""))
        for e in errs:
            ok = False
            print(f"      ERREUR: {e}")
        for w in warns:
            print(f"      avert.: {w}")
    print("  ->", "VALIDÉ" if ok else "ÉCHEC")
    return ok


if __name__ == "__main__":
    slug = sys.argv[1]
    total = int(sys.argv[2])
    sys.exit(0 if run(slug, total) else 1)
