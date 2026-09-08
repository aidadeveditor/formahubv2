#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Formahub — podcasts de la formation Bilan de compétences et repositionnement.

  a = Camille, animatrice de la série ;
  b = Marc, consultant en évolution professionnelle.

Trois épisodes d'environ 9 minutes : l'inventaire, l'exploration du marché,
la conversion. Chaque épisode reprend la mise en situation du module, ses
idées structurantes et l'étude de cas chiffrée, et se termine par ce qu'on
peut faire dès le lendemain.

Usage :
    FH_OUT=<dossier formations> python3 _tooling/podcast_bilan.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_podcasts as bp

HOSTS = {
    "a": {"nom": "Camille", "role": "animatrice"},
    "b": {"nom": "Marc", "role": "consultant en évolution professionnelle"},
}

P = {}

# ============================================================
# Module 1 — Faire l'inventaire
# ============================================================

P["bilan-competences/module-1"] = {
    "formation": "Bilan de compétences et repositionnement",
    "titre": "Faire l'inventaire : extraire ses compétences transférables",
    "module_id": "formation-bilan-competences-module-1",
    "hosts": HOSTS,
    "resume": "Pourquoi huit ans de métier produisent une expertise dense et l'incapacité à la nommer, "
              "et comment en sortir en partant de réalisations datées plutôt que de souvenirs.",
    "lignes": [
        ("a", "Premier module de la formation Bilan de compétences. Marc, la situation de départ est très concrète : huit ans dans la même entreprise, un contrat qui se termine dans six mois, et un CV qui commence par « responsable de l'animation commerciale d'un portefeuille de quarante partenaires »."),
        ("b", "C'est exact, et c'est incompréhensible pour quiconque ne connaît pas le secteur. Trois recruteurs ont posé la même question — « concrètement, vous faisiez quoi ? » — et la personne s'est entendue répondre en décrivant son entreprise plutôt que son travail."),
        ("a", "Derrière ça, tu dis qu'il y a une difficulté plus profonde."),
        ("b", "Elle ne sait pas elle-même quelles compétences elle possède au-delà de son secteur. Huit ans d'un métier produisent deux choses en même temps : une expertise dense, et l'incapacité à la nommer. Parce que ce qu'on fait tous les jours cesse d'apparaître comme une compétence. Ça devient « normal », donc invisible."),
        ("a", "Commençons par le vocabulaire, alors. Qu'est-ce qu'une compétence, exactement ?"),
        ("b", "Ce n'est ni une tâche, ni un savoir, ni un trait de caractère. « Gérer les plannings », c'est une tâche. « Connaître le droit du travail », c'est un savoir. « Rigoureux », c'est un trait de caractère, et c'est invérifiable. Une compétence, c'est ce que vous savez faire, avec un résultat observable."),
        ("a", "Comment on la formule, du coup ?"),
        ("b", "Un verbe d'action, un objet, un contexte, un résultat. Pas « bon relationnel », mais « obtenir l'accord de partenaires indépendants sans lien hiérarchique, sur un réseau de quarante points de vente ». C'est plus long, c'est vérifiable, et surtout ça se discute en entretien."),
        ("a", "Il y a une erreur que tu appelles « confondre modestie et imprécision »."),
        ("b", "Beaucoup de gens croient qu'être précis, c'est se vanter. C'est l'inverse. La règle qui règle le problème : ne portez aucun jugement sur vous-même, décrivez des faits et laissez le lecteur juger. « Excellente pédagogue » est prétentieux et invérifiable. « Cent soixante personnes formées l'an dernier, sur des sessions auxquelles elles n'étaient pas obligées de venir » est factuel — et beaucoup plus convaincant."),
        ("a", "Passons à la méthode. Tu insistes pour qu'on parte des réalisations, pas des compétences."),
        ("b", "C'est le point le plus important du module. Si vous vous demandez « quelles sont mes compétences ? », vous répondez ce que vous croyez déjà savoir de vous, et vous tournez en rond. Si vous listez quinze à vingt-cinq réalisations datées et que vous en extrayez ensuite les capacités, vous découvrez des choses. L'ordre compte."),
        ("a", "Vingt-cinq réalisations, c'est beaucoup."),
        ("b", "C'est le volume qui fait apparaître les récurrences. Une compétence qui revient dans cinq réalisations, sur cinq contextes différents, est solide. Une qui n'apparaît qu'une fois est peut-être un concours de circonstances. C'est la répétition qui sert de preuve, et elle n'apparaît pas en dessous de quinze."),
        ("a", "Et il y a une contrainte de rédaction que tu qualifies d'inconfortable."),
        ("b", "Employer « je », jamais « nous ». C'est désagréable, ça sonne égocentrique, et c'est exactement ce qui distingue votre contribution de celle de l'équipe. Dans l'étude de cas, six fiches sur vingt ont dû être réécrites pour cette raison. Deux d'entre elles ont révélé que la contribution personnelle était mince — elles ont été retirées. Les quatre autres ont fait apparaître une contribution précise que le récit collectif masquait."),
        ("a", "Il y a une question qui revient souvent dans ce module et qui a l'air très efficace."),
        ("b", "« Quand tu dis que vous avez décidé de changer d'approche, qui a proposé ce changement, et qu'as-tu dû faire pour qu'il soit accepté ? ». Posée cinq ou six fois par la personne qui aidait, elle a produit l'essentiel de l'inventaire final. C'est pour ça que je recommande de faire l'exercice à deux : seul, on ne se pose jamais cette question."),
        ("a", "Autre travers : ne retenir que les grands succès."),
        ("b", "Le quotidien porte l'essentiel de vos compétences réelles. Et j'ajoute une chose que presque personne ne prépare : les échecs rattrapés sont le meilleur matériau d'entretien qui existe. Un projet qui a dérapé et que vous avez remis d'aplomb en dit infiniment plus sur ce que vous savez faire qu'un succès linéaire."),
        ("a", "Une fois qu'on a l'inventaire, comment on le trie ?"),
        ("b", "Trois familles. Les compétences techniques : faciles à nommer, et les moins transférables — elles sont attachées à un outil ou à un secteur. Les compétences transverses : plus difficiles à nommer, et les plus transférables. Et les compétences comportementales, entre les deux. Le paradoxe du repositionnement, c'est que ce qui est le plus facile à écrire est le moins utile pour changer de métier."),
        ("a", "Tu ajoutes une nuance importante sur la transférabilité."),
        ("b", "Une compétence transférable qu'aucun employeur ne sait reconnaître dans votre formulation ne vous sert à rien. La transférabilité n'est pas une propriété de la compétence, c'est une propriété de la façon dont vous la dites. C'est tout le travail du module 2."),
        ("a", "Parlons des compétences invisibles, c'est une notion que j'aime beaucoup."),
        ("b", "Il faut aller les chercher délibérément, avec quatre questions. Qu'est-ce que je fais tous les jours sans y penser ? Qu'est-ce que les collègues viennent me demander spontanément ? Qu'est-ce que j'ai appris par nécessité, parce qu'il n'y avait personne d'autre ? Et qu'est-ce qui vient d'ailleurs que du travail ?"),
        ("a", "La deuxième est frappante."),
        ("b", "Les sollicitations spontanées de collègues sont l'information la plus fiable qui existe sur vos compétences, et elle est gratuite. Quand trois personnes viennent vous voir pour la même chose, c'est qu'elles ont identifié une capacité que vous ne voyez plus."),
        ("a", "Venons-en à l'étude de cas. Cinq semaines, deux heures par semaine."),
        ("b", "Semaine 1, la liste brute, sans filtrer : trente-huit lignes. Et deux surprises immédiates. Un remplacement de six mois sur un poste de coordination logistique, jamais mentionné parce que c'était « juste un remplacement ». Et l'organisation bénévole d'un événement annuel de trois cents personnes depuis quatre ans, écartée parce que « pas professionnelle »."),
        ("a", "Aucune des deux au CV."),
        ("b", "Et ce sont pourtant celles qui portent les compétences de gestion de projet les plus démontrables du parcours. C'est pour ça que la consigne est de ne rien filtrer pendant l'inventaire : le tri vient après, et il ne se fait pas sur l'étiquette « professionnel » ou « bénévole »."),
        ("a", "Semaine 4, l'extraction."),
        ("b", "Cinquante-deux mentions de capacités relevées sur les vingt fiches, regroupées en quatorze compétences distinctes. Six apparaissent dans cinq réalisations ou plus, sur des contextes différents : analyser des données pour poser un diagnostic ; conduire un entretien d'exploration ; concevoir et animer une formation pour un public non captif ; obtenir un résultat sans lien hiérarchique ; documenter une demande pour obtenir un arbitrage ; construire un outil de suivi utilisé par d'autres."),
        ("a", "Et le chiffre qui résume tout ?"),
        ("b", "Quatre de ces six ne figuraient dans aucune version antérieure du CV. Pas parce qu'elles étaient cachées — parce qu'elles étaient trop quotidiennes pour être remarquées."),
        ("a", "Un mot sur le dispositif lui-même, le bilan de compétences officiel. Qu'est-ce qu'il apporte ?"),
        ("b", "Il structure une réflexion et il impose un calendrier, ce qui est déjà beaucoup. Mais il ne donne pas de réponse, et aucun dispositif ne le fait. Attendre qu'il décide à votre place est le meilleur moyen d'en sortir déçu. Deux points pratiques : le document de synthèse vous appartient, il ne peut être communiqué à personne sans votre accord écrit, y compris à un employeur qui l'aurait financé. Et les conditions de financement ont changé plusieurs fois en deux ans — vérifiez-les sur une source officielle, pas sur un article."),
        ("a", "Il y a d'autres dispositifs."),
        ("b", "Quatre besoins, quatre réponses. S'orienter, c'est le bilan. Être conseillé, c'est le conseil en évolution professionnelle. Certifier ce qu'on sait déjà faire, c'est la validation des acquis. Combler un écart identifié, c'est une formation. Identifiez le besoin avant de choisir l'outil — et surtout, la formation vient après le ciblage. En engager une pour trouver sa voie est la façon la plus coûteuse de retarder la décision."),
        ("a", "Dernier point : l'inventaire ne dit pas tout."),
        ("b", "Ce que vous savez faire et ce que vous voulez faire ne se superposent pas. Une compétence forte peut être associée à un rejet net, et c'est une raison parfaitement légitime. Il faut donc poser à côté de l'inventaire une deuxième liste : ce que je ne veux plus, en distinguant le rédhibitoire de l'acceptable. Sans cette distinction, on écarte des pistes entières pour un critère secondaire."),
        ("a", "On arrive à quoi, à la fin du module ?"),
        ("b", "À trois ou quatre hypothèses de cible. Pas à un métier. Une seule piste est une fermeture prématurée, douze est une absence de tri. Trois ou quatre, c'est ce que le module 2 va pouvoir tester."),
        ("a", "Ce qu'on fait demain ?"),
        ("b", "Prenez une feuille et notez dix réalisations des trois dernières années, sans filtrer, y compris ce qui n'est pas professionnel. Puis reprenez la première et réécrivez-la avec « je ». Vous verrez tout de suite si la phrase tient."),
        ("a", "Au module 2, on sort de soi pour aller regarder le marché. Merci Marc."),
    ],
}

