# Formahub — Plateforme Multi-Formations V8

Plateforme d'auto-formation professionnelle 100 % statique (HTML5, CSS3, JS vanilla), sans étape de build, déployable sur **Cloudflare Pages** ou **GitHub Pages**.

## 🚀 Caractéristiques

- **10 formations, 40 modules** : SEO (5), Content Marketing (4), IA Générative (5), Gestion de projet (4), Management d'équipe (4), CRM Salesforce (3), Analytics et mesure de la performance (4), Excel et analyse de données (4), RSE et transition écologique (4), Bilan de compétences et repositionnement (3).
- **≈ 279 000 mots** de contenu rédigé, soit ~7 000 mots et 50 à 75 minutes par module — **37 h 45** de formation (somme des durées affichées).
- **Moteur de quiz JSON** (`quiz-engine.js`) : 240 questions (6 par module), correction instantanée et feedback explicatif.
- **Suivi de progression** en `localStorage`, avec sauvegarde chiffrée par **code secret** vers Cloudflare Workers KV, via le Worker `formahub-sync`.
- **Écoute audio de chaque module** (`assets/js/audio.js`) : voix neuronales **Microsoft Azure Speech** (via le Worker `formahub-sync`, code dans `../workers/formahub-sync.js`), avec repli automatique sur la voix du navigateur ; choix de la voix, du ton et de la vitesse (0,75× à 2×). Le cours est lu section par section, les volets s'ouvrent au fur et à mesure et le passage en cours est surligné.
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
    podcast-audio.mp3          export audio réel du podcast, ex. NotebookLM (facultatif)
