#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Formahub — podcasts de la formation Analytics et mesure de la performance.

  a = Camille, animatrice de la série ;
  b = Sofia, responsable analytics.

Quatre épisodes d'environ 9 minutes : cadrer la mesure, lire une audience,
analyser, restituer. Le fil narratif suit celui des modules — une même
entreprise, du budget d'acquisition au comité de direction.

Usage :
    FH_OUT=<dossier formations> python3 _tooling/podcast_analytics.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_podcasts as bp

HOSTS = {
    "a": {"nom": "Camille", "role": "animatrice"},
    "b": {"nom": "Sofia", "role": "responsable analytics"},
}

P = {}

# ============================================================
# Module 1 — Cadrer la mesure
# ============================================================

P["analytics-mesure/module-1"] = {
    "formation": "Analytics et mesure de la performance",
    "titre": "Cadrer la mesure : du besoin de décision au plan de marquage",
    "module_id": "formation-analytics-mesure-module-1",
    "hosts": HOSTS,
    "resume": "Avoir énormément de données et aucune réponse : pourquoi le test de la décision "
              "précède tout, et comment descendre d'une question métier jusqu'aux événements.",
    "lignes": [
        ("a", "Premier module de la formation Analytics. Sofia, la scène d'ouverture est une réunion budgétaire, et une question toute simple."),
        ("b", "« Nous avons dépensé cent quatre-vingt mille euros en acquisition l'an dernier. Qu'est-ce que cela a rapporté ? ». On ouvre l'outil d'analytics : quatre cent douze mille sessions, en hausse de dix-huit pour cent, un taux de rebond de cinquante-quatre pour cent, deux minutes quarante de durée moyenne, vingt-quatre sources de trafic."),
        ("a", "Et aucun de ces chiffres ne répond."),
        ("b", "Aucun. Ce n'est ni un problème d'outil ni un problème de compétence. L'outil enregistre consciencieusement ce qu'on lui a demandé d'enregistrer — c'est-à-dire ce qu'il propose par défaut. Personne n'a jamais écrit quelle décision cette mesure devait servir."),
        ("a", "Tu dis que c'est la cause première de l'inutilité de la plupart des dispositifs."),
        ("b", "Et elle est antérieure à toute question technique. Compter n'est pas mesurer. Un outil compte tout seul ; mesurer suppose d'avoir décidé à quoi ça sert."),
        ("a", "D'où le test de la décision. Explique-le."),
        ("b", "Pour chaque indicateur affiché, une question : si ce chiffre passait du simple au double, ou de moitié, qu'est-ce que je ferais différemment ? Si la réponse est « rien », l'indicateur est décoratif. On le retire."),
        ("a", "C'est brutal."),
        ("b", "C'est le seul filtre qui vaille. Et il y a une seule exception : deux ou trois indicateurs de cadrage, qu'on garde pour situer l'ordre de grandeur. Pas davantage, et ils ne se commentent pas en réunion."),
        ("a", "Une fois qu'on a gardé les bons, comment on les écrit ?"),
        ("b", "Un indicateur exploitable tient en une ligne et contient cinq éléments : la mesure, le segment, la période, la référence de comparaison, et le propriétaire. « Le taux de conversion » n'est pas un indicateur. « Coût par demande qualifiée, par canal, sur quatre-vingt-dix jours glissants, comparé au trimestre précédent, propriétaire le responsable acquisition » — ça, c'en est un."),
        ("a", "Pourquoi le propriétaire ?"),
        ("b", "Parce qu'un indicateur sans propriétaire n'est commenté par personne, et parce que la plupart des disputes de chiffres sont des disputes de définitions. C'est le document qui fait référence, pas l'outil. Quand deux personnes ne sont pas d'accord, on relit la ligne, pas l'écran."),
        ("a", "Tu as un avertissement sur les taux."),
        ("b", "N'affichez jamais un taux sans son numérateur. Un taux monte aussi quand le dénominateur baisse. Un taux de conversion qui progresse pendant que le trafic s'effondre est une mauvaise nouvelle présentée comme une bonne, et ça arrive tout le temps."),
        ("a", "Il y a une distinction entre indicateurs avancés et de résultat."),
        ("b", "L'indicateur de résultat, c'est le chiffre d'affaires, la demande signée — il arrive tard. L'indicateur avancé, c'est ce qui le précède : le nombre de devis envoyés, l'atteinte d'une page à valeur. Un dispositif sans indicateur avancé permet de constater, jamais de piloter, parce qu'au moment où le résultat bouge il est trop tard pour agir."),
        ("a", "Et il y a un piège sur les indicateurs avancés."),
        ("b", "Un indicateur avancé dont le lien avec le résultat n'a jamais été vérifié est une croyance, pas une mesure. On en hérite souvent : personne ne sait plus pourquoi on suit ce chiffre-là, et il est devenu vrai par habitude."),
        ("a", "Passons au plan de mesure. Comment on descend de la question aux événements ?"),
        ("b", "Toujours dans le même sens : question métier, décision, indicateur, données nécessaires, événements à collecter. Jamais l'inverse. Si vous partez des événements disponibles, vous reconstruisez le tableau de bord par défaut de l'outil, et vous avez fait un tour complet pour revenir au point de départ."),
        ("a", "Combien d'événements ?"),
        ("b", "Quinze à vingt-cinq. La contrainte de volume n'est pas une coquetterie : c'est ce qui garde le dispositif lisible dans deux ans, quand vous ne serez peut-être plus là. Tout marquer « au cas où » produit une centaine d'événements dont personne ne connaît la définition."),
        ("a", "Comment on distingue un événement d'une propriété ?"),
        ("b", "Ce qui varie est une propriété, pas un nom d'événement. Test très simple : si vous vous surprenez à additionner régulièrement plusieurs événements pour obtenir un chiffre, ils auraient dû n'en faire qu'un, avec une propriété qui les distingue."),
        ("a", "Et il y a une décision irréversible."),
        ("b", "Une propriété ne s'ajoute jamais rétroactivement. C'est la décision la moins réversible du dispositif : le jour où vous vous apercevez que l'événement ne porte pas la source, vous avez perdu tout l'historique. Cette anticipation vaut plus que n'importe quel raffinement technique."),
        ("a", "Et si on doit changer une définition ?"),
        ("b", "On ne redéfinit pas un événement. On en crée un nouveau, et on arrête l'ancien à une date connue, écrite dans un journal des modifications. Sinon vos courbes comparent deux choses différentes sans que rien ne le signale."),
        ("a", "Venons-en à ce qu'on n'aura jamais : le consentement, les bloqueurs."),
        ("b", "Une part des visiteurs refuse le suivi, une autre le bloque. Vous ne mesurez donc jamais la totalité. La règle qui en découle : les valeurs absolues sont fausses et le resteront ; les tendances et les comparaisons à collecte inchangée, elles, sont fiables — et elles suffisent à décider."),
        ("a", "Et le réflexe devant une chute brutale ?"),
        ("b", "On vérifie l'instrument avant d'interpréter le phénomène. Une chute de trafic de trente pour cent du jour au lendemain est presque toujours une balise cassée, pas un effondrement du marché. Le journal des modifications se consulte avant le tableau de bord."),
        ("a", "Reprenons l'étude de cas : les cent quatre-vingt mille euros."),
        ("b", "Étape une, et c'est la plus importante : reformuler la question en décision. On demande au directeur « selon la réponse, que ferez-vous ? ». Réponse : reconduire le budget global mais le redistribuer entre canaux."),
        ("a", "Et ça change tout."),
        ("b", "Complètement. La question n'est plus « les cent quatre-vingt mille euros ont-ils été rentables », qui appelle un chiffre unique et invérifiable, mais « quels canaux méritent quelle part ». C'est une comparaison. Et une comparaison est infiniment plus atteignable qu'une valeur absolue — c'est presque toujours le cas, d'ailleurs."),
        ("a", "Ensuite ?"),
        ("b", "On écrit l'indicateur, on descend aux événements, et le diagnostic tombe vite : l'événement de demande existe mais ne porte pas la source, et rien ne relie une demande du site à sa fiche dans le CRM. Deux manques, corrigeables, mais aucun rétroactif."),
        ("a", "Combien de temps pour corriger ?"),
        ("b", "Deux semaines, dont l'essentiel est la coordination avec l'équipe qui administre le CRM. C'est presque toujours la partie longue, et il vaut mieux la prévoir comme telle que la découvrir."),
        ("a", "Et la dernière étape ?"),
        ("b", "Assumer ce qu'on ne saura pas. Environ un tiers des demandes arriveront sans canal identifié, parce que ces visiteurs ont refusé le consentement. La tentation est de les répartir au prorata des autres."),
        ("a", "Et il ne faut pas."),
        ("b", "Une ligne « source inconnue » assumée vaut mieux qu'une répartition inventée. La fausse précision se paie au premier recoupement, et elle coûte la confiance dans tout le reste du tableau."),
        ("a", "Un mot pour finir sur les questions qui ne passent pas le test."),
        ("b", "Une question qui ne prépare aucune décision est de la curiosité. Mais elle cache souvent une bonne question, et ça vaut la peine de la chercher plutôt que de refermer la conversation. « Combien de visiteurs viennent d'Espagne ? » ne sert à rien ; « faut-il traduire le site ? » est la vraie question derrière."),
        ("a", "Ce qu'on fait demain ?"),
        ("b", "Ouvrez votre tableau de bord et passez chaque bloc au test de la décision. Notez ceux qui ne le passent pas. Vous en aurez retiré la moitié, et vous saurez enfin quoi construire à la place."),
        ("a", "Au module 2, on entre dans ce que les outils comptent réellement. Merci Sofia."),
    ],
}