# ============================================================
# Module 2 — Cibler et explorer le marché
# ============================================================

P["bilan-competences/module-2"] = {
    "formation": "Bilan de compétences et repositionnement",
    "titre": "Cibler : explorer un marché et tester ses hypothèses",
    "module_id": "formation-bilan-competences-module-2",
    "hosts": HOSTS,
    "resume": "Quarante candidatures sans réponse n'apprennent rien. Comment comprendre un marché "
              "avant de s'y présenter, par l'entretien exploratoire.",
    "lignes": [
        ("a", "Module 2, et la situation de départ est déprimante : quarante candidatures, deux refus automatiques, trente-huit silences, aucun entretien. La conclusion qui s'impose, c'est que le marché est fermé."),
        ("b", "Et cette conclusion est presque certainement fausse. Elle repose sur une erreur de méthode, pas sur une réalité du marché. La personne a candidaté avant d'avoir compris. Elle ne sait pas comment ces postes sont réellement pourvus, ni ce que recouvrent leurs intitulés, ni pourquoi son profil est écarté."),
        ("a", "Le silence ne dit rien."),
        ("b", "C'est le point de départ du module. Un désaccord de vocabulaire et une incompétence réelle produisent exactement le même silence. Quarante candidatures sans réponse n'apprennent rien du tout — c'est un signal sans contenu. Et pendant qu'on les envoie, on croit travailler."),
        ("a", "Ta recommandation est radicale : arrêter de candidater."),
        ("b", "Quatre semaines sans aucune candidature. Ce temps sert à comprendre le marché. C'est l'étape que presque tout le monde saute parce qu'elle ne produit rien de visible, et c'est elle qui détermine l'essentiel de ce qui suit."),
        ("a", "Commençons par la cible. Qu'est-ce qui distingue une hypothèse d'une cible ?"),
        ("b", "« La formation » n'est pas une cible, c'est un mot. Une cible comporte quatre éléments : un poste, un type d'organisation, une zone géographique et un niveau. « Formateur interne, en entreprise de plus de deux cents salariés, à moins de quarante minutes de chez moi, sur des fonctions terrain » — ça, c'est testable. On peut aller vérifier si ça existe et comment on y entre."),
        ("a", "Et le premier obstacle, c'est le vocabulaire."),
        ("b", "Vous ne connaissez pas les intitulés du secteur que vous visez. C'est mécanique : chaque métier a ses mots. Dans l'étude de cas, la personne cherchait « formation en entreprise ». En observant dix parcours réels, elle a trouvé six intitulés différents pour la même chose, dont un seul était utilisé dans ses recherches."),
        ("a", "Et le résultat quand elle a relancé la recherche ?"),
        ("b", "Vingt-trois offres sur quatre semaines glissantes, contre quatre trouvées jusque-là. Le marché n'était pas fermé, il était invisible. Cette découverte a pris trois heures, et elle explique à elle seule une bonne partie des trois semaines précédentes."),
        ("a", "Tu recommandes d'observer des parcours plutôt que de réfléchir."),
        ("b", "Dix parcours réels de gens qui occupent le poste visé. Ça donne deux choses : le vocabulaire, et les chemins effectivement empruntés. Deuxième enseignement dans le cas : sur dix formateurs internes observés, huit venaient du métier opérationnel qu'ils formaient, et aucun n'avait de diplôme de formateur. Le profil de la personne n'était donc pas un handicap — c'était le profil standard."),
        ("a", "Et si personne ne vient d'un profil comparable ?"),
        ("b", "Ce n'est pas impossible, mais ce sera long, et il faut le savoir avant de s'engager. À l'inverse, si les origines sont variées, le métier est ouvert. Cette seule observation vaut des semaines d'hésitation."),
        ("a", "On arrive à l'outil central du module : l'entretien exploratoire."),
        ("b", "C'est l'outil au meilleur rendement de tout le repositionnement, et presque personne ne l'emploie. Trente minutes avec quelqu'un qui fait le métier, pour lui demander des faits. Pas un avis sur votre projet — des faits."),
        ("a", "Quels faits ?"),
        ("b", "À quoi ressemble une semaine ordinaire. Qu'est-ce qui est difficile dans ce travail, et que les gens de l'extérieur n'imaginent pas. Comment vous avez été recruté, vous. Qu'est-ce qui fait qu'on tient dans ce poste, et qu'est-ce qui fait qu'on part."),
        ("a", "Pourquoi surtout pas demander un avis sur son projet ?"),
        ("b", "Parce que les gens sont polis. Ils vous diront que c'est intéressant, et vous n'aurez rien appris. Un fait, lui, ne cherche pas à vous ménager."),
        ("a", "Comment on obtient ces rendez-vous ? C'est là que la plupart des gens bloquent."),
        ("b", "Un message de quatre lignes, pas plus. Qui vous êtes en une phrase. Ce que vous cherchez à comprendre, précisément. La durée annoncée — vingt à trente minutes. Et une phrase qui change tout : « je ne cherche pas de poste chez vous ». Pas de CV joint, surtout."),
        ("a", "Ça fonctionne à quel taux ?"),
        ("b", "Entre trente et cinquante pour cent d'acceptation pour une demande claire et non intéressée. Dans l'étude de cas : douze messages, cinq réponses positives, une négative, six sans réponse. Quarante-deux pour cent. Et un détail très parlant — les trois premiers messages, envoyés avant d'avoir intégré le format, étaient plus longs et mentionnaient une recherche d'emploi. Aucun n'a reçu de réponse. Les neuf suivants, au bon format, en ont produit cinq."),
        ("a", "Donc le format n'est pas un détail de style."),
        ("b", "Il porte tout. Dès que la personne en face sent une candidature déguisée, elle passe en mode filtrage et la conversation est perdue. D'où la deuxième règle absolue : ne transformez jamais un entretien exploratoire en candidature, même si l'occasion se présente. Vous perdez la conversation et l'accès au réseau derrière."),
        ("a", "Et la question de fin ?"),
        ("b", "« Qui d'autre me conseilleriez-vous de rencontrer ? ». C'est ce qui rend la série possible. Dans le cas, quinze entretiens : cinq issus des messages initiaux, dix obtenus par cette question. À partir du sixième, il n'a plus été nécessaire de solliciter des inconnus."),
        ("a", "Qu'est-ce que ces quinze entretiens ont appris, en premier ?"),
        ("b", "Le canal réel de recrutement. Sur quinze personnes, onze avaient obtenu leur poste en interne ou par recommandation. Les postes ouverts à l'externe correspondaient à des entreprises en croissance ou en réorganisation. Cette information a réorienté toute la stratégie : l'effort devait porter sur la visibilité et le réseau, pas sur le volume de candidatures."),
        ("a", "C'est exactement l'inverse de ce qu'elle faisait."),
        ("b", "Et c'est très courant. Concentrer son effort sur les annonces dans un métier qui recrute par réseau est une erreur d'allocation, pas un manque de travail. La personne travaillait beaucoup, dans la mauvaise direction."),
        ("a", "Parlons de la lecture des offres. Tu dis qu'une exigence n'est pas éliminatoire."),
        ("b", "Les offres décrivent un candidat idéal, les recrutements se font sur des candidats réels. Autre signal utile : une offre republiée trois fois signale un poste difficile à pourvoir. C'est précisément là qu'il faut se présenter quand on ne coche pas toutes les cases."),
        ("a", "Et la rémunération ?"),
        ("b", "Connaissez la fourchette avant d'être en situation de négocier. C'est une question qu'on peut poser en entretien exploratoire, justement parce qu'on n'est pas candidat."),
        ("a", "Reste l'écart entre le profil et la cible. Comment on le traite ?"),
        ("b", "D'abord on le qualifie, et c'est le point où les gens se trompent le plus. Il existe trois écarts. L'écart de vocabulaire : vous savez faire, vous ne le dites pas dans leurs mots. L'écart de preuve : vous savez faire, vous ne pouvez pas le montrer. L'écart de compétence : vous ne savez pas faire. Les trois appellent des réponses opposées."),
        ("a", "Dans quel ordre ?"),
        ("b", "Le vocabulaire d'abord, il se traite en une semaine. La preuve ensuite. La formation en dernier, et seulement après vérification auprès de deux professionnels du métier. Une formation dont vous ne pouvez pas nommer le poste visé et l'écart comblé ne comble rien."),
        ("a", "Comment on comble un écart de preuve rapidement ?"),
        ("b", "En cherchant la plus petite démonstration possible. Une demi-journée d'intervention vaut mieux qu'un projet de six mois jamais engagé. Dans le cas, une seule intervention réalisée a suffi à transformer la candidature."),
        ("a", "Et pour finir, l'arbitrage entre les pistes."),
        ("b", "Deux pistes hiérarchisées, soixante-dix et trente pour cent de l'effort, et le critère de bascule écrit à l'avance. Écrit avant, parce qu'après on le tord. Et le signal d'arrêt de l'exploration : quand trois entretiens consécutifs ne vous apprennent plus rien, elle a produit ce qu'elle pouvait. Décidez."),
        ("a", "Tu ajoutes un mot sur la durée."),
        ("b", "L'usure est le premier facteur d'échec d'une recherche longue. Maintenez des activités sans rapport, et comptez les entretiens exploratoires comme des résultats — parce que c'en sont. Attendre la certitude est une façon de ne jamais commencer."),
        ("a", "Ce qu'on fait demain ?"),
        ("b", "Ouvrez les profils de dix personnes qui occupent le poste que vous visez, et notez uniquement les intitulés exacts de leurs postes. Trois heures maximum. Relancez ensuite votre recherche d'offres sur ces intitulés-là — c'est souvent la découverte la plus rentable du parcours."),
        ("a", "Au module 3, on convertit : CV, réseau, entretien. Merci Marc."),
    ],
}

