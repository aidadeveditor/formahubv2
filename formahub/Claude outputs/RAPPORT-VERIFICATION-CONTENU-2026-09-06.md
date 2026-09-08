# Formahub — audit du contenu des 10 formations

**6 septembre 2026.** Complément au rapport sur les ressources externes : cette fois, l'audit porte sur le contenu que tu as écrit — les 40 modules et les 240 questions de quiz.

Méthode : extraction du texte des 40 modules (1,7 million de caractères), relecture intégrale module par module, et vérification par recherche web de chaque affirmation portant sur le monde extérieur — réglementation, référentiels normés, comportement réel des outils, syntaxe des formules. Les entreprises et chiffres fictifs des mises en situation ont été exclus du périmètre : ce sont des supports pédagogiques, pas des allégations.

---

## Verdict

**Le contenu tient.** Sur 40 modules et 240 questions, l'audit a produit **9 corrections**, dont aucune ne remet en cause la pédagogie d'un module. Deux formations ressortent sans une seule erreur, et le module le plus exposé juridiquement — Bilan de compétences — est le plus solide de tous.

| Formation | Verdict | Corrections |
|---|---|---|
| Content Marketing | Fiable | 0 |
| Management d'équipe | Fiable | 0 |
| IA Générative | Fiable | 0 |
| Bilan de compétences | Fiable | 1 (date à un jour près) |
| Excel & analyse de données | Fiable | 1 (erreur de calcul) |
| RSE & transition écologique | Fiable | 1 (montant d'amende) |
| CRM Salesforce | Fiable avec réserve | 2 |
| Gestion de projet | Fiable avec réserve | 2 (Scrum) |
| SEO | Fiable avec réserve | 3 (obsolescence Google) |
| Analytics & mesure | Fiable avec réserve | 3 (GA4 vs Universal Analytics) |

---

## Les 9 corrections appliquées

### Erreurs de fait

**Excel, module 2 — un calcul faux.** « Le 4 septembre 2026 vaut 46 265 » : le numéro de série Excel de cette date est **46 269**. Quatre jours d'écart, vérifié par calcul direct et recoupé sur des repères connus (01/01/2000 = 36 526, 01/01/2020 = 43 831). La leçon reste juste, seul le nombre était faux.

**RSE, module 4 — un montant d'amende surestimé du triple.** « Sanction jusqu'à 300 000 euros » pour une allégation de neutralité carbone non conforme. Le vrai montant, article L. 229-69 du code de l'environnement, est de **100 000 € pour une personne morale** (20 000 € pour une personne physique), pouvant être porté au total des dépenses de l'opération. Les 300 000 € correspondent à un autre fondement juridique — la pratique commerciale trompeuse, en droit de la consommation. La confusion est fréquente ; sur un module RSE elle est gênante.

**Bilan de compétences, module 1 — une date à un jour près.** La participation de 150 € s'applique aux demandes déposées **à compter du 2 avril 2026**, pas du 1er (décret n° 2026-234 du 30 mars 2026, publié le 1er avril). J'ai profité de la correction pour ajouter le montant antérieur (103,20 € depuis le 1er janvier 2026) et l'exonération des demandeurs d'emploi.

### Obsolescences — le contenu était vrai, il ne l'est plus

**Analytics, module 2 — trois descriptions d'Universal Analytics présentées comme actuelles.** C'est le lot le plus important, parce que le module reste volontairement agnostique en outil et décrit donc ces mécanismes comme des généralités :

- *« Selon les outils, elle peut aussi se clore à minuit ou lors d'un changement de source »* — c'étaient les règles d'Universal Analytics, produit arrêté en 2023-2024. Les outils actuels ne découpent les sessions que par inactivité.
- *« Les modèles linéaire et à dépréciation temporelle… »* — Google Analytics a **retiré ces modèles en 2023**. Il n'en reste que deux : dernier clic et piloté par les données, ce dernier étant désormais le défaut (le module disait le contraire).
- *« L'arrivée d'un paramètre de campagne ouvre une nouvelle session et réattribue la source »* — la réattribution est réelle et la règle « jamais d'UTM sur un lien interne » reste juste, mais l'ouverture d'une nouvelle session ne se produit plus, et le compteur de sessions n'est donc pas gonflé. La justification était fausse même si le conseil était bon.

**SEO — trois points périmés :**

- *Module 3, `FAQPage`* — Google a **retiré l'affichage enrichi FAQ** des résultats de recherche. Le balisage reste correct et sans risque, mais il ne produit plus l'accordéon de questions promis. C'était la correction la plus utile : un apprenant aurait perdu du temps à baliser pour rien.
- *Module 1, rendu JavaScript « différé de plusieurs jours »* — Google annonce un **délai médian de l'ordre de cinq secondes**, la grande majorité des pages étant rendues en quelques minutes. Le module en faisait un point clé « que la plupart des supports passent sous silence », ce qui amplifiait l'erreur.
- *Module 4, « 410 : sortie de l'index plus rapide qu'un 404 »* — croyance SEO répandue, contredite par Google : l'écart de traitement est minime en pratique.

**CRM Salesforce, module 1 — une manipulation qui ne marche pas.** « Une règle de validation bloque la création d'un Compte dont le nom existe déjà » : une règle de validation n'évalue que l'enregistrement en cours de sauvegarde, elle **ne peut pas interroger les autres enregistrements**. La fonctionnalité prévue pour ça est la gestion native des doublons (règle de correspondance + règle de doublon). Un apprenant qui tentait de reproduire l'exercice se serait heurté à un mur. Le nom du parcours Trailhead « Salesforce Platform Basics » a aussi été mis à jour — il s'appelle désormais « Agentforce 360 Platform Basics ».

### Contresens sur un référentiel

**Gestion de projet, module 2 — deux erreurs sur Scrum**, gênantes parce que le module recommande lui-même le Scrum Guide en lecture complémentaire : un apprenant qui va vérifier découvre la contradiction.

- *« Le Sprint Backlog… ne change pas en cours de sprint »* — le Scrum Guide dit exactement l'inverse : c'est un plan vivant, mis à jour tout au long du sprint. Ce qui ne se renégocie pas, c'est l'**Objectif de Sprint**. Le module protégeait le mauvais artefact.
- *Les cinq événements* — la liste donnée était Planning, Daily, Revue, Rétrospective et « affinage du backlog ». Le cinquième événement est en réalité **le Sprint lui-même**, l'événement conteneur ; l'affinage est une activité continue, hors liste — ce que le module disait d'ailleurs deux lignes plus loin, se contredisant lui-même.

---

## Les quiz : 238 sur 240

Les 40 fichiers sont techniquement irréprochables : JSON valide, schéma homogène, 6 questions et 3 choix partout, aucun index de réponse hors bornes, aucun doublon d'option, aucun champ vide.

Sur le fond, **deux questions seulement** posaient problème — et dans les deux cas parce qu'elles retranscrivaient fidèlement une erreur du cours, pas par défaut de conception :

- `analytics-mesure/module-2`, q3 : la bonne réponse restait la bonne, mais sa formulation enseignait le mécanisme GA4 périmé. Reformulée.
- `gestion-de-projet/module-2`, q6 : « le contenu du sprint change en cours de sprint » était donné comme marqueur de Scrum de façade — c'est en réalité le comportement normal. Recentrée sur l'Objectif de Sprint.

Aucune autre question n'avait de réponse marquée fausse, d'explication contradictoire, ou d'option meilleure que celle retenue.

---

## Ce qui a été vérifié et trouvé juste

C'est la partie longue, et elle compte autant que la liste des erreurs.

**Bilan de compétences** — le module le plus dense juridiquement, et sans faute : durée légale de 24 h incluant le travail personnel, trois phases réglementaires, confidentialité et propriété du document au bénéficiaire, plafond CPF 2026 de 1 600 €, durée minimale de 13 h dont deux tiers en interaction directe, carence de 5 ans, neutralisation en cas d'abondement. La réforme VAE (loi du 21 décembre 2022, France VAE, suppression du délai minimal d'expérience, délais de 2 et 3 mois) est exacte. Et le congé de bilan de compétences, supprimé en 2019, n'est mentionné nulle part — l'erreur classique évitée.

