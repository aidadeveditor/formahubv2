#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Formahub — podcasts de la formation Excel et analyse de données appliquée.

  a = Camille, animatrice de la série ;
  b = Karim, analyste de données.

Quatre épisodes d'environ 9 minutes : structurer la donnée, les fonctions
qui font le travail, TCD et Power Query, puis le tableau de bord et les
contrôles.

Le sujet est technique : les épisodes portent sur les principes et les
pièges, pas sur la syntaxe — celle-ci se lit dans le module, elle ne
s'écoute pas. Les noms de fonctions ne sont cités que lorsqu'ils portent
une décision.

Usage :
    FH_OUT=<dossier formations> python3 _tooling/podcast_excel.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_podcasts as bp

HOSTS = {
    "a": {"nom": "Camille", "role": "animatrice"},
    "b": {"nom": "Karim", "role": "analyste de données"},
}

P = {}

# ============================================================
# Module 1 — Structurer une donnée exploitable
# ============================================================

P["excel-analyse-donnees/module-1"] = {
    "formation": "Excel et analyse de données appliquée",
    "titre": "Structurer une donnée exploitable",
    "module_id": "formation-excel-analyse-donnees-module-1",
    "hosts": HOSTS,
    "resume": "Douze mille quatre cents lignes, huit défauts et une réponse pour lundi : "
              "pourquoi la préparation est quatre-vingts pour cent du travail, et l'écart de dix pour cent qu'elle révèle.",
    "lignes": [
        ("a", "Premier module de la formation Excel. Karim, la scène est un vendredi quatorze heures et une demande pour lundi matin."),
        ("b", "Quelle catégorie de produits a le plus reculé sur le trimestre, et dans quelles régions. La réponse existe : elle est dans un fichier de douze mille quatre cents lignes que le service commercial vient d'envoyer. On l'ouvre, et là."),
        ("a", "Raconte."),
        ("b", "La première ligne est un titre étalé sur huit colonnes fusionnées. Les en-têtes sont en ligne quatre. La colonne Région contient « Sud-Ouest », « sud ouest » en minuscules, « S.O. » en initiales, et trois cent quarante cellules vides. Les montants sont alignés à gauche, ce qui veut dire qu'Excel les considère comme du texte. Des lignes « Total mensuel » sont intercalées tous les trente enregistrements. Et une colonne empile client, contact et téléphone séparés par des barres obliques."),
        ("a", "Deux options, dis-tu."),
        ("b", "La première, très tentante : commencer à filtrer et à faire des sommes tout de suite. Vous obtiendrez un chiffre lundi matin, et il sera faux. La seconde : consacrer deux heures à rendre le fichier analysable, et vingt minutes à répondre à la question."),
        ("a", "C'est la proportion que tu défends dans tout le module."),
        ("b", "Quatre-vingts pour cent de préparation, vingt pour cent d'analyse. Et j'ajoute une chose : celui qui vous répond en vingt minutes n'a pas été rapide, il a sauté la préparation. C'est utile à savoir quand on se compare à un collègue."),
        ("a", "Commençons par la distinction de fond du module."),
        ("b", "Un tableau lisible et un tableau exploitable sont deux objets différents. Le tableau lisible a des titres fusionnés, des sous-totaux, de la couleur — il est fait pour l'œil humain. Le tableau exploitable obéit à trois phrases : une ligne est une observation, une colonne est une variable, une cellule est une valeur."),
        ("a", "Et on ne peut pas avoir les deux ?"),
        ("b", "Pas dans le même onglet, et c'est l'erreur la plus tenace. La solution est de séparer trois onglets : les données brutes intactes, les données nettoyées, et la présentation construite par formules. Chacun fait bien une seule chose."),
        ("a", "Tu identifies cinq défauts qui rendent un fichier inanalysable."),
        ("b", "Les cellules fusionnées. Les valeurs multiples dans une même colonne. Les lignes de synthèse intercalées. Le mauvais typage — des nombres stockés en texte, des dates en texte. Et les en-têtes qui ne sont pas en première ligne. Ces cinq-là, et on a couvert l'immense majorité des cas."),
        ("a", "Tu recommandes un diagnostic d'ouverture. En combien de temps ?"),
        ("b", "Moins de deux minutes, six gestes. Contrôle-Fin, pour voir jusqu'où le fichier croit s'étendre. Regarder si le bouton Fusionner est actif. Vérifier l'alignement des colonnes numériques. Chercher le mot « Total ». Ouvrir le filtre sur chaque colonne de catégorie pour compter les modalités. Et regarder le minimum et le maximum des dates."),
        ("a", "Et à quoi ça sert, concrètement ?"),
        ("b", "À annoncer un délai honnête avant de s'engager, pas après. Dans l'étude de cas, la phrase dite à la direction est « réponse lundi matin, pas vendredi soir ». C'est le premier livrable, et il vaut mieux qu'un chiffre faux dans l'heure."),
        ("a", "Tu as une phrase forte sur les erreurs."),
        ("b", "Les erreurs graves sont celles qui restent plausibles. Un chiffre qui double, ça se voit et quelqu'un le signale. Un écart de six pour cent uniformément réparti ne se voit jamais, il circule, et on décide dessus pendant deux ans."),
        ("a", "Reprenons l'étude de cas, minutée."),
        ("b", "Minutes zéro à cinq, le diagnostic. Contrôle-Fin renvoie très au-delà des données réelles : le fichier traîne des colonnes et des lignes fantômes. Quatre colonnes numériques alignées à gauche. Quatre cent dix occurrences du mot « Total ». Onze modalités dans la colonne Région pour six régions réelles. Les cinq défauts sont là."),
        ("a", "Ensuite la structure."),
        ("b", "On supprime les trois premières lignes pour ramener les en-têtes en ligne un. Et surtout, on supprime les colonnes et lignes fantômes — on les supprime, on ne les efface pas. L'effacement laisse la structure en place et continue de fausser la détection de plage."),
        ("a", "Puis les lignes de total."),
        ("b", "Filtre sur « Total mensuel », suppression des quatre cent dix lignes, et contrôle du compte : douze mille quatre cents moins quatre cent dix égale onze mille neuf cent quatre-vingt-dix. Le compte tombe juste, donc aucune ligne utile n'a été emportée. Ce contrôle prend cinq secondes et il évite de découvrir la perte trois semaines plus tard."),
        ("a", "Et le moment le plus instructif ?"),
        ("b", "Le typage. On convertit les quatre colonnes numériques avec le bon séparateur décimal. La somme des montants passe de trois millions neuf cent cinquante mille à quatre millions quatre cent deux mille euros."),
        ("a", "Quatre cent cinquante-deux mille euros d'écart."),
        ("b", "Qui correspondent aux mille trois cent quatre-vingts cellules stockées en texte, qui comptaient pour zéro. Sans cette conversion, l'analyse aurait sous-estimé le chiffre d'affaires de dix pour cent, uniformément réparti, donc invisible. C'est exactement le type d'erreur dont je parlais."),
        ("a", "Un montant aligné à gauche, donc."),
        ("b", "C'est du texte, et il compte pour zéro dans toute somme. C'est le réflexe le plus rentable de la formation : regarder l'alignement avant de sommer."),
        ("a", "Et les catégories ?"),
        ("b", "Onze modalités de région ramenées à six, plus une septième pour les vides — après vérification du pays de livraison, ce sont des exports. Le principe général : un vide a presque toujours un sens, comprenez-le avant de le remplir ou de l'écarter. Le remplir par zéro ou par la valeur du dessus sans vérifier est une façon rapide de fabriquer des données fausses."),
        ("a", "Sur la façon de corriger, tu as une règle."),
        ("b", "Toute correction manuelle est perdue. Au-delà de dix répétitions, il faut une règle, pas un geste. Une table de correspondance qui traduit les onze écritures en six régions se rejoue le mois prochain ; deux cents corrections à la main, non."),
        ("a", "Et l'ordre des opérations compte ?"),
        ("b", "Il n'est pas arbitraire. Défusionner, supprimer les synthèses, normaliser les espaces, corriger les variantes, convertir les types, séparer les colonnes multiples, dédoublonner. Dans un autre ordre, chaque étape défait la précédente."),
        ("a", "Un mot sur le dédoublonnage."),
        ("b", "Ne cliquez jamais sur « Supprimer les doublons » avant d'avoir compté et qualifié ce qui est en double. Deux lignes identiques peuvent être une double saisie, ou deux commandes réelles du même client le même jour. L'outil ne fait pas la différence, vous si."),
        ("a", "Et le réflexe de mise en forme qui compte ?"),
        ("b", "Contrôle-L après le nettoyage, systématiquement, pour convertir la plage en tableau structuré, avec un nom explicite. Les plages s'étendent alors toutes seules quand des lignes arrivent, et les formules se relisent parce qu'elles portent des noms de colonnes au lieu de coordonnées."),
        ("a", "Dernier point : la reproductibilité."),
        ("b", "Le journal de transformation. Six lignes, cinq minutes : ce qu'on a fait, dans quel ordre, avec quel arbitrage. Il rend l'analyse reproductible le mois prochain, défendable si on la conteste, et transmissible si vous n'êtes pas là."),
        ("a", "Et les chiffres de contrôle ?"),
        ("b", "Quatre, relevés avant et après : le nombre de lignes, la somme principale, le nombre de modalités distinctes, et la plage de dates. Ce sont eux qui vous disent qu'un nettoyage a mal tourné — sinon vous ne le sauriez jamais."),
        ("a", "Et le nettoyage se fait sur une copie."),
        ("b", "Toujours. Sans source intacte, plus rien n'est vérifiable, et le jour où quelqu'un conteste un chiffre vous n'avez aucun moyen de remonter."),
        ("a", "Ce qu'on fait demain ?"),
        ("b", "Prenez le fichier que vous utilisez le plus souvent et faites-lui le diagnostic en six gestes. Deux minutes. Regardez en particulier l'alignement de vos colonnes de montants — c'est là que se cachent les dix pour cent."),
        ("a", "Au module 2, les fonctions. Merci Karim."),
    ],
}

