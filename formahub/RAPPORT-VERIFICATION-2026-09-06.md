# Formahub — vérification de véracité

**Contrôle du 6 septembre 2026.** Deux volets : les formations externes listées (49 lignes françaises + 75 lignes espagnoles) et le contenu pédagogique des 40 modules internes.

Méthode : chargement effectif de chaque page contrôlée, et vérification des codes de certification directement sur France Compétences. Ce qui n'a pas pu être chargé est marqué « non vérifié » — jamais présumé correct.

---

## Verdict en une phrase

Le contenu des 40 modules est solide et vérifie bien mieux que prévu ; **le problème est dans les pages de ressources externes**, où cinq lignes contiennent une allégation d'éligibilité CPF fausse ou périmée, et où la colonne « accès libre » de la page Espagne est inexacte sur 30 lignes.

---

## Volet 1 — Formations externes françaises

### Grave : allégations CPF fausses ou périmées

Ces cinq lignes envoyaient vers un financement qui n'existe pas ou plus. C'est le cas le plus coûteux : on découvre l'erreur au moment de payer.

| Ligne | Ce qui était affiché | Ce que dit la vérification |
|---|---|---|
| **LiveMentor — SEO** | « RS6710 — éligible CPF » | RS6710 **expiré le 19/07/2026**, remplacé par RS7589. Et son intitulé réel est *« Entreprendre et développer sa clientèle grâce au marketing digital »* — ce n'est pas une certification SEO. L'organisme affiche toujours l'ancien code sur son site. |
| **Jedha — Prompt Engineer** | « RS7234 — certification *Generative AI* » | RS7234 est enregistré au nom de **LION**, pour *« Intégrer l'utilisation des outils numériques et de l'IA dans la gestion de projet »*. Aucun rapport avec Jedha ni avec le prompt engineering. |
| **26 Academy — gestion de projet agile** | « RS5487 / RNCP37091 » | RS5487 *« Gérer un projet en mobilisant les méthodes agiles »* (Simplon.co) est **inactif depuis le 08/07/2026**. RNCP37091 est actif, mais c'est *« Manager d'unité opérationnelle »*, un titre de **niveau 7** de Montpellier BS — pas une formation agile courte. |
| **Skillevos — parcours IA** | « Éligible CPF » | Le site de l'organisme dit lui-même être **« en cours d'agrément EDOF »**. À ce stade le financement passe par l'OPCO, pas par le CPF individuel. Prix réels affichés : 1 300 à 2 300 €, pas « Variable ». |
| **Perma France — IA générative** | « ≈ 1 490 €, éligible CPF » | **Aucune trace de cet organisme.** Recherche élargie infructueuse. Un organisme introuvable avec un tarif calé juste sous le plafond CPF, c'est le profil type de l'arnaque CPF. → **ligne supprimée.** |

### À corriger : chiffres et libellés

| Ligne | Affiché | Réel |
|---|---|---|
| Participation obligatoire | « entre 103,20 € et 150 € » | **150 €**, décret n° 2026-234 du 30 mars 2026, en vigueur depuis le 6 avril 2026 |
| E&H Academy | « Variable » | **4 000 € HT**, 56 h sur 8 jours — et aucune session ouverte au moment du contrôle |
| Wemodo | « 1 740 à 2 088 € » | **1 640 €**, 42 h sur 3 mois |
| Phoenix Performance | « Variable » | **1 650 € TTC** — soit 1 500 € de CPF + 150 € de participation, tarif construit pour tomber juste |
| Nova Formation | « 43 h — 2 850 € » | La page annonce **204 h** et **n'affiche aucun tarif** |
| Mantra | « ≈ 1 990 € » | Aucun tarif public sur le site. Renommage GrowthMakers → Mantra confirmé (2023) |
| DELE / Instituto Cervantes | « 500 à 3 000 € selon le niveau » | Confusion entre deux choses : **l'inscription à l'examen** coûte de l'ordre de 100 à 250 €. Les 500–3 000 € correspondent à une *formation de préparation* vendue par un tiers. Lien redirigé vers la page tarifs officielle |
| 26 Academy / Walter Learning | « Manager des équipes de proximité » | Intitulé exact du RS6626 : **« Manager des équipes et piloter l'efficacité collective »**, certificateur SCYFCO, actif jusqu'au 31/05/2027 |
| The Business Legion | — | Site **injoignable** au contrôle (erreur serveur). À revérifier |
| L'Air des Pichoulis | « Éligible CPF » | Qualiopi confirmé, mais éligibilité **auto-déclarée sans code RS/RNCP publié** |

