#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, json, os
sys.path.insert(0, "/tmp")
from fh_builder import build

M = {}
QUIZ = {}
FORM = "Excel &amp; analyse de données appliquée"

M["excel-analyse-donnees/module-3"] = {
 "formation": FORM,
 "titre": "Tableaux Croisés Dynamiques et Power Query",
 "num": 3, "total": 4, "duree": "70 min", "niveau": "Intermédiaire",
 "module_id": "formation-excel-analyse-donnees-module-3",
 "situation": [
   "Votre rapport mensuel de ventes vous prend trois heures. Vous connaissez le déroulé par cœur : ouvrir l'extraction, refaire les manipulations du module 1, recopier les formules du module 2, mettre à jour les plages des graphiques, contrôler, corriger ce qui a bougé.",
   "Ce mois-ci, la demande change. La direction veut le rapport consolidé sur les douze régions, et non plus sur le siège seul. Douze fichiers vous arrivent, un par région. Ils ont la même structure — sauf que trois d'entre eux ont les colonnes dans un ordre différent, deux comportent une colonne supplémentaire, et un a été renommé « Montant TTC » alors que les autres sont en HT.",
   "En empilant tout cela à la main, vous en avez pour la journée, et vous recommencerez le mois prochain. Le calcul est vite fait : trois heures fois douze mois, plus une journée de consolidation par mois, c'est un peu plus d'un mois de travail par an consacré à recopier des colonnes.",
   "Ce module traite des deux outils qui suppriment ce mois de travail — le tableau croisé dynamique pour l'analyse, Power Query pour la préparation — et de la discipline qui empêche un fichier automatisé de devenir un fichier incompréhensible.",
 ],
 "objectifs": [
   "Construire un tableau croisé dynamique qui répond à une question précise",
   "Reconnaître les fonctionnalités du TCD qui produisent des chiffres trompeurs",
   "Consolider plusieurs fichiers de structure voisine avec Power Query",
   "Dépivoter un tableau à colonnes mensuelles pour le rendre analysable",
   "Construire une chaîne de transformation rejouable en un clic",
   "Maintenir un fichier vivant sans le casser à chaque actualisation",
 ],
 "sections": [
  {"titre": "Le tableau croisé dynamique : ce qu'il fait, et ce qu'il exige",
   "paras": [
     "Un tableau croisé dynamique fait une seule chose, et il la fait très bien : il <strong>agrège une colonne de valeurs selon une ou plusieurs colonnes de catégories</strong>. Somme des montants par région et par mois, moyenne des délais par segment, nombre de commandes par commercial et par catégorie. C'est tout, et c'est l'essentiel de ce qu'on demande à une analyse.",
     "Sa force n'est pas de calculer — une somme conditionnelle fait la même chose — mais de permettre de changer la question sans réécrire quoi que ce soit. Faire passer une variable des lignes aux colonnes, ajouter un niveau de détail, changer l'agrégation de la somme à la moyenne : chacune de ces opérations prend une seconde. Sur une analyse exploratoire, où l'on ne sait pas d'avance quelle découpe sera parlante, cette souplesse change tout.",
     "En contrepartie, le TCD exige une donnée d'entrée rigoureusement conforme à la règle du module 1. Une ligne par observation, une colonne par variable, une seule ligne d'en-têtes, aucune cellule fusionnée, aucun total intercalé. Ce n'est pas une préférence : un tableau croisé dynamique construit sur des données mal structurées produit un résultat, et ce résultat est faux.",
     "Les quatre zones de construction méritent d'être comprises pour ce qu'elles sont, et non apprises par cœur. <strong>Lignes</strong> et <strong>Colonnes</strong> découpent : elles portent des variables catégorielles. <strong>Valeurs</strong> agrège : elle porte la variable numérique et le mode de calcul. <strong>Filtres</strong> restreint le périmètre global.",
     "Une règle de lecture aide à choisir : mettez en <strong>lignes</strong> la variable qui a beaucoup de modalités et que l'on parcourt du regard vers le bas — les produits, les clients ; mettez en <strong>colonnes</strong> celle qui en a peu et que l'on compare de gauche à droite — les trimestres, les segments. Un TCD à quarante colonnes est illisible ; le même avec quarante lignes et quatre colonnes se lit sans effort.",
   ],
   "blocks": [
     {"type": "method", "titre": "construire un TCD qui répond à une question",
      "paras": ["La règle préalable, celle qui distingue une analyse d'un tâtonnement : écrivez la question en français avant d'insérer le tableau. « Quelle catégorie a le plus reculé au T4, et dans quelles régions ? » — cette phrase détermine à elle seule la construction."],
      "steps": [
        "<strong>Vérifiez la source</strong> : une seule ligne d'en-têtes, aucun total intercalé, plage convertie en tableau structuré. Un TCD bâti sur un tableau structuré s'étendra tout seul aux nouvelles lignes ; sur une plage figée, il ignorera silencieusement les données ajoutées.",
        "<strong>Insérez le TCD dans un onglet dédié</strong>, jamais à côté des données. Un TCD grandit et rétrécit à chaque manipulation, et il écrasera ce qui se trouve à sa droite sans prévenir.",
        "<strong>Placez d'abord la valeur</strong>, et vérifiez immédiatement le grand total contre un calcul indépendant — une somme directe de la colonne. S'ils diffèrent, arrêtez-vous : il y a un problème de source, et tout ce que vous construirez ensuite en héritera.",
        "<strong>Ajoutez la variable de découpe principale en lignes</strong>, celle qui porte la question. Lisez le résultat avant d'ajouter quoi que ce soit d'autre.",
        "<strong>Ajoutez la seconde dimension en colonnes</strong>, et une seule. Un TCD à trois dimensions empilées ne se lit pas ; s'il en faut une troisième, elle va en filtre, et on regarde les modalités l'une après l'autre.",
        "<strong>Nommez le champ de valeurs</strong> en double-cliquant sur son en-tête : « Somme de Montant_HT » devient « CA HT ». Un TCD qu'on va montrer se nomme, sinon il porte les traces de sa fabrication.",
      ]},
     {"type": "exemple", "titre": "la question du module 1, résolue en trois minutes",
      "paras": [
        "Question : « quelle catégorie a le plus reculé au T4, et dans quelles régions ? ». Elle contient trois éléments — une mesure (le chiffre d'affaires), deux découpes (catégorie, région), une comparaison temporelle (T4 contre le reste).",
        "<em>Premier TCD :</em> Catégorie en lignes, Trimestre en colonnes, somme du montant en valeurs. Six lignes, quatre colonnes. La réponse à la première moitié de la question apparaît immédiatement : Mobilier passe de 412 k€ au T3 à 338 k€ au T4, soit -18 %, quand les autres catégories varient de moins de 5 %.",
        "<em>Second TCD :</em> Région en lignes, Trimestre en colonnes, filtre sur Catégorie = Mobilier. Sept lignes, quatre colonnes. Le recul est concentré : Sud-Ouest -41 %, Est -33 %, les cinq autres régions entre -2 % et +3 %.",
        "Trois minutes, deux tableaux, et une réponse précise. Le travail utile n'a pas été de construire les TCD — c'est mécanique — mais d'avoir écrit la question en trois éléments avant de commencer. Un analyste qui ouvre un TCD sans question précise passe une heure à déplacer des champs et n'obtient rien de mieux.",
      ]},
     {"type": "pitfall", "titre": "le TCD construit sur une plage figée",
      "paras": [
        "Vous créez un TCD sur la plage A1:H12000. Le mois suivant, vous collez 1 000 lignes supplémentaires, vous actualisez, et les chiffres n'ont pas bougé — ou ont bougé un peu, ce qui est pire. La plage source est restée A1:H12000.",
        "Le symptôme trompeur est qu'actualiser <em>semble</em> fonctionner : aucun message, un léger recalcul. Rien ne vous dit que les 1 000 nouvelles lignes sont hors périmètre.",
        "Deux protections. La bonne : construire le TCD sur un tableau structuré, qui s'étend seul. La vérification systématique, à faire de toute façon : comparer le grand total du TCD à une somme directe de la colonne source. Cet écart de trente secondes est le seul contrôle qui détecte tous les problèmes de périmètre, quelle qu'en soit la cause.",
      ]},
   ]},

  {"titre": "Les fonctionnalités du TCD qui trompent",
   "paras": [
     "Un tableau croisé dynamique offre des options puissantes qui produisent, mal comprises, des chiffres faux sans jamais signaler quoi que ce soit. Quatre méritent une attention particulière.",
     "<strong>Le mode d'agrégation par défaut.</strong> Excel choisit la somme si la colonne est entièrement numérique, et le <em>nombre</em> si elle contient ne serait-ce qu'une cellule texte. Un TCD qui affiche « 11 990 » là où vous attendiez « 4 402 000 » ne s'est pas trompé de calcul : il vous dit que votre colonne de montants contient du texte quelque part. C'est un excellent détecteur de typage, à condition de lire l'en-tête plutôt que le chiffre.",
     "<strong>Les champs calculés.</strong> Un champ calculé applique sa formule <em>sur les totaux agrégés</em>, et non ligne à ligne. Pour une somme, cela ne change rien. Pour tout ce qui est un ratio, cela change tout : un champ calculé « marge / chiffre d'affaires » donne le bon résultat, mais un champ calculé « prix moyen × quantité » donne le produit des totaux, qui n'a aucun sens. La règle sûre : <strong>tout ce qui se calcule ligne à ligne se calcule dans une colonne de la source, jamais dans un champ calculé</strong>. Le champ calculé est réservé aux ratios de deux agrégats.",
     "<strong>L'affichage en pourcentage.</strong> Le menu « Afficher les valeurs » propose « % du total général », « % du total de la ligne », « % du total de la colonne », plus une dizaine de variantes. Ces trois-là ne répondent pas à la même question, et l'erreur la plus fréquente est de prendre l'un pour l'autre : « 12 % » peut vouloir dire douze pour cent des ventes totales, douze pour cent des ventes de la région, ou douze pour cent des ventes du trimestre. Le TCD ne l'écrit nulle part. C'est à vous de le préciser dans le titre du tableau, faute de quoi il sera mal lu — y compris par vous, trois semaines plus tard.",
     "<strong>Les regroupements de dates.</strong> Excel propose de regrouper automatiquement une colonne de dates par mois, trimestre, année. C'est commode et cela comporte un piège : le regroupement par mois <em>sans</em> l'année agrège tous les mois de janvier de toutes les années ensemble. Sur un fichier d'un an, aucun effet visible. Le jour où l'on ajoute l'année précédente, les chiffres doublent silencieusement. Cochez toujours Mois <em>et</em> Années.",
     "Un point général sur les totaux : le TCD calcule ses totaux à partir des données sources, et non en additionnant les cellules affichées. Sur des moyennes ou des pourcentages, le total général n'est donc pas la somme de la colonne affichée — c'est la moyenne de tout, ce qui est correct mais surprend systématiquement. Ne « corrigez » jamais ce comportement : il est juste.",
   ],
   "blocks": [
     {"type": "exemple", "titre": "le champ calculé qui donne 340 % de marge",
      "paras": [
        "Un analyste veut afficher le taux de marge par catégorie. Il crée un champ calculé <code>Marge / CA</code> et obtient des taux plausibles, entre 18 % et 34 %. Satisfait, il ajoute un second champ calculé, <code>Prix_unitaire × Quantite</code>, pour contrôler le chiffre d'affaires. Le résultat est absurde : plusieurs milliards.",
        "L'explication : le champ calculé opère sur les agrégats. Il a multiplié la <em>somme</em> des prix unitaires de la catégorie — un nombre qui n'a aucun sens — par la <em>somme</em> des quantités. Le premier champ calculé fonctionnait parce qu'un ratio de deux sommes est légitime ; le second ne pouvait pas fonctionner.",
        "La correction est toujours la même : créer une colonne <code>CA = Prix_unitaire * Quantite</code> dans la table source, et sommer cette colonne dans le TCD. Le calcul se fait ligne à ligne, puis l'agrégation. Jamais l'inverse.",
        "La règle mnémotechnique : <strong>agréger puis diviser est correct, agréger puis multiplier ne l'est presque jamais.</strong>",
      ]},
     {"type": "pitfall", "titre": "la modalité fantôme qui survit au nettoyage",
      "paras": [
        "Vous avez corrigé « sud ouest » en « Sud-Ouest » dans la source, vous actualisez le TCD, et « sud ouest » apparaît toujours dans la liste des filtres — avec un total à zéro.",
        "Le TCD conserve en mémoire cache les modalités rencontrées, y compris disparues. Ce n'est pas un bug, c'est un choix de conception qui permet de garder une mise en forme stable. Mais une modalité fantôme dans un filtre est un piège pour le lecteur, qui la coche et obtient un tableau vide.",
        "Le correctif : clic droit sur le TCD &gt; Options &gt; Données &gt; Nombre d'éléments à conserver par champ = Aucun, puis actualiser. À faire systématiquement avant de diffuser un tableau de bord, sinon vos filtres proposeront des choix qui n'existent plus.",
      ]},
   ]},

  {"titre": "Power Query : préparer une fois, rejouer indéfiniment",
   "paras": [
     "Power Query, présent dans le ruban Données sous « Récupérer et transformer », est l'outil qui manquait à Excel : un <strong>enregistreur de transformations</strong>. Vous décrivez une fois la suite d'opérations qui mène du fichier brut au fichier propre, et cette suite se rejoue à la demande sur des données nouvelles.",
     "La différence avec ce que vous avez fait au module 1 n'est pas la puissance — les opérations sont les mêmes — mais la <em>persistance</em>. Un nettoyage manuel disparaît avec le fichier ; une requête Power Query reste, se lit, se modifie et se documente.",
     "Le principe de fonctionnement tient en trois idées. <strong>Une requête est une suite d'étapes nommées</strong>, visibles dans un volet à droite de l'éditeur, dans l'ordre où elles s'appliquent. Vous pouvez cliquer sur n'importe quelle étape pour voir l'état des données à ce moment-là, en insérer une au milieu, en supprimer une. <strong>Rien n'est modifié à la source</strong> : Power Query lit le fichier d'origine et produit un résultat ailleurs. <strong>Le résultat se charge dans une feuille ou dans le modèle de données</strong>, et se réactualise d'un clic.",
     "Les opérations qui couvrent l'essentiel des besoins sont peu nombreuses et se font toutes à la souris. <em>Supprimer les lignes du haut</em> pour retirer les titres parasites. <em>Utiliser la première ligne pour les en-têtes</em>. <em>Modifier le type</em> de chaque colonne — c'est ici que se règle définitivement le problème du typage. <em>Remplacer les valeurs</em>, <em>Format &gt; Supprimer les espaces</em>, <em>Format &gt; Majuscules</em>. <em>Fractionner la colonne</em> par délimiteur, qui gère un nombre variable de valeurs par ligne, contrairement à la commande Convertir. <em>Filtrer</em> pour éliminer les lignes de total. <em>Colonne conditionnelle</em>, qui construit un SI sans écrire de formule.",
     "Trois opérations méritent d'être connues nommément parce qu'elles n'ont pas d'équivalent simple ailleurs.",
     "<strong>Dépivoter les colonnes</strong> transforme un tableau à colonnes mensuelles en tableau long : sélectionnez les douze colonnes de mois, Transformer &gt; Dépivoter les colonnes, et vous obtenez deux colonnes, Attribut et Valeur. C'est l'opération qui règle en un clic le problème du module 1 sur les tableaux de suivi mensuel, et c'est probablement la plus utile de tout Power Query.",
     "<strong>Fusionner des requêtes</strong> rapproche deux tables sur une clé commune — l'équivalent d'une RECHERCHEX, mais sans formule, et surtout avec un affichage direct du nombre de lignes appariées. Le type de jointure se choisit explicitement : « externe gauche » conserve toutes les lignes de la table de gauche, « anti » ne conserve que les lignes <em>non</em> appariées, ce qui donne directement la liste des non-correspondances du module 2.",
     "<strong>Ajouter des requêtes</strong> empile plusieurs tables de même structure. Combiné à la connexion « À partir d'un dossier », c'est ce qui résout la consolidation de douze fichiers régionaux en une opération.",
   ],
   "blocks": [
     {"type": "method", "titre": "consolider un dossier de fichiers en une requête",
      "paras": ["Le cas de la mise en situation : douze fichiers régionaux, même structure à quelques écarts près, à consolider tous les mois."],
      "steps": [
        "<strong>Rangez les fichiers dans un dossier dédié</strong>, et rien d'autre dedans. Power Query lira tout ce qui s'y trouve : un fichier temporaire ouvert par quelqu'un, un PDF, un ancien export, et la requête échouera ou intégrera des données parasites.",
        "<strong>Données &gt; Obtenir des données &gt; À partir d'un fichier &gt; À partir d'un dossier</strong>, puis Transformer les données. Vous obtenez la liste des fichiers, pas encore leur contenu.",
        "<strong>Combinez</strong> par le bouton de la colonne Content. Power Query prend le premier fichier comme modèle et crée automatiquement une requête de transformation appliquée à tous. Vérifiez ce que ce modèle a déduit — c'est l'étape que l'on survole et où se logent les erreurs.",
        "<strong>Conservez la colonne Source.Name</strong>, qui porte le nom du fichier d'origine. Elle vous donne gratuitement la région, et surtout elle permet de retrouver d'où vient une ligne suspecte. Ne la supprimez jamais.",
        "<strong>Traitez les écarts de structure</strong> : l'ordre des colonnes n'a aucune importance, Power Query apparie par nom. Une colonne supplémentaire dans deux fichiers apparaîtra, remplie de valeurs nulles ailleurs. Une colonne portant un nom différent — « Montant TTC » contre « Montant HT » — sera traitée comme une colonne distincte, et c'est le piège de l'opération.",
        "<strong>Ajoutez une étape de contrôle</strong> : après consolidation, un regroupement par Source.Name donnant le nombre de lignes de chaque fichier. Comparez ce compte à ce que chaque région annonce. C'est le seul moyen de détecter qu'un fichier n'a pas été lu.",
      ]},
     {"type": "exemple", "titre": "la colonne Montant TTC, et pourquoi elle est dangereuse",
      "paras": [
        "Onze fichiers ont une colonne « Montant HT ». Le douzième a « Montant TTC ». Après consolidation, la table comporte deux colonnes : « Montant HT » renseignée sur onze régions et vide sur la douzième, « Montant TTC » renseignée uniquement sur la douzième.",
        "Le résultat est visible — une colonne à moitié vide se remarque — et c'est une chance. Le scénario réellement dangereux est celui où le douzième fichier aurait nommé sa colonne « Montant HT » en y mettant des montants TTC. Rien n'apparaîtrait, et la région concernée serait surévaluée de 20 % dans tous les tableaux, indéfiniment.",
        "La conduite : ne jamais consolider sans un contrôle de vraisemblance par fichier source. Un regroupement Source.Name donnant nombre de lignes, somme et montant moyen révèle immédiatement une région dont le panier moyen est 20 % au-dessus des autres. Trente secondes de contrôle contre une erreur permanente et invisible.",
        "Et une fois le problème identifié : ne le corrigez pas dans votre requête par une division par 1,2. Demandez le fichier en HT. Une correction cachée dans une étape de requête sera oubliée, et elle deviendra fausse le jour où la région corrigera son export de son côté.",
      ]},
     {"type": "pitfall", "titre": "l'étape « Type modifié » automatique",
      "paras": [
        "Power Query ajoute automatiquement une étape « Type modifié » après l'import, en déduisant le type de chaque colonne des <em>premières</em> lignes du fichier. Sur un fichier dont les cent premières lignes ont un code produit numérique et dont la ligne 3 000 porte un code alphanumérique, le type déduit sera le nombre, et cette ligne deviendra une erreur.",
        "Pire, cette étape mémorise la <em>liste des colonnes</em> au moment de sa création. Si le fichier du mois suivant comporte une colonne de plus, l'étape ne la typera pas ; s'il en comporte une de moins, la requête échouera avec un message peu explicite.",
        "La bonne pratique : supprimez l'étape « Type modifié » automatique, et retypez explicitement les colonnes dont vous avez besoin, en dernière étape de la requête plutôt qu'en première. Les codes qui ressemblent à des nombres — codes postaux, références, numéros de compte — se typent en texte, toujours, sous peine de perdre leurs zéros initiaux.",
      ]},
   ]},

  {"titre": "Le fichier vivant : actualiser sans casser",
   "paras": [
     "Un fichier automatisé a une propriété désagréable : il continue de produire des résultats même quand quelque chose a changé en amont. Un fichier manuel s'arrête et vous alerte ; un fichier automatisé, lui, se contente de recalculer sur ce qu'il trouve. C'est le prix de l'automatisation, et il se paie par de la discipline.",
     "<strong>La règle de l'onglet unique de contrôle.</strong> Tout classeur automatisé porte un onglet « Contrôles » placé en première position, contenant cinq à huit formules qui s'évaluent seules après chaque actualisation. Nombre de lignes consolidées et sa variation par rapport au mois précédent. Nombre de fichiers sources effectivement lus. Somme de la colonne principale, avec sa variation. Nombre de valeurs distinctes de chaque colonne catégorielle. Nombre de lignes en erreur. Plage de dates.",
     "Chacune de ces formules affiche « OK » ou une alerte, par un simple <code>SI</code> comparant à une fourchette attendue. Le but n'est pas d'être exhaustif : c'est de rendre une anomalie <strong>impossible à ne pas voir</strong> par quelqu'un qui ouvre le fichier sans le connaître.",
     "<strong>L'ordre d'actualisation compte.</strong> Dans un classeur combinant requêtes et tableaux croisés dynamiques, actualisez d'abord les requêtes, puis les TCD. Données &gt; Actualiser tout le fait dans le bon ordre — mais uniquement si les TCD sont construits sur les tables issues des requêtes, et non sur des copies figées. Un TCD pointant vers une plage collée à la main ne verra jamais la nouvelle donnée.",
     "<strong>La documentation vit dans le fichier, pas à côté.</strong> Un onglet « Lisez-moi » en première position : d'où viennent les données, quelles requêtes existent et ce qu'elles font, quels onglets sont calculés et ne doivent pas être modifiés à la main, quels paramètres sont modifiables et par qui, quels contrôles vérifier avant diffusion. Un document séparé aura divergé du fichier dans les trois mois ; un onglet ne se perd pas.",
     "<strong>Le nommage des étapes de requête.</strong> Power Query nomme ses étapes « Personnalisé1 », « Type modifié2 », « Lignes filtrées3 ». Renommez-les en français, d'un clic droit : « Retirer les lignes de total », « Normaliser les codes produits », « Filtrer sur l'année en cours ». Une requête à vingt étapes bien nommées <em>est</em> sa propre documentation, et se relit en une minute. La même requête aux noms par défaut demande une demi-heure de rétro-ingénierie.",
   ],
   "blocks": [
     {"type": "h3", "titre": "Ce qui casse un fichier automatisé, par ordre de fréquence",
      "paras": [
        "<strong>Le déplacement d'un fichier source.</strong> Le chemin est mémorisé dans la requête. Un dossier renommé, un fichier passé sur un autre disque partagé, et la requête échoue. Parade : centralisez les chemins dans un onglet Paramètres et référencez-les, plutôt que de les laisser en dur dans chaque requête.",
        "<strong>Le renommage d'une colonne à la source.</strong> Power Query référence les colonnes par leur nom. Un renommage casse la requête — ce qui est une bonne nouvelle, puisque l'erreur est bruyante et immédiate. Le contraire serait bien pire.",
        "<strong>L'ajout d'une colonne à la source.</strong> Généralement sans effet, sauf si une étape « Colonnes supprimées » avait été construite en listant les colonnes à retirer plutôt que celles à garder. Préférez toujours « Supprimer les autres colonnes » à « Supprimer les colonnes » : la première résiste à un ajout, la seconde le laisse passer.",
        "<strong>La modification manuelle d'un onglet calculé.</strong> Quelqu'un corrige une valeur directement dans la table issue de la requête. La correction disparaît à la première actualisation, et la personne conclut que le fichier est instable. Parade : protéger les onglets calculés et l'écrire dans le Lisez-moi.",
        "<strong>Un fichier source ouvert par un collègue.</strong> Selon le format, la lecture échoue ou renvoie une version partielle. Parade : lire depuis une copie déposée dans un dossier dédié, jamais depuis le fichier de travail de quelqu'un d'autre.",
      ]},
     {"type": "exemple", "titre": "trois heures devenues huit minutes",
      "paras": [
        "État final du fichier de la mise en situation, après une journée de construction.",
        "<em>Une requête « Sources »</em> qui lit le dossier des douze fichiers régionaux, les empile, conserve Source.Name, retire les lignes de total, normalise les codes produits et les régions par une table de correspondance, et type explicitement les huit colonnes utiles. Vingt-deux étapes, toutes nommées en français.",
        "<em>Une requête « Referentiel »</em> qui lit le référentiel produits et le déduplique sur le code en gardant la ligne la plus récente.",
        "<em>Une requête « Ventes »</em> qui fusionne les deux en jointure externe gauche, et une requête « Non appariés » en jointure anti, chargée dans un onglet de contrôle.",
        "<em>Quatre TCD</em> construits sur la table Ventes, et un onglet Contrôles à six formules.",
        "Le déroulé mensuel : déposer les douze fichiers dans le dossier, ouvrir le classeur, Actualiser tout, lire l'onglet Contrôles, vérifier l'onglet des non appariés, diffuser. Huit minutes quand rien n'a bougé, une demi-heure quand une région a changé quelque chose — et dans ce cas, on sait exactement laquelle et quoi.",
        "Le gain réel n'est pas le temps. C'est que le rapport est désormais <strong>reproductible et vérifiable</strong> : deux personnes qui l'exécutent obtiennent le même résultat, et n'importe qui peut ouvrir la requête pour voir ce qui est fait aux données. Le temps gagné est agréable ; c'est la reproductibilité qui rend l'analyse défendable.",
      ]},
   ]},

  {"titre": "Choisir entre formule, TCD et requête",
   "paras": [
     "Vous disposez maintenant de trois outils qui se recouvrent partiellement, et la question « lequel employer ? » revient à chaque tâche. Trois critères tranchent, dans cet ordre.",
     "<strong>La tâche est-elle récurrente ?</strong> Si l'opération sera refaite chaque mois, elle relève de Power Query, quelle que soit sa simplicité. Une transformation triviale répétée douze fois par an coûte plus cher qu'une requête construite une fois. Si elle est réellement unique, une manipulation manuelle documentée suffit.",
     "<strong>La tâche transforme-t-elle les données ou les agrège-t-elle ?</strong> Nettoyer, rapprocher, empiler, dépivoter : Power Query. Compter, sommer, moyenner selon des catégories : tableau croisé dynamique. Les formules gardent leur place pour les calculs ligne à ligne — une marge, un délai, une catégorie de tranche — qui doivent exister dans la table avant toute agrégation.",
     "<strong>Le résultat doit-il être exploré ou publié ?</strong> Une question ouverte, dont on ne sait pas encore quelle découpe sera parlante, appelle un TCD, qu'on manipule en direct. Un chiffre destiné à figurer à un endroit précis d'un rapport appelle une formule, généralement <code>LIREDONNEESTABCROISDYNAMIQUE</code> pointant vers un TCD, ou une somme conditionnelle directe. Un TCD dans un rapport diffusé est une invitation à ce que le lecteur déplace un champ et casse la mise en page.",
     "Ces trois outils ne se remplacent pas : ils s'enchaînent. La chaîne complète d'une analyse mature est toujours la même — <strong>Power Query prépare, des colonnes de formules calculent ligne à ligne, un tableau croisé dynamique agrège, et une couche de présentation figée expose</strong>. Le module 4 traite de cette dernière couche.",
   ],
   "blocks": [
     {"type": "pitfall", "titre": "tout basculer dans Power Query par enthousiasme",
      "paras": [
        "Power Query est satisfaisant à utiliser, et la tentation qui suit sa découverte est d'y faire passer l'intégralité du traitement, y compris les calculs qui relèvent d'une simple colonne de formule.",
        "Le coût apparaît plus tard. Une logique métier enfouie dans une colonne conditionnelle de requête est invisible depuis la feuille : personne ne la voit en ouvrant le fichier, et il faut entrer dans l'éditeur pour comprendre pourquoi une ligne porte telle valeur. Une colonne de formule dans la table, elle, se lit d'un clic et se vérifie ligne à ligne.",
        "Le partage raisonnable : <strong>Power Query pour tout ce qui concerne la forme des données</strong> — structure, types, nettoyage, jointures, empilage. <strong>Les formules pour tout ce qui relève d'une règle métier</strong> — un seuil de remise, une catégorie de client, une règle d'exclusion. La règle métier doit rester visible, parce que c'est celle qui sera discutée en réunion.",
      ]},
   ]},
 ],

 "etude_cas": {
   "titre": "Consolider douze fichiers régionaux et supprimer la journée mensuelle",
   "html": """
<p>Reprenons la demande : douze fichiers régionaux de structure voisine, un rapport à produire chaque mois. Voici la construction complète, avec les décisions prises à chaque étape.</p>
<p><strong>Étape 1 — inspecter avant de consolider.</strong> Avant toute requête, ouvrir les douze fichiers et relever, pour chacun : le nombre de lignes, la liste des en-têtes, la présence de lignes de total, le format des dates. Une demi-heure, et elle évite trois jours de débogage.</p>
<p>Constat : neuf fichiers strictement identiques ; deux avec une colonne « Commentaire » supplémentaire ; un — la région Est — avec « Montant TTC » au lieu de « Montant HT », et des dates au format américain MJA. Ce dernier fichier est la vraie difficulté, et il vaut mieux le savoir maintenant que de le découvrir dans un chiffre aberrant.</p>
<p><strong>Étape 2 — poser la question du bon interlocuteur.</strong> Avant de coder quoi que ce soit, un appel à la région Est : peuvent-ils exporter en HT comme les autres ? Réponse : oui, c'était un paramètre de leur outil, corrigé pour le mois prochain. Cinq minutes d'appel évitent une correction permanente dans la requête — et surtout une correction qui serait devenue fausse dès le mois suivant, une fois leur export changé, sans que personne ne s'en souvienne.</p>
<p>Pour le mois en cours, on traite le fichier à part et on documente. C'est le bon arbitrage : un correctif temporaire assumé et daté vaut mieux qu'un correctif permanent oublié.</p>
<p><strong>Étape 3 — organiser le dossier.</strong> Un dossier <code>sources/2026-09/</code> contenant exclusivement les douze fichiers, nommés <code>ventes_&lt;region&gt;_2026-09.xlsx</code>. Rien d'autre. Le nommage porte la région et la période, ce qui rend la colonne Source.Name directement exploitable et le tri chronologiquement correct.</p>
<p><strong>Étape 4 — construire la requête de consolidation.</strong> À partir d'un dossier, puis Combiner. Power Query génère une requête modèle ; on l'inspecte immédiatement et on supprime son étape « Type modifié » automatique, pour les raisons vues plus haut.</p>
<p>Étapes ajoutées, dans l'ordre, et toutes renommées en français : retirer les deux premières lignes de titre ; promouvoir la première ligne en en-têtes ; filtrer pour éliminer les lignes contenant « Total » ; extraire la région depuis Source.Name ; supprimer les autres colonnes en ne conservant que les huit utiles — formulation qui résiste à l'ajout d'une colonne « Commentaire » ; normaliser le code produit par suppression des espaces et formatage à quatre chiffres ; normaliser la région par une table de correspondance chargée depuis un onglet du classeur ; typer explicitement les huit colonnes, le code produit en texte.</p>
<p>Vingt-deux étapes. La requête est chargée dans une table nommée <em>Ventes_brutes</em>.</p>
<p><strong>Étape 5 — contrôler la consolidation avant d'aller plus loin.</strong> Une seconde requête, en référence à la première, qui regroupe par région et renvoie nombre de lignes, somme des montants et montant moyen. Chargée dans l'onglet Contrôles.</p>
<p>Ce tableau révèle immédiatement deux choses. La région Est affiche un panier moyen 19,7 % au-dessus de la moyenne des autres — la confirmation attendue du problème HT/TTC. Et la région Centre affiche 340 lignes contre environ 1 000 pour les régions de taille comparable. Vérification : leur fichier avait été exporté sur le mois en cours au lieu du mois précédent. Sans ce contrôle, le rapport aurait sous-estimé le Centre de deux tiers, et l'erreur serait passée pour une baisse d'activité.</p>
<p>C'est le point le plus important de toute l'étude de cas : <strong>le contrôle par source a trouvé une anomalie que personne ne cherchait</strong>, et qui n'avait rien à voir avec la difficulté anticipée.</p>
<p><strong>Étape 6 — fusionner avec le référentiel.</strong> Une requête Referentiel, dédupliquée sur le code. Une fusion en jointure externe gauche entre Ventes_brutes et Referentiel, qui donne la table Ventes. Une seconde fusion, en jointure anti, qui donne la table des non appariés — chargée dans l'onglet Contrôles, avec son nombre de lignes.</p>
<p>Cette jointure anti remplace tout le travail manuel du module 2 : la liste des non-correspondances est produite automatiquement, à chaque actualisation, sans qu'on ait à y penser.</p>
<p><strong>Étape 7 — les colonnes de règle métier, en formules.</strong> Dans la table Ventes, deux colonnes ajoutées en formules Excel et non dans la requête : la marge, et la catégorie de remise par table de correspondance. Ce sont des règles métier, susceptibles d'être discutées en réunion : elles doivent rester visibles dans la feuille.</p>
<p><strong>Étape 8 — les tableaux croisés dynamiques.</strong> Quatre TCD dans un onglet Analyses : CA par catégorie et trimestre ; CA par région et mois ; marge par catégorie avec taux de couverture ; top vingt des produits par marge. Chacun construit sur la table Ventes, donc extensible automatiquement.</p>
<p><strong>Étape 9 — l'onglet Contrôles, version finale.</strong> Sept lignes : nombre total de lignes et variation contre le mois précédent ; nombre de fichiers lus, attendu 12 ; tableau par région avec nombre de lignes, somme et panier moyen ; nombre de non appariés et taux ; plage de dates, entièrement contenue dans le mois ; nombre de lignes en erreur ; écart entre le grand total du TCD principal et la somme directe de la colonne, attendu zéro.</p>
<p><strong>Étape 10 — le Lisez-moi.</strong> Une page : origine des données, description des quatre requêtes, onglets à ne pas modifier, procédure mensuelle en cinq lignes, contrôles à vérifier avant diffusion, et l'historique des incidents connus — dont le HT/TTC de la région Est, avec sa date de résolution annoncée.</p>
<p><strong>Résultat.</strong> Construction : une journée. Exécution mensuelle : huit minutes en régime normal. Sur l'année, un peu plus d'un mois de travail libéré.</p>
<p><strong>La leçon transposable.</strong> Le gain de temps est ce qui justifie le projet auprès d'une hiérarchie, mais ce n'est pas ce qui compte le plus. Le contrôle par source a détecté une erreur de périmètre que la méthode manuelle n'aurait jamais trouvée, parce qu'en travaillant à la main on regarde le résultat, jamais la composition du résultat. Automatiser libère précisément le temps qu'il faut pour vérifier — à condition de l'employer à cela, et c'est un choix, pas une conséquence.</p>
"""},

 "checklist": {
   "titre": "Checklist — TCD, requêtes et fichiers vivants",
   "items": [
     "Chaque TCD est construit sur un tableau structuré ou une table de requête, jamais sur une plage figée",
     "Le grand total du TCD a été comparé à une somme directe de la colonne source",
     "Le TCD est dans un onglet dédié, sans rien à sa droite",
     "L'en-tête du champ de valeurs a été vérifié : somme et non nombre",
     "Aucun champ calculé ne réalise une multiplication entre deux agrégats",
     "Tout calcul ligne à ligne existe dans une colonne de la source",
     "Le mode d'affichage en pourcentage est précisé dans le titre du tableau",
     "Les regroupements de dates cochent Mois et Années, jamais Mois seul",
     "Le cache des modalités disparues a été vidé avant diffusion",
     "Les fichiers sources sont seuls dans un dossier dédié, nommés par région et période",
     "L'étape Type modifié automatique a été supprimée et remplacée par un typage explicite en fin de requête",
     "Les codes à zéros initiaux sont typés en texte",
     "La colonne Source.Name est conservée",
     "Les étapes de requête sont renommées en français",
     "Supprimer les autres colonnes est employé plutôt que Supprimer les colonnes",
     "Un contrôle par fichier source affiche nombre de lignes, somme et moyenne",
     "Une jointure anti produit automatiquement la liste des non-correspondances",
     "Les règles métier sont en colonnes de formules visibles, pas enfouies dans une requête",
     "Un onglet Contrôles en première position s'évalue seul après chaque actualisation",
     "Un onglet Lisez-moi documente les requêtes, les onglets protégés et la procédure mensuelle",
   ]},

 "glossaire": [
   ("Tableau croisé dynamique", "Outil d'agrégation d'une colonne de valeurs selon des colonnes de catégories. Exige une source rigoureusement structurée."),
   ("Champ calculé", "Calcul défini dans le TCD, appliqué aux totaux agrégés et non ligne à ligne. Légitime pour un ratio, faux pour un produit."),
   ("Cache du TCD", "Mémoire des modalités rencontrées, y compris disparues. À vider avant diffusion pour éviter les filtres proposant des valeurs inexistantes."),
   ("Power Query", "Enregistreur de transformations intégré à Excel. Décrit une fois la préparation des données et la rejoue à la demande."),
   ("Étape de requête", "Opération nommée d'une transformation, visible et modifiable dans l'ordre. Une requête bien nommée est sa propre documentation."),
   ("Dépivoter", "Transformation d'un tableau à colonnes de périodes en tableau long à trois colonnes. L'opération la plus utile de Power Query."),
   ("Fusionner des requêtes", "Rapprochement de deux tables sur une clé, équivalent d'une recherche mais sans formule, avec comptage direct des lignes appariées."),
   ("Jointure anti", "Type de fusion ne conservant que les lignes sans correspondance. Produit automatiquement la liste des non-correspondances."),
   ("Ajouter des requêtes", "Empilage de tables de même structure. Combiné à la connexion sur dossier, il consolide n fichiers en une opération."),
   ("Source.Name", "Colonne portant le nom du fichier d'origine après consolidation. À conserver systématiquement : elle permet de tracer toute ligne suspecte."),
   ("Onglet Contrôles", "Onglet de vérifications automatiques évaluées après chaque actualisation. Rend une anomalie impossible à ne pas voir."),
   ("LIREDONNEESTABCROISDYNAMIQUE", "Fonction extrayant une valeur précise d'un TCD pour l'exposer dans un rapport figé, sans exposer le TCD lui-même."),
 ],

 "retenir": [
   "Un TCD agrège une valeur selon des catégories : sa force est de permettre de changer la question sans rien réécrire.",
   "Écrivez la question en français avant d'insérer un TCD : c'est elle qui détermine la construction.",
   "Beaucoup de modalités en lignes, peu en colonnes : un TCD à quarante colonnes est illisible.",
   "Comparez toujours le grand total du TCD à une somme directe de la source : c'est le contrôle qui détecte tous les problèmes de périmètre.",
   "Un TCD sur plage figée ignore silencieusement les lignes ajoutées ; sur tableau structuré, il s'étend seul.",
   "Un TCD qui affiche un nombre au lieu d'une somme vous signale que la colonne contient du texte.",
   "Agréger puis diviser est correct ; agréger puis multiplier ne l'est presque jamais : les produits se calculent en colonne de source.",
   "Précisez dans le titre de quoi le pourcentage est un pourcentage : le TCD ne l'écrit nulle part.",
   "Regroupez les dates par Mois et Années, jamais par Mois seul, sous peine d'agréger deux années ensemble.",
   "Videz le cache des modalités disparues avant de diffuser, sinon vos filtres proposeront des valeurs qui n'existent plus.",
   "Une opération récurrente relève de Power Query, quelle que soit sa simplicité.",
   "Supprimez l'étape Type modifié automatique et retypez explicitement en fin de requête.",
   "Conservez toujours Source.Name : c'est ce qui permet de retrouver d'où vient une ligne suspecte.",
   "Contrôlez toute consolidation par un regroupement par fichier source : nombre de lignes, somme et moyenne.",
   "Renommez les étapes de requête en français : une requête bien nommée est sa propre documentation.",
   "Préférez Supprimer les autres colonnes à Supprimer les colonnes : la première résiste à un ajout à la source.",
   "Laissez les règles métier en formules visibles ; réservez Power Query à la forme des données.",
   "Un fichier automatisé continue de produire des résultats quand quelque chose a changé : l'onglet Contrôles est ce qui remplace l'alerte.",
   "Automatiser libère le temps nécessaire à la vérification — encore faut-il l'employer à cela.",
 ],

 "exercices": [
  {"titre": "Corriger trois tableaux croisés dynamiques", "niveau": "Débutant",
   "enonce": [
     "Trois TCD produisent des résultats douteux. Pour chacun, dites ce qui se passe et comment corriger.",
     "<strong>A.</strong> Un TCD sur les ventes affiche « 11 990 » comme grand total, alors que le chiffre d'affaires attendu est d'environ 4,4 M€.",
     "<strong>B.</strong> Un TCD affiche le chiffre d'affaires par mois. Après l'ajout de l'année précédente dans la source et une actualisation, tous les mois ont exactement doublé et il n'y a toujours que douze lignes.",
     "<strong>C.</strong> Un TCD affiche le taux de marge par catégorie via un champ calculé <code>Marge / CA</code>. Les taux paraissent corrects, mais le total général affiche un taux différent de la moyenne des lignes, et personne ne comprend lequel est juste.",
   ],
   "corrige": """
<p><strong>A — le TCD compte au lieu de sommer.</strong></p>
<p>11 990 est le nombre de lignes de la table. L'en-tête du champ de valeurs affiche « Nombre de Montant_HT » et non « Somme de Montant_HT ». Excel choisit le comptage dès qu'une colonne contient au moins une valeur non numérique.</p>
<p><em>Correction immédiate :</em> double-clic sur l'en-tête du champ &gt; Somme. Mais cela masque le problème sans le résoudre : la somme obtenue ignorera les cellules texte, qui compteront pour zéro. Le TCD ne vous signalera plus rien, et vous aurez un total sous-évalué.</p>
<p><em>Correction réelle :</em> retourner à la source et trouver les valeurs non numériques. <code>=NB(Ventes[Montant_HT])</code> compte les cellules numériques ; l'écart avec <code>=NBVAL(Ventes[Montant_HT])</code> donne le nombre de cellules texte. Puis Données &gt; Convertir, comme au module 1.</p>
<p><em>Ce qu'il faut retenir de ce cas :</em> le comptage automatique n'est pas un défaut du TCD, c'est un détecteur de typage gratuit. Un analyste expérimenté ne corrige pas l'affichage, il va voir pourquoi.</p>
<p><strong>B — le regroupement de dates sans l'année.</strong></p>
<p>La colonne de dates a été regroupée par Mois uniquement. Tous les mois de janvier, toutes années confondues, sont agrégés dans une seule ligne « janvier ». Sur une année de données, le comportement était indiscernable du bon ; avec deux années, chaque mois porte la somme des deux.</p>
<p><em>Correction :</em> clic droit sur un libellé de mois &gt; Grouper, et cocher Mois <strong>et</strong> Années. Le TCD affiche alors une hiérarchie année puis mois, avec vingt-quatre lignes.</p>
<p><em>Le détail qui rend ce cas instructif :</em> le doublement exact aurait pu passer pour une croissance si les deux années avaient été de volumes différents. Ici, un doublement à la ligne près sur les douze mois est trop régulier pour être une variation d'activité — c'est ce genre de régularité suspecte qui doit déclencher une vérification. Une croissance réelle n'est jamais aussi propre.</p>
<p><strong>C — le total général d'un ratio n'est pas la moyenne des lignes.</strong></p>
<p>Aucun des deux n'est faux : ils répondent à deux questions différentes, et le TCD affiche la bonne réponse à la question qu'il pose.</p>
<p>Le total général du champ calculé vaut <em>somme de toutes les marges divisée par somme de tous les chiffres d'affaires</em>. C'est le taux de marge global de l'entreprise, pondéré par le poids de chaque catégorie. La moyenne arithmétique des taux affichés, elle, donnerait le taux moyen des catégories en les traitant à poids égal — une catégorie représentant 2 % du chiffre d'affaires y pèserait autant qu'une catégorie en représentant 40 %.</p>
<p><em>Lequel est juste ?</em> Le total général, dans la quasi-totalité des usages. « Quel est notre taux de marge ? » veut dire « quelle part de notre chiffre d'affaires est de la marge », donc un ratio de deux totaux. La moyenne des taux ne répond à cette question que si toutes les catégories font le même volume.</p>
<p><em>Ce qu'il faut faire :</em> ne rien corriger, et écrire dans le titre ou en note « taux de marge pondéré par le chiffre d'affaires ». Le problème n'est pas le calcul, c'est qu'il n'est pas explicité — et une valeur non explicitée finit toujours par être mal interprétée par quelqu'un.</p>
<p><em>Le piège à ne pas commettre :</em> remplacer le champ calculé par une moyenne des taux pour que le total « corresponde ». Vous auriez un tableau cohérent à l'œil et un chiffre de marge globale faux dans tous les rapports de l'entreprise. La cohérence visuelle n'est pas un critère de justesse, et c'est pourtant l'argument qui emporte la décision neuf fois sur dix.</p>
"""},

  {"titre": "Automatiser un rapport hebdomadaire", "niveau": "Intermédiaire",
   "enonce": [
     "Chaque lundi, vous recevez par courriel un export CSV de l'activité de la semaine, toujours le même format. Vous devez produire un rapport de quatre indicateurs par équipe et l'envoyer à midi. L'opération vous prend actuellement une heure et quart.",
     "Concevez le dispositif automatisé. Précisez la structure des dossiers, les requêtes, les contrôles, et ce qui se passe la semaine où l'export arrive avec un jour de retard ou dans un format légèrement modifié.",
   ],
   "corrige": """
<p><strong>Le principe : rendre l'exécution hebdomadaire aussi mécanique que possible, et rendre les anomalies bruyantes.</strong> Une tâche hebdomadaire a une particularité : elle est faite dans l'urgence, souvent par quelqu'un d'autre en cas d'absence. Tout ce qui demande du jugement au moment de l'exécution finira par être fait de travers.</p>
<p><strong>1. La structure des dossiers.</strong> Un dossier <code>entrees/</code> où l'on dépose l'export de la semaine, toujours sous le même nom — <code>activite_semaine.csv</code>. Un dossier <code>archives/</code> où l'on déplace l'export de la semaine précédente, renommé <code>activite_AAAA-Snn.csv</code>. Un classeur <code>rapport.xlsx</code>. Un dossier <code>livrables/</code>.</p>
<p><em>Pourquoi un nom fixe dans entrees/ plutôt que la lecture d'un dossier :</em> avec un nom fixe, la requête pointe vers un chemin unique et ne peut pas se tromper de fichier. Avec un dossier, deux exports oubliés ensemble seraient empilés silencieusement — accident classique et coûteux. Le nom fixe force à archiver, ce qui est aussi la bonne discipline.</p>
<p><strong>2. Les requêtes.</strong> Une requête <em>Import</em> qui lit le CSV, en précisant explicitement l'encodage et le séparateur plutôt qu'en laissant Power Query deviner — un CSV français mal détecté produit une seule colonne, ou pire, des montants décalés d'un facteur mille selon le séparateur décimal.</p>
<p>Étapes : supprimer l'étape de typage automatique, promouvoir les en-têtes, filtrer les lignes vides, normaliser le nom d'équipe par table de correspondance, typer explicitement, ajouter une colonne de date de semaine calculée depuis la date de l'enregistrement.</p>
<p>Une requête <em>Historique</em> qui lit le dossier archives/ et empile les semaines précédentes : elle permet les comparaisons hebdomadaires, qui sont ce qui donne du sens aux quatre indicateurs. Un chiffre sans sa semaine précédente n'est pas interprétable.</p>
<p><strong>3. Les indicateurs.</strong> Un TCD par équipe sur la table courante, un second sur l'historique pour la tendance sur huit semaines. Les quatre indicateurs sont extraits en cellules figées par <code>LIREDONNEESTABCROISDYNAMIQUE</code>, dans un onglet Rapport mis en forme et destiné à l'envoi. Le TCD lui-même n'est jamais diffusé : un destinataire qui déplace un champ casse la mise en page et vous appelle.</p>
<p><strong>4. Les contrôles, calibrés sur ce qui peut réellement mal tourner.</strong></p>
<p><em>Le fichier lu est-il bien celui de cette semaine ?</em> Contrôle de la plage de dates de l'export contre la semaine attendue. C'est le contrôle le plus important : rejouer le rapport sur l'export de la semaine précédente est l'erreur la plus fréquente et la plus embarrassante, parce qu'elle produit un rapport parfaitement crédible.</p>
<p><em>Le volume est-il vraisemblable ?</em> Nombre de lignes comparé à la moyenne des huit dernières semaines, alerte au-delà de 30 % d'écart.</p>
<p><em>Toutes les équipes sont-elles présentes ?</em> Nombre d'équipes distinctes contre la valeur attendue. Une équipe absente de l'export ne produit pas d'erreur, elle produit une ligne manquante dans le rapport — que personne ne remarque.</p>
<p><em>Y a-t-il des valeurs nouvelles non normalisées ?</em> Une équipe renommée à la source apparaîtrait comme une équipe supplémentaire.</p>
<p><strong>5. La procédure du lundi, en cinq lignes dans le Lisez-moi.</strong> Archiver l'export précédent ; déposer le nouveau sous le nom fixe ; ouvrir le classeur et Actualiser tout ; lire l'onglet Contrôles, quatre lignes qui doivent afficher OK ; exporter l'onglet Rapport en PDF dans livrables/ et l'envoyer.</p>
<p>Quinze minutes au lieu de soixante-quinze, et exécutable par n'importe qui.</p>
<p><strong>6. La semaine où quelque chose change.</strong></p>
<p><em>L'export arrive avec un jour de retard.</em> Rien de technique à faire. Ce qui compte est la conduite à tenir, et elle doit être écrite : n'exécutez pas le rapport sur le fichier de la semaine précédente pour « avoir quelque chose ». Envoyez un message court disant que l'export est en retard et annonçant l'heure de diffusion. Un rapport en retard est un incident mineur ; un rapport faux diffusé à l'heure est un incident majeur, et il reste dans les mémoires.</p>
<p><em>Une colonne est renommée à la source.</em> La requête échoue avec un message nommant la colonne manquante. Bonne nouvelle : l'erreur est bruyante. Correction en deux minutes dans l'étape concernée. Notez le changement dans l'historique du Lisez-moi — si la source change ses en-têtes une fois, elle le refera.</p>
<p><em>Une colonne est ajoutée.</em> Sans effet, à condition d'avoir utilisé « Supprimer les autres colonnes ». C'est ici que ce choix montre sa valeur.</p>
<p><em>Le séparateur décimal change.</em> Le cas vicieux : la requête ne plante pas, les montants sont divisés ou multipliés par mille, et le rapport reste plausible si l'ordre de grandeur est mal connu. C'est exactement ce que le contrôle de volume attrape, et c'est la raison pour laquelle il porte sur la somme et pas seulement sur le nombre de lignes.</p>
<p><strong>Le test du dispositif :</strong> faites-le exécuter par un collègue un lundi où vous êtes absent, sans intervenir. S'il y arrive, vous avez un processus. S'il vous appelle, vous avez une procédure incomplète — et sa question vous dit exactement quelle ligne manque au Lisez-moi.</p>
"""},

  {"titre": "Reprendre un fichier automatisé par quelqu'un d'autre", "niveau": "Avancé",
   "enonce": [
     "Vous héritez d'un classeur de reporting comportant neuf requêtes Power Query, dont les étapes portent les noms par défaut, six TCD, des liaisons vers trois classeurs externes, et un onglet de synthèse alimenté par des formules pointant vers les TCD. Le fichier fonctionne, mais personne ne sait exactement ce qu'il fait, et un chiffre est contesté par le contrôle de gestion.",
     "Décrivez votre démarche pour comprendre, vérifier et fiabiliser ce fichier, en sachant qu'il doit continuer à produire son rapport chaque mois pendant votre travail.",
   ],
   "corrige": """
<p><strong>Point de départ : un chiffre contesté est une chance.</strong> Il vous donne un point d'entrée précis et un mandat. Ne commencez pas par un audit général — vous vous noieriez dans neuf requêtes — mais par la remontée de ce chiffre unique jusqu'à sa source. Le reste de la compréhension viendra en chemin, et il viendra dans le bon ordre.</p>
<p><strong>Phase 1 — remonter la chaîne du chiffre contesté.</strong></p>
<p>Partez de la cellule de synthèse. Formules &gt; Repérer les antécédents vous donne le TCD qui l'alimente. Le TCD vous donne sa table source, dans l'onglet Sources de données du volet des champs. La table vous donne la requête. La requête vous donne ses étapes.</p>
<p>Documentez cette chaîne au fur et à mesure sur une feuille de papier. Elle vous servira de squelette pour tout le reste, et vous constaterez que les huit autres requêtes s'y rattachent presque toutes.</p>
<p>Ouvrez ensuite la requête et parcourez ses étapes <strong>une par une, en cliquant sur chacune</strong> pour voir l'état des données. C'est la fonctionnalité décisive de Power Query pour la reprise d'un travail existant : vous voyez la transformation s'opérer, sans avoir à lire de code. Trente à quarante minutes pour une requête de vingt étapes, et vous en ressortez avec une compréhension complète.</p>
<p>Renommez chaque étape en français au fur et à mesure de votre lecture. Vous documentez sans effort supplémentaire, et vous vous forcez à comprendre chaque étape puisqu'il faut la nommer. Une étape que vous n'arrivez pas à nommer est une étape que vous n'avez pas comprise — et c'est très souvent là qu'est le problème.</p>
<p><strong>Phase 2 — trouver l'écart.</strong></p>
<p>Recalculez le chiffre contesté indépendamment, sur les données brutes, par vos propres moyens. Comparez. Trois issues, et il faut les traiter différemment.</p>
<p><em>Les deux chiffres coïncident :</em> le fichier a raison, et la contestation vient d'une divergence de définition avec le contrôle de gestion — périmètre, période, retraitements. C'est le cas le plus fréquent et le plus facile à résoudre : organisez une confrontation des deux définitions, écrites, et l'une des deux sera retenue. Le fichier n'est pas en cause.</p>
<p><em>Les chiffres diffèrent et vous identifiez l'étape responsable :</em> corrigez, mesurez l'impact sur l'historique, et annoncez comme au module 2 — factuel, chiffré, correction déjà faite.</p>
<p><em>Les chiffres diffèrent et vous ne trouvez pas pourquoi :</em> le cas le plus instructif. Procédez par bissection. Comparez les résultats intermédiaires étape par étape entre votre calcul et la requête : nombre de lignes après le filtrage, somme après la jointure, nombre de lignes après la déduplication. L'écart apparaît à une étape précise, et cette étape est votre réponse. Les trois suspects habituels, dans l'ordre : une jointure interne qui a silencieusement supprimé des lignes non appariées, un filtre trop large écrit il y a deux ans, une déduplication qui a gardé la mauvaise ligne.</p>
<p><strong>Phase 3 — les risques structurels, une fois le chiffre réglé.</strong></p>
<p>Vous avez maintenant la légitimité pour aller plus loin. Trois vérifications, par ordre de gravité.</p>
<p><em>Les liaisons externes.</em> Données &gt; Modifier les liens. Pour chacun des trois classeurs : existe-t-il toujours, à ce chemin, et qui le maintient ? Un lien vers un fichier disparu renvoie la dernière valeur connue, figée, sans aucun signal — le risque le plus dangereux d'un classeur hérité, parce qu'il produit des chiffres périmés et plausibles. Vérifiez la date de dernière modification de chaque classeur lié : un fichier source non modifié depuis huit mois dans un rapport mensuel est une alerte.</p>
<p><em>Les jointures.</em> Dans chaque fusion, le type de jointure. Une jointure interne supprime les lignes non appariées sans rien dire. Si vous en trouvez une, ajoutez immédiatement une requête en jointure anti pour mesurer ce qui disparaît : c'est souvent la découverte principale d'une reprise de fichier.</p>
<p><em>Les TCD.</em> Pour chacun : sa source est-elle bien une table de requête ou une plage figée ? Son grand total correspond-il à une somme directe ? Les regroupements de dates cochent-ils l'année ?</p>
<p><strong>Phase 4 — fiabiliser sans réécrire.</strong></p>
<p>La tentation est de tout reconstruire proprement. Résistez : le fichier tourne, et un fichier neuf qui tourne mal une seule fois vous coûtera toute la confiance acquise.</p>
<p>Ajoutez plutôt une couche de sécurité par-dessus l'existant. Un onglet Contrôles avec six vérifications, dont l'écart entre chaque TCD et sa source. Un onglet Lisez-moi avec la chaîne que vous avez documentée en phase 1. Les étapes renommées, déjà faites. Une requête anti par jointure, chargée en contrôle.</p>
<p>Ces quatre ajouts ne changent aucun chiffre, ils rendent le fichier lisible et surveillé. C'est 80 % du bénéfice pour 20 % du risque, et cela peut se faire sans interrompre la production mensuelle.</p>
<p><strong>Phase 5 — ce qu'il faut réécrire, et quand.</strong> Ne réécrivez que ce qui remplit deux conditions : c'est démontré fragile, et vous avez un mois sans échéance devant vous. Une requête dont vous avez prouvé qu'elle perd des lignes mérite d'être refaite ; une requête laide mais juste ne le mérite pas. « Je ne comprends pas ce que ça fait » n'est pas une raison de réécrire — c'est une raison de continuer à lire.</p>
<p><strong>Ce que vous ne saurez jamais complètement.</strong> Un fichier hérité contient toujours des décisions dont la raison est perdue : un filtre qui exclut trois clients, une correction manuelle appliquée à une région. Ne les supprimez pas parce qu'elles vous paraissent injustifiées. Listez-les dans le Lisez-moi sous un titre « décisions dont l'origine est inconnue », et posez la question à la personne la plus ancienne du service. Vous obtiendrez la réponse pour la moitié d'entre elles, et pour l'autre moitié, vous aurez au moins rendu visible ce qui était invisible — ce qui est déjà considérable.</p>
"""},
 ],

 "ressources": [
   "<strong>Support Microsoft — « Créer un tableau croisé dynamique »</strong> et la page sur les options de calcul du champ de valeurs : la liste complète des modes d'affichage, dont plusieurs sont peu connus et très utiles (différence par rapport à, % du parent, cumul).",
   "<strong>L'éditeur avancé de Power Query</strong> (Accueil &gt; Éditeur avancé) affiche le code M généré par vos clics. Vous n'avez pas besoin de l'écrire, mais le lire une fois montre que chaque étape est une ligne, et rend la logique des requêtes beaucoup plus claire.",
   "<strong>Le module 1 de cette formation</strong> — Power Query automatise les sept opérations de nettoyage vues au module 1, mais il ne dispense pas de les comprendre : une requête reproduit fidèlement une méthode fausse.",
   "<strong>Le module 4 de cette formation</strong> — la couche de présentation qui s'appuie sur les TCD construits ici, et les contrôles qui empêchent de diffuser un chiffre faux.",
 ],
}

