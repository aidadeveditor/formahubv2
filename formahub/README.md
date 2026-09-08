# Formahub — Plateforme Multi-Formations V7

Plateforme d'auto-formation professionnelle 100 % statique (HTML5, CSS3, JS vanilla), sans étape de build, déployable sur **Cloudflare Pages** ou **GitHub Pages**.

## 🚀 Caractéristiques

- **10 formations, 40 modules** : SEO (5), Content Marketing (4), IA Générative (5), Gestion de projet (4), Management d'équipe (4), CRM Salesforce (3), Analytics et mesure de la performance (4), Excel et analyse de données (4), RSE et transition écologique (4), Bilan de compétences et repositionnement (3).
- **≈ 279 000 mots** de contenu rédigé, soit ~7 000 mots et 50 à 75 minutes par module — **37 h 45** de formation (somme des durées affichées).
- **Moteur de quiz JSON** (`quiz-engine.js`) : 240 questions (6 par module), correction instantanée et feedback explicatif.
- **Suivi de progression** en `localStorage`, avec sauvegarde chiffrée par **code secret** vers Cloudflare Workers KV (`functions/api/progress/[id].js`).
- **Écoute audio de chaque module** (`assets/js/audio.js`) : la synthèse vocale du navigateur lit le cours section par section, ouvre les volets au fur et à mesure et surligne le passage en cours.
- **Podcast par module** : un dialogue à deux voix d'environ 9 minutes, décrit dans `podcast.json` à côté du module.
- **Consultation hors ligne** : un service worker (`sw.js`) et un bouton « Rendre disponible hors ligne » téléchargent toute la plateforme dans le navigateur.
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
index.html                     catalogue + panneaux sauvegarde et hors ligne
ressources-externes.html
formations-espagne.html
sw.js                          service worker (cache hors ligne)
offline-manifest.json          liste des ressources à télécharger (généré)
assets/css/style.css           design tokens + thème clair/sombre
assets/js/progress.js          localStorage, thème, mise en page des modules
assets/js/quiz-engine.js       chargement et correction des quiz
assets/js/sync.js              code secret, chiffrement, sauvegarde auto
assets/js/offline.js           service worker, téléchargement, bandeau hors ligne
assets/js/audio.js             lecture vocale du module et lecteur de podcast
formations/<slug>/module-N/
    index.html                 le module
    quiz.json                  module_id, version, 6 questions
    podcast.json               dialogue à deux voix (facultatif)
functions/api/progress/[id].js Pages Function (binding PROGRESS_KV)
wrangler.jsonc
```

L'ordre des scripts compte : `audio.js` est chargé **après** `progress.js`, car il lit les
volets repliables que celui-ci construit au chargement.

Le `module_id` de chaque `quiz.json` doit correspondre à l'attribut `data-module-id`
du bouton « Marquer comme terminé » de la page — c'est cette clé qui relie le quiz
à la progression enregistrée.

## 🔊 Audio et podcasts

L'écoute repose sur la **Web Speech API** : aucun fichier son n'est hébergé, la voix est
celle du système. Sous Windows, une voix française s'ajoute dans *Paramètres → Heure et
langue → Voix* ; sur Android et iOS elles sont installées d'origine. Sans voix disponible,
le lecteur le dit au lieu de faire semblant de lire.

La **lecture du module** fonctionne sur les 40 modules sans travail supplémentaire : elle
lit la page. Le **podcast**, lui, est un contenu écrit — il n'apparaît que si le module
contient un `podcast.json`, sinon le lecteur affiche « à venir ».

```bash
# écrire les podcasts d'une formation
python3 _tooling/podcast_<slug>.py            # écrit les podcast.json
```

Le script d'une formation déclare ses dialogues dans un dictionnaire et appelle
`build_podcasts.build()`, qui vérifie la structure (au moins 12 répliques, deux voix,
pas de HTML dans le texte parlé) et calcule la durée. Compter 1 300 à 1 600 mots par
épisode, soit 9 à 10 minutes.

## 📥 Mode hors ligne

Après chaque ajout de module ou de podcast, régénérer la liste des ressources :

```bash
python3 _tooling/build_offline.py
```

Le service worker demande une origine sécurisée : il fonctionne sur le site déployé et sur
`localhost`, jamais sur un fichier ouvert directement depuis le disque.

## 🔒 Sauvegarde par code secret

Le code choisi ne quitte pas le navigateur. On en dérive l'adresse de stockage
(`SHA-256("formahub-id:" + code)`) et une clé AES-GCM (PBKDF2, 150 000 itérations) : le
KV ne reçoit qu'un bloc chiffré. Conséquence à assumer — **un code perdu est une
sauvegarde perdue**, personne ne peut la rouvrir. Saisir le même code sur un autre
appareil y restaure la progression ; si les deux côtés ont des données, la plateforme
propose de fusionner, de prendre la sauvegarde ou de garder l'appareil courant.

Sont synchronisés : progression des modules, cases cochées, sections lues, inscriptions
aux formations externes, dernier module consulté, préférences de lecture et thème.

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
- liens « module précédent / suivant » corrects ;
- les cinq scripts sont présents, `audio.js` après `progress.js` ;
- si un `podcast.json` existe : `module_id` aligné, au moins 12 répliques, deux voix,
  aucun HTML dans le texte parlé.
