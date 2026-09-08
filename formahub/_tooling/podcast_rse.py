#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Formahub — podcasts de la formation RSE et transition écologique.

  a = Camille, animatrice de la série ;
  b = Inès, consultante RSE.

Quatre épisodes d'environ 9 minutes : le cadre réglementaire après Omnibus,
le bilan d'émissions, la double matérialité et le plan d'action, puis le
reporting et le greenwashing.

Les chiffres et les dates cités reprennent ceux des modules, qui sont la
référence : toute correction se fait d'abord là-bas, puis ici.

Usage :
    FH_OUT=<dossier formations> python3 _tooling/podcast_rse.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_podcasts as bp

HOSTS = {
    "a": {"nom": "Camille", "role": "animatrice"},
    "b": {"nom": "Inès", "role": "consultante RSE"},
}

P = {}

# ============================================================
# Module 1 — Le cadre
# ============================================================

P["rse-transition-ecologique/module-1"] = {
    "formation": "RSE et transition écologique en entreprise",
    "titre": "Le cadre : ce que recouvre la RSE et ce que la réglementation impose",
    "module_id": "formation-rse-transition-ecologique-module-1",
    "hosts": HOSTS,
    "resume": "Après la révision Omnibus, « suis-je soumis ? » est devenue la mauvaise question. "
              "La bonne : qui me demande quoi, sur quel fondement, et que suis-je obligé de fournir.",
    "lignes": [
        ("a", "Premier module de la formation RSE. Inès, la mise en situation empile trois demandes le même mois."),
        ("b", "Une entreprise de trois cent quatre-vingts salariés, cent vingt millions de chiffre d'affaires. Son plus gros client, un groupe coté, envoie un questionnaire ESG de cent quatre-vingts questions à retourner sous trois semaines, en précisant que le référencement en dépend. La banque demande des éléments extra-financiers pour une ligne de crédit. Et le service commercial annonce avoir perdu un appel d'offres public parce que le dossier ne comportait pas de bilan d'émissions."),
        ("a", "Et la première question du directeur général."),
        ("b", "« On n'est pas soumis à la CSRD, si ? ». La réponse est non — depuis la révision de mars 2026, les seuils sont à mille salariés et quatre cent cinquante millions d'euros de chiffre d'affaires. L'entreprise en est loin. Et cette réponse ne règle strictement rien."),
        ("a", "C'est le point de départ de tout le parcours, si je comprends bien."),
        ("b", "La question « suis-je soumis ? » est devenue secondaire. La question qui compte, c'est : qui me demande quoi, sur quel fondement, et que suis-je obligé de fournir. Les trois demandes du mois ne viennent pas de la CSRD, elles viennent d'un client, d'une banque et d'un acheteur public."),
        ("a", "Commençons par le vocabulaire, parce qu'on entend trois mots pour ce qui semble être la même chose."),
        ("b", "Trois mots, trois usages. La RSE est un mot de management : la responsabilité d'une entreprise vis-à-vis de ses impacts. L'ESG est un mot d'investisseur : une grille pour évaluer un risque financier. La transition écologique est un mot de politique publique. Employez le bon devant le bon interlocuteur — devant votre banque, on parle ESG."),
        ("a", "Et la double matérialité, dont on entend beaucoup parler ?"),
        ("b", "Deux regards. La matérialité d'impact : ce que l'entreprise fait subir au monde. La matérialité financière : ce que le monde fait subir à l'entreprise. Les deux ne conduisent pas aux mêmes priorités, et une démarche solide fait les deux et les confronte. On y revient en détail au module 3."),
        ("a", "Venons-en au cadre européen après mars 2026."),
        ("b", "La CSRD ne vise plus que les entreprises de plus de mille salariés et de plus de quatre cent cinquante millions de chiffre d'affaires, les deux critères ensemble, à partir de l'exercice 2027. Le périmètre s'est considérablement resserré."),
        ("a", "Donc les PME sont tranquilles ?"),
        ("b", "Non, et c'est exactement le contresens à éviter. Elles ne sont pas soumises au reporting, mais elles reçoivent les questionnaires des grandes entreprises qui, elles, le sont. La pression passe par la chaîne de valeur, pas par le texte."),
        ("a", "Et il existe une protection contre ça."),
        ("b", "C'est le point le plus utile de toute la réglementation pour une PME, et presque personne ne le connaît : une entreprise soumise ne peut pas exiger d'un partenaire de moins de mille salariés davantage que le périmètre VSME, le standard volontaire prévu pour les petites structures. Et elle doit mentionner ce droit de refus. C'est un plafond opposable."),
        ("a", "Ce qui change la conversation avec le client."),
        ("b", "Totalement. Et la conséquence pratique est très importante : un socle de données VSME construit une fois répond à la quasi-totalité des sollicitations. C'est la réponse structurelle aux demandes multiples — vous ne répondez plus questionnaire par questionnaire."),
        ("a", "Tu insistes beaucoup sur la date des sources."),
        ("b", "Toute source antérieure à mars 2026 sur le périmètre CSRD est obsolète. C'est une matière où les articles vieillissent en quelques mois. Datez ce que vous affirmez, et vérifiez sur une source officielle — pas sur un billet de blog."),
        ("a", "Le resserrement européen a-t-il supprimé les obligations françaises ?"),
        ("b", "Aucunement, et c'est l'angle mort classique. Les seuils français sont bien plus bas et les sanctions effectives. Le bilan d'émissions réglementaire s'impose au-delà de cinq cents salariés, tous les quatre ans, avec un plan de transition depuis 2023, sous peine de cinquante mille euros d'amende et d'exclusion des marchés publics."),
        ("a", "Ce qui explique l'appel d'offres perdu."),
        ("b", "En partie. Et il y a une exposition encore plus large, sans aucun seuil : le droit de la consommation. Il s'applique dès qu'on communique, quelle que soit la taille. C'est celle qu'on ignore le plus souvent, et c'est celle qui a mordu dans l'étude de cas."),
        ("a", "Raconte."),
        ("b", "Semaine 1, une demi-journée pour établir la carte des obligations. Conclusions attendues : non soumise à la CSRD, non soumise au bilan réglementaire à trois cent quatre-vingts salariés, soumise à l'index égalité, déjà traité. Et une conclusion inattendue : le site internet annonce des « livraisons neutres en carbone »."),
        ("a", "Et cette mention pose problème."),
        ("b", "Elle tombe sous le décret de 2022, qui exige la publication d'un bilan d'émissions, d'une trajectoire de réduction et du détail des projets de compensation. Aucun des trois n'existe. L'entreprise est en infraction, l'exposition est immédiate, et personne n'avait identifié le sujet."),
        ("a", "Qu'est-ce qui a été fait ?"),
        ("b", "La mention a été retirée du site le jour même, remplacée par une formulation factuelle sur les actions engagées. Coût : zéro. C'est le premier livrable de la fonction RSE, et il a supprimé le risque le plus concret du dossier en quelques heures. Comme démonstration d'utilité auprès d'une direction, c'est difficile à battre."),
        ("a", "Et le questionnaire de cent quatre-vingts questions ?"),
        ("b", "Lecture complète et classement en trois piles. Quarante questions relèvent du périmètre VSME et sont documentables rapidement. Soixante demandent des données que l'entreprise possède mais n'a jamais consolidées — consommations par site, répartition des achats, accidentologie. Quatre-vingts demandent des politiques formalisées ou des données de chaîne de valeur qui n'existent pas."),
        ("a", "Et la réponse au client ?"),
        ("b", "Un appel au responsable achats, pas un courriel. Message tenu : nous répondons intégralement sur le périmètre VSME, qui est le standard prévu pour les entreprises de notre taille, et nous ajoutons les consommations par site ; au-delà, la réglementation prévoit un droit de refus en dessous de mille salariés ; dites-nous lesquelles de ces questions sont réellement décisives et nous verrons ce que nous pouvons construire d'ici douze mois."),
        ("a", "Réaction du client ?"),
        ("b", "Douze questions sont déterminantes. Les autres relèvent d'un formulaire standard appliqué à tous les fournisseurs sans distinction de taille. Le périmètre passe de cent quatre-vingts à environ cent dix questions, dont douze qui comptent vraiment. C'est ce que produit un appel de vingt minutes appuyé sur un texte."),
        ("a", "Un mot sur les référentiels volontaires — ISO 26000, EcoVadis, les autres."),
        ("b", "Deux précisions qui évitent des dépenses inutiles. On ne peut pas être certifié ISO 26000 : c'est une ligne directrice, pas une norme certifiable, et l'entendre annoncé comme une certification est un bon révélateur. Et EcoVadis mesure la maturité d'un système de gestion, pas une performance environnementale physique. On peut avoir une très bonne note et des émissions en hausse."),
        ("a", "Comment on choisit, alors ?"),
        ("b", "À partir du demandeur, jamais l'inverse. Si vos clients demandent EcoVadis, vous faites EcoVadis. Sinon vous achetez une réponse à une question que personne ne pose. Et surtout, n'empilez pas les référentiels : chacun consomme du temps de production de preuves."),
        ("a", "Ce qui amène ton avertissement sur la RSE de conformité."),
        ("b", "Elle consomme toute la ressource en production de preuves, et il ne reste plus rien pour agir. Tenez un ratio explicite entre le temps passé à répondre et le temps passé à faire. Si vous ne le tenez pas, il glisse vers cent pour cent de réponse, sans que personne ne l'ait décidé."),
        ("a", "Dernier point du module : où placer la fonction."),
        ("b", "Le rattachement hiérarchique décide de tout. Seule la direction générale ou financière donne accès aux arbitrages d'investissement. Rattachée à la communication, la fonction produit des plaquettes ; rattachée aux ressources humaines, elle produit des actions internes. Aucune des deux ne pèse sur un budget d'équipement."),
        ("a", "Et sur la posture ?"),
        ("b", "La légitimité vient des chiffres, pas des convictions. Une position défendue par valeur est classée comme une opinion, et une opinion s'arbitre contre une autre opinion. Un chiffre, non."),
        ("a", "Par quoi on commence, alors ?"),
        ("b", "Surtout pas par la stratégie. L'ordre est : mesurer, prioriser sur les chiffres, agir, puis formaliser. Et choisir un premier livrable qui produise un résultat visible en six mois et qui serve à quelqu'un d'autre que vous."),
        ("a", "Ce qu'on fait demain ?"),
        ("b", "Ouvrez le site internet de votre entreprise et relevez toutes les affirmations environnementales qui s'y trouvent — neutralité, éco-responsable, engagé pour le climat. Pour chacune, demandez-vous si vous pourriez produire la preuve. C'est une heure de travail, et c'est souvent là que se trouve le risque le plus immédiat."),
        ("a", "Au module 2, on mesure. Merci Inès."),
    ],
}