# ============================================================
# Module 2 — Lire une audience
# ============================================================

P["analytics-mesure/module-2"] = {
    "formation": "Analytics et mesure de la performance",
    "titre": "Lire une audience : sessions, sources et attribution",
    "module_id": "formation-analytics-mesure-module-2",
    "hosts": HOSTS,
    "resume": "Trois outils, trois chiffres, aucune décision : comment expliquer un écart "
              "plutôt que de chercher à le supprimer.",
    "lignes": [
        ("a", "Module 2, et une réunion qui s'enlise. Même mois, même campagne, trois chiffres. La régie annonce trois cent quarante conversions, l'analytics cent quatre-vingt-dix, le CRM cent vingt demandes réellement arrivées chez les commerciaux."),
        ("b", "Et chacun défend l'outil qu'il administre. La réunion se conclut sans décision, sur l'idée qu'il faudrait « fiabiliser les données » — une formule qui ne veut rien dire et qui garantit qu'on se retrouvera au même point le mois suivant."),
        ("a", "Alors lequel est le bon ?"),
        ("b", "Les trois sont exacts. Ils comptent trois choses différentes, avec trois définitions et trois fenêtres différentes, et personne dans la salle ne sait lesquelles. C'est la situation la plus courante du métier, et elle ne se résout pas en changeant d'outil."),
        ("a", "Commençons par la base : qu'est-ce qu'une session ?"),
        ("b", "Une convention de découpage, rien de plus. Une suite d'interactions séparées par une période d'inactivité. Ce n'est pas une visite au sens humain — quelqu'un qui laisse un onglet ouvert pendant sa pause déjeuner génère deux sessions."),
        ("a", "Et un utilisateur ?"),
        ("b", "Un identifiant de navigateur. Pas une personne. La même personne sur son téléphone, son ordinateur professionnel et son ordinateur personnel compte pour trois utilisateurs. Le nombre d'utilisateurs surestime donc toujours le nombre de personnes."),
        ("a", "Donc on ne dit jamais « personnes »."),
        ("b", "Jamais. C'est une hygiène de vocabulaire qui évite des conclusions fausses en cascade. Et corollaire pratique : si votre site a une zone connectée, transmettre un identifiant de compte est le chantier au meilleur rendement de tout le dispositif. C'est ce qui recolle les trois navigateurs sur une seule personne."),
        ("a", "Parlons des indicateurs d'engagement, parce qu'ils sont partout."),
        ("b", "Et ils sont trompeurs pour la plupart. Le rebond et la session engagée portent le même nom sur deux définitions opposées selon les outils : vérifiez laquelle s'applique chez vous avant toute comparaison."),
        ("a", "Les pages par session ?"),
        ("b", "Elles montent quand la navigation est mauvaise. Sur un site de service, une hausse des pages par session signifie souvent que les gens ne trouvent pas ce qu'ils cherchent. C'est une mauvaise nouvelle présentée comme un signe d'intérêt."),
        ("a", "Et la durée moyenne de session ?"),
        ("b", "La dernière page d'une session compte zéro seconde dans la plupart des configurations, parce que l'outil mesure l'écart entre deux vues de page. La durée moyenne est donc structurellement sous-estimée. Quelqu'un qui lit votre article pendant dix minutes et repart compte zéro."),
        ("a", "On remplace par quoi ?"),
        ("b", "Par des mesures d'intention : l'atteinte d'une page à valeur — tarifs, contact —, la profondeur de lecture, le retour à sept jours, la complétion d'une action. Ce sont des faits, pas des proxys."),
        ("a", "Et comparer son taux de rebond à une moyenne sectorielle ?"),
        ("b", "Jamais. Ni l'outil, ni la définition, ni la collecte ne sont les mêmes. Vous comparez deux nombres qui n'ont en commun que leur nom."),
        ("a", "Un mot sur le trafic direct, qu'on interprète souvent comme de la notoriété."),
        ("b", "Le direct est le fourre-tout de ce que l'outil n'a pas su rattacher : un lien depuis une application, un document, un courriel, une redirection qui perd l'information. Le lire comme une mesure de notoriété est une des erreurs les plus répandues."),
        ("a", "Venons-en aux UTM et à la nomenclature."),
        ("b", "Elle se décide avant la première campagne, parce qu'elle n'est pas rétroactive. Et l'outil distingue les majuscules : « Newsletter » et « newsletter » sont deux sources différentes, ce qui suffit à rendre un rapport inexploitable au bout de six mois."),
        ("a", "Une erreur fréquente ?"),
        ("b", "Poser des UTM sur des liens internes. Ils ne servent qu'aux liens entrants. Sur un lien interne, l'UTM ouvre une nouvelle session et détruit la vraie source : la personne était arrivée par une recherche, elle devient « campagne interne ». Vous perdez l'information que vous cherchiez à mesurer."),
        ("a", "L'attribution, maintenant. À quel canal revient la conversion ?"),
        ("b", "L'attribution est une convention de partage, pas une vérité. Un même parcours donne quatre conclusions différentes selon le modèle. Et le dernier clic, qui est le modèle par défaut presque partout, surévalue systématiquement les canaux de fin de parcours — la recherche de marque, le courriel de relance."),
        ("a", "Comment on s'en sort ?"),
        ("b", "En regardant le rôle d'assistance à côté du modèle. Un canal absent du dernier clic mais présent dans la moitié des parcours est un canal de découverte. Le couper parce qu'il ne convertit pas au dernier clic est une erreur classique, et elle se voit trois mois plus tard sur le volume total."),
        ("a", "Et si on change de modèle ?"),
        ("b", "C'est une rupture de collecte. On la date, et on ne compare pas au travers. Sinon vous attribuez à une action ce qui n'est qu'un changement de convention comptable."),
        ("a", "Reprenons l'étude de cas. Trois cent quarante, cent quatre-vingt-dix, cent vingt."),
        ("b", "Une demi-journée, sur un périmètre volontairement étroit : une seule campagne, un seul mois, une seule conversion. Étape une, écrire ce que compte chaque outil. La régie : trois cent quarante conversions, fenêtre de trente jours après clic et un jour après impression. L'analytics : cent quatre-vingt-dix sessions, dernier clic non direct, trente jours. Le CRM : cent vingt fiches, dédoublonnées par adresse électronique."),
        ("a", "Et là ?"),
        ("b", "La moitié du travail est faite, et personne n'a encore ouvert un tableur. Trois définitions écrites noir sur blanc suffisent déjà à changer la conversation."),
        ("a", "Premier écart ?"),
        ("b", "Le post-impression. Sur les trois cent quarante, quatre-vingt-quinze sont post-impression : la personne a vu la publicité sans cliquer, puis est venue par un autre chemin. L'analytics ne peut pas les voir, par construction. Il reste deux cent quarante-cinq conversions après clic, contre cent quatre-vingt-dix mesurées."),
        ("a", "Deuxième écart ?"),
        ("b", "Le consentement. Le taux du site est de soixante-douze pour cent, stable depuis janvier. L'analytics ne voit donc qu'environ trois quarts des demandes réelles. Cent quatre-vingt-dix mesurées correspondent à un ordre de grandeur de deux cent soixante demandes, ce qui recouvre les deux cent quarante-cinq de la régie à la précision près de l'exercice."),
        ("a", "Donc l'écart est expliqué."),
        ("b", "Entièrement, en deux mouvements. Et le plus intéressant reste à venir : le passage de deux cent quarante-cinq à cent vingt, que personne n'avait examiné."),
        ("a", "Qu'est-ce qu'on y trouve ?"),
        ("b", "Trente-huit doublons, cinquante et une demandes rejetées par le formulaire pour adresse invalide ou champ obligatoire mal rempli, et trente-six demandes arrivées en boîte générique sans être saisies dans le CRM, faute de règle sur qui les traite."),
        ("a", "Ce qui veut dire ?"),
        ("b", "Que quatre-vingt-sept demandes sur deux cent quarante-cinq se perdent entre le site et le commercial. Plus d'un tiers. Et personne ne le savait, parce que chacun regardait son propre chiffre. Le sujet n'était pas la fiabilité des outils."),
        ("a", "Et c'est réparable."),
        ("b", "Les cinquante et un rejets de formulaire sont un problème de conception, réparable en une journée. Les trente-six non saisies sont un problème d'organisation qui se règle par une règle. Le rapprochement n'a pas produit un chiffre juste, il a produit deux décisions."),
        ("a", "La règle générale, alors ?"),
        ("b", "Deux outils ne seront jamais égaux. Ne cherchez pas à réconcilier au chiffre près : cherchez un écart stable et expliqué, et surveillez sa stabilité plutôt que sa valeur. Un écart de trente-cinq pour cent stable est une information ; un écart qui bouge est une alerte."),
        ("a", "Ce qu'on fait demain ?"),
        ("b", "Prenez deux outils qui affichent le même chiffre chez vous, et écrivez pour chacun ce qu'il compte exactement — définition, fenêtre, dédoublonnage. Vingt minutes, et vous saurez déjà d'où vient l'essentiel de l'écart."),
        ("a", "Au module 3, on passe de la mesure à l'analyse. Merci Sofia."),
    ],
}