# ============================================================
# Module 2 — Les fonctions qui font le travail
# ============================================================

P["excel-analyse-donnees/module-2"] = {
    "formation": "Excel et analyse de données appliquée",
    "titre": "Les fonctions qui font réellement le travail",
    "module_id": "formation-excel-analyse-donnees-module-2",
    "hosts": HOSTS,
    "resume": "Mille huit cents erreurs visibles et trois cents lignes fausses sans le moindre signal : "
              "pourquoi la non-correspondance est la partie la plus informative d'un rapprochement.",
    "lignes": [
        ("a", "Module 2. Le fichier est propre, et on demande la marge par catégorie. Le prix de vente est dans la table de commandes, le prix d'achat dans un référentiel envoyé par les achats."),
        ("b", "On écrit une recherche pour ramener le prix d'achat à côté de chaque commande. Résultat : mille huit cents lignes sur onze mille neuf cent quatre-vingt-dix affichent une erreur. Le réflexe immédiat, c'est de les masquer avec une fonction de gestion d'erreur pour « nettoyer » l'affichage."),
        ("a", "Et ce serait la pire décision."),
        ("b", "Parce que trois choses différentes se cachent derrière ces mille huit cents erreurs. Des références réellement absentes du référentiel. Des références présentes mais écrites différemment. Et une plage de recherche qui s'est décalée à la recopie."),
        ("a", "Et il y a pire."),
        ("b", "Parmi les dix mille cent quatre-vingt-dix lignes sans erreur, environ trois cents ont ramené le prix d'achat du mauvais produit. Sans le moindre signal. C'est ça, le vrai sujet du module : les erreurs visibles sont les gentilles."),
        ("a", "Commençons par les références, que tu appelles la source silencieuse des tableaux faux."),
        ("b", "Une formule ne contient pas des cellules, elle contient des chemins vers des cellules. Le mode de référence — relatif, absolu, mixte — décide de ce qui se passe quand vous recopiez. Et la touche F4, qui bascule d'un mode à l'autre, est le raccourci au meilleur rendement de tout Excel."),
        ("a", "Le décalage silencieux, c'est quoi ?"),
        ("b", "Vous recopiez une formule vers le bas, la plage de recherche descend avec elle, et à la deux centième ligne elle ne couvre plus le début du référentiel. Les résultats restent plausibles. Le contrôle qui l'attrape : vérifier la dernière ligne d'une colonne recopiée, pas seulement la première. Presque personne ne le fait."),
        ("a", "Et la solution de fond ?"),
        ("b", "Les références de tableau structuré, celles qui portent des noms de colonnes. Elles ne suppriment pas le risque, elles suppriment le problème : il n'y a plus rien à figer."),
        ("a", "Passons au rapprochement de deux tables. Quelle fonction ?"),
        ("b", "RECHERCHEX si votre version le permet, sinon INDEX et EQUIV combinés. RECHERCHEV, jamais — et pour une raison précise : sans son quatrième argument, elle active la recherche approximative et vous renvoie le prix du produit d'à côté, sans aucun signal. C'est très exactement la source des trois cents lignes fausses de la mise en situation."),
        ("a", "Mais tu dis que la fonction n'est pas le vrai sujet."),
        ("b", "Le vrai sujet, c'est la non-correspondance. Et avant même de rapprocher, il y a un contrôle à faire : l'unicité de la clé du référentiel."),
        ("a", "C'est-à-dire ?"),
        ("b", "Vérifier qu'un code produit n'apparaît qu'une fois dans le référentiel. Dans le cas, il apparaît jusqu'à trois fois : quatorze produits y figurent en double ou en triple, avec des prix d'achat différents correspondant à des dates d'application successives. Sans ce contrôle, la recherche prend la première occurrence, arbitrairement, et personne ne le sait."),
        ("a", "Comment on tranche ?"),
        ("b", "Avec les achats, pas tout seul. Décision prise : on retient le prix le plus récent, on garde les autres dans un onglet d'historique, et on note l'arbitrage au journal. Ce n'est pas une décision technique, c'est une décision métier — et c'est pour ça qu'elle s'écrit."),
        ("a", "Ensuite, on mesure."),
        ("b", "Mille huit cents lignes non rapprochées, soit quinze pour cent des lignes et onze virgule trois pour cent du chiffre d'affaires. Et l'écart entre ces deux pourcentages est déjà une information."),
        ("a", "Qu'est-ce qu'il dit ?"),
        ("b", "Que les lignes non rapprochées portent des montants inférieurs à la moyenne. Ça oriente vers des produits d'entrée de gamme plutôt que vers un incident aléatoire. Deux chiffres, et l'hypothèse est déjà bien avancée."),
        ("a", "Puis on classe."),
        ("b", "On extrait les références distinctes non trouvées — deux cent quatorze codes — et on les lit. Trois familles apparaissent en quelques minutes : des espaces en fin de code, des zéros initiaux perdus par le format, et des produits réellement déréférencés."),
        ("a", "Comment on confirme chaque hypothèse ?"),
        ("b", "Toujours de la même façon : on applique la transformation candidate et on compte combien de correspondances elle rétablit. Supprimer les espaces récupère quatre-vingt-neuf codes. Remettre les zéros initiaux en récupère quatre-vingt-dix-huit. Les vingt-sept restants ne répondent à aucune transformation : ce sont les vrais déréférencés."),
        ("a", "C'est une démarche presque expérimentale."),
        ("b", "C'est ça qui rend le résultat solide. Et une règle générale en sort : un taux de non-correspondance au-delà de deux pour cent signale un problème de format ou de périmètre, pas des cas isolés. En dessous, on traite au cas par cas ; au-dessus, on cherche une cause commune."),
        ("a", "Un point de méthode sur la normalisation des clés."),
        ("b", "Elle se fait dans une colonne dédiée, jamais à l'intérieur de la formule de recherche. Parce qu'une colonne se vérifie ligne à ligne, alors qu'une transformation cachée dans une formule est invisible et se propage silencieusement."),
        ("a", "Venons-en à la gestion d'erreur, puisqu'on a commencé par là."),
        ("b", "SIERREUR ne doit jamais transformer une donnée manquante en zéro ou en vide. Zéro n'est pas l'absence de valeur : zéro entre dans les sommes et tire les moyennes vers le bas. Une donnée manquante doit rester visible, et être comptée."),
        ("a", "Et donc ?"),
        ("b", "Affichez le taux de couverture à côté de tout total calculé sur des données incomplètes. « Marge moyenne de vingt-deux pour cent, calculée sur quatre-vingt-cinq pour cent du chiffre d'affaires » est une phrase honnête. « Marge de vingt-deux pour cent » toute seule ne l'est pas."),
        ("a", "Parlons des calculs conditionnels."),
        ("b", "Deux pièges. Le premier : un compte conditionnel qui renvoie zéro sur des valeurs pourtant visibles a presque toujours pour cause un espace de fin ou une différence de type. Le second concerne les dates : la borne haute d'une période s'écrit en strictement inférieur au jour suivant, sinon les lignes horodatées du dernier jour disparaissent silencieusement."),
        ("a", "Les dates, encore."),
        ("b", "C'est la première fabrique de résultats faux. Et pour regrouper par mois, créez une vraie date au premier du mois plutôt qu'un libellé texte — sinon le tri met août avant avril, par ordre alphabétique, et le graphique est absurde."),
        ("a", "Un mot sur les formules de décision."),
        ("b", "Une cascade de plus de trois conditions imbriquées se remplace par une table de correspondance. La règle devient visible, modifiable par quelqu'un d'autre, et discutable en réunion. Une formule de deux cents caractères, non."),
        ("a", "Et les seuils ?"),
        ("b", "Aucun seuil en dur dans une formule. Un seuil vit dans une cellule nommée. Sinon aucune analyse de sensibilité n'est possible, et le jour où la direction demande « et si on montait le seuil à quinze pour cent ? », vous repartez pour une heure."),
        ("a", "Un principe général pour finir ?"),
        ("b", "Créer une colonne intermédiaire vaut presque toujours mieux qu'une formule ingénieuse. La colonne se vérifie ligne à ligne, la formule ingénieuse se vérifie en la refaisant. Et personne ne la refait."),
        ("a", "Ce qu'on fait demain ?"),
        ("b", "Sur votre dernier rapprochement de tables, comptez les non-correspondances et calculez leur part du chiffre d'affaires. Si les deux pourcentages diffèrent nettement, vous tenez déjà une piste sur la nature du problème."),
        ("a", "Au module 3, on arrête de refaire le travail chaque mois. Merci Karim."),
    ],
}