# ============================================================
# Module 2 — Mesurer
# ============================================================

P["rse-transition-ecologique/module-2"] = {
    "formation": "RSE et transition écologique en entreprise",
    "titre": "Mesurer : le bilan d'émissions et les trois scopes",
    "module_id": "formation-rse-transition-ecologique-module-2",
    "hosts": HOSTS,
    "resume": "La difficulté d'un bilan carbone n'est pas le calcul : c'est la collecte, "
              "le périmètre et l'incertitude — et un facteur trois qu'il faut savoir trancher.",
    "lignes": [
        ("a", "Module 2. La décision est prise, l'entreprise fait son bilan d'émissions en interne, après un devis de cabinet à vingt-cinq mille euros jugé élevé pour une première itération. Et la première semaine ne se passe pas comme prévu."),
        ("b", "On croit toujours que la difficulté sera le calcul. Elle est ailleurs. Personne ne sait qui détient les relevés d'électricité des trois sites : la comptabilité a les factures, en euros, pas en kilowattheures. Les services généraux ont changé de fournisseur en cours d'année et ne retrouvent pas le premier semestre. Les achats ont un état par fournisseur, en montants, sans aucune quantité."),
        ("a", "Et le premier résultat ?"),
        ("b", "Il varie d'un facteur trois selon qu'on calcule les achats à partir des montants ou à partir des quantités physiques. Ces trois difficultés — la collecte, le périmètre, l'incertitude — sont l'essentiel du travail réel. Le calcul lui-même, c'est une multiplication."),
        ("a", "Justement, reprenons la base. Une tonne équivalent CO2, un facteur d'émission."),
        ("b", "Une donnée d'activité multipliée par un facteur d'émission. Mille litres de gazole, un facteur exprimé en kilos de CO2 par litre, et vous avez vos tonnes. Le facteur vient d'une base publique, la Base Empreinte en France."),
        ("a", "Et le piège ?"),
        ("b", "Précisez toujours la base, sa version, et le type de facteur. Sans cela, votre bilan n'est comparable à rien — pas même à lui-même l'année suivante. Et surtout, ne mélangez jamais des facteurs de périmètres différents dans un même bilan : chaque ligne serait juste, et le total dénué de sens."),
        ("a", "Les trois scopes, maintenant."),
        ("b", "Le scope 1, c'est ce que vous brûlez : vos chaudières, vos véhicules. Le scope 2, c'est l'énergie que vous achetez, essentiellement l'électricité. Le scope 3, c'est tout le reste : les achats, le transport, les déplacements, l'usage des produits vendus, la fin de vie."),
        ("a", "Et c'est le scope 3 le sujet."),
        ("b", "Il représente couramment de soixante-dix à plus de quatre-vingt-quinze pour cent du total. Un bilan limité aux scopes 1 et 2 mesure moins de quinze pour cent de l'empreinte. Ce n'est pas un bilan partiel, c'est un bilan qui regarde à côté."),
        ("a", "Certains le trouvent facultatif parce qu'il est difficile."),
        ("b", "C'est l'erreur centrale du module. Un ordre de grandeur incertain sur quatre-vingt-cinq pour cent de l'empreinte vaut infiniment mieux qu'une mesure précise sur quinze pour cent. On préfère souvent la précision parce qu'elle est confortable, mais elle ne dit rien."),
        ("a", "Et l'intérêt d'un bilan, ce n'est pas son total."),
        ("b", "C'est la hiérarchie qu'il révèle. Et cette hiérarchie est presque toujours contre-intuitive. On arrive en pensant que c'est le transport ou l'électricité, et on trouve les achats. Le total, lui, ne sert à rien tout seul."),
        ("a", "Parlons du périmètre. Tu dis qu'il s'écrit avant."),
        ("b", "Une note d'une page : les entités incluses, les postes inclus, les postes exclus avec leur motif, la base de facteurs, l'année de référence. Écrite avant de calculer, sinon le périmètre finit par être celui des données qu'on a réussi à trouver."),
        ("a", "Il y a un point technique sur l'année de référence."),
        ("b", "Prévoyez dès le départ la règle de recalcul. Sans elle, une cession d'activité fera apparaître une baisse d'émissions qui n'en est pas une. Et de manière générale : un changement de méthode n'est jamais une réduction. Si vous changez de méthode, présentez les deux effets séparément."),
        ("a", "La collecte, maintenant. Tu annonces soixante-dix pour cent du temps."),
        ("b", "Sur un premier bilan, oui. Donc elle se prépare comme un projet, avec un interlocuteur nommé par donnée et une date. Et on commence par les postes lourds, pas par ceux dont la donnée est facile — sinon on passe trois semaines sur deux pour cent de l'empreinte."),
        ("a", "Ton conseil le plus concret sur la collecte ?"),
        ("b", "Demandez les consommations en kilowattheures, pas en euros. C'est la première cause de blocage, et elle se règle en formulant la demande correctement dès le premier message."),
        ("a", "Et la méthode d'ensemble ?"),
        ("b", "Deux passes. La première couvre cent pour cent du périmètre, grossièrement, avec des ratios là où il le faut. La seconde raffine les trois ou quatre postes qui font quatre-vingts pour cent du total. Attendre la donnée parfaite avant de publier est la façon la plus sûre de ne jamais publier."),
        ("a", "On arrive à l'étude de cas, le fameux facteur trois."),
        ("b", "Sur les achats, le calcul par ratios monétaires donne deux mille neuf cents tonnes ; le calcul physique, extrapolé, environ neuf cents. La tentation immédiate est de retenir le chiffre qui arrange — le plus flatteur, ou le plus prudent selon le tempérament. Les deux réflexes sont mauvais."),
        ("a", "Parce que ?"),
        ("b", "Un écart de ce type est une information. Il faut l'expliquer avant de conclure. Et le geste décisif, c'est de le localiser plutôt que de le constater : on décompose famille par famille au lieu de regarder le total."),
        ("a", "Ça donne quoi ?"),
        ("b", "Sur six familles d'achats, quatre donnent des résultats cohérents à vingt pour cent près entre les deux méthodes. L'écart provient presque intégralement de deux familles : la sous-traitance et le matériel informatique. Un écart global est ininterprétable ; un écart concentré sur deux postes se diagnostique."),
        ("a", "Et le diagnostic ?"),
        ("b", "La sous-traitance, c'est quatre virgule deux millions d'euros d'achats. Le ratio monétaire du secteur des services donne environ mille cent tonnes. Or l'essentiel de ces prestations est de la main-d'œuvre facturée à un taux journalier élevé : le montant est important, le contenu matériel est faible. Le ratio surestime massivement."),
        ("a", "Et l'informatique ?"),
        ("b", "Trois cent quatre-vingts mille euros. Le ratio monétaire donne environ quatre-vingt-dix tonnes ; le calcul physique — deux cent dix ordinateurs portables, quarante écrans, des serveurs — en donne environ deux cent quarante. Ici le ratio sous-estime, parce que la fabrication d'un équipement électronique est très émettrice rapportée à son prix."),
        ("a", "Deux biais de sens contraire."),
        ("b", "Qui se compensent partiellement, ce qui rendait l'écart global encore plus trompeur. Le total masquait les deux. C'est pour ça qu'on ne raisonne jamais sur un total."),
        ("a", "Et la règle de décision, finalement ?"),
        ("b", "En une phrase : on retient la donnée physique partout où elle existe et où le facteur est adapté, et on conserve le ratio monétaire ailleurs, en le signalant. C'est une règle qu'on peut écrire, défendre et reproduire l'année suivante — ce qui est exactement ce qu'on demande à une méthode."),
        ("a", "Parlons de l'incertitude, parce que beaucoup de gens la cachent."),
        ("b", "Un bilan est une estimation, pas une comptabilité. Ce qui est attendu, c'est la traçabilité, pas l'exactitude. Et afficher son incertitude rend un bilan plus crédible : une fausse précision — quatre mille sept cent douze virgule trois tonnes — signale au contraire que la méthode n'a pas été comprise."),
        ("a", "Comment on la présente utilement ?"),
        ("b", "On teste la robustesse des conclusions aux bornes hautes et basses. Si la conclusion « les achats sont le premier poste » tient dans les deux cas, c'est ça qu'on présente — pas le chiffre central. La conclusion est solide même si le nombre ne l'est pas."),
        ("a", "Tu recommandes aussi de publier deux chiffres."),
        ("b", "L'absolu et l'intensité, par exemple les tonnes par million d'euros de chiffre d'affaires. L'absolu mesure ce que l'atmosphère reçoit ; l'intensité mesure l'effort accompli. Une entreprise en croissance peut améliorer son intensité et augmenter son absolu — les deux sont vrais et il faut les dire tous les deux."),
        ("a", "Un garde-fou pratique ?"),
        ("b", "Ayez des ordres de grandeur en tête. L'erreur la plus fréquente d'un premier bilan est un facteur mille sur une unité — des kilos pris pour des tonnes. Un résultat qui ne ressemble à rien de connu est presque toujours une erreur d'unité, pas une découverte."),
        ("a", "Et sur la restitution ?"),
        ("b", "Un bilan n'est pas une performance, c'est un diagnostic. Consacrez trois quarts de la restitution à ce qu'on en fait. Présenter le total comme un résultat oriente immédiatement la discussion vers « est-ce que c'est beaucoup ? », qui est une question sans réponse utile."),
        ("a", "Ce qu'on fait demain ?"),
        ("b", "Demandez à votre comptabilité l'état des achats de l'année dernière par famille, en montants. Une heure, et vous saurez déjà où se situe probablement votre premier poste d'émissions — avant même d'avoir calculé quoi que ce soit."),
        ("a", "Au module 3, on priorise et on chiffre. Merci Inès."),
    ],
}