# ============================================================
# Module 3 — Se rendre visible et convertir
# ============================================================

P["bilan-competences/module-3"] = {
    "formation": "Bilan de compétences et repositionnement",
    "titre": "Se rendre visible et convertir : candidature, réseau, entretien",
    "module_id": "formation-bilan-competences-module-3",
    "hosts": HOSTS,
    "resume": "Un CV qui répond à une offre plutôt qu'il ne raconte une carrière, "
              "un message qui nomme l'objection, et un entretien préparé sur cinq questions.",
    "lignes": [
        ("a", "Dernier module de la formation. Marc, la cible est arrêtée, l'écart de preuve est comblé, et l'offre parfaite paraît. Et là, le problème."),
        ("b", "Le CV. Deux pages, chronologique, huit ans de fonction commerciale. Le mot « formation » y apparaît une fois, dans une liste de tâches, en dernière position. Un recruteur qui le parcourt en quarante secondes verra un commercial qui postule à un poste de formateur, et il classera la candidature."),
        ("a", "Alors que le module 2 avait établi que le profil correspondait."),
        ("b", "Exactement. Le problème n'est pas le profil, c'est que la candidature ne le montre pas. Tout le module tient dans cet écart-là."),
        ("a", "Premier principe : le CV répond à une offre."),
        ("b", "Ce n'est pas un document biographique, c'est un argumentaire construit pour une offre précise. Et le CV chronologique intégral est le pire format possible pour un changement de métier, parce qu'il met en avant ce qui compte le moins : ce que vous avez fait le plus longtemps, dans le secteur que vous quittez."),
        ("a", "Quelle structure tu proposes ?"),
        ("b", "Quatre blocs. Le titre du poste visé, en tête — celui de l'offre, mot pour mot. Un bandeau de quatre lignes. Les compétences démontrées, chiffrées. Et le parcours condensé, en dernier."),
        ("a", "Le bandeau, c'est quoi exactement ?"),
        ("b", "Quatre lignes qui énoncent des faits et une direction. Jamais d'adjectifs. Pas « professionnelle rigoureuse et passionnée » — « cent soixante personnes formées l'an dernier sur des sessions non obligatoires ; huit ans d'expérience opérationnelle du métier ; cherche à transmettre ces savoir-faire en interne »."),
        ("a", "Et il faut reprendre le vocabulaire de l'offre."),
        ("b", "Mot pour mot. C'est celui que le lecteur cherche, et souvent celui que filtrent les outils de présélection. Dans l'étude de cas, les cinq exigences de l'offre ont été relevées littéralement, et les cinq figuraient déjà dans l'inventaire du module 1 — sous d'autres noms. Le travail n'était pas d'acquérir quoi que ce soit, il était de traduire."),
        ("a", "Combien de temps ça prend ?"),
        ("b", "Quarante-cinq minutes dans le cas. Et le test qui suit vaut le détour : faire lire le CV quarante secondes à quelqu'un d'extérieur au secteur, puis lui demander « qu'est-ce que cette personne sait faire ? ». La réponse a été : « former des gens qui ne sont pas obligés de venir ». C'est exactement le message visé, et c'était la première fois qu'il passait."),
        ("a", "Donc le CV unique envoyé partout, c'est fini."),
        ("b", "Dix CV adaptés produisent davantage que cent envois identiques, et demandent moins de temps total — parce que les cent envois s'accompagnent de cent attentes et de cent déceptions. Le volume est une stratégie valable quand le profil correspond déjà. En repositionnement, seule l'adaptation fonctionne."),
        ("a", "Passons au message d'accroche. Trois paragraphes."),
        ("b", "Le premier énonce le fait le plus pertinent, celui qui rend la candidature légitime. Le deuxième nomme l'objection et la retourne. Le troisième s'appuie sur un élément précis de l'offre."),
        ("a", "Nommer l'objection soi-même, c'est contre-intuitif."),
        ("b", "Le lecteur la formulera de toute façon. Autant la formuler avant lui, et la traiter par un fait. Dans le cas : « mon parcours est commercial et non pédagogique, et c'est probablement la première chose que vous noterez » — puis le retournement, ces publics pouvaient partir à tout moment, donc l'enjeu pédagogique était plus élevé, pas moins."),
        ("a", "Qu'est-ce qui ne doit pas y figurer ?"),
        ("b", "Aucune mention de passion, de sens ou de valeurs. Aucune formule sur l'entreprise. Et le test décisif : rien qui puisse être écrit à l'identique dans une autre candidature. La motivation est invérifiable et universelle — elle explique pourquoi ce poste, elle ne remplace jamais la compétence."),
        ("a", "Venons-en au réseau. Comment on l'active sans mendier un emploi ?"),
        ("b", "« Je cherche du travail » ne s'active pas : c'est trop vague pour être retenu. Une recherche formulée précisément se retient et remonte. Et la question à poser n'est pas « as-tu quelque chose ? », qui met les gens en difficulté, mais « connais-tu quelqu'un à qui je pourrais parler ? », à laquelle on peut presque toujours répondre."),
        ("a", "Tu insistes sur les liens faibles."),
        ("b", "Ils produisent plus d'opportunités que les liens forts, pour une raison mécanique : vos proches connaissent les mêmes personnes que vous. L'information nouvelle vient des gens que vous voyez rarement."),
        ("a", "Et l'indicateur, sur ce canal ?"),
        ("b", "Pas le nombre de candidatures. Le nombre de personnes qui savent précisément ce que vous cherchez. C'est ce qu'on peut compter, et ça monte."),
        ("a", "Tu as un critère pour distinguer le travail utile de l'occupation."),
        ("b", "Une action progresse si elle met votre candidature devant un être humain, ou si elle vous apporte une information nouvelle. Le reste est de l'occupation. C'est un critère dur, et il évite de confondre activité et progression — ce qui est le piège central d'une recherche longue."),
        ("a", "L'entretien, maintenant. Tu parles de cinq questions qui décident."),
        ("b", "La première, c'est la réponse de deux minutes sur votre parcours. Elle ouvre l'entretien et elle donne le cadre de tout ce qui suit. Si elle est floue, vous passez le reste de l'heure à rattraper. Elle se prépare et elle se répète à voix haute — pas dans sa tête."),
        ("a", "Et les points faibles ?"),
        ("b", "Nommez un manque réel et secondaire. C'est contre-intuitif, mais un manque nommé inquiète moins qu'un manque que l'interlocuteur devine et que vous n'évoquez pas. Le silence sur un point évident se lit comme une tentative de dissimulation."),
        ("a", "Il y a une question que tu dis la plus révélatrice."),
        ("b", "« Avez-vous des questions ? ». Elle est traitée comme une formalité de fin, et elle est très regardée. Préparez-en quatre, sur le contenu du travail : à quoi ressemble une semaine, comment on mesure la réussite du poste à six mois, qu'est-ce qui a manqué à la personne précédente. Pas sur les congés."),
        ("a", "Et sur les périodes délicates : un trou de parcours, un licenciement."),
        ("b", "La longueur de l'explication crée le problème que le fait ne crée pas. Un licenciement s'explique en une phrase, sur un ton neutre, et on passe. Trois minutes de justification transforment un non-événement en sujet."),
        ("a", "Reprenons l'étude de cas, du CV à la signature."),
        ("b", "Jour 1 : le CV reconstruit en quarante-cinq minutes, le message d'accroche en quatorze lignes. Jour 2, et c'est l'étape que la plupart des gens omettent : le contact humain avant l'envoi. L'une des quinze personnes rencontrées en entretien exploratoire connaissait quelqu'un dans cette entreprise. Trois lignes lui ont été envoyées, sans rien demander d'autre qu'une information : est-ce que le poste est déjà pourvu en interne ?"),
        ("a", "C'est le module 2 qui paie."),
        ("b", "Entièrement. Les quinze entretiens exploratoires n'avaient produit aucune candidature sur le moment. Ils produisent ici un accès direct, une information sur le poste, et une candidature qui arrive recommandée plutôt que dans une pile."),
        ("a", "Et la négociation, à la fin ?"),
        ("b", "Trois règles. Ne répondez jamais à une proposition dans la conversation où elle est faite : quarante-huit heures sont attendues et ne compromettent rien. Le salaire n'est pas la seule variable — la date de prise de poste, une formation, l'intitulé, le rythme coûtent souvent moins à l'employeur et valent parfois davantage pour vous. Et formulez vos demandes en une fois, avec leur raison, en disant que vous signez si elles aboutissent."),
        ("a", "Pourquoi en une fois ?"),
        ("b", "Parce qu'une demande qui arrive après une autre donne le sentiment d'un puits sans fond, et ça abîme la relation avant même le premier jour."),
        ("a", "Un dernier garde-fou ?"),
        ("b", "Relisez vos critères rédhibitoires avant de signer. Ils ont été écrits à froid, au module 1. Le soulagement est un mauvais conseiller, et accepter par soulagement est l'erreur la plus fréquente de toute cette étape."),
        ("a", "Et sur la durée ?"),
        ("b", "Une recherche de repositionnement est structurellement plus longue qu'une recherche à poste équivalent. Le savoir à l'avance évite de prendre la durée pour un échec. Ce n'est pas un signal sur vous, c'est une caractéristique de l'exercice."),
        ("a", "Ce qu'on fait demain ?"),
        ("b", "Prenez une offre qui vous intéresse vraiment, relevez ses cinq exigences mot pour mot, et vérifiez que chacune apparaît dans votre CV avec les mots de l'offre. Celles qui manquent sont presque toujours dans votre inventaire, sous un autre nom."),
        ("a", "Trois modules, de l'inventaire à la signature. Merci Marc, et bon courage à celles et ceux qui sont en chemin."),
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