QUIZ["excel-analyse-donnees/module-3"] = {
 "module_id": "formation-excel-analyse-donnees-module-3",
 "version": "2.0", "last_verified": "2026-09-04",
 "questions": [
  {"id":"q1","question":"Un TCD affiche 11 990 comme grand total au lieu du chiffre d'affaires attendu. Que vous dit-il ?",
   "choices":[{"key":"a","text":"Que la plage source est trop grande et inclut des lignes vides"},
              {"key":"b","text":"Que le TCD n'a pas été actualisé depuis le dernier ajout de données"},
              {"key":"c","text":"Qu'il compte au lieu de sommer, donc que la colonne contient au moins une valeur non numérique"}],
   "correct_answer":"c","feedback":"Excel bascule en comptage dès qu'une cellule texte est présente. Ne corrigez pas seulement l'affichage : allez traiter le typage à la source."},
  {"id":"q2","question":"Pourquoi ne faut-il jamais créer un champ calculé multipliant deux champs entre eux ?",
   "choices":[{"key":"a","text":"Parce que les champs calculés ralentissent excessivement l'actualisation"},
              {"key":"b","text":"Parce qu'Excel limite les champs calculés à une seule opération"},
              {"key":"c","text":"Parce qu'un champ calculé opère sur les totaux agrégés : il multiplierait la somme des prix par la somme des quantités"}],
   "correct_answer":"c","feedback":"Agréger puis diviser est correct, agréger puis multiplier ne l'est presque jamais. Le produit se calcule en colonne de la table source."},
  {"id":"q3","question":"Quel piège comporte le regroupement automatique d'une colonne de dates par mois ?",
   "choices":[{"key":"a","text":"Sans cocher Années, il agrège tous les mois de janvier de toutes les années ensemble"},
              {"key":"b","text":"Il convertit les dates en texte et casse les tris"},
              {"key":"c","text":"Il exclut automatiquement les mois sans aucune donnée"}],
   "correct_answer":"a","feedback":"Invisible sur une seule année, le problème double silencieusement tous les chiffres le jour où l'on ajoute l'année précédente."},
  {"id":"q4","question":"Quelle opération de Power Query transforme un tableau à douze colonnes mensuelles en tableau analysable ?",
   "choices":[{"key":"a","text":"Fusionner les requêtes"},
              {"key":"b","text":"Dépivoter les colonnes"},
              {"key":"c","text":"Ajouter les requêtes"}],
   "correct_answer":"b","feedback":"Sélectionner les douze colonnes de mois puis Transformer > Dépivoter donne la structure longue en un clic. Probablement l'opération la plus utile de Power Query."},
  {"id":"q5","question":"Après avoir consolidé douze fichiers régionaux, quel contrôle faut-il poser en priorité ?",
   "choices":[{"key":"a","text":"Un regroupement par fichier source affichant nombre de lignes, somme et montant moyen"},
              {"key":"b","text":"Une vérification que le nombre total de lignes est un multiple de douze"},
              {"key":"c","text":"Un tri par date pour vérifier l'ordre chronologique"}],
   "correct_answer":"a","feedback":"C'est ce contrôle qui révèle qu'une région a exporté le mauvais mois, ou que ses montants sont en TTC quand les autres sont en HT."},
  {"id":"q6","question":"Où doit vivre une règle métier, comme un seuil de remise ?",
   "choices":[{"key":"a","text":"Dans une colonne conditionnelle de la requête Power Query, pour qu'elle soit automatisée"},
              {"key":"b","text":"Dans une colonne de formule visible dans la feuille, ou dans une table de paramètres"},
              {"key":"c","text":"Dans un champ calculé du tableau croisé dynamique"}],
   "correct_answer":"b","feedback":"Power Query pour la forme des données, les formules pour les règles métier : ce sont elles qui seront discutées en réunion, elles doivent rester visibles."},
 ]}

for k, m in M.items():
    w, full = build(k, m)
    print(f"{k:34s} cours: {w} mots | page: {full} mots")
for k, q in QUIZ.items():
    p = os.path.join("/tmp/out_v2", k, "quiz.json")
    os.makedirs(os.path.dirname(p), exist_ok=True)
    json.dump(q, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    open(p, "a", encoding="utf-8").write("\n")
    print(f"{k}: quiz {len(q['questions'])} questions")