# ============================================================
# Module 3 — Double matérialité et plan d'action
# ============================================================

P["rse-transition-ecologique/module-3"] = {
    "formation": "RSE et transition écologique en entreprise",
    "titre": "Double matérialité et plan d'action : prioriser, chiffrer, embarquer",
    "module_id": "formation-rse-transition-ecologique-module-3",
    "hosts": HOSTS,
    "resume": "Comment passer d'un bilan à un plan qui soit réellement exécuté : "
              "un seuil assumé, quatre leviers, le coût de la tonne évitée et un porteur nommé.",
    "lignes": [
        ("a", "Module 3. Le bilan est fait : quatre mille sept cents tonnes, dont soixante-deux pour cent sur les achats. La direction demande un plan pour le comité de janvier, dans dix semaines."),
        ("b", "Et deux écueils symétriques attendent. Le premier : produire une liste de quarante actions sans hiérarchie, où le remplacement des gobelets figure à côté de la refonte d'une famille d'achats. Ce document sera approuvé sans discussion — parce qu'on n'arbitre pas une liste de quarante lignes — et rien n'en sortira."),
        ("a", "Et le second ?"),
        ("b", "Retenir trois actions visibles et faciles, dont l'effet cumulé fera deux pour cent de l'empreinte, et se retrouver dans deux ans à devoir expliquer pourquoi rien n'a bougé."),
        ("a", "Il y a aussi une difficulté que le bilan n'a pas vue."),
        ("b", "Le comité social et économique a remonté deux sujets : les conditions de travail des équipes de nuit à l'entrepôt, et l'absence de perspectives pour les postes les moins qualifiés. Ces sujets n'émettent pas une tonne de CO2. Ils comptent pourtant, ils relèvent bien de la RSE, et aucun bilan carbone ne les fera jamais apparaître."),
        ("a", "C'est l'effet pervers de la qualité du carbone."),
        ("b", "Ce qui ne se mesure pas en tonnes disparaît du champ de vision. D'où la consigne : établissez la liste d'enjeux avant de regarder les chiffres, sinon le plan sera amputé de sa moitié sociale."),
        ("a", "D'où la double matérialité. Mais si on n'est pas soumis au reporting, à quoi sert-elle ?"),
        ("b", "C'est d'abord une méthode pour décider ce sur quoi on travaille. Elle est utile même sans aucune obligation. La règle est simple : un enjeu est matériel s'il l'est en impact ou en financier — l'un ou l'autre suffit. Ce « ou » empêche d'écarter un impact réel au motif qu'il ne coûte rien à l'entreprise."),
        ("a", "Comment on la conduit sans y passer six mois ?"),
        ("b", "Six semaines. On reprend les thèmes des standards européens et on les reformule pour l'entreprise — une vingtaine d'enjeux. On consulte. On cote en réunion, deux heures. Et on tranche."),
        ("a", "La consultation, on est tenté de la sauter."),
        ("b", "Elle coûte une heure et elle apporte l'information que vous n'avez pas. Dans le cas : neuf entretiens de vingt minutes. Ne la supprimez jamais du calendrier — c'est toujours la première variable d'ajustement, et c'est toujours une erreur."),
        ("a", "Et la cotation ?"),
        ("b", "Deux règles qui évitent la matrice qui ne décide rien. Fixez le nombre d'enjeux retenus avant de coter, et laissez la cotation déterminer lesquels — sinon on ajuste le seuil pour garder tout le monde content. Et prenez une échelle à quatre niveaux : une échelle à dix rend les arbitrages impossibles, tout finit à six ou sept."),
        ("a", "Écarter, c'est un livrable ?"),
        ("b", "C'est le livrable. Une analyse qui conclut que tout est important n'a rien décidé. Dans le cas : vingt-six enjeux au départ, dix retenus, seize écartés — chacun avec sa phrase de justification, ce qui permet de le rouvrir plus tard sans repartir de zéro."),
        ("a", "Et les deux sujets du comité social et économique ?"),
        ("b", "Retenus tous les deux, le travail de nuit avec la cotation d'impact maximale. Il y a eu une objection en séance : « ce n'est pas de la RSE, c'est des ressources humaines ». La réponse donnée : trente personnes, un absentéisme double, un impact direct sur la santé — si cela n'est pas de la responsabilité sociétale, le mot n'a plus de sens."),
        ("a", "Et l'argument a porté."),
        ("b", "Il a été accepté, et ce moment a probablement fait plus pour la crédibilité de la fonction que tout le bilan carbone. Parce qu'il montrait que la RSE servait à traiter un problème réel de l'entreprise, pas à produire un rapport."),
        ("a", "Passons du poste d'émission à l'action."),
        ("b", "Un poste d'émission n'est pas une action. « Les achats » n'est pas actionnable. On décompose jusqu'au niveau où une action est concevable : quelle famille, quel fournisseur, quel produit. Ensuite seulement on passe les quatre leviers."),
        ("a", "Quels sont ces quatre leviers ?"),
        ("b", "Consommer moins, substituer, améliorer l'efficacité, agir sur la chaîne de valeur. Quatre, pas davantage. Et le premier est le plus efficace et le plus négligé, parce qu'il touche à l'organisation et non à la technique. On préfère toujours changer un équipement plutôt que de changer une habitude."),
        ("a", "Sur la chaîne de valeur, tu as une consigne précise."),
        ("b", "On ne travaille pas avec trois cents fournisseurs, mais avec cinq. Un courrier envoyé au panel entier ne produit rien — il produit du taux de réponse, pas de la réduction. Cinq fournisseurs qui pèsent, une vraie conversation avec chacun."),
        ("a", "Vient le chiffrage. Quatre chiffres par action."),
        ("b", "Tonnes évitées, coût, délai, effet financier. Sans les quatre, c'est une intention, pas une action. Et on les obtient en allant voir les personnes concernées, pas en estimant depuis son bureau."),
        ("a", "Et si on n'y arrive pas ?"),
        ("b", "On reclasse en « à instruire ». Dans le cas, cinq pistes sur quatorze. C'est une conclusion honnête, pas un échec — et ça évite de mettre au plan des actions dont personne ne sait ce qu'elles coûtent."),
        ("a", "Le coût de la tonne évitée, c'est l'outil central ?"),
        ("b", "Il permet de comparer des actions qui n'ont rien à voir entre elles, et il révèle celles qui rapportent. Dans le cas : neuf actions chiffrées, trois à coût négatif — donc qui font gagner de l'argent — quatre entre quarante et cent vingt euros la tonne, et deux au-delà de quatre cents."),
        ("a", "Une découverte au passage ?"),
        ("b", "La réduction des invendus, envisagée au départ comme une action secondaire, s'est révélée la meilleure du plan. Le directeur commercial la poussait depuis deux ans sans succès, pour des raisons purement financières. Le bilan carbone lui a donné un second argument — et c'est l'argument supplémentaire qui a débloqué le sujet, pas le premier."),
        ("a", "C'est une leçon assez générale, non ?"),
        ("b", "Très. Une bonne partie de ce qu'un plan RSE fait aboutir, ce sont des projets qui existaient déjà et qui manquaient d'un allié. Chercher ces projets-là avant d'en inventer de nouveaux est le meilleur usage des premières semaines."),
        ("a", "Un mot sur l'objectif chiffré, celui qu'on annonce."),
        ("b", "Il découle de la somme des actions, jamais l'inverse. Un objectif annoncé avant le plan se comblera par de la compensation, parce qu'il faudra bien tenir la promesse. Et la règle est : réduire d'abord, contribuer ensuite et à part. Compenser avant d'avoir réduit vous prive de l'argument d'avoir fait le travail."),
        ("a", "Reste l'exécution. Qu'est-ce qui fait qu'un plan est exécuté ?"),
        ("b", "Trois choses. Chaque action a un porteur qui n'est pas vous. Le budget est logé chez ce porteur, pas dans un budget RSE séparé — un budget séparé marginalise le sujet et le rend arbitrable en bloc. Et l'indicateur est suivi."),
        ("a", "Quel type d'indicateur ?"),
        ("b", "Des indicateurs d'avancement, mesurés chaque mois. Les tonnes évitées se mesurent une fois par an, ce qui est beaucoup trop tard pour corriger quoi que ce soit. On suit l'exécution, pas le résultat."),
        ("a", "Combien d'actions par an ?"),
        ("b", "Cinq au maximum. La contrainte n'est pas le budget, c'est l'attention disponible des porteurs. Un plan à quinze actions est un plan à trois actions réelles et douze lignes qui glissent."),
        ("a", "Un dernier geste, avant le comité ?"),
        ("b", "Faites valider chaque action par son porteur en bilatéral, avant la séance. C'est le geste qui décide de l'exécution. Une action découverte en comité par celui qui devra la porter est une action perdue, même si elle est votée."),
        ("a", "Et la sensibilisation, dans tout ça ?"),
        ("b", "Elle crée un langage commun et elle ne réduit aucune émission. Comptez-la ailleurs que dans le plan de réduction. Confondre sensibilisation et action est la façon la plus courante de produire un plan qui ne fait rien baisser."),
        ("a", "Ce qu'on fait demain ?"),
        ("b", "Prenez votre premier poste d'émissions et décomposez-le jusqu'au niveau où vous pouvez nommer une action et une personne. Si vous n'y arrivez pas, vous n'avez pas encore décomposé assez loin — c'est le meilleur test qui soit."),
        ("a", "Au module 4, on rend compte, et on évite le greenwashing. Merci Inès."),
    ],
}

