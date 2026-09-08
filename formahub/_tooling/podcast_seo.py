#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Formahub — podcasts de la formation SEO Fondamentaux (5 modules).

Dialogue à deux voix, environ 9 minutes par module :
  a = Camille, animatrice, pose les questions de l'apprenante ;
  b = Julien, consultant SEO, répond et chiffre.

Chaque épisode reprend la mise en situation du module, ses idées
structurantes, l'étude de cas avec ses chiffres, et se termine par ce
qu'on fait concrètement en rentrant au bureau. Il ne remplace pas le
module : il le prépare et le révise.

Usage :
    FH_OUT=<dossier formations> python3 _tooling/podcast_seo.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_podcasts as bp

HOSTS = {
    "a": {"nom": "Camille", "role": "animatrice"},
    "b": {"nom": "Julien", "role": "consultant SEO"},
}

P = {}

# ============================================================
# Module 1 — Introduction au SEO et les 3 piliers
# ============================================================

P["seo/module-1"] = {
    "formation": "SEO Fondamentaux",
    "titre": "Introduction au SEO et les 3 piliers",
    "module_id": "formation-seo-module-1",
    "hosts": HOSTS,
    "resume": "Pourquoi un site ne « remonte pas », comment un moteur travaille vraiment, "
              "et comment savoir lequel des trois piliers vous bloque avant de dépenser un euro.",
    "lignes": [
        ("a", "Bienvenue dans le podcast Formahub. Aujourd'hui, le premier module de la formation SEO. Julien, je te lis la phrase qui ouvre ce module, parce qu'elle est terriblement banale : « Notre site ne remonte nulle part sur Google. On a pourtant payé une agence quinze mille euros l'an dernier. » Tu l'entends souvent, celle-là ?"),
        ("b", "Chaque semaine, à peu près mot pour mot. Et elle contient déjà trois pièges. Un délai irréaliste, parce qu'on veut des résultats avant la fin du trimestre. Un budget dépensé sans traçabilité, donc impossible à auditer. Et surtout, aucune définition de ce que « remonter » veut dire. Tant qu'on n'a pas répondu à « remonter sur quoi ? », on ne peut rien faire d'utile."),
        ("a", "Commençons par là, alors. Qu'est-ce qu'on répond quand le directeur commercial dit « sur logiciel de gestion » ?"),
        ("b", "On va regarder ensemble le top dix de cette requête. Dans le cas du module, il est occupé par des acteurs qui ont plusieurs milliers de liens entrants et quinze ans d'antériorité. Ce n'est pas une question de motivation, c'est une question d'ordre de grandeur. Donc on reformule avec lui, et on vise ce que tapent vraiment les prospects qualifiés : logiciel de gestion pour PME du bâtiment, par exemple."),
        ("a", "Tu es en train de dire que la partie la plus utile de la mission, c'est de faire changer d'avis le client sur son objectif."),
        ("b", "Exactement. Et c'est vrai bien au-delà du SEO. Un objectif inatteignable rend tout le reste du travail invérifiable."),
        ("a", "Avant d'entrer dans le diagnostic, il y a une chose que le module explique et que je voudrais qu'on clarifie : la différence entre le SEO et le SEA. On les oppose souvent comme deux options concurrentes."),
        ("b", "La bonne image, c'est louer contre construire. Le SEA, la publicité, c'est de la location : tu paies, tu es visible immédiatement, tu arrêtes de payer, tu disparais le jour même. Le SEO, c'est de la construction : c'est lent, c'est incertain les premiers mois, et ça continue de produire quand tu arrêtes d'investir."),
        ("a", "Donc il faut choisir ?"),
        ("b", "Non, il faut séquencer. On ouvre en SEA pour tenir le calendrier commercial, on construit le SEO en parallèle, et on décroît le SEA position par position, à mesure que l'organique prend le relais. Jamais d'un coup. L'erreur classique, c'est de couper la publicité le jour où on lance le SEO, et de se retrouver avec un trou de six mois."),
        ("a", "Passons au cœur du module : comment fonctionne réellement un moteur. Tu insistes beaucoup sur le fait qu'il y a trois étapes distinctes."),
        ("b", "Trois étapes, et les confondre produit des diagnostics faux et des budgets gaspillés. Explorer, c'est le robot qui vient lire la page. Indexer, c'est le moteur qui décide de la garder dans sa bibliothèque. Classer, c'est le fait de la sortir en réponse à une requête donnée. Une page peut être explorée sans être indexée. Une page indexée peut n'être classée sur rien."),
        ("a", "Et c'est là que beaucoup de gens perdent du temps."),
        ("b", "Ils optimisent une page qui n'est pas indexée. C'est-à-dire qu'ils réécrivent le titre, ils travaillent le maillage, ils ajoutent du contenu, sur une page que le moteur n'a même pas retenue. C'est l'erreur la plus coûteuse en heures de travail, et elle est invisible tant qu'on ne regarde pas le rapport d'indexation."),
        ("a", "Alors donne-nous l'arbre de diagnostic. Le module dit que c'est la compétence la plus rentable de tout ce chapitre."),
        ("b", "Quatre questions, dans l'ordre, et on ne passe jamais à la suivante avant d'avoir répondu à la précédente. Un : la page est-elle explorée ? Deux : est-elle indexée ? Trois : est-elle présente sur la requête visée ? Quatre : à quelle position, et avec quel taux de clic ?"),
        ("a", "Et selon l'endroit où ça bloque, on ne fait pas du tout la même chose."),
        ("b", "Rien à voir. Si ce n'est pas exploré, c'est un problème d'accès, souvent technique. Si c'est exploré mais pas indexé, c'est généralement un problème de qualité ou de rendu. Si c'est indexé mais absent de la requête, c'est un problème de ciblage. Et si tu es dans le top cinq avec un taux de clic faible, ton problème n'est pas le classement du tout, c'est le titre et la description que les gens voient."),
        ("a", "Tu as mentionné le rendu. C'est le piège du JavaScript, dont parle le module."),
        ("b", "Le réflexe à prendre est simple : affiche le code source brut de ta page et cherche une phrase de ton article dedans. Si elle n'y est pas, ton contenu n'existe qu'après exécution du JavaScript. Le moteur finit souvent par le voir, mais plus tard, moins bien, et parfois pas du tout. C'est un retardateur d'indexation qui coûte très cher sur un site à fort volume."),
        ("a", "Venons-en aux trois piliers. Technique, contenu, popularité. Tu as une formule que j'aime bien sur la technique."),
        ("b", "La technique, c'est le plancher, pas le plafond. Elle n'a jamais fait monter personne. Elle empêche de monter. Donc on la traite jusqu'à ce qu'elle ne bloque plus, et on passe au contenu. Le perfectionnisme technique est un piège confortable : c'est mesurable, c'est satisfaisant, et ça peut occuper un an sans produire un clic supplémentaire."),
        ("a", "Le contenu, deuxième pilier."),
        ("b", "Là, le changement de paradigme est ancien mais mal digéré. On n'écrit plus pour placer un mot-clé un certain nombre de fois. On écrit pour répondre à une intention, mieux que ce qui est déjà en ligne. La question à se poser devant une page, c'est : qu'est-ce que celle-ci apporte que les dix premiers résultats n'apportent pas ?"),
        ("a", "Et la popularité, le netlinking."),
        ("b", "L'autorité se reçoit, elle ne s'achète pas — en tout cas pas durablement. Le principe est celui du vote : un lien depuis un site reconnu de ton secteur vaut infiniment plus que trente liens d'annuaires. Et surtout, le netlinking arrive en phase quatre, jamais en phase un. Acheter des liens vers un contenu qui ne mérite pas d'être cité, c'est financer la visibilité d'une page qui décevra."),
        ("a", "On arrive à l'étude de cas, et j'aime beaucoup son dénouement. Reprends-nous le diagnostic de cette PME, en quinze jours."),
        ("b", "Jours un et deux : on recadre l'objectif, comme on vient de le dire. Jours trois à cinq : on applique l'arbre. La Search Console annonce trois cent quarante URLs connues, quatre-vingt-neuf indexées seulement. Le statut dominant sur le blog, c'est « explorée, actuellement non indexée ». Et le test du HTML brut confirme que les articles dépendent du JavaScript."),
        ("a", "Donc deux causes."),
        ("b", "Un problème de rendu qui retarde l'indexation, et une qualité éditoriale insuffisante : des articles de trois cents mots produits en série. Jours six à neuf, on qualifie les trois piliers. Technique : bloquant, deux cent cinquante et une pages non indexées. Contenu : faible, aucun ciblage documenté. Popularité : correcte, l'agence a obtenu une trentaine de liens honnêtes."),
        ("a", "Et là, la phrase qui fait mal."),
        ("b", "Les quinze mille euros ont été investis sur le seul pilier qui n'était pas le problème. Ce n'est pas de la malhonnêteté, la plupart du temps. C'est qu'on a vendu ce qu'on savait faire, sans poser les quatre questions."),
        ("a", "Et la feuille de route qu'on restitue ?"),
        ("b", "Quatre phases, dans cet ordre. Corriger le rendu et obtenir l'indexation des pages stratégiques. Construire le ciblage sur des requêtes réellement accessibles. Réécrire en profondeur une quinzaine de pages plutôt que d'en produire cinquante nouvelles. Et seulement ensuite, faire pointer les liens déjà obtenus vers les pages retravaillées."),
        ("a", "Parlons calendrier, parce que c'est ce qu'on te demandera toujours. Qu'est-ce qu'on promet, et à quelle échéance ?"),
        ("b", "L'indexation se joue en semaines. Les premiers mouvements de position, entre un et trois mois. Les effets significatifs sur le trafic, entre quatre et six mois. La maturité, au-delà de douze. Annoncer autre chose, c'est condamner un projet sain à être jugé comme un échec au mois deux."),
        ("a", "Dernier point avant de conclure : tu dis dans le module qu'être premier ne veut plus rien dire."),
        ("b", "Regarde une page de résultats aujourd'hui. Il y a des annonces en haut, un résumé généré par l'IA, un bloc de questions connexes, parfois une carte, des vidéos. Être premier des résultats naturels peut te placer très bas dans l'écran. Le bon raisonnement, c'est la part de visibilité : quelle surface tu occupes réellement sur l'écran de quelqu'un qui tape ta requête."),
        ("a", "Si on doit retenir trois choses de ce module ?"),
        ("b", "Un : on ne fait rien avant d'avoir répondu à « remonter sur quoi ». Deux : les quatre questions de l'arbre de diagnostic, dans l'ordre, sur toute page qui pose problème. Trois : la technique empêche de monter, le contenu fait monter, et l'autorité se reçoit après."),
        ("a", "Et concrètement, lundi matin ?"),
        ("b", "Ouvre la Search Console de ton site, va dans le rapport d'indexation, et compare le nombre de pages connues au nombre de pages indexées. Si l'écart est important, tu viens de trouver ton chantier numéro un, et il n'a rien à voir avec l'écriture."),
        ("a", "Le module deux enchaîne sur la recherche de mots-clés, c'est-à-dire précisément le « remonter sur quoi ». Merci Julien, et bonne écoute pour la suite."),
    ],
}