**RSE** — remarquablement à jour sur des textes très récents : directive EmpCo (UE 2024/825) applicable au 27 septembre 2026 sans seuil de taille ; retrait annoncé de la directive Green Claims en juin 2025, non formalisé ; SBTi Corporate Net-Zero Standard v2.0 publié le 11 juin 2026 — exact au jour près. S'ajoutent les points déjà validés au premier rapport : seuils Omnibus, ESRS révisés, transposition au 19 mars 2027, 15 catégories de scope 3, BEGES à 6 catégories et 23 postes.

**Excel** — la syntaxe et l'ordre des arguments de **toutes** les formules du cours et des corrigés ont été vérifiés un par un : RECHERCHEV, RECHERCHEX, INDEX/EQUIV, SOMME.SI.ENS, NB.SI.ENS, SOMMEPROD, SI.CONDITIONS, SIERREUR, SI.NON.DISP, TEXTE, ESTNUM/ESTNA, GAUCHE/DROITE/STXT, TROUVE/CHERCHE, DATE. Aucune erreur de syntaxe, séparateur point-virgule cohérent, contraintes de version signalées quand elles existent (RECHERCHEX en 365/2021, SI.CONDITIONS en 365/2019, TEXTE.AVANT/APRES en 365 seulement), et aucun résultat de calcul faux dans les corrigés — hors le numéro de série corrigé plus haut. Les nuances difficiles sont justes : limite de 127 couples dans SOMME.SI.ENS, inversion d'ordre des arguments entre SOMME.SI.ENS et NB.SI.ENS, RECHERCHEV en approximatif par défaut, TROUVE sensible à la casse contre CHERCHE qui ne l'est pas, SUPPRESPACE qui ne retire pas les espaces insécables.