# ============================================================
# Module 3 — De la mesure à l'analyse
# ============================================================

P["analytics-mesure/module-3"] = {
    "formation": "Analytics et mesure de la performance",
    "titre": "De la mesure à l'analyse : entonnoirs, cohortes et tests",
    "module_id": "formation-analytics-mesure-module-3",
    "hosts": HOSTS,
    "resume": "Une refonte à quarante mille euros écartée en vingt minutes d'entonnoir, "
              "et les quatre façons les plus courantes de conclure trop vite.",
    "lignes": [
        ("a", "Module 3. Le taux de conversion du site est passé de trois virgule un à deux virgule six pour cent en deux mois. Environ quarante demandes commerciales perdues par mois. Et la réunion de crise a déjà trouvé la solution."),
        ("b", "La page d'accueil serait « datée », il faudrait la refondre. Un devis circule, quarante mille euros et trois mois de travail. Personne dans la salle n'a de raison de penser que la page d'accueil est en cause — c'est simplement la seule hypothèse formulée."),
        ("a", "Et une hypothèse unique finit toujours par être adoptée."),
        ("b", "C'est le mécanisme. La baisse est réelle, elle ne vient pas de la page d'accueil, et il faut deux heures d'analyse pour le montrer. Deux heures contre quarante mille euros."),
        ("a", "Quels sont les outils ?"),
        ("b", "Quatre. L'entonnoir, qui localise la marche qui casse. La segmentation, qui dit sur qui. Les cohortes, qui distinguent un effet durable d'un accident. Et le test contrôlé, seul moyen de savoir si une correction fonctionne."),
        ("a", "Commençons par l'entonnoir. Comment on le lit ?"),
        ("b", "En mouvement, pas en niveau. La règle est là. La marche à traiter n'est pas la plus basse — souvent la plus basse est normalement basse — c'est celle qui s'écarte de son histoire. D'où le corollaire : un entonnoir observé une seule fois ne sert presque à rien."),
        ("a", "Et il y a une subtilité de construction."),
        ("b", "Fermé ou ouvert. Un entonnoir fermé n'accepte que les parcours qui passent par toutes les marches dans l'ordre ; un entonnoir ouvert accepte les entrées en cours de route. Les deux sont légitimes et ils ne se comparent pas. Écrivez la forme et la fenêtre sur le rapport, sinon on comparera deux choses différentes."),
        ("a", "Passons à la segmentation. Tu dis que la moyenne est un mensonge confortable."),
        ("b", "Devant une variation globale, le premier réflexe doit être de vérifier si les poids des segments ont bougé. Parce que chaque segment peut progresser pendant que le total baisse — il suffit que la part du segment le moins performant ait augmenté. C'est un effet de composition, pas une dégradation, et ça se traite complètement différemment."),
        ("a", "Il y a un risque à trop segmenter."),
        ("b", "En découpant assez, on trouve toujours quelque chose qui n'existe pas. Deux garde-fous. Fixez un volume plancher par segment et refusez de commenter en dessous — ce refus est une compétence, pas une timidité. Et formulez l'hypothèse avant de découper."),
        ("a", "Et avant d'agir sur un segment ?"),
        ("b", "Il doit tenir sur une seconde période indépendante. Un segment intéressant sur un seul mois est une coïncidence jusqu'à preuve du contraire."),
        ("a", "Les cohortes, maintenant. À quoi elles servent ?"),
        ("b", "À mesurer ce qui dure. Les totaux cachent très efficacement une rétention qui s'effondre : une acquisition en hausse compense la fuite et la courbe globale reste plate. Vous ne le voyez qu'en regardant chaque génération d'utilisateurs séparément."),
        ("a", "Une règle de lecture ?"),
        ("b", "Ne comparez que des cohortes de même âge, et excluez les cohortes trop jeunes des graphiques. Une cohorte de deux semaines paraît toujours excellente parce qu'elle n'a pas encore eu le temps de partir."),
        ("a", "On arrive aux quatre façons de conclure trop vite."),
        ("b", "La corrélation prise pour une causalité. La saisonnalité oubliée. La variable cachée — deux choses varient ensemble parce qu'une troisième les fait bouger. Et la régression vers la moyenne : après un mois exceptionnellement mauvais, le mois suivant sera meilleur quoi que vous fassiez, et vous attribuerez ce retour à la normale à votre action."),
        ("a", "Comment on se protège ?"),
        ("b", "Une seule question, posée systématiquement : quelle observation me ferait changer d'avis ? Si vous ne pouvez pas y répondre, votre hypothèse est irréfutable, et une hypothèse irréfutable n'est pas une analyse."),
        ("a", "Tu as aussi un mot sur les graphiques."),
        ("b", "Le graphique à deux axes verticaux fait apparaître des relations qui n'existent pas. En choisissant bien les échelles, on fait coïncider n'importe quelles deux courbes. C'est la représentation la plus trompeuse du métier, et elle est partout."),
        ("a", "Reprenons l'étude de cas. Deux heures pour retirer un devis de quarante mille euros."),
        ("b", "Étape une, le réflexe du module 1 : vérifier l'instrument avant le phénomène. Journal des modifications — une mise à jour du formulaire déployée le 8 avril. Recoupement avec le nombre de fiches créées dans le CRM : la baisse est réelle, ce n'est pas un artefact de collecte. On peut analyser."),
        ("a", "L'entonnoir ?"),
        ("b", "Quatre marches : page produit vue, page contact atteinte, formulaire commencé, formulaire envoyé. Les trois premières sont stables à un point près. La quatrième passe de soixante et onze à cinquante-deux pour cent."),
        ("a", "Donc la perte est entièrement entre le début et l'envoi du formulaire."),
        ("b", "Et la page d'accueil n'apparaît même pas dans l'entonnoir : elle ne peut pas être en cause. Cette seule observation retire le devis de la table, et elle a pris vingt minutes."),
        ("a", "La segmentation, ensuite."),
        ("b", "On segmente la seule marche qui bouge, et uniquement celle-là. Par appareil : ordinateur stable à soixante-quatorze pour cent, mobile effondré de soixante-huit à trente-neuf. Par navigateur au sein du mobile : un navigateur concentre la quasi-totalité de la chute. Par source : aucun effet — ce qui est cohérent avec une cause technique et pas avec un problème d'audience."),
        ("a", "Et le mécanisme ?"),
        ("b", "La mise à jour du 8 avril a ajouté un champ de sélection dont l'affichage est défectueux sur ce navigateur mobile : la liste s'ouvre hors de l'écran. L'utilisateur ne peut pas la renseigner, le champ est obligatoire, l'envoi est refusé sans message d'erreur visible. Le formulaire n'est pas long, il est impossible à terminer."),
        ("a", "Il reste une vérification."),
        ("b", "La coïncidence de date. La chute commence-t-elle bien le 8 avril ? Oui, décrochage net à cette date sur le segment concerné, et rien avant. Sans cette vérification, on aurait une corrélation entre un déploiement et une baisse, sans certitude de lien. La coïncidence sur un segment précis, et sur lui seul, rend l'explication difficile à contester."),
        ("a", "Et ensuite on teste la correction ?"),
        ("b", "Non, et c'est une décision réfléchie. On corrige et on ne teste pas. Un test compare deux options quand on ignore laquelle est meilleure. Ici, il s'agit de réparer un défaut : personne ne défend l'idée qu'un formulaire impossible à envoyer soit une bonne option."),
        ("a", "Ce qui nous amène au test A/B. Quand il est utile, et comment."),
        ("b", "Un test se dimensionne avant d'être lancé : effet minimal détectable, volume nécessaire, durée. Un ordre de grandeur à retenir — détecter un effet deux fois plus petit demande environ quatre fois plus de visiteurs. C'est ce qui rend beaucoup de tests impossibles sur les petits sites, et il vaut mieux le savoir avant."),
        ("a", "La durée ?"),
        ("b", "Au moins deux semaines entières, même si le volume est atteint en trois jours. Sinon vous testez un mardi contre un dimanche."),
        ("a", "Et l'arrêt anticipé ?"),
        ("b", "Arrêter un test dès qu'il devient significatif peut porter la probabilité de conclure à tort à près d'un cas sur trois. C'est l'erreur la plus répandue, et la plus coûteuse, parce qu'elle produit des convictions fausses qu'on réutilise ensuite pendant des années."),
        ("a", "Quand ne faut-il pas tester ?"),
        ("b", "Trois cas. Une correction de défaut, comme dans le cas. Une décision de principe — on ne teste pas si on respecte une obligation légale. Et un effet lointain, qui mettrait six mois à se manifester : le test n'aura jamais la puissance nécessaire."),
        ("a", "Ce qu'on fait demain ?"),
        ("b", "Construisez l'entonnoir de votre parcours principal, quatre marches maximum, et regardez-le sur six mois plutôt que sur le mois en cours. La marche qui a bougé vous saute aux yeux, et c'est la seule qui mérite qu'on la segmente."),
        ("a", "Au module 4, on restitue. Merci Sofia."),
    ],
}