# ============================================================
# Module 3 — TCD et Power Query
# ============================================================

P["excel-analyse-donnees/module-3"] = {
    "formation": "Excel et analyse de données appliquée",
    "titre": "Tableaux croisés dynamiques et Power Query",
    "module_id": "formation-excel-analyse-donnees-module-3",
    "hosts": HOSTS,
    "resume": "Un mois de travail par an passé à recopier des colonnes : "
              "comment consolider douze fichiers une fois et rejouer en un clic.",
    "lignes": [
        ("a", "Module 3. Le rapport mensuel prend trois heures, et ce mois-ci la demande change : consolidé sur les douze régions."),
        ("b", "Douze fichiers arrivent. Même structure — sauf que trois ont les colonnes dans un ordre différent, deux ont une colonne supplémentaire, et un a été exporté en montant TTC alors que les autres sont en hors taxes."),
        ("a", "Et le calcul du coût ?"),
        ("b", "Trois heures fois douze mois, plus une journée de consolidation par mois : un peu plus d'un mois de travail par an consacré à recopier des colonnes. C'est ce chiffre qui justifie le module, pas l'élégance de l'outil."),
        ("a", "Commençons par le tableau croisé dynamique. Qu'est-ce qu'il fait exactement ?"),
        ("b", "Il agrège une valeur selon des catégories. Sa force réelle n'est pas de calculer — une formule calcule aussi — c'est de permettre de changer la question sans rien réécrire. Vous glissez un champ, la question devient autre."),
        ("a", "Et il exige quelque chose."),
        ("b", "Des données rangées, celles du module 1. Un tableau croisé sur un fichier mal structuré produit des résultats faux avec un air de sérieux, ce qui est la pire combinaison."),
        ("a", "Un conseil de construction ?"),
        ("b", "Écrivez la question en français avant d'insérer le tableau. C'est elle qui détermine ce qui va en lignes, en colonnes et en valeurs. Et une règle de lisibilité : beaucoup de modalités en lignes, peu en colonnes. Un tableau à quarante colonnes ne se lit pas."),
        ("a", "Un contrôle systématique ?"),
        ("b", "Comparer le grand total du tableau croisé à une somme directe de la source. C'est le contrôle qui détecte tous les problèmes de périmètre — une plage figée qui ignore les nouvelles lignes, un filtre oublié, une modalité exclue."),
        ("a", "Justement, la plage figée."),
        ("b", "Un tableau croisé construit sur une plage fixe ignore silencieusement les lignes ajoutées le mois suivant. Sur un tableau structuré, il s'étend tout seul. C'est la raison la plus concrète du réflexe Contrôle-L du module 1."),
        ("a", "Quelles fonctionnalités du tableau croisé trompent ?"),
        ("b", "Trois. D'abord, un tableau qui affiche un nombre au lieu d'une somme vous signale que la colonne contient du texte — c'est un diagnostic gratuit, encore faut-il le lire comme tel."),
        ("a", "Ensuite ?"),
        ("b", "Le champ calculé. Il agrège d'abord, puis applique la formule. Agréger puis diviser est correct ; agréger puis multiplier ne l'est presque jamais. C'est ce qui produit des taux de marge à trois cent quarante pour cent qu'on retrouve dans un rapport. Les produits se calculent en colonne de source, pas dans le tableau croisé."),
        ("a", "Et la troisième ?"),
        ("b", "Le cache des modalités. Une valeur supprimée de la source survit dans les filtres du tableau croisé, parfois pendant des mois. Videz le cache avant de diffuser, sinon vos filtres proposent des régions qui n'existent plus."),
        ("a", "Un détail sur les dates ?"),
        ("b", "Regroupez par Mois et Années ensemble, jamais par Mois seul — sinon janvier 2025 et janvier 2026 sont additionnés, et le total est juste au sens arithmétique et faux au sens de la question."),
        ("a", "Passons à Power Query. Comment tu le présentes en une phrase ?"),
        ("b", "Préparer une fois, rejouer indéfiniment. Vous enregistrez la suite des transformations, et le mois suivant vous cliquez sur Actualiser. Le critère de décision est simple : une opération récurrente relève de Power Query, quelle que soit sa simplicité."),
        ("a", "Reprenons l'étude de cas : douze fichiers."),
        ("b", "Étape un, et c'est celle qu'on saute : inspecter avant de consolider. Ouvrir les douze fichiers et relever pour chacun le nombre de lignes, les en-têtes, la présence de lignes de total, le format des dates. Une demi-heure, et elle évite trois jours de débogage."),
        ("a", "Le constat ?"),
        ("b", "Neuf fichiers identiques, deux avec une colonne « Commentaire » en plus, et un — la région Est — en montant TTC avec des dates au format américain. Ce dernier est la vraie difficulté, et il vaut mieux le savoir maintenant que de le découvrir dans un chiffre aberrant."),
        ("a", "Et là tu fais quelque chose d'inattendu."),
        ("b", "Un appel téléphonique. Avant de coder quoi que ce soit : est-ce que la région Est peut exporter en hors taxes comme les autres ? Réponse : oui, c'était un paramètre de leur outil, corrigé pour le mois prochain. Cinq minutes."),
        ("a", "Contre quoi ?"),
        ("b", "Contre une correction permanente dans la requête, qui serait devenue fausse dès le mois suivant — une fois leur export corrigé — sans que personne ne s'en souvienne. C'est le genre de bombe à retardement qu'on pose de bonne foi."),
        ("a", "Et pour le mois en cours ?"),
        ("b", "On traite ce fichier à part, et on le documente. Un correctif temporaire assumé et daté vaut infiniment mieux qu'un correctif permanent oublié."),
        ("a", "Comment on organise les sources ?"),
        ("b", "Un dossier par période, contenant exclusivement les douze fichiers, nommés avec la région et la période. Rien d'autre dans le dossier. Le nommage rend la colonne de fichier source directement exploitable, et le tri chronologiquement correct."),
        ("a", "La requête, ensuite."),
        ("b", "On combine, et le premier geste est de supprimer l'étape « Type modifié » que Power Query ajoute automatiquement. Elle fige les types sur ce qu'il a vu au moment de la création, et elle casse à la première donnée qui sort du cadre. On retype explicitement en fin de requête."),
        ("a", "Les autres étapes ?"),
        ("b", "Retirer les lignes de titre, promouvoir les en-têtes, filtrer les lignes de total, extraire la région depuis le nom de fichier, et conserver les colonnes utiles. Un détail qui compte : préférez « Supprimer les autres colonnes » à « Supprimer les colonnes ». La première résiste à un ajout de colonne à la source, la seconde échoue."),
        ("a", "Et le nommage des étapes ?"),
        ("b", "Renommez-les en français. Une requête bien nommée est sa propre documentation — et dans six mois, c'est vous le lecteur étranger."),
        ("a", "Un contrôle après consolidation ?"),
        ("b", "Un regroupement par fichier source : nombre de lignes, somme, moyenne. C'est ce qui attrape le fichier importé deux fois ou celui qui manque. Et conservez toujours la colonne de fichier source : c'est elle qui permet de retrouver d'où vient une ligne suspecte."),
        ("a", "Résultat ?"),
        ("b", "Trois heures devenues huit minutes. Et une journée de consolidation mensuelle supprimée."),
        ("a", "Il y a un enthousiasme dont tu mets en garde."),
        ("b", "Tout basculer dans Power Query. Laissez les règles métier en formules visibles, dans la feuille, où quelqu'un peut les lire et les contester. Réservez Power Query à la forme des données. Une règle de marge enfouie dans une étape de requête est invisible pour tout le monde, y compris pour vous."),
        ("a", "Et un fichier automatisé, c'est sans risque ?"),
        ("b", "Au contraire, et c'est le point le plus important du module. Un fichier automatisé continue de produire des résultats quand quelque chose a changé. Il ne se plaint pas. D'où l'onglet Contrôles, qui remplace l'alerte que l'outil ne donnera jamais."),
        ("a", "Une phrase à retenir ?"),
        ("b", "Automatiser libère le temps nécessaire à la vérification — encore faut-il l'employer à cela. Sinon on a juste rendu l'erreur plus rapide."),
        ("a", "Ce qu'on fait demain ?"),
        ("b", "Chronométrez votre rapport récurrent, et listez les manipulations que vous refaites à l'identique chaque mois. Celles-là, et uniquement celles-là, relèvent de Power Query."),
        ("a", "Au module 4, on passe au tableau de bord. Merci Karim."),
    ],
}