**IA générative** — le module 5 fait exactement ce qu'il faut sur une matière mouvante : bases légales et sous-traitance RGPD (art. 28), condition d'originalité humaine du droit d'auteur, minimisation. Et il **évite délibérément de citer des dates sur l'AI Act**, renvoyant à une vérification juridique à jour plutôt que d'avancer un calendrier qui aurait vieilli. C'est le bon réflexe, et c'est rare.

**Management** — aucune erreur. Les attributions sont correctes (Hersey/Blanchard, Amy Edmondson et la sécurité psychologique, Thomas-Kilmann, Daniel Pink, ANACT/INRS), et aucune affirmation erronée de droit du travail : le module ne confond pas entretien annuel et entretien professionnel.

**SEO** — hors les trois points corrigés, tout le reste tient : seuils Core Web Vitals (LCP 2,5 s, INP 200 ms, CLS 0,1) avec la mention correcte du remplacement du FID par l'INP en mars 2024, distinction crawl/rendu/indexation/classement, libellés exacts des statuts Search Console, interaction robots.txt/noindex, canonical comme indication et non ordre, codes HTTP, E-E-A-T, rétention de 16 mois dans Search Console, limite de 500 URL de Screaming Frog.

**Analytics** — hors les trois points GA4, toute la partie statistique est correcte et bien expliquée : seuil de significativité, arrêt anticipé et inflation des faux positifs, relation quadratique entre effet et taille d'échantillon, corrélation contre causalité, régression vers la moyenne, effet de composition. Les définitions GA4 de session (30 min d'inactivité) et de session engagée (10 s, ou conversion, ou 2 pages) sont exactes.

**CRM Salesforce** — hors les deux points corrigés, le modèle de données est conforme au produit réel : objets standard et relations, conversion de piste irréversible, probabilité automatique par étape, fusion de comptes, suivi d'historique de champ, Flow présenté comme l'outil actuel avec Workflow Rules et Process Builder correctement situés comme antérieurs. Les catégories de prévision décrites recoupent fidèlement le champ standard Forecast Category.

**Content Marketing** — aucune erreur. Les références bibliographiques sont exactes (Sheridan, Miller, Handley, Halvorson), et la mécanique de l'Apple Mail Privacy Protection est correctement décrite sans être nommée.

Un point de méthode mérite d'être relevé : dans tous les modules, les chiffres présentés comme des ordres de grandeur le sont explicitement, et aucune statistique n'est attribuée à une source inventée. Le « Selon l'ADEME, 68 % » du module IA 1 est un faux volontaire, étiqueté comme tel dans l'exercice de détection d'hallucinations. C'est cette discipline-là qui explique le faible nombre d'erreurs.

---

## Corrections appliquées où

Dans les scripts générateurs quand ils existent, directement dans le HTML sinon.

| Fichier | Nature |
|---|---|
| `_tooling/mod2.py` | Analytics module 2 — 4 corrections GA4 + quiz q3 |
| `_tooling/excel_mod2.py` | Numéro de série de date |
| `_tooling/rse_mod4.py` | Montant de la sanction, 2 occurrences |
| `_tooling/bilan_mod1.py` | Date d'application du décret, 2 occurrences |
| `formations/seo/module-1,3,4/index.html` | Rendu JS, FAQPage, 410 |
| `formations/gestion-de-projet/module-2/` | Scrum — index.html + quiz.json |
| `formations/crm-relation-client/module-1/index.html` | Règle de doublon, nom Trailhead |
| `_tooling/build_ressources.py` | Date du décret CPF corrigée + exonérations |

Les quatre modules régénérés depuis leur script ont été revalidés : HTML complet, quiz à 6 questions, JSON valide.

**Une correction sur mon propre rapport précédent :** j'y ai écrit que la participation de 150 € s'appliquait depuis le 6 avril 2026. C'est le 2 avril. La page Ressources externes a été corrigée en conséquence, et enrichie des deux cas d'exonération — dont celui des demandeurs d'emploi, qui pourrait te concerner directement et changer tous les restes à charge affichés.

## Ce qui reste non vérifié

- Les **exercices corrigés** des formations sans script générateur n'ont été relus que pour leurs affirmations factuelles, pas recalculés pas à pas.
- Les **liens sortants** des blocs « Pour aller plus loin » n'ont pas été testés un par un.
- Toujours en attente côté ressources externes : les 23 codes du plan LABORA 2026, l'édition 2026 du campus virtuel LABORA, et The Business Legion.
