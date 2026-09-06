# Formahub — Plateforme Multi-Formations V5

Plateforme d'auto-formation professionnelle 100 % statique (HTML5, CSS3, JS vanilla), sans étape de build, déployable sur **Cloudflare Pages** ou **GitHub Pages**.

## 🚀 Caractéristiques

- **10 formations, 40 modules** : SEO (5), Content Marketing (4), IA Générative (5), Gestion de projet (4), Management d'équipe (4), CRM Salesforce (3), Analytics et mesure de la performance (4), Excel et analyse de données (4), RSE et transition écologique (4), Bilan de compétences et repositionnement (3).
- **≈ 279 000 mots** de contenu rédigé, soit ~7 000 mots et 50 à 75 minutes par module — **37 h 45** de formation (somme des durées affichées).
- **Moteur de quiz JSON** (`quiz-engine.js`) : 240 questions (6 par module), correction instantanée et feedback explicatif.
- **Suivi de progression** en `localStorage`, avec synchronisation optionnelle vers Cloudflare Workers KV (`functions/api/progress/[id].js`).
- **Onglet Ressources externes** : tableau filtrable, calcul du reste à charge et solde CPF.
- **Onglet Formations Espagne** : dispositifs espagnols, présentés par condition d'accès.
- **Mode sombre / clair** accessible (WCAG AA), piloté par `data-theme` et les variables CSS de `:root`.

## 📐 Structure d'un module

Chaque module suit le même gabarit pédagogique :

| Bloc | Rôle |
|---|---|
| Mise en situation | Un problème concret, résolu plus loin par l'étude de cas |
| Objectifs | Ce que l'apprenant saura **faire** à l'issue du module |
| Sections de cours | Explications, encadrés « Méthode », « Exemple » et « Erreur fréquente » |
| Étude de cas | Le cas d'ouverture traité pas à pas, avec les arbitrages explicités |
| Checklist opérationnelle | À reprendre dans le travail réel |
| Glossaire | 9 à 13 termes définis |
| À retenir | 13 à 17 points clés |
| Exercices | 3 exercices gradués (Débutant → Avancé) avec corrigé commenté dépliable |
| Quiz | 6 questions avec feedback |
| Ressources | Prolongements sélectionnés |

## 🗂️ Arborescence

```
index.html                     catalogue des formations
ressources-externes.html
assets/css/style.css           design tokens + thème clair/sombre
assets/js/progress.js          localStorage, thème, sync cloud
assets/js/quiz-engine.js       chargement et correction des quiz
formations/<slug>/module-N/
    index.html                 le module
    quiz.json                  module_id, version, 6 questions
functions/api/progress/[id].js Pages Function (binding PROGRESS_KV)
wrangler.jsonc
```

Le `module_id` de chaque `quiz.json` doit correspondre à l'attribut `data-module-id`
du bouton « Marquer comme terminé » de la page — c'est cette clé qui relie le quiz
à la progression enregistrée.

## 🛠️ Déploiement Cloudflare Pages

```bash
# Déploiement direct, sans étape de build
npx wrangler pages deploy .
```

Le binding KV `PROGRESS_KV` est configuré dans `wrangler.jsonc`. Sans lui, la
progression reste purement locale au navigateur — la plateforme fonctionne
normalement, mais la progression ne suit pas d'un appareil à l'autre.

## ✅ Contrôle qualité

Avant toute mise en ligne, vérifier pour chaque module :

- équilibre des balises HTML et absence de caractères parasites ;
- présence des huit blocs pédagogiques ;
- toutes les classes CSS employées existent dans `style.css` ;
- `module_id` du quiz identique au `data-module-id` de la page ;
- clé de réponse (`correct_answer`) présente dans les choix ;
- aucun HTML brut dans le texte des choix — `quiz-engine.js` injecte via
  `innerHTML`, donc une balise non échappée s'affiche vide (utiliser `&lt;`, `&gt;`) ;
- liens « module précédent / suivant » corrects.