# ============================================================
# Module 2 — Recherche de mots-clés stratégiques
# ============================================================

P["seo/module-2"] = {
    "formation": "SEO Fondamentaux",
    "titre": "Recherche de mots-clés stratégiques",
    "module_id": "formation-seo-module-2",
    "hosts": HOSTS,
    "resume": "Comment décider ce qu'on écrit — et surtout ce qu'on refuse d'écrire — "
              "en partant de l'intention de recherche plutôt que d'un nombre d'articles.",
    "lignes": [
        ("a", "Deuxième module de la formation SEO, et cette fois on parle de ciblage. Julien, la mise en situation est encore une phrase qu'on entend partout : « Il nous faut vingt articles de blog ce trimestre, on a besoin de visibilité. »"),
        ("b", "Le budget est validé, le rédacteur attend le brief, et tout pousse à commencer à écrire. C'est exactement comme ça qu'on produit vingt articles qui ne généreront jamais de trafic. Parce que personne n'a vérifié si quelqu'un cherche ces sujets, sous quelle forme, et si le site a la moindre chance de se positionner dessus."),
        ("a", "Alors commençons par le début : qu'est-ce qu'un mot-clé, au fond ?"),
        ("b", "La trace écrite d'un besoin. Ce n'est pas une chaîne de caractères à placer dans un texte, c'est quelqu'un qui a un problème et qui l'a formulé en cinq mots. Tout le module découle de là : avant le volume, avant la difficulté, on qualifie l'intention."),
        ("a", "Les quatre intentions, rappelle-les nous."),
        ("b", "Informationnelle : la personne veut comprendre. Navigationnelle : elle cherche un site précis. Commerciale : elle compare avant d'acheter. Transactionnelle : elle est prête à passer à l'acte. Et la même thématique peut donner quatre pages différentes, une par intention."),
        ("a", "Comment on qualifie l'intention sans se tromper ?"),
        ("b", "On ne devine pas, on observe. Tape la requête, regarde le top dix, et demande-toi quel format domine. Si ce sont dix guides longs, l'intention est informationnelle. Si ce sont dix pages produit, elle est transactionnelle. Le top dix est la réponse observable de Google à la question « qu'est-ce que les gens attendent ici ». Trois minutes suffisent."),
        ("a", "Et si je ne suis pas d'accord avec ce que je vois ?"),
        ("b", "C'est le combat le plus coûteux du SEO, et on ne le gagne pas. Si le top dix est composé de comparatifs et que tu publies une page de vente, tu peux avoir le meilleur contenu du marché, tu ne rentreras pas. L'intention détermine le format, jamais l'inverse."),
        ("a", "Passons à la constitution de la liste. Il faut des outils payants ?"),
        ("b", "Pas pour commencer, et c'est important à dire parce que ça bloque beaucoup de gens. La source la plus sous-exploitée est gratuite : c'est ta propre Search Console. Elle te dit sur quelles requêtes tu apparais déjà, y compris celles que tu n'avais jamais ciblées. Ensuite viennent l'autocomplétion, les questions connexes, les recherches associées en bas de page, le vocabulaire de tes clients dans les mails et les tickets support, et les sites concurrents."),
        ("a", "Et les volumes affichés par les outils, on en fait quoi ?"),
        ("b", "On s'en sert pour hiérarchiser, jamais pour prévoir un trafic. Ce sont des estimations arrondies, souvent regroupées entre variantes proches. Annoncer « cette requête fait mille recherches par mois, donc on aura tant de visites », c'est une promesse qu'on ne peut pas tenir."),
        ("a", "Vient l'arbitrage. Volume, difficulté, valeur métier. Comment on tranche ?"),
        ("b", "On score chaque candidate sur quatre critères : la valeur métier, l'accessibilité, le volume et l'effort. Et en cas d'égalité, c'est la valeur métier qui tranche. Une requête à cent recherches mensuelles qui amène des prospects qualifiés vaut mieux qu'une requête à cinq mille qui amène des étudiants en recherche de définition."),
        ("a", "Tu peux donner le calcul qui renverse l'intuition ?"),
        ("b", "Prends une requête générique à cinq mille recherches, sur laquelle tu peux espérer la quinzième position : ça fait quelques clics par mois, et des clics peu qualifiés. Prends maintenant dix requêtes de longue traîne à cent cinquante recherches, sur lesquelles tu peux viser le top trois : tu captes une part bien plus importante de chacune, et les visiteurs correspondent à ton offre. Le total de trafic est supérieur, et la qualité n'a rien à voir."),
        ("a", "C'est le principe de la longue traîne."),
        ("b", "Et pour un site jeune, il n'y a pas d'autre point d'entrée réaliste. Le trafic se construit par cumul de petites requêtes gagnées, pas par une victoire frontale sur le terme générique que le patron connaît. D'ailleurs c'est une erreur classique du module : viser la requête que le patron connaît."),
        ("a", "Une fois qu'on a la liste, on fait le mapping sémantique. Qu'est-ce que c'est exactement ?"),
        ("b", "Un document, souvent un simple tableau, qui associe chaque intention à une URL et une seule. La règle structurante tient en cinq mots : une URL, une intention. Le mapping est ce qui rend cette règle tenable quand plusieurs personnes écrivent."),
        ("a", "Qu'est-ce qu'on met dedans ?"),
        ("b", "Pour chaque ligne : la requête principale, l'intention qualifiée, le format de page attendu, l'URL cible, le statut — existante, à réécrire, à créer — et la personne responsable. Cinq colonnes, pas quinze. Un mapping que personne ne tient à jour ne sert à rien."),
        ("a", "Et si on n'a pas ce document ?"),
        ("b", "On produit des doublons. C'est le sujet suivant du module : la cannibalisation. Deux pages du même site qui visent la même intention. Elles se disputent la même place, elles se partagent les liens internes, et généralement aucune des deux n'atteint le top cinq alors qu'une seule page bien faite y serait."),
        ("a", "Comment on la détecte ?"),
        ("b", "Dans la Search Console, tu filtres sur une requête et tu regardes quelles pages remontent. Si tu vois deux URLs alterner au fil des semaines sur la même requête, tu tiens ta cannibalisation."),
        ("a", "Et on la traite comment ?"),
        ("b", "Trois traitements possibles, et il faut choisir le bon. Si les deux pages sont redondantes, on fusionne : on garde la meilleure, on y reverse ce que l'autre avait d'utile, et on redirige en trois cent un. Si les intentions divergent en réalité, on différencie : on réécrit chacune pour qu'elle assume clairement son angle. Et la désindexation n'arrive qu'en dernier recours."),
        ("a", "L'erreur, ce serait quoi ?"),
        ("b", "Créer un troisième article sur le même sujet en espérant que celui-là marchera. On ajoute un concurrent interne de plus. Avant de créer une page, la question à se poser est toujours : est-ce qu'une page existante ne vise pas déjà cette intention ?"),
        ("a", "Passons à l'étude de cas, qui est assez spectaculaire. Soixante articles qui ne rapportent rien."),
        ("b", "Un site qui a publié soixante articles en deux ans, avec un trafic organique stagnant à quatre cents visites mensuelles, et une demande de vingt articles de plus. Première étape : mesurer avant de produire. L'export Search Console sur douze mois montre que sur soixante articles, onze génèrent quatre-vingt-douze pour cent du trafic."),
        ("a", "Onze sur soixante."),
        ("b", "Et trente-quatre articles n'ont jamais dépassé cinq clics sur l'année, quinze ne sont même pas indexés. Le problème n'est manifestement pas le volume de production."),
        ("a", "Et quand on regarde pourquoi ces trente-quatre ne marchent pas ?"),
        ("b", "Trois causes, par ordre de fréquence. Dix-huit traitent des sujets sans aucun volume de recherche : des sujets choisis en réunion, jamais vérifiés. Neuf sont en cannibalisation deux à deux, sur des angles quasi identiques. Et sept visent des requêtes verrouillées par des acteurs nationaux, qui n'ont jamais dépassé la sixième page."),
        ("a", "Donc la contre-proposition à la directrice marketing."),
        ("b", "Pas vingt articles. Consolider les neuf cas de cannibalisation en quatre pages. Réécrire en profondeur les onze articles qui performent, pour les faire passer du top quinze au top cinq. Et ne produire que six nouveaux contenus, tous issus du mapping, sur des requêtes scorées. Budget identique, moins de livrables, impact très supérieur."),
        ("a", "Et les dix-huit articles sans volume, on les supprime ?"),
        ("b", "Surtout pas à la légère. Ceux qui reçoivent des liens externes sont redirigés vers le contenu pertinent le plus proche. Les autres, on les laisse en l'état, sans investissement supplémentaire. L'inaction ciblée est souvent le meilleur arbitrage — supprimer massivement des pages crée plus de problèmes que ça n'en résout."),
        ("a", "La leçon du cas ?"),
        ("b", "La question « combien d'articles ? » est presque toujours la mauvaise question. Celle qui compte, c'est : quelles intentions ne sont pas couvertes, et lesquelles le sont deux fois ? Un audit d'une journée a redirigé un budget trimestriel entier vers ce qui allait réellement produire."),
        ("a", "Ce qu'on fait lundi matin, alors ?"),
        ("b", "Ouvre la Search Console sur douze mois, trie tes pages par clics décroissants, et regarde combien de pages font quatre-vingts pour cent de ton trafic. Ce simple tri te dit déjà si ton chantier est de produire, de réécrire ou de fusionner."),
        ("a", "Le module trois entre dans la page elle-même : structure, balises, maillage. Merci Julien."),
    ],
}