functions/api/progress/[id].js sauvegarde en local (wrangler pages dev) — en ligne, c'est le Worker formahub-sync
functions/api/tts.js           synthèse Azure en local (wrangler pages dev) — en ligne, c'est le Worker formahub-sync
../workers/formahub-sync.js    Worker Cloudflare : clé Azure + sauvegarde chiffrée (KV) (hors de formahub/, jamais déployé comme fichier)
wrangler.jsonc
```

L'ordre des scripts compte : `audio.js` est chargé **après** `progress.js`, car il lit les
volets repliables que celui-ci construit au chargement.

Le `module_id` de chaque `quiz.json` doit correspondre à l'attribut `data-module-id`
du bouton « Marquer comme terminé » de la page — c'est cette clé qui relie le quiz
à la progression enregistrée.

## 🔊 Audio et podcasts

### Voix Microsoft Azure Speech (par défaut)

Le lecteur utilise les **voix neuronales Azure** via le Worker Cloudflare
**`formahub-sync`**. La clé Azure n'est **jamais** dans le code, ni dans le dépôt
GitHub (public), ni dans le navigateur : elle vit en *Secret* dans ce Worker, qui
l'ajoute à chaque appel et relaie vers Azure (région `francecentral` par défaut).

Le code du Worker est dans `formahubv2/workers/formahub-sync.js`, en dehors de
`formahub/` pour ne jamais être servi comme fichier du site. Installation :

1. dash.cloudflare.com → Workers & Pages → Create → Worker, nom **`formahub-sync`** → Deploy
2. Edit code → coller `workers/formahub-sync.js` → Deploy
3. Settings → Bindings → Add → KV namespace : nom **`PROGRESS_KV`**, namespace de Formahub
   (id `6513daa6…`, le même que dans `wrangler.jsonc`) — pour la sauvegarde par code secret
4. Settings → Variables and Secrets → Add : `AZURE_KEY`, type **Secret**, valeur = la clé
   (facultatif : `AZURE_REGION`, `ALLOWED_ORIGINS` pour un domaine perso)

Vérification : l'adresse racine du Worker doit répondre `"azure":true` et `"kv":true`.

`audio.js` trouve le Worker tout seul tant que le site est sur `*.workers.dev`
(`formahubv2.<compte>.workers.dev` → `formahub-sync.<compte>.workers.dev`). Sur un domaine
perso, renseigner la constante `TTS_WORKER` en haut de `audio.js` et `SYNC_WORKER` en haut de `sync.js`. Le Worker n'accepte que
les appels venant des pages du même compte `workers.dev`, de `localhost` et de `ALLOWED_ORIGINS`.

Ne jamais créer de fichier `.dev.vars` ou `.env` dans `formahub/` : ce dossier est
déployé tel quel. En local, `functions/api/tts.js` sert de relais :
`npx wrangler pages dev . --binding AZURE_SPEECH_KEY=… --binding AZURE_SPEECH_REGION=francecentral`.

À chaque mise en ligne, changer `VERSION` en haut de `sw.js` pour que les navigateurs
rechargent la coquille (dont `audio.js`) — les modules téléchargés hors ligne sont conservés.

Réglages proposés dans chaque barre d'écoute (mémorisés et synchronisés par code secret) :

| Réglage | Contenu |
|---|---|
| **Voix** | voix Azure françaises (fr-FR, fr-CA, fr-BE, fr-CH) et multilingues, lues en direct depuis Azure ; puis les voix du navigateur, utilisables hors ligne |
| **Ton** | 6 tons prédéfinis (neutre, posé, chaleureux, dynamique, plus grave, plus aigu) + les *styles* propres à la voix Azure choisie (enjoué, triste, calme…) |
| **Vitesse** | 0,75× à **2×**, appliquée en direct par le lecteur (la voix garde sa hauteur) |

Le podcast propose une voix par intervenant (par défaut Denise et Henri) et un ton commun.

**Coûts et quotas** — chaque extrait synthétisé est conservé dans le navigateur (cache `fhtts-v1`, 500 extraits max) : une
réécoute ne reconsomme rien. Changer de voix ou de ton crée de nouveaux extraits ; changer
la vitesse, non. Les paragraphes courts sont regroupés (~700 caractères par requête) pour
rester sous la limite de requêtes par minute du palier gratuit ; en cas de refus
momentané (429), le lecteur patiente et réessaie. Le Worker refuse les appels venant
d'un autre site que Formahub. Garder la ressource Azure en palier gratuit (F0) : au-delà du
quota mensuel, Azure refuse au lieu de facturer.

**Repli** — si Azure ne répond pas (hors ligne, clé invalide, quota épuisé), la lecture
bascule d'elle-même sur la voix du navigateur au même endroit, et l'indique.

### Voix du navigateur (secours)

La **Web Speech API** reste disponible sans réseau : c'est la voix du système. Sous
Windows, une voix française s'ajoute dans *Paramètres → Heure et langue → Voix* ; sur
Android et iOS elles sont installées d'origine.

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

### Podcast en audio réel (NotebookLM ou autre)

La voix de synthèse du navigateur reste le mode par défaut, mais un vrai fichier
audio posé à côté de `podcast.json` prend automatiquement le relais : `audio.js`
cherche `podcast-audio.mp3`, puis `.m4a`, puis `.wav` dans le dossier du module, et
affiche un lecteur natif avec la transcription en dessous dès que l'un des trois existe.
Rien à activer : c'est juste la présence du fichier qui change le rendu.

Pour produire ce fichier avec Google NotebookLM :

```bash
# 1. Exporter une formation (ou un seul module) en PDF, prêt à déposer dans NotebookLM
python3 _tooling/build_pdf_notebooklm.py seo               # tous les modules de la formation
python3 _tooling/build_pdf_notebooklm.py seo/module-3       # un seul module
```

Les PDF sont écrits dans `../notebooklm-exports/<slug>/` — donc **en dehors de**
`formahub/`, pour ne jamais être déployés sur Cloudflare Pages. Chaque PDF reprend le
cours complet du module (mise en situation, sections, exemples, étude de cas,
checklist, glossaire, à retenir, exercices avec corrigés développés) ainsi que les
6 questions du quiz et leurs réponses commentées — de quoi laisser NotebookLM générer
un « Audio Overview » fidèle au contenu réel.

2. Déposer le PDF comme source dans un notebook NotebookLM, générer l'audio, le
   télécharger, puis le placer dans `formations/<slug>/module-N/podcast-audio.mp3`
   (renommer si NotebookLM propose un autre format — `.m4a` et `.wav` sont acceptés
   tels quels).

Le fichier audio n'est pas ajouté au mode hors ligne en un clic (`build_offline.py`)
ni au manifeste de cache : ce sont des fichiers potentiellement lourds à multiplier
par 40 modules, à inclure à la main si besoin plus tard.

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

Le site est servi en fichiers statiques : le dossier `functions/` ne s'exécute pas en
ligne. La sauvegarde et la voix Azure passent donc par le Worker `formahub-sync`
(binding KV `PROGRESS_KV` + secret `AZURE_KEY`, voir *Audio*). Sans ce binding, la
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
