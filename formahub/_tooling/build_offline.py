#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Formahub — génère offline-manifest.json.

Le service worker lit ce fichier quand l'utilisatrice clique sur
« Rendre disponible hors ligne » : il contient la liste exhaustive
des adresses à enregistrer dans le cache du navigateur.

Usage :
    python3 _tooling/build_offline.py [racine_du_site]

Sans argument, la racine est le dossier parent de _tooling.
À relancer après chaque ajout de formation, de module ou de podcast.
"""
import json
import os
import sys
from datetime import date

# Dossiers qui n'ont rien à faire dans le cache d'un navigateur
SKIP_DIRS = {"_tooling", ".git", ".github", "functions", "node_modules", "__pycache__"}
KEEP_EXT = {".html", ".json", ".css", ".js", ".svg", ".png", ".webp", ".ico", ".webmanifest"}
# Fichiers de service, jamais utiles hors ligne
SKIP_FILES = {"sw.js", "offline-manifest.json", "wrangler.jsonc"}


def collect(root):
    urls = ["./"]
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS and not d.startswith("."))
        for name in sorted(filenames):
            if name in SKIP_FILES or name.startswith("."):
                continue
            ext = os.path.splitext(name)[1].lower()
            if ext not in KEEP_EXT:
                continue
            rel = os.path.relpath(os.path.join(dirpath, name), root)
            urls.append(rel.replace(os.sep, "/"))
    return urls


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    urls = collect(root)

    total_bytes = 0
    for u in urls:
        if u == "./":
            continue
        p = os.path.join(root, u)
        if os.path.exists(p):
            total_bytes += os.path.getsize(p)

    manifest = {
        "version": date.today().isoformat(),
        "count": len(urls),
        "approx_bytes": total_bytes,
        "urls": urls,
    }
    out = os.path.join(root, "offline-manifest.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=1)

    modules = sum(1 for u in urls if u.endswith("/index.html") and u.startswith("formations/"))
    podcasts = sum(1 for u in urls if u.endswith("/podcast.json"))
    print(f"offline-manifest.json : {len(urls)} adresses, "
          f"{total_bytes / 1024 / 1024:.2f} Mo, "
          f"{modules} modules, {podcasts} podcasts")


if __name__ == "__main__":
    main()