# ============================================================
# Module 3 — Optimisation on-page et balisage sémantique
# ============================================================

P["seo/module-3"] = {
    "formation": "SEO Fondamentaux",
    "titre": "Optimisation on-page et balisage sémantique",
    "module_id": "formation-seo-module-3",
    "hosts": HOSTS,
    "resume": "Une page correctement ciblée mais bloquée en deuxième page : ce qui la débloque, "
              "et pourquoi ce n'est presque jamais « retoucher un peu le texte ».",
    "lignes": [
        ("a", "Module trois, et on entre dans la page. Julien, la situation de départ est celle qui rend fou : une page bloquée en douzième position depuis quatre mois, correctement ciblée, indexée, sur un site sans problème technique."),
        ("b", "C'est la situation la plus fréquente du métier, et c'est là que se joue l'essentiel des gains accessibles. Parce que l'on-page, c'est tout ce que tu maîtrises entièrement : la structure, les balises, le contenu, le maillage. Tu ne dépends ni d'un développeur, ni d'un site tiers."),
        ("a", "Commençons par la structure. Les titres, les fameux H1, H2, H3."),
        ("b", "Une seule règle à retenir, et elle règle quatre-vingt-dix pour cent des cas : la balise porte le sens, le CSS porte l'apparence. On ne choisit jamais un niveau de titre parce qu'il a la bonne taille à l'écran. Si le H2 est trop gros à ton goût, tu changes le style, tu ne descends pas en H3."),
        ("a", "Et il y a un test que tu proposes pour vérifier une structure."),
        ("b", "Le test du plan lu seul. Tu prends tous tes titres, tu les mets bout à bout, et tu les lis sans le reste du texte. Si ça raconte la page, la structure est bonne. Si ça ne veut rien dire, il faut la reprendre avant d'écrire une ligne de plus."),
        ("a", "Parlons du Title, la balise qui s'affiche dans les résultats."),
        ("b", "Cinquante-cinq à soixante caractères, avec l'information essentielle dans les quarante premiers, parce que c'est ce qui reste visible sur mobile. Le mot-clé principal en tête. Et surtout un différenciateur : quelque chose que les autres titres de la page de résultats n'affichent pas."),
        ("a", "Un différenciateur, c'est-à-dire ?"),
        ("b", "Un chiffre, une année, un format annoncé. Regarde le top dix avant d'écrire ton titre : si les dix commencent tous par « Comment choisir », tu ne gagnes rien à faire le onzième. Le module raisonne d'ailleurs en pixels plutôt qu'en caractères, parce qu'un titre en majuscules ou plein de M sera tronqué plus tôt."),
        ("a", "On dit souvent que Google réécrit les titres. Ça ne rend pas l'exercice inutile ?"),
        ("b", "Non, et c'est un contresens fréquent. Google réécrit surtout quand le titre est mauvais : dupliqué sur des dizaines de pages, purement générique, ou déconnecté du contenu. Un bon titre est conservé la plupart du temps. Et même réécrit, il reste un signal sur le sujet de la page."),
        ("a", "La meta description, maintenant. Elle sert à quoi si elle ne fait pas classer ?"),
        ("b", "Elle ne classe pas, elle fait cliquer. C'est le seul espace publicitaire gratuit d'une page de résultats, et beaucoup de gens le laissent vide. Le schéma qui marche tient en trois temps : bénéfice, objection, action. Ce que la personne va y gagner, ce qui pourrait la retenir, et ce qu'elle doit faire."),
        ("a", "Venons-en au contenu lui-même. Il y a une phrase du module que je veux te faire commenter : « on n'ajoute pas des mots-clés à un texte, on traite des questions »."),
        ("b", "C'est le renversement le plus important du module. Si tu traites réellement une question, le vocabulaire du domaine arrive tout seul, parce qu'on ne peut pas expliquer un sujet sans employer les mots du sujet. Alors que si tu pars du mot-clé, tu écris un texte qui sonne faux et qui ne répond à rien."),
        ("a", "Et la longueur ? On me demande toujours combien de mots il faut."),
        ("b", "Il n'existe aucune longueur cible. Aucune. On ajoute des réponses, jamais des mots. Allonger un texte pour atteindre un nombre imposé est une des erreurs les plus répandues, et le résultat se voit immédiatement : des paragraphes de remplissage que personne ne lit et qui diluent la page."),
        ("a", "Tu parles aussi de la pyramide inversée."),
        ("b", "Répondre tout de suite. La personne a posé une question, elle doit trouver la réponse dans les premières lignes, pas après quatre paragraphes d'introduction historique. Ensuite tu développes, tu nuances, tu donnes les cas particuliers. Le suspense est un genre littéraire, ce n'est pas un genre web."),
        ("a", "Le maillage interne, maintenant. Tu dis que c'est le levier le plus sous-utilisé."),
        ("b", "Et le seul qui soit gratuit. Un lien interne fait trois choses en même temps : il guide le lecteur, il répartit l'autorité entre tes pages, et il dit au moteur de quoi parle la page d'arrivée, par le texte de l'ancre. Trois effets, zéro coût, et personne ne s'en occupe."),
        ("a", "Il y a des pièges ?"),
        ("b", "Deux principalement. Utiliser toujours la même ancre exacte, ce qui produit un schéma artificiel très reconnaissable. Et laisser des pages importantes à quatre ou cinq clics de l'accueil. La profondeur de clic compte : ce qui est loin est exploré moins souvent et jugé moins important."),
        ("a", "Les images et les données structurées, pour finir sur les fondamentaux."),
        ("b", "Sur les images, trois réflexes : un poids raisonnable, un format moderne, et un attribut alt écrit pour l'accessibilité d'abord. L'alt décrit l'image à quelqu'un qui ne la voit pas. Ce n'est pas un endroit où empiler des mots-clés — et quand on le remplit correctement, il est de toute façon pertinent."),
        ("a", "Et les données structurées ?"),
        ("b", "Elles n'améliorent pas le classement. Elles améliorent l'affichage : les étoiles, le prix, la durée de la recette. Donc elles améliorent le taux de clic. C'est déjà beaucoup, mais il faut être clair sur ce qu'on en attend."),
        ("a", "L'étude de cas, maintenant. La page de la douzième à la cinquième position."),
        ("b", "Un guide « comment choisir un logiciel de facturation », bloqué en douzième position depuis quatre mois. Mille neuf cents recherches mensuelles sur la requête, deux mille quatre cents impressions, trente et un clics — un taux de clic de un virgule trois pour cent."),
        ("a", "Première étape ?"),
        ("b", "Vérifier l'évidence, comme au module un. Page indexée, intention correcte, aucun problème technique. Le terrain on-page est donc bien le bon terrain. Ça prend dix minutes et ça évite de travailler dans le vide."),
        ("a", "Ensuite ?"),
        ("b", "On compare les plans. Les cinq premiers résultats traitent tous trois thèmes absents de la page : la facturation électronique obligatoire, l'intégration avec les outils comptables, et la reprise de données quand on change d'outil. La page n'est pas mal écrite, elle est incomplète. C'est presque toujours ça, en position onze à vingt."),
        ("a", "Et le bloc des questions connexes ?"),
        ("b", "Il remonte quatre questions, dont deux ne sont couvertes nulle part dans la page. C'est du renseignement gratuit sur ce que les gens attendent, et c'est affiché sur la page de résultats de n'importe quelle requête."),
        ("a", "Qu'est-ce qui a été fait, concrètement ?"),
        ("b", "Trois sections ajoutées, environ sept cents mots, qui traitent réellement les thèmes manquants. Un tableau comparatif de six critères que personne d'autre n'affiche sur cette requête — c'est l'élément différenciant. Le titre réécrit, avec le mot-clé en tête, un chiffre et une année. La meta description rédigée, elle était absente. Cinq liens internes contextuels ajoutés depuis des articles bien positionnés, avec des ancres variées. Et la signature de l'auteur avec sa fonction, plus la date de mise à jour."),
        ("a", "Résultat ?"),
        ("b", "À huit semaines : position moyenne cinq virgule deux, taux de clic quatre virgule huit pour cent, cent soixante-dix-huit clics mensuels. Près de six fois le trafic initial. Aucun lien externe acquis, aucun développement."),
        ("a", "Et tu insistes sur le fait qu'il y a deux mouvements distincts là-dedans."),
        ("b", "C'est essentiel à comprendre. Le contenu ajouté a fait bouger la position, de douze à cinq. Le titre et la description ont fait bouger le taux de clic, de un virgule trois à quatre virgule huit. Ce sont deux leviers différents, sur deux métriques différentes. Si tu les confonds, tu ne sais jamais ce qui a marché."),
        ("a", "Ce qu'on fait lundi matin ?"),
        ("b", "Prends une page qui traîne en deuxième page. Ouvre les cinq premiers résultats de sa requête, note leurs titres de section, et compare avec ton plan. La liste des thèmes que tu n'as pas traités est ta liste de travail, et elle est généralement courte."),
        ("a", "Au module quatre, on passe au SEO technique et au netlinking. Merci Julien."),
    ],
}