# ============================================================
# Module 4 — Reporting, communication et greenwashing
# ============================================================

P["rse-transition-ecologique/module-4"] = {
    "formation": "RSE et transition écologique en entreprise",
    "titre": "Reporting, communication et greenwashing",
    "module_id": "formation-rse-transition-ecologique-module-4",
    "hosts": HOSTS,
    "resume": "Trois formulations sur quatre exposent à une sanction, dont une qui repose sur "
              "un chiffre exact. Comment refuser sans bloquer, et rendre compte honnêtement.",
    "lignes": [
        ("a", "Dernier module. Le plan a produit : environ deux cent quatre-vingt-dix tonnes évitées et cent dix-huit mille euros d'économies nettes sur douze mois. Le comité de direction veut le faire savoir."),
        ("b", "Et le marketing revient avec quatre formulations. « Une entreprise engagée pour le climat. » « Nos livraisons sont neutres en carbone. » « Moins vingt pour cent d'émissions depuis 2024. » « Une gamme éco-responsable. » Trois de ces quatre vous exposent à une sanction, et la quatrième est contestable."),
        ("a", "Laquelle est la plus délicate ?"),
        ("b", "La troisième, parce qu'elle repose sur un chiffre réel. Les émissions ont bien baissé de vingt pour cent — mais l'essentiel de cette baisse vient d'un changement de méthode de calcul sur les achats, pas d'une réduction. Le marketing ne le sait pas. Vous, si."),
        ("a", "Commençons par la distinction de fond du module."),
        ("b", "Le reporting rend compte devant un lecteur qui évalue. La communication valorise devant un lecteur qu'on veut convaincre. Ce sont deux exercices différents, et les confondre produit la plupart des accidents. La règle qui les relie : tout ce qui est communiqué doit être retrouvable, au même périmètre, dans un document de reporting que vous accepteriez de montrer à un contradicteur."),
        ("a", "Qui valide, dans l'entreprise ?"),
        ("b", "La fonction RSE valide toute communication environnementale avant diffusion. Elle seule sait ce que les chiffres recouvrent. Ce n'est pas une question de pouvoir, c'est une question de qui connaît le périmètre."),
        ("a", "Parlons du cadre juridique, qui s'est beaucoup resserré."),
        ("b", "Deux choses à retenir. Le droit de la consommation s'applique sans aucun seuil de taille dès qu'une entreprise communique — il n'y a pas de PME protégée ici. Et la directive européenne sur les allégations, dite EmpCo, s'applique au 27 septembre 2026 dans tous les États membres, sans seuil, et vise directement les formules génériques."),
        ("a", "Et le principe qui sous-tend tout ça ?"),
        ("b", "La preuve doit avoir la même profondeur que l'allégation. Si vous dites « engagés pour le climat », vous devez prouver un engagement global. Si vous dites « moins trente pour cent d'émissions de fabrication sur cette gamme, périmètre matières et transport », vous devez prouver exactement ça — ce qui est beaucoup plus facile."),
        ("a", "Donc être précis protège."),
        ("b", "Plus vous êtes précis, plus vous êtes en sécurité, et plus vous êtes convaincant. C'est assez rare pour être signalé : le droit pousse ici exactement dans le même sens qu'une bonne communication."),
        ("a", "Revenons au cas du chiffre exact qui dit quelque chose de faux."),
        ("b", "C'est le point le plus subtil du module. Le droit s'intéresse à ce que l'affirmation fait comprendre au lecteur, pas à son exactitude arithmétique. « Moins vingt pour cent depuis 2024 » est arithmétiquement vrai et fait comprendre une réduction qui n'a pas eu lieu. Un changement de méthode de calcul n'est jamais une réduction d'émissions."),
        ("a", "Reprenons les quatre formulations, une par une, avec leur version défendable."),
        ("b", "« Une entreprise engagée pour le climat » : allégation générique, périmètre implicite l'entreprise entière, preuve disponible un plan de cinq actions et deux cent quatre-vingt-dix tonnes. Version défendable : « nous nous sommes engagés à réduire nos émissions de dix-huit pour cent d'ici 2030, plan et résultats publiés »."),
        ("a", "La neutralité des livraisons ?"),
        ("b", "Doublement exposée : mention de neutralité reposant sur une compensation, sans bilan, trajectoire et projets publiés au sens du décret de 2022. Version défendable : « nous avons réduit de douze pour cent les émissions de nos livraisons depuis 2024, et nous finançons un projet de reforestation à hauteur de quatre-vingts tonnes ». Les deux éléments séparés, aucun n'annulant l'autre."),
        ("a", "Le moins vingt pour cent ?"),
        ("b", "« Deux cent quatre-vingt-dix tonnes de CO2 évitées en 2026 grâce à quatre actions, soit six pour cent de nos émissions. » C'est plus modeste, c'est vrai, et c'est incontestable."),
        ("a", "Et la gamme éco-responsable ?"),
        ("b", "Allégation générique sur un périmètre produit. Version défendable, sous réserve de vérifier les fiches fournisseur : « une gamme dont les émissions de fabrication sont inférieures de trente pour cent à notre gamme standard, sur le périmètre matières et transport »."),
        ("a", "Il y a d'autres formulations qui exposent ?"),
        ("b", "Trois autres à connaître. Un label auto-décerné, ou décerné par une structure que l'on finance, tombe sous l'interdiction des labels non certifiés. Une comparaison sans point de comparaison explicite n'est pas défendable. Et présenter le respect d'une obligation légale comme un engagement est explicitement interdit — le tri des déchets n'est pas une initiative."),
        ("a", "Un réflexe d'archivage ?"),
        ("b", "Constituez un dossier de preuves et gardez-le. Un contrôle peut porter sur une communication d'il y a deux ans, et les personnes qui l'ont produite ne sont plus forcément là."),
        ("a", "Venons-en à l'étude de cas : comment on refuse trois formulations sur quatre sans bloquer le communiqué."),
        ("b", "Jour 1 : ne pas répondre par un refus dans la journée. On reprend chaque formulation avec les cinq questions de validation et on prépare la version défendable de chacune. Une heure de travail. On arrive ensuite à la conversation avec des propositions plutôt qu'avec des objections."),
        ("a", "Et la conversation elle-même ?"),
        ("b", "Jour 2, seul à seul avec le marketing. Pas en réunion, pas par courriel. L'enjeu n'est pas de gagner un arbitrage, c'est d'installer un réflexe durable — et cela ne se fait pas devant témoins."),
        ("a", "L'ordre de la conversation compte, tu dis."),
        ("b", "Énormément. D'abord ce qui est possible : « on a un excellent message, deux cent quatre-vingt-dix tonnes et cent dix-huit mille euros, et personne ne peut le contester ». Ensuite le cadre, sans dramatiser : il y a un texte européen qui s'applique fin septembre, sans seuil de taille, et il vise exactement les formules génériques. Ce n'est pas propre à votre entreprise."),
        ("a", "Et ce qu'il ne faut surtout pas faire ?"),
        ("b", "Ne dites jamais « greenwashing » à un collègue. Le mot accuse, il ferme la discussion, et il est presque toujours inexact — la personne en face ne cherche pas à tromper, elle ne sait pas ce que le chiffre recouvre."),
        ("a", "Et un refus sec ?"),
        ("b", "Un refus sans version de remplacement crée un adversaire. Une reformulation crée un processus. La deuxième fois, le marketing viendra vous voir avant d'écrire — et c'est ça, le vrai résultat de la conversation, pas le communiqué."),
        ("a", "Passons au rapport. Que publier quand on n'y est pas obligé ?"),
        ("b", "Peu, mais solide. Chaque affirmation porte un chiffre, une date et un périmètre. Sans les trois, elle n'apporte aucune information. Et une règle qui surprend : publiez au moins un objectif manqué et un poste non couvert, chiffré."),
        ("a", "Pourquoi publier ses faiblesses ?"),
        ("b", "Parce qu'un rapport entièrement positif décrédibilise tout le reste. Un lecteur averti sait qu'aucune démarche ne réussit sur toute la ligne. L'aveu chiffré est ce qui rend le reste crédible."),
        ("a", "Et si on rate un objectif annoncé ?"),
        ("b", "Ça s'écrit. Se taire expose, et retirer discrètement un objectif du site se remarque — quelqu'un a toujours gardé la version précédente. On écrit l'écart, sa cause, et ce qu'on change."),
        ("a", "Un principe pour éviter que le rapport devienne un exercice autonome ?"),
        ("b", "Le rapport ne contient que ce qui sert déjà en interne. Aucun indicateur n'est créé pour être publié. Le jour où vous produisez des chiffres que personne n'utilise dans l'entreprise, le rapport est devenu une fin en soi et il mourra avec la personne qui le porte."),
        ("a", "Justement : ce qui fait tenir une démarche au-delà d'une personne."),
        ("b", "L'intérêt bien compris de ceux qui l'exécutent, pas leur adhésion à ses finalités. C'est la phrase la plus importante du module. Une action portée par un directeur commercial parce qu'elle réduit ses invendus tiendra ; une action portée par conviction personnelle partira avec la personne."),
        ("a", "Donc on n'attend pas l'adhésion."),
        ("b", "Attendre l'adhésion pour agir, c'est ne jamais commencer. On agit, les résultats arrivent, et l'adhésion vient après — dans cet ordre-là."),
        ("a", "Ce qu'on fait demain ?"),
        ("b", "Prenez la dernière communication environnementale de votre entreprise et posez-vous une question : si un journaliste me demandait la preuve de cette phrase, dans quel document je la trouve et à quel périmètre ? Si vous ne savez pas répondre en deux minutes, la phrase est à reformuler."),
        ("a", "Quatre modules, du cadre au communiqué. Merci Inès, et bravo à celles et ceux qui sont allés au bout."),
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