### Ce qui est juste — et mérite d'être dit

- **Le calcul du reste à charge est correct.** Les plafonds 2026 retenus (1 500 € pour une certification RS hors CléA, 1 600 € pour un bilan de compétences, 900 € pour le permis B, RNCP non plafonné) sont exacts. La formule et l'avertissement sur les fourchettes de prix sont honnêtes.
- **La WAB** : 1 485 €, 42 h sur 8 semaines, RS7500 actif du 28/01/2026 au 28/01/2029, intitulé SEO + GEO. Exact de bout en bout — la meilleure ligne de la page.
- **École Polytechnique** : 14 400 € TTC, 68 h, RNCP41077BC05. Exact.
- **E&H Academy** : RS7389 *« Définir et déployer une stratégie de durabilité en entreprise »*, certificateur Des Enjeux et Des Hommes, enregistré le 27/11/2025. Exact.
- Les renommages signalés (Webmyday → Wemodo, GrowthMakers → Mantra) sont tous les deux confirmés.

---

## Volet 2 — Dispositifs espagnols

### Grave : la colonne structurante est fausse sur 30 lignes

La page classe chaque ligne par condition d'accès, et « libre » y signifie *« ouvert à tous, tout de suite, sans convocatoria ni statut »*. Les 30 lignes eFundae (25 cours durabilité + 5 itinéraires numériques) portent cette étiquette.

En réalité, `efundae.es/course/view.php?id=…` **renvoie vers un écran de connexion**, pas vers un cours. Il faut créer un compte plateforme Fundae, et le catalogue est orienté *trabajadores* et *autónomos*. Ce n'est pas un accès libre.

→ Nouvelle catégorie d'accès **« Compte requis »**, avec un filtre dédié et une note sur chaque ligne.

### Autres corrections

- **Femxa — convocatoria estatal.** Les deux cours contrôlés existent, sont gratuits, avec durées et publics conformes (150 h desempleados inclus ✓ ; 200 h trabajadores/autónomos ✓). Mais deux éléments décisifs manquaient : les places sont **réparties par communauté autonome** et la Comunitat Valenciana ne figurait pas dans la liste servie pour *Gestión integral de residuos* ; et *Sistemas de gestión ambiental* impose des visioconférences à horaires fixes (24 sept – 4 déc, 18h–21h) plus un **examen en présentiel à Madrid**. Note ajoutée sur les 7 lignes.
- **Campus virtuel LABORA** — la mention « millésime 2025 » était honnête mais noyée dans un tableau présenté comme actuel. Reformulée en avertissement explicite.
- **Plan LABORA 2026, 23 codes** — `puntlabora.gva.es` n'était pas joignable au contrôle. La mention « préinscription ouverte », relevée le 4 septembre, n'a **pas pu être revérifiée** : elle est désormais présentée comme telle plutôt qu'affirmée.
- **EOI Formación Abierta**, **Mi Competencia Digital**, **buscador Fundae** : liens actifs, descriptions conformes.

---

## Volet 3 — Contenu des 40 modules

C'est la bonne surprise. J'ai extrait le texte des 40 modules (1,7 million de caractères) et contrôlé les affirmations vérifiables : réglementation, normes, chiffres, noms de fonctions et d'outils.