# ============================================================
# Module 4 — SEO technique et netlinking
# ============================================================

P["seo/module-4"] = {
    "formation": "SEO Fondamentaux",
    "titre": "SEO technique et netlinking",
    "module_id": "formation-seo-module-4",
    "hosts": HOSTS,
    "resume": "Codes HTTP, redirections, indexation, migrations et profil de liens : "
              "les décisions qui font perdre quarante pour cent du trafic en trois semaines.",
    "lignes": [
        ("a", "Module quatre, et on attaque la partie qui fait peur : le SEO technique. Julien, la mise en situation, c'est une refonte réussie qui tourne mal."),
        ("b", "Trois semaines après la mise en ligne du nouveau site, le trafic organique a chuté de quarante-deux pour cent. Et le site est objectivement meilleur : design moderne, plus rapide, navigation repensée. L'agence dit que tout a été fait dans les règles et que ça va revenir."),
        ("a", "Ça ne revient pas tout seul, j'imagine."),
        ("b", "Jamais. Ce scénario est le plus coûteux du référencement et le plus évitable. Il se joue presque toujours sur trois ou quatre décisions techniques prises sans en mesurer la portée."),
        ("a", "Commençons par les codes de réponse. Trois cent un, trois cent deux : quelle différence ?"),
        ("b", "Trois cent un veut dire « cette page a déménagé pour de bon ». Trois cent deux veut dire « elle est ailleurs temporairement, je compte revenir ». La conséquence est concrète : le trois cent un transmet l'autorité accumulée par l'ancienne URL, le trois cent deux beaucoup moins, parce que le moteur garde l'ancienne en mémoire en attendant ton retour."),
        ("a", "Et dans le doute ?"),
        ("b", "Trois cent un. L'erreur classique, c'est le trois cent deux par défaut du serveur, que personne ne pense à changer parce que la redirection marche visuellement. L'utilisateur arrive au bon endroit, donc tout semble correct — et pendant ce temps l'autorité ne passe pas."),
        ("a", "Tu parles aussi de chaînes de redirection."),
        ("b", "Une URL qui redirige vers une deuxième, qui redirige vers une troisième. Ça arrive naturellement après plusieurs refontes successives. Chaque maillon coûte du temps de chargement et dilue le signal. La règle : on aplatit, la première URL doit pointer directement vers la destination finale."),
        ("a", "Passons à robots point txt. Il y a une confusion très répandue là-dessus."),
        ("b", "La plus coûteuse du module. Bloquer une page dans robots point txt n'est pas la désindexer. Tu interdis au robot de lire la page — donc il ne lira jamais la directive de retrait qui se trouve dedans. Résultat : la page peut rester dans l'index, parfois pendant des mois, affichée sans description."),
        ("a", "Alors comment on désindexe réellement ?"),
        ("b", "Dans l'ordre. Un : tu ouvres l'accès, tu enlèves le blocage. Deux : tu mets une balise noindex, follow sur la page. Trois : tu vérifies dans la Search Console que la page a bien disparu de l'index. Et quatre, seulement à ce moment-là, tu peux bloquer si tu veux économiser du crawl."),
        ("a", "Et la balise canonique ?"),
        ("b", "Elle sert à dire « la version de référence de cette page, c'est celle-ci ». Deux règles : elle est autoréférente par défaut, chaque page se désigne elle-même. Et elle ne pointe jamais vers un contenu différent. Sur une pagination, la page deux n'est pas une copie de la page un — mettre une canonique de la deux vers la une fait disparaître tout ce qu'elle contient."),
        ("a", "Il y a une erreur que tu appelles « la combinaison qui rend une page ingérable »."),
        ("b", "Cumuler des directives contradictoires. Un noindex plus une canonique vers une autre page plus un blocage robots. Chacune dit quelque chose de différent, le moteur en retient une, et tu ne sais plus laquelle. Une intention, un mécanisme. C'est tout."),
        ("a", "Les Core Web Vitals, maintenant. On en fait beaucoup de bruit."),
        ("b", "Trois indicateurs : le temps d'affichage du contenu principal, la réactivité aux interactions, et la stabilité visuelle. Le troisième est celui qu'on sous-estime : une bannière qui apparaît en cours de chargement et décale tout le contenu, c'est très pénalisant, et c'est très courant."),
        ("a", "Et le score de cent, il faut le viser ?"),
        ("b", "Presque jamais. Les Web Vitals fonctionnent par seuils : sortir du rouge compte, passer de quatre-vingt-cinq à cent ne se justifie que très rarement au regard du travail demandé. Et surtout, on pilote sur les données de terrain — celles de tes vrais visiteurs, avec leurs vrais téléphones — pas sur le score obtenu depuis ton poste en fibre."),
        ("a", "On arrive aux migrations. Tu as une méthode en huit étapes dans le module, mais donne-nous le principe."),
        ("b", "Tout tient à l'inventaire des URLs, fait avant la bascule. Tu exportes la liste complète des URLs existantes, avec leur trafic sur douze mois, et tu construis un tableau de correspondance ancienne URL vers nouvelle URL. Après la bascule, il faut le reconstituer à partir d'archives, et c'est un cauchemar."),
        ("a", "Et l'erreur de la redirection vers l'accueil ?"),
        ("b", "Rediriger en masse des pages vers la page d'accueil est traité comme un faux quatre cent quatre. Aucune autorité n'est transférée, et l'utilisateur qui cherchait une fiche précise atterrit sur une page d'accueil qui ne répond pas à sa question. C'est un des réflexes les plus destructeurs qui soient."),
        ("a", "Reprenons l'étude de cas, alors. La refonte qui coûte quarante-deux pour cent."),
        ("b", "Jour un, on écarte la panne globale. Le site répond bien, il n'est pas en noindex, le robots point txt est correct. La chute est donc sélective : c'est un problème d'URLs, pas d'accès."),
        ("a", "Ensuite ?"),
        ("b", "Le rapport d'indexation. Les pages indexées passent de mille deux cent quarante à huit cent quatre-vingt-dix. Et le rapport « introuvable » compte six cent dix URLs apparues en trois semaines. Le diagnostic se précise : des URLs ont changé sans redirection."),
        ("a", "Comment on quantifie ce qui a été perdu ?"),
        ("b", "On croise deux listes : l'export des pages qui généraient du trafic dans les douze mois précédant la refonte, et la liste des erreurs quatre cent quatre. Résultat : cent quatre-vingt-sept anciennes URLs qui recevaient du trafic organique n'ont aucune redirection. Elles représentaient quarante-six pour cent du trafic de la période — ce qui correspond à l'ordre de grandeur de la perte."),
        ("a", "Et il y avait deux causes secondaires."),
        ("b", "Sur les URLs effectivement redirigées, quarante pour cent le sont en trois cent deux au lieu de trois cent un, à cause du réglage par défaut du nouveau serveur. Et un tiers des redirections pointent vers la page d'accueil au lieu de l'équivalent réel. Les trois erreurs du module, réunies sur un seul projet."),
        ("a", "Le plan de correction ?"),
        ("b", "Reconstituer le tableau de correspondance pour les cent quatre-vingt-sept URLs, à partir de l'archive du site et des titres relevés dans la Search Console. Mettre les trois cent un vers les pages équivalentes, jamais vers l'accueil. Convertir tous les trois cent deux. Aplatir les chaînes créées par ces corrections successives. Régénérer et resoumettre le sitemap, et demander l'indexation des trente pages les plus stratégiques."),
        ("a", "Résultat ?"),
        ("b", "Environ quatre-vingts pour cent du trafic perdu récupéré en sept semaines. Les vingt pour cent restants correspondent à des pages dont l'équivalent n'existait plus : le contenu avait été supprimé, pas seulement déplacé. Aucune redirection ne répare ça."),
        ("a", "Passons au netlinking pour finir. On en revient à ce que tu disais au module un."),
        ("b", "L'autorité se reçoit. Le module donne six critères pour évaluer un lien : la thématique du site source, son autorité réelle, la position du lien dans la page, le texte de l'ancre, le caractère éditorial ou payant, et la stabilité dans le temps. Un lien en pied de page d'un annuaire ne vaut rien ; un lien dans le corps d'un article d'un média de ton secteur vaut beaucoup."),
        ("a", "Et il faut déclarer les liens payants ?"),
        ("b", "Oui, avec les attributs prévus pour ça — sponsorisé pour un lien payé, contenu utilisateur pour un forum ou un commentaire. Ne pas déclarer un lien payant, c'est prendre un risque pour un gain qui, de toute façon, ne dure pas."),
        ("a", "Qu'est-ce qui fonctionne durablement, alors ?"),
        ("b", "Produire quelque chose qu'on a envie de citer : une donnée que personne d'autre n'a, un test mené sérieusement, un outil utile. Ensuite seulement, on va le faire savoir. Et j'insiste : le netlinking arrive en phase quatre. Lancer une campagne de liens en phase un, c'est payer pour envoyer des gens sur une page qui les décevra."),
        ("a", "Ce qu'on fait lundi matin ?"),
        ("b", "Si une refonte est prévue chez toi dans les mois qui viennent, exporte dès maintenant la liste de tes URLs avec leur trafic sur douze mois, et range ce fichier quelque part de sûr. C'est dix minutes de travail qui peuvent sauver la moitié de ton trafic."),
        ("a", "Le module cinq clôt la formation avec la mesure de performance et le SEO à l'ère de l'IA. Merci Julien."),
    ],
}