# ============================================================
# Module 4 — Du tableau au tableau de bord
# ============================================================

P["excel-analyse-donnees/module-4"] = {
    "formation": "Excel et analyse de données appliquée",
    "titre": "Du tableau au tableau de bord : représenter, contrôler, partager",
    "module_id": "formation-excel-analyse-donnees-module-4",
    "hosts": HOSTS,
    "resume": "Un chiffre juste que personne ne lit et un chiffre faux que personne ne détecte "
              "échouent de la même façon.",
    "lignes": [
        ("a", "Dernier module. Le rapport est automatisé : huit minutes le premier lundi du mois, quatre tableaux croisés justes, des contrôles qui s'évaluent seuls. Techniquement, c'est fait."),
        ("b", "Et deux choses disent que ça ne l'est pas. La première : en comité, personne n'ouvre le fichier. On vous demande de « dire l'essentiel », vous le dites de mémoire — donc quatre tableaux et une journée de construction ont produit un commentaire oral de deux minutes."),
        ("a", "Et la seconde ?"),
        ("b", "Plus sérieuse. Le mois dernier, un chiffre présenté s'est révélé faux : une région dont l'export avait été rejoué deux fois. Le contrôle existait, dans l'onglet Contrôles, en cellule B7. Personne ne l'avait regardé, vous compris, parce qu'il était huit heures moins le quart et que le fichier s'était toujours bien comporté."),
        ("a", "Les deux problèmes n'en font qu'un, dis-tu."),
        ("b", "Un chiffre juste que personne ne lit et un chiffre faux que personne ne détecte échouent exactement de la même façon. Il s'agit de rendre le résultat lisible et l'anomalie visible."),
        ("a", "Commençons par les graphiques. Comment on choisit ?"),
        ("b", "À partir de la question, jamais de l'esthétique. Une évolution dans le temps : une courbe. Une comparaison entre catégories : des barres horizontales triées. Une relation entre deux grandeurs : un nuage de points. Il n'y a pas trente cas."),
        ("a", "Et le titre ?"),
        ("b", "Il énonce la conclusion. « La marge recule sur le Sud-Ouest depuis mars », pas « Évolution de la marge par région ». Une étiquette descriptive laisse au lecteur un travail qu'il ne fera pas."),
        ("a", "Tu identifies six constructions qui trompent. Les principales ?"),
        ("b", "L'axe tronqué sur des barres : le lecteur y compare des longueurs, donc une barre doit partir de zéro. Le double axe, qui suggère une corrélation dont l'intensité dépend entièrement d'un choix d'échelle arbitraire — deux graphiques empilés disent la même chose honnêtement."),
        ("a", "Et sur les chiffres eux-mêmes ?"),
        ("b", "Une moyenne sans médiane, et un pourcentage sans effectif. Deux chiffres exacts et deux informations incomplètes. « Quarante pour cent de hausse » sur une base de cinq commandes ne veut rien dire, et il faut l'écrire."),
        ("a", "Tu as une formule là-dessus."),
        ("b", "Un graphique peut être entièrement exact et conduire à une conclusion fausse. Seule une habitude le détecte : demander systématiquement l'effectif, le périmètre et la dispersion. Trois questions, à chaque chiffre."),
        ("a", "Passons au tableau de bord. Par quoi on commence ?"),
        ("b", "Pas par les données disponibles. Par les décisions à prendre. Et dans l'étude de cas, ça commence par une conversation de vingt minutes avec le directeur commercial."),
        ("a", "Quelles questions ?"),
        ("b", "Deux. « Le mois dernier, après avoir eu ces chiffres, qu'avez-vous décidé ? » Réponse : rien de précis. Puis la vraie : « qu'auriez-vous aimé savoir et que vous n'aviez pas ? » Réponse : « où on perd, et si c'est en train de s'aggraver ou pas »."),
        ("a", "Et cette phrase suffit ?"),
        ("b", "C'est le cahier des charges complet. Elle contient une localisation — où — et une dynamique — ça s'aggrave ou pas. Les quatre tableaux croisés existants donnaient des niveaux, pas des variations : ils ne pouvaient structurellement pas répondre."),
        ("a", "Et l'arbitrage qui en découle ?"),
        ("b", "Il apparaît au brouillon papier, et c'est pour ça qu'on fait un brouillon papier. « Où on perd » demande une contribution à la variation, pas un pourcentage d'évolution. Une région qui baisse de trente pour cent mais pèse trois pour cent du chiffre d'affaires n'est pas le sujet ; une région qui baisse de six pour cent en pesant trente-cinq pour cent, si."),
        ("a", "Et on ne trouve pas ça en manipulant des champs."),
        ("b", "Jamais. C'est exactement le genre d'arbitrage qu'on ne fait pas quand on commence par construire. Vingt minutes de conversation et un brouillon à la main valent trois versions du fichier."),
        ("a", "Quelle structure pour la page ?"),
        ("b", "Trois bandes. En haut, quelques chiffres clés, chacun avec sa comparaison. Au centre, deux graphiques dont les titres sont des conclusions. En bas, un tableau de détail filtrable. Une page, une audience, une fréquence."),
        ("a", "Pourquoi le tableau de détail ?"),
        ("b", "Un chiffre sans accès aux enregistrements qui le composent ne permet aucune action. Quand le directeur voit que le Sud-Ouest décroche, la question suivante est « quels clients ? ». S'il ne peut pas descendre, il vous appelle, et le tableau de bord n'a servi à rien."),
        ("a", "Et quand on demande d'ajouter un bloc ?"),
        ("b", "Le nombre de blocs est fixe. Toute addition exige une suppression, et c'est au demandeur de choisir laquelle. C'est la seule règle qui empêche un tableau de bord de grossir jusqu'à l'illisible — parce que chaque demande est légitime prise isolément."),
        ("a", "Venons-en aux contrôles, et à l'incident du mois dernier."),
        ("b", "Le principe est simple à énoncer : un contrôle qui demande d'être consulté ne protège de rien. Il doit s'imposer à quelqu'un de pressé, à huit heures moins le quart."),
        ("a", "Concrètement ?"),
        ("b", "Un contrôle en échec bloque l'affichage. Le tableau de bord affiche un bandeau rouge à la place des chiffres, et il faut aller lever l'anomalie pour voir quoi que ce soit. Ce n'est pas de la sévérité gratuite : c'est la seule chose qui fonctionne."),
        ("a", "Comment on choisit les contrôles ?"),
        ("b", "Ils se déduisent des incidents passés, jamais d'une anticipation exhaustive. L'export rejoué deux fois a eu lieu : on ajoute un contrôle de doublon par fichier source. On ne cherche pas à imaginer tout ce qui pourrait arriver, on couvre ce qui est arrivé."),
        ("a", "Le contrôle le plus puissant ?"),
        ("b", "Recalculer chaque chiffre affiché par un second chemin indépendant. Si le total du tableau croisé et une somme directe divergent, quelque chose a bougé. Ça coûte une formule et ça attrape presque tout."),
        ("a", "Et avant de diffuser ?"),
        ("b", "Quatre questions. Est-ce vraisemblable ? Sur quelle population ? Qu'est-ce qui a changé depuis le mois dernier ? Et quelle question va-t-on me poser ? La dernière est la plus utile : elle vous fait préparer la réponse plutôt que la subir."),
        ("a", "Sur la diffusion elle-même ?"),
        ("b", "Diffusez le résultat en PDF daté, pas le moteur. Un fichier diffusé cesse de vous appartenir : il est modifié, renommé, renvoyé, et un jour quelqu'un présente une version de trois mois en croyant qu'elle est à jour."),
        ("a", "Dernière question : quand Excel n'est plus le bon outil ?"),
        ("b", "Cinq signaux. Le volume qui dépasse ce que le fichier supporte. Plusieurs personnes qui doivent écrire en même temps. Un besoin d'historisation — savoir ce que le chiffre disait il y a six mois. Une fréquence quotidienne. Et une criticité réglementaire, où il faut une piste d'audit."),
        ("a", "Et en dehors de ces cas ?"),
        ("b", "L'avantage décisif d'Excel reste qu'il est lisible et vérifiable par tout le monde. Migrer trop tôt vers un outil plus puissant, c'est échanger cette transparence contre une boîte noire que trois personnes savent ouvrir."),
        ("a", "Si on ne devait retenir qu'une chose de toute la formation ?"),
        ("b", "Les erreurs qui comptent sont silencieuses. La compétence centrale de l'analyse n'est pas la maîtrise des fonctions, c'est l'habitude du contrôle."),
        ("a", "Ce qu'on fait demain ?"),
        ("b", "Prenez votre dernier rapport et demandez à celui qui le reçoit ce qu'il a décidé après l'avoir lu. Si la réponse est « rien de précis », vous savez par où commencer — et ce n'est pas par une nouvelle courbe."),
        ("a", "Quatre modules, du fichier brut au tableau de bord. Merci Karim, et bravo à celles et ceux qui sont allés au bout."),
    ],
}


if __name__ == "__main__":
    out = os.environ.get("FH_OUT")
    if not out:
        out = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "formations")
    bp.set_out(out)
    for key in sorted(P):
        bp.build(key, P[key])
    bp.report()
