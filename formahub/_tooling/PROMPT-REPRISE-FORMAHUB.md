# Formahub — prompt de reprise

Colle ce message tel quel au début d'une nouvelle conversation (ou attache ce fichier).

---

## Contexte

Je travaille sur **Formahub**, une plateforme d'auto-formation professionnelle que je
développe sur mon poste Windows, dans :

```
C:\Users\aidaz\Documents\Claude - Formahub\formahubv2\formahub
```

Elle est aujourd'hui **complète et validée** : 6 formations, 25 modules, ~140 000 mots,
150 questions de quiz, ~21 heures de contenu. Je veux **ajouter une nouvelle formation**
au même standard.

### Ce qui existe

| Formation | Slug | Modules |
|---|---|---|
| SEO Fondamentaux | `seo` | 5 |
| Content Marketing & Stratégie Éditoriale | `content-marketing` | 4 |
| IA Générative appliquée au contenu | `ia-generative` | 5 |
| Gestion de Projet, les fondamentaux | `gestion-de-projet` | 4 |
| Management d'équipe, les bases | `management-equipe` | 4 |
| CRM et relation client (Salesforce) | `crm-relation-client` | 3 |

Site 100 % statique — HTML5, CSS3, JS vanilla, aucune étape de build.
Déploiement : `npx wrangler pages deploy .` (Cloudflare Pages).
Le binding KV `PROGRESS_KV` est configuré et fonctionnel dans `wrangler.jsonc`.
**Je gère moi-même Git et GitHub** — ne t'en occupe pas.

### Arborescence

```
index.html                      catalogue (durées et volume affichés par parcours)
ressources-externes.html        49 formations externes, filtres thématique + financement
assets/css/style.css            design tokens, thème clair/sombre, tous les blocs V5
assets/js/progress.js           localStorage, thème, sync cloud
assets/js/quiz-engine.js        chargement et correction des quiz
formations/<slug>/module-N/index.html
formations/<slug>/module-N/quiz.json
functions/api/progress/[id].js  Pages Function
_tooling/                       les scripts de génération (voir ci-dessous)
```

---

## Ce que je veux que tu fasses

**Développer une nouvelle formation complète**, au format exact des 25 modules existants.

Ma liste de candidates, par ordre de priorité discuté :

1. **Analytics & mesure de la performance** (4 modules) — le chaînon manquant : le SEO,
   le contenu et le CRM produisent de la donnée, rien n'apprend à la lire.
2. **Excel & analyse de données appliquée** (4 modules) — la compétence la plus
   transférable, sans obsolescence.
3. **Email & marketing automation** (3-4 modules) — complète contenu → CRM → cycle de vie.

Autres candidates : acquisition payante / SEA (3), négociation & vente consultative (3-4),
communication écrite professionnelle (3), RSE & transition écologique (4),
bilan de compétences & repositionnement (3).

**Commence par me demander laquelle**, puis propose-moi le plan des modules
(titre + les 5 sections de chacun) avant d'écrire le contenu.

---

## Le standard de contenu — le point le plus important

Il doit s'agir d'une **vraie formation complète, pas d'une présentation commentée**.
L'apprenant doit sortir du module **capable de faire**, pas seulement d'avoir compris.
C'est l'exigence sur laquelle j'ai fait refaire une première version trop courte.

Concrètement, par module : **~2 800 à 3 400 mots de cours** (5 000 à 6 500 mots pour la
page entière, blocs pédagogiques compris), **50 à 55 minutes**, et cette structure fixe :

| Bloc | Contenu attendu |
|---|---|
| Mise en situation | Un problème concret et daté, que l'étude de cas résoudra plus loin |
| Objectifs | 6 verbes d'action — ce qu'on saura **faire** |
| 4 à 5 sections | Prose dense, avec encadrés « Méthode » (étapes numérotées), « Exemple » et « Erreur fréquente » |
| Étude de cas | Le cas d'ouverture traité pas à pas, chiffré, avec les arbitrages explicités et une leçon transposable |
| Checklist | 14 à 20 items opérationnels |
| Glossaire | 9 à 13 termes |
| À retenir | 13 à 17 points |
| 3 exercices | Débutant → Intermédiaire → Avancé, chacun avec un corrigé commenté long et argumenté |
| Quiz | 6 questions, 3 choix, feedback explicatif sur chacune |
| Ressources | 4 prolongements, dont un renvoi aux autres modules de la formation |

### Règles de rédaction

- **Chaque module s'ouvre sur une mise en situation que l'étude de cas résout.** Ce fil
  narratif est ce qui distingue une formation d'un plan de cours.