# ============================================================
# Module 5 — Mesure de performance et SEO à l'ère de l'IA
# ============================================================

P["seo/module-5"] = {
    "formation": "SEO Fondamentaux",
    "titre": "Mesure de performance et SEO à l'ère de l'IA",
    "module_id": "formation-seo-module-5",
    "hosts": HOSTS,
    "resume": "Rendre compte honnêtement d'un canal dont les effets sont décalés, "
              "et produire ce qu'un résumé automatique ne peut pas remplacer.",
    "lignes": [
        ("a", "Dernier module de la formation SEO, et il commence par une question de comité de direction : « concrètement, qu'est-ce que le SEO nous a rapporté ce trimestre ? »"),
        ("b", "Avec un détail qui rend la question piégeuse. Le trafic organique a progressé de vingt-deux pour cent, mais la moitié de cette hausse vient de requêtes de marque, à cause d'une campagne de notoriété. Donc ça ne vient pas du travail SEO."),
        ("a", "Et là tu as deux mauvaises réponses possibles."),
        ("b", "Dire plus vingt-deux pour cent serait exact et malhonnête. Dire « je ne peux pas répondre » serait honnête et inutile. Tout le module est dans cet écart : un reporting qui informe plutôt qu'un reporting qui rassure."),
        ("a", "Commençons par les métriques. La Search Console en donne quatre."),
        ("b", "Impressions, clics, taux de clic, position moyenne. Et la règle absolue, c'est qu'aucune ne signifie quoi que ce soit isolément. On les lit croisées, toujours."),
        ("a", "Donne un exemple."),
        ("b", "Les impressions montent, les clics stagnent. Vu seul, ça semble mauvais. Croisé, ça veut souvent dire que tu apparais sur de nouvelles requêtes, mais en position basse, ou avec un titre qui ne donne pas envie. Ce n'est pas un échec, c'est une indication de ce qu'il faut travailler ensuite."),
        ("a", "Et le piège de la position moyenne ?"),
        ("b", "C'est une moyenne, donc elle masque les extrêmes. Une position moyenne qui se dégrade pendant que les clics montent, c'est très souvent bon signe : tu captes de nouvelles requêtes, sur lesquelles tu es forcément mal placé au début, et elles tirent la moyenne vers le bas. Donc on analyse requête par requête, jamais au niveau du site."),
        ("a", "Tu insistes beaucoup sur la segmentation marque et hors marque."),
        ("b", "C'est le seul périmètre qui mesure réellement ton travail. Quelqu'un qui tape le nom de ton entreprise serait venu de toute façon. Le SEO se juge sur les requêtes où la personne ne te connaissait pas. Tu filtres les requêtes contenant ton nom de marque, et tu regardes le reste."),
        ("a", "Il y a d'autres segmentations utiles ?"),
        ("b", "Par appareil, parce que les positions et les taux de clic n'ont rien à voir entre mobile et ordinateur. Par page, pour repérer ce qui porte le trafic. Et par pays si tu es sur plusieurs marchés. Une donnée agrégée ne dit rien ; une donnée segmentée dit quoi faire."),
        ("a", "Justement, comment on identifie ce qui vaut l'effort du trimestre suivant ?"),
        ("b", "Le module donne trois configurations rentables. La première : beaucoup d'impressions, un taux de clic anormalement bas, alors que la position est correcte. Là, le problème est le titre et la description, pas le contenu. C'est une demi-journée de travail pour un gain immédiat."),
        ("a", "La deuxième ?"),
        ("b", "Les requêtes en position cinq à quinze. Ce sont celles où quelques améliorations font franchir un seuil visible. En dessous de la position cinquante, en revanche, le travail on-page seul ne suffira pas — et savoir où ne pas investir fait partie du métier."),
        ("a", "Et la troisième, que tu dis la plus négligée ?"),
        ("b", "Les requêtes que tu captes déjà sans les avoir jamais ciblées. Tu apparais en position vingt sur une requête à laquelle aucune de tes pages n'était destinée. Ça veut dire que le besoin existe, que Google te juge vaguement pertinent, et que personne chez toi n'a écrit la page qui répondrait vraiment. C'est le meilleur rendement du trimestre, et c'est gratuit à trouver."),
        ("a", "Parlons du reporting. Comment on le structure ?"),
        ("b", "En cinq blocs. Ce qui a été fait. Ce que ça a produit, sur des indicateurs adaptés à l'horizon. Ce qui se construit et ne se voit pas encore. Ce qui n'a pas marché. Et ce qu'on fait le mois prochain. Le bloc « ce qui n'a pas marché » est celui qui donne sa crédibilité à tous les autres."),
        ("a", "Adapter l'indicateur à l'horizon, c'est important pour toi."),
        ("b", "C'est ce qui condamne le plus de projets sains. Au mois deux, l'indicateur pertinent est l'indexation et les premières positions gagnées, pas le chiffre d'affaires. Si tu promets du chiffre d'affaires au mois deux, tu seras jugé sur cette promesse, et tu échoueras alors que le travail était bon."),
        ("a", "Tu recommandes aussi d'énoncer soi-même les limites d'attribution."),
        ("b", "Toujours. L'attribution au dernier clic sous-estime les contenus de découverte : quelqu'un lit un article, revient un mois plus tard en tapant le nom de la marque, et convertit. Tout est crédité à la marque. Donc ton chiffre est un plancher, pas une mesure exacte. Le dire toi-même te crédibilise ; le laisser découvrir par quelqu'un d'autre te décrédibilise."),
        ("a", "Reprenons l'étude de cas, avec la réponse au comité."),
        ("b", "Étape une : on isole. Vingt-deux pour cent au total, neuf pour cent hors marque. C'est le neuf qu'on présente, en expliquant pourquoi il est plus bas que le chiffre que la direction a déjà vu dans l'outil d'analytics. Il faut l'anticiper, sinon ça passe pour une reculade."),
        ("a", "Étape deux ?"),
        ("b", "On rattache au métier. Sur le trimestre, l'organique hors marque a généré quarante-sept demandes de devis contre trente et une au trimestre précédent. Avec un taux de transformation connu et un panier moyen connu, on peut énoncer un ordre de grandeur de chiffre d'affaires — présenté comme un ordre de grandeur, jamais comme un chiffre comptable."),
        ("a", "Étape trois, ce qui se construit."),
        ("b", "Trente-quatre requêtes sont passées de la troisième à la deuxième page. Elles ne produisent pas encore de clics, mais elles constituent le stock du trimestre suivant. C'est exactement l'indicateur d'horizon intermédiaire dont on parlait, et c'est ce qui rend un reporting SEO lisible pour une direction."),
        ("a", "Et ce qui n'a pas marché ?"),
        ("b", "Six articles produits sur des sujets définitionnels, quarante visites cumulées. Ils sont directement exposés aux résumés générés par l'IA. La conséquence est assumée devant la direction : la production du trimestre suivant est réorientée vers un baromètre sectoriel adossé aux données de l'entreprise."),
        ("a", "Ce qui nous amène au dernier sujet, celui qui change le métier en ce moment. Les résumés IA et le zéro clic."),
        ("b", "Le principe est simple à énoncer. Si un résumé automatique peut répondre à la place de ta page, le trafic ne viendra pas, quelle que soit ta position. Une définition, une conversion d'unité, une date : tout ça se répond dans l'encadré, et l'utilisateur ne clique jamais."),
        ("a", "Donc qui est touché, et qui ne l'est pas ?"),
        ("b", "Le contenu générique et définitionnel est massivement touché. Ce qui l'est beaucoup moins : ce qui demande une décision, une comparaison fine, un accompagnement, un outil, ou une donnée qu'on ne trouve pas ailleurs. Et tout ce qui suppose de faire confiance à quelqu'un plutôt qu'à un texte."),
        ("a", "D'où la notion de gain d'information."),
        ("b", "C'est la seule défense durable. Le module identifie quatre sources : des données propres que tu es seul à avoir, des tests que tu as réellement menés, une expérience vécue qu'on ne peut pas inventer, et une synthèse d'expert qui tranche là où les autres restent prudents."),
        ("a", "Tu as un exemple de ce contraste ?"),
        ("b", "Deux articles sur le même sujet. Le premier explique ce qu'est le sujet : il est parfaitement remplaçable par un résumé. Le second donne les résultats d'un test mené sur ses propres clients, avec les chiffres et ce qui n'a pas marché : un résumé peut le citer, il ne peut pas le remplacer. Et souvent, il l'attribue."),
        ("a", "Une erreur à éviter absolument, pour finir ?"),
        ("b", "Continuer à produire du volume générique en espérant que la quantité compense. Ça ne compensera pas. C'est le seul segment de contenu dont la valeur baisse mécaniquement en ce moment."),
        ("a", "Ce qu'on fait lundi matin ?"),
        ("b", "Ouvre la Search Console, filtre pour exclure les requêtes contenant ta marque, trie par impressions décroissantes, et regarde les vingt premières lignes dont le taux de clic est inférieur à deux pour cent. Tu viens de te fabriquer ta liste de travail du mois, et elle est chiffrée."),
        ("a", "Et voilà, la formation SEO est bouclée. Cinq modules, du diagnostic à la mesure. Merci Julien, et bravo à celles et ceux qui sont allés au bout."),
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
