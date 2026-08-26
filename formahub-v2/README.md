# Formahub — Plateforme Multi-Formations V2

Formahub est une plateforme de formation personnelle et d'auto-évaluation continue, 100% statique et hébergeable gratuitement sur Cloudflare Pages.

## Nouveautés de la Version 2 (V2)
- **Questionnaires complets sur 100% des 25 modules** : 4 questions ciblées par module avec choix multiples et feedbacks pédagogiques explicatifs détaillés.
- **Moteur de quiz dynamique (`quiz-engine.js`)** : calcul de score en direct, explications contextuelles immédiates et enregistrement de progression dans le `localStorage` (+ synchronisation KV Cloudflare optionnelle).
- **Catalogue de 25 ressources externes vérifiées** avec simulateur de reste à charge CPF 2026 selon la formule légale.
- **UI accessible et responsive** avec mode sombre dynamique et respect de `prefers-reduced-motion`.

## Déploiement sur Cloudflare Pages
```bash
# Test en local avec support Workers KV
npx wrangler pages dev . --kv=PROGRESS_KV

# Déploiement direct en production
npx wrangler pages deploy .
```