- **Les modules se citent entre eux** explicitement (« vu au module 2 », « n'y allez pas
  avant d'avoir… »).
- **Les corrigés d'exercice sont la partie la plus dense** : ils expliquent le raisonnement,
  écartent les fausses pistes, et disent ce qu'il ne faut *pas* faire. Un corrigé qui donne
  seulement la bonne réponse est raté.
- **Les encadrés « Erreur fréquente » nomment un piège réel**, pas une maladresse théorique.
- Ton professionnel, en français, phrases pleines. Pas de listes à puces dans la prose de cours.
- Sur les sujets sensibles (surcharge, conflits, santé au travail), **borner le rôle du
  manager** : décrire sans diagnostiquer, agir sur la charge et les priorités, orienter vers
  la médecine du travail / RH. Ne jamais proposer de médiation sur du harcèlement ou de la
  discrimination.

---

## L'outillage — utilise-le, ne le réinvente pas

Tout est dans `_tooling/` sur mon disque. **Commence par le récupérer** (stage les fichiers
dans ton conteneur) :

| Fichier | Rôle |
|---|---|
| `fh_builder.py` | Le générateur. Expose `build(clé, dict) -> (mots_cours, mots_page)` et rend le gabarit HTML V5 complet |
| `exemple_module.py` | Un module réel et complet (CRM module 3) — **le modèle à imiter** pour la structure du dict et le niveau de rédaction |
| `validate.py` | Le harnais de validation à passer après chaque formation |
| `build_ressources.py` | Le générateur de `ressources-externes.html` (utile seulement si je te demande de la mettre à jour) |

### Schéma du dictionnaire de module

```python
M["<slug>/module-N"] = {
  "formation": "...", "titre": "...", "num": N, "total": T,
  "duree": "50 min", "niveau": "Débutant|Intermédiaire",
  "module_id": "formation-<slug>-module-N",
  "situation": [...],          # 2-3 paragraphes
  "objectifs": [...],          # 6 items
  "sections": [{"titre":..., "paras":[...], "blocks":[...]}],
  "etude_cas": {"titre":..., "html":...},
  "checklist": {"titre":..., "items":[...]},
  "glossaire": [(terme, définition), ...],
  "retenir": [...],
  "exercices": [{"titre":..., "niveau":..., "enonce":[...], "corrige":"..."}],
  "ressources": [...],
}
```

Types de `blocks` disponibles : `h3` (sous-section), `html` (brut, pour un tableau),
`exemple`, `method` (avec `steps`), `pitfall`.

### Schéma du `quiz.json`

```json
{
  "module_id": "formation-<slug>-module-N",
  "version": "2.0",
  "last_verified": "AAAA-MM-JJ",
  "questions": [
    {"id": "q1", "question": "...",
     "choices": [{"key":"a","text":"..."}, {"key":"b","text":"..."}, {"key":"c","text":"..."}],
     "correct_answer": "b",
     "feedback": "..."}
  ]
}
```

### Validation — obligatoire avant livraison

```bash
FH_OUT=<dossier de sortie> FH_CSS=<chemin style.css> python3 validate.py <slug> <nb-modules>
```

Elle vérifie : équilibre des balises, caractères parasites, présence des 8 blocs
pédagogiques, couverture CSS, `module_id` du quiz aligné sur le `data-module-id` du HTML,
clé de réponse valide, absence de HTML brut dans les choix, liens précédent/suivant.
**Ne me livre rien tant qu'elle n'affiche pas VALIDÉ.**

---

## Les pièges déjà rencontrés — ne les refais pas

1. **HTML brut dans un choix de quiz.** `quiz-engine.js` injecte via `innerHTML` : une
   balise non échappée s'affiche **vide**, et la réponse devient invisible à l'écran.
   Écris `&lt;meta name=&quot;robots&quot;&gt;`, jamais `<meta name="robots">`.
2. **Guillemets doubles imbriqués** dans les chaînes Python — cause de `SyntaxError` à
   répétition. Utilise les guillemets typographiques « " " » à l'intérieur.
3. **Caractères parasites.** Un caractère non latin glissé dans le texte passe inaperçu
   à la relecture ; la validation le détecte, prends-la au sérieux.
4. **Nouvelle classe CSS.** Si tu en introduis une, ajoute-la à `style.css` **en
   n'utilisant que les variables existantes** (`var(--text-muted)`, etc.) pour que le mode
   sombre fonctionne sans travail supplémentaire. Ne modifie aucune règle existante.
5. **Ne pas oublier le catalogue.** `index.html` affiche le nombre de modules, la durée
   par parcours et le volume total : mets-le à jour, avec une carte pour la nouvelle
   formation. Le README aussi.

---

## Livraison

Pour chaque fichier produit : `SendUserFile`, puis écriture sur mon disque au chemin absolu
`C:\Users\aidaz\Documents\Claude - Formahub\formahubv2\formahub\formations\<slug>\module-N\`.
Les modules ne sont utilisables qu'une fois écrits là — un fichier seulement envoyé dans la
conversation n'atteint pas le projet.

Travaille **formation par formation, module par module**, et livre au fur et à mesure
plutôt qu'en une fois à la fin.