**Le module RSE 1, le plus exposé, est exact sur tous les points contrôlés :**

| Affirmation du module | Vérification |
|---|---|
| Seuils CSRD post-Omnibus : 1 000 salariés / 450 M€ | ✓ |
| Omnibus I publiée au JOUE le 26/02/2026, en vigueur le 18/03/2026 | ✓ directive (UE) 2026/470 |
| Réduction d'environ 80 % du périmètre | ✓ |
| Transposition française au plus tard le 19/03/2027 | ✓ |
| ESRS révisés adoptés le 03/07/2026, −61 % de points de données | ✓ |
| 12 normes ESRS : 2 transversales, 5 environnementales, 4 sociales, 1 gouvernance | ✓ |
| Facultatif sur l'exercice 2026, obligatoire à partir de 2027 | ✓ |
| ISO 26000 est une ligne directrice non certifiable | ✓ |
| SBTi Corporate Net-Zero Standard v2.0, juin 2026 | ✓ |
| GHG Protocol : 15 catégories de scope 3 ; BEGES : 6 catégories, 23 postes | ✓ |

**Excel** — les 19 fonctions citées (RECHERCHEX, SOMME.SI.ENS, SIERREUR, SI.NON.DISP, SUPPRESPACE, SOMMEPROD, ESTNUM, NB.JOURS.OUVRES…) existent toutes et sont correctement orthographiées en français.

**IA générative, module 1** — le « Selon l'ADEME, 68 % » qu'un contrôle automatique signale n'est pas une erreur : c'est un exemple **délibérément faux**, étiqueté dans le module même comme « chiffre fabriqué + attribution erronée », dans l'exercice de détection d'hallucinations. Bien construit.

**Aucune statistique non sourcée** détectée dans l'ensemble des modules. Le contenu s'appuie sur du raisonnement et des cas construits plutôt que sur des chiffres d'étude invérifiables — c'est précisément ce qui le rend robuste au fact-checking.

**Non vérifié** : le détail pédagogique des formations gestion de projet, management, content marketing et bilan de compétences (peu d'affirmations factuelles externes à contrôler), et les 240 questions de quiz.

---

## Ce qui a été corrigé

Les corrections sont dans les **scripts générateurs**, pas seulement dans le HTML — le contenu reste régénérable.

- `_tooling/build_ressources.py` — 16 corrections : 1 ligne supprimée, 5 allégations CPF requalifiées en « Sous conditions » avec avertissement, 8 prix ou libellés rectifiés, participation obligatoire fixée à 150 €, et un nouveau bloc « vérifier le code de certification » expliquant comment contrôler un code sur France Compétences.
- `_tooling/build_formations_espagne.py` — 8 corrections : nouvelle catégorie d'accès « Compte requis » (badge, filtre, compteur) appliquée aux 30 lignes eFundae, avertissement territorial et logistique sur les 7 lignes Femxa, millésime 2025 signalé, statut d'inscription LABORA requalifié.

Bilan de la page française : 49 → **48 ressources**, 30 → **23 réellement éligibles CPF**. Les 7 lignes retirées du décompte CPF ne disparaissent pas : elles passent en « Sous conditions » avec la raison écrite.

## Ce qu'il reste à faire

1. **Rouvrir `puntlabora.gva.es`** depuis Valence et confirmer, code par code, lesquels des 23 cours du plan 2026 sont encore en préinscription. C'est le plus gros bloc non vérifié.
2. **Vérifier l'édition 2026 du campus virtuel LABORA** — si seule l'édition 2025 existe encore, les 10 lignes concernées sont à retirer.
3. **Recontrôler The Business Legion** quand le site répondra.
4. **Confirmer la couverture territoriale** des 5 cours Femxa non contrôlés individuellement.
5. Prochaine revalidation trimestrielle : **décembre 2026**.
