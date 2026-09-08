#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Formahub — générateur des podcasts de module (podcast.json).

Chaque module peut recevoir un podcast : un dialogue à deux voix, lu par
la synthèse vocale du navigateur (assets/js/audio.js). Le script est
écrit à la main dans _tooling/podcast_<slug>.py ; ce module ne fait que
le mettre en forme, le vérifier et l'écrire au bon endroit.

Utilisation depuis un script de formation :

    import build_podcasts as bp
    bp.set_out("/chemin/vers/formations")
    bp.build("seo/module-1", {...})
    bp.report()

Schéma attendu :
    {
      "formation": "SEO Fondamentaux",
      "titre": "Introduction au SEO et les 3 piliers",
      "module_id": "formation-seo-module-1",
      "resume": "une phrase de présentation",
      "hosts": {"a": {"nom": "Camille", "role": "animatrice"},
                "b": {"nom": "Julien", "role": "consultant SEO"}},
      "lignes": [("a", "..."), ("b", "..."), ...],
    }
"""
import json
import os
import re

OUT = "/tmp/podcasts"
MOTS_PAR_MINUTE = 155          # débit moyen d'une voix de synthèse française
_stats = []


def set_out(path):
    global OUT
    OUT = path


def _mots(lignes):
    return sum(len(re.findall(r"\w+", t)) for _, t in lignes)


def _verifier(key, p):
    """Refuse ce qui produirait un podcast illisible ou inécoutable."""
    errs = []
    lignes = p.get("lignes") or []

    if len(lignes) < 12:
        errs.append(f"{len(lignes)} répliques seulement — un dialogue en demande au moins 12")

    voix = {v for v, _ in lignes}
    if not voix <= {"a", "b"}:
        errs.append(f"voix inconnue : {voix - {'a', 'b'}}")
    if len(voix) < 2:
        errs.append("une seule voix : ce n'est pas un dialogue")

    for i, (v, t) in enumerate(lignes, 1):
        if re.search(r"<[a-zA-Z/]", t):
            errs.append(f"réplique {i} : du HTML dans le texte parlé")
        if "&" in t and re.search(r"&[a-z]+;", t):
            errs.append(f"réplique {i} : entité HTML non résolue")
        if len(t) > 900:
            errs.append(f"réplique {i} : {len(t)} caractères, à découper en deux tours de parole")
        if not t.strip():
            errs.append(f"réplique {i} : vide")

    # Un monologue déguisé : plus de cinq répliques d'affilée de la même voix
    suite, precedente = 1, None
    for v, _ in lignes:
        suite = suite + 1 if v == precedente else 1
        if suite > 5:
            errs.append("plus de cinq répliques consécutives de la même voix")
            break
        precedente = v

    for champ in ("formation", "titre", "module_id", "hosts"):
        if not p.get(champ):
            errs.append(f"champ manquant : {champ}")

    if errs:
        raise ValueError(f"{key} :\n    - " + "\n    - ".join(errs))


def build(key, p):
    _verifier(key, p)
    slug, mod = key.split("/")
    lignes = p["lignes"]
    mots = _mots(lignes)
    minutes = max(1, round(mots / MOTS_PAR_MINUTE))

    data = {
        "module_id": p["module_id"],
        "formation": p["formation"],
        "titre": p["titre"],
        "version": p.get("version", "1.0"),
        "duree_estimee": f"{minutes} min",
        "mots": mots,
        "resume": p.get("resume", ""),
        "hosts": p["hosts"],
        "lignes": [{"v": v, "t": t.strip()} for v, t in lignes],
    }

    path = os.path.join(OUT, slug, mod)
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, "podcast.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)

    _stats.append((key, len(lignes), mots, minutes))
    return mots, minutes


def report():
    if not _stats:
        print("aucun podcast généré")
        return
    print(f"\n{'module':28} {'répliques':>10} {'mots':>7} {'durée':>7}")
    print("-" * 56)
    for key, n, mots, minutes in _stats:
        print(f"{key:28} {n:>10} {mots:>7} {minutes:>5} min")
    total_mots = sum(s[2] for s in _stats)
    total_min = sum(s[3] for s in _stats)
    print("-" * 56)
    print(f"{len(_stats)} podcasts · {total_mots} mots · {total_min} min d'écoute")