# ============================================================
# Module 4 — Restituer et décider
# ============================================================

P["analytics-mesure/module-4"] = {
    "formation": "Analytics et mesure de la performance",
    "titre": "Restituer et décider : tableaux de bord, reporting et culture de la mesure",
    "module_id": "formation-analytics-mesure-module-4",
    "hosts": HOSTS,
    "resume": "Une analyse juste qui ne change rien coûte exactement autant qu'une analyse fausse : "
              "comment restituer pour obtenir une décision.",
    "lignes": [
        ("a", "Dernier module. Sofia, l'analyse du module précédent était impeccable : la cause trouvée, la correction déployée, le taux revenu à son niveau. Et la réunion se passe mal."),
        ("b", "Elle s'attarde douze minutes sur une diapositive secondaire où le trafic d'un canal a baissé de quatre pour cent. Quelqu'un conteste un chiffre au motif que « le CRM ne dit pas la même chose ». Et on passe au point suivant sans qu'aucune décision ait été prise — pas même celle de suivre la conversion par appareil, qui était la recommandation."),
        ("a", "Le problème n'est ni l'analyse ni l'audience."),
        ("b", "Il est dans la restitution. Trop de chiffres présentés à parité, aucune hiérarchie, aucune décision formulée, et un ordre du jour qui n'a pas été conçu pour décider. Et le constat qui donne son ton au module : une analyse juste qui ne change rien coûte exactement autant qu'une analyse fausse."),
        ("a", "Commençons par les tableaux de bord. Tu en veux trois, pas un."),
        ("b", "Un tableau conçu pour tout le monde n'est lu par personne. Trois tableaux courts coûtent moins cher à faire vivre qu'un tableau de vingt blocs : l'opérationnel, lu chaque jour par ceux qui agissent ; le pilotage, lu chaque semaine ; et la direction, lu chaque mois, trois ou quatre chiffres."),
        ("a", "Une règle de composition ?"),
        ("b", "Six blocs au maximum. L'indicateur le plus actionnable en haut à gauche, parce que c'est là que va l'œil. Une comparaison sur chaque chiffre — un nombre seul ne dit rien. Et chaque bloc doit être cliquable vers les éléments concernés : un bloc non cliquable est une affiche, pas un outil de décision."),
        ("a", "Comment on le construit ?"),
        ("b", "Par soustraction. On observe un mois ce que les gens regardent réellement, et on retire le reste. C'est plus efficace que n'importe quel atelier de conception, parce que ça mesure l'usage au lieu de le supposer."),
        ("a", "Passons aux représentations. Il y a des choix qui trompent."),
        ("b", "Le temps se lit en courbe. Les catégories en barres horizontales triées — pas en secteurs, où l'œil compare mal des angles. Les parts d'un tout, rarement en camembert, et jamais au-delà de trois ou quatre parts."),
        ("a", "L'axe tronqué ?"),
        ("b", "Trompeur sur des barres, parce que la longueur de la barre est censée être proportionnelle à la valeur. Légitime sur une courbe si la graduation est visible, parce qu'on y lit une variation. La nuance compte."),
        ("a", "Et le nombre de séries ?"),
        ("b", "Trois au maximum par graphique. Au-delà, chacun y voit ce qu'il cherchait — et c'est exactement ce qui s'est passé pendant les douze minutes sur le canal à moins quatre pour cent. Règle générale : un graphique qui exige une explication orale est à refaire, parce qu'il circulera sans vous."),
        ("a", "Venons-en au commentaire d'analyse. Tu proposes quatre temps."),
        ("b", "Le constat, chiffré et segmenté. La cause, avec son degré de certitude. La décision proposée. Et le coût de l'inaction, chiffré."),
        ("a", "Pourquoi le degré de certitude ?"),
        ("b", "Parce qu'écrire « cause établie » ici et « hypothèse à vérifier » là rend crédibles les causes que vous présentez comme établies. Si tout est affirmé sur le même ton, on doute de tout. La gradation est ce qui donne du poids à l'affirmation."),
        ("a", "Et le coût de l'inaction ?"),
        ("b", "C'est l'élément le plus efficace d'une restitution. « Quarante demandes par mois tant que ce n'est pas tranché » déplace la conversation d'un débat sur les chiffres vers un arbitrage sur une dépense. C'est ce qui transforme un constat en décision."),
        ("a", "Un signe qu'un commentaire ne sert à rien ?"),
        ("b", "« Nous continuons à surveiller ». C'est le signe le plus fiable d'un commentaire purement descriptif : il décrit ce que le lecteur voit déjà et il n'engage rien."),
        ("a", "Reprenons l'étude de cas : on rejoue la réunion."),
        ("b", "Même analyse, même auditoire, même durée. Seule la restitution change. Ce qui avait échoué : onze diapositives à parité dont neuf décrivaient des chiffres stables, aucune décision formulée, un chiffre analytics cité sans avoir été rapproché du CRM, et le point le plus important en quatrième position — quand l'attention est déjà consommée."),
        ("a", "Première correction ?"),
        ("b", "Réduire à trois constats. Un seul mérite vraiment une décision : la conversion mobile. On y ajoute deux arbitrages réels. Les huit autres diapositives passent en annexe — ce qui suffit à les retirer de la conversation."),
        ("a", "C'est le point dur, non ? Retirer."),
        ("b", "Trois constats au maximum, et c'est une discipline difficile. Mais ce que vous n'écartez pas, la réunion l'écartera à votre place, et mal — elle gardera le plus anecdotique, parce que c'est celui sur lequel tout le monde peut avoir un avis."),
        ("a", "Deuxième correction ?"),
        ("b", "Écrire chaque constat en quatre temps. Pour le premier : constat chiffré et segmenté ; cause établie avec la date de déploiement ; décision — correctif fait, plus suivi par appareil ; coût de l'inaction — quarante demandes par mois, quatre-vingts déjà perdues. Sept lignes en tout."),
        ("a", "Et le débat sur la fiabilité ?"),
        ("b", "On le désamorce avant qu'il s'ouvre, avec une ligne de périmètre dans le document : « chiffres analytics, couverture d'environ soixante-douze pour cent stable depuis janvier ; l'écart avec le CRM est de trente-cinq pour cent, expliqué et suivi mensuellement »."),
        ("a", "Une phrase."),
        ("b", "Écrite une fois, elle retire à quiconque la possibilité d'utiliser l'écart comme objection. Et surtout, elle montre que la question a déjà été traitée. C'est le meilleur rapport effet-effort de tout le module."),
        ("a", "Les graphiques ont été refaits aussi."),
        ("b", "Les barres empilées de toutes les sources sont remplacées par une courbe à deux séries, mobile et ordinateur, avec un repère vertical daté au 8 avril. Le graphique à deux axes est supprimé au profit d'un tableau de quatre lignes. Aucune information n'est perdue, et la démonstration devient lisible en trois secondes."),
        ("a", "Et l'ouverture de la séance ?"),
        ("b", "Document envoyé vingt-quatre heures avant, annoncé comme considéré lu. Et la séance ne s'ouvre pas par le contexte, mais par : « je vous demande d'arbitrer trois choses ; la première coûte quarante demandes par mois tant qu'elle n'est pas tranchée »."),
        ("a", "Sur la conduite de la revue, tu as des règles."),
        ("b", "Une revue de performance décide, elle ne s'informe pas. Les chiffres s'envoient avant, la séance les suppose lus. Et un point sans relevé de décision écrit reviendra à l'identique le mois suivant — c'est mécanique, et c'est ce qui donne l'impression que les réunions tournent en rond."),
        ("a", "Parlons de la durée de vie du dispositif."),
        ("b", "Sans propriétaire nommé et sans temps identifié dans son agenda, un dispositif dérive en dix-huit mois, quels que soient les moyens investis au départ. Ce n'est pas une question de qualité initiale."),
        ("a", "Comment on l'entretient ?"),
        ("b", "Une revue semestrielle qui pose une seule question à chaque indicateur : qui s'apercevrait de sa suppression ? Elle retire couramment un tiers du dispositif. Et cet allègement est ce qui permet au reste de rester juste."),
        ("a", "Un signe de maturité ?"),
        ("b", "Qu'une décision visible ait été prise publiquement sur un chiffre du dispositif. Tant que ce n'est jamais arrivé, la mesure est un rituel. Le jour où quelqu'un annonce en comité « on arrête ça, les chiffres le disent », la culture a changé."),
        ("a", "Une limite d'usage, pour finir ?"),
        ("b", "Les indicateurs d'activité individuels ne se projettent jamais en réunion. Le suivi individualisé relève des ressources humaines et de la conformité, pas de l'analyste. Et un tableau de bord qui devient un instrument de surveillance perd immédiatement la coopération de ceux qui alimentent la donnée — c'est la loi de Goodhart appliquée aux gens."),
        ("a", "Ce qu'on fait demain ?"),
        ("b", "Reprenez votre dernier rapport et comptez les constats. Si vous en avez plus de trois, choisissez-en trois et mettez le reste en annexe. Puis ajoutez à chacun une ligne : ce que ça coûte de ne rien décider."),
        ("a", "Quatre modules, du plan de mesure au comité de direction. Merci Sofia."),
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
