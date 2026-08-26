# Formahub — Plateforme Multi-Formations V4

Plateforme d'auto-formation professionnelle 100% statique (HTML5, CSS3, JS vanilla), optimisée pour **GitHub Pages** et **Cloudflare Pages**.

## 🚀 Caractéristiques
- **6 Formations complètes** : SEO, Content Marketing, IA Générative, Gestion de projet, Management d'équipe, CRM Salesforce.
- **25 Modules rédigés** avec objectifs ADDIE, cours théoriques, exercices pratiques et quiz interactifs.
- **Moteur de Quiz JSON** (`quiz-engine.js`) avec correction instantanée et feedback explicatif.
- **Suivi de progression** en `localStorage` + synchronisation optionnelle Cloudflare Workers KV (`functions/api/progress/[id].js`).
- **Onglet Ressources Externes** avec tableau filtrable, calcul du reste à charge et solde CPF (1 353,80 €).
- **Mode Sombre / Clair** accessible (WCAG AA).

## 🛠️ Déploiement Cloudflare Pages
```bash
# Déploiement direct sans étape de build
npx wrangler pages deploy .
```