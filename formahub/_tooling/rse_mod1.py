#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, json, os
sys.path.insert(0, "/tmp")
from fh_builder import build

M = {}
QUIZ = {}
FORM = "RSE &amp; transition écologique en entreprise"

M["rse-transition-ecologique/module-1"] = {
 "formation": FORM,
 "titre": "Le Cadre : ce que Recouvre la RSE et ce que la Réglementation Impose",
 "num": 1, "total": 4, "duree": "65 min", "niveau": "Débutant",
 "module_id": "formation-rse-transition-ecologique-module-1",
 "situation": [
   "Vous travaillez dans une entreprise de 380 salariés et 120 millions d'euros de chiffre d'affaires. Trois choses arrivent en même temps.",
   "Votre plus gros client, un groupe coté, vous adresse un questionnaire ESG de 180 questions à retourner sous trois semaines, en indiquant que le référencement en dépend. Votre banque demande des éléments extra-financiers pour l'instruction d'une ligne de crédit. Et le service commercial vous annonce avoir perdu un appel d'offres public au motif que le dossier ne comportait pas de bilan d'émissions de gaz à effet de serre.",
   "Le directeur général vous demande de traiter le sujet. Sa première question est : « on n'est pas soumis à la CSRD, si ? ». La réponse est non — depuis la révision de mars 2026, les seuils sont à 1 000 salariés et 450 millions d'euros de chiffre d'affaires, et vous en êtes loin.",
   "Cette réponse ne règle rien, et c'est le point de départ de tout ce parcours. La question « suis-je soumis ? » est devenue secondaire ; la question qui compte est « qui me demande quoi, sur quel fondement, et que suis-je obligé de fournir ». Ce module construit la carte qui permet d'y répondre.",
 ],
 "objectifs": [
   "Distinguer ce que recouvrent la RSE, l'ESG et la transition écologique, et employer chaque terme à bon escient",
   "Situer les obligations européennes après la révision Omnibus de mars 2026",
   "Identifier les obligations françaises qui s'appliquent indépendamment de la CSRD",
   "Comprendre la pression de la chaîne de valeur et le droit de refus qui la borne",
   "Choisir un référentiel volontaire en fonction de ce qu'on cherche à obtenir",
   "Positionner la fonction RSE là où elle a une chance d'aboutir",
 ],
 "sections": [
  {"titre": "RSE, ESG, transition écologique : trois mots, trois usages",
   "paras": [
     "Ces trois termes circulent comme des synonymes, et ils ne le sont pas. Les confondre conduit à des malentendus coûteux en réunion, parce que chacun désigne un point de vue différent sur le même objet.",
     "<strong>La RSE — responsabilité sociétale des entreprises</strong> — est un concept de <em>management</em>. Il désigne la prise en compte, par une organisation, des effets de ses décisions sur la société et l'environnement. C'est le point de vue de l'entreprise sur elle-même. La définition de référence est celle de la norme ISO 26000 : la responsabilité d'une organisation vis-à-vis des impacts de ses décisions et activités sur la société et l'environnement, se traduisant par un comportement transparent et éthique.",
     "<strong>L'ESG — environnement, social, gouvernance</strong> — est un vocabulaire d'<em>investisseur</em>. Il est né dans la finance pour évaluer un risque et une performance extra-financière depuis l'extérieur. Quand une banque ou un fonds vous parle d'ESG, il ne vous demande pas si vous êtes une entreprise responsable : il évalue si vos pratiques constituent un risque pour son investissement. C'est une nuance essentielle, et elle explique la forme des questionnaires que vous recevez, qui portent bien plus sur l'existence de politiques et de procédures que sur des résultats.",
     "<strong>La transition écologique</strong> est un terme de <em>politique publique</em>, désignant le passage d'un modèle économique à un autre — décarbonation, économie circulaire, préservation du vivant. Elle est plus étroite que la RSE, qui inclut le social et la gouvernance, et plus large qu'elle, puisqu'elle engage aussi les États et les ménages.",
     "En pratique : vous <em>faites</em> de la RSE, vous êtes <em>évalué</em> sur des critères ESG, et vous <em>contribuez</em> à la transition écologique. Employer le bon terme devant le bon interlocuteur est le premier signe de sérieux sur ces sujets, et l'employer de travers décrédibilise immédiatement.",
     "Une dernière notion structure tout le reste : la <strong>double matérialité</strong>. Elle distingue deux questions que l'on mélange constamment. La <em>matérialité d'impact</em> : quels effets mon activité produit-elle sur l'environnement et la société ? La <em>matérialité financière</em> : quels risques et opportunités les enjeux environnementaux et sociaux font-ils peser sur mon activité ? Le module 3 y est entièrement consacré, mais retenez dès maintenant qu'un questionnaire ESG interroge presque toujours la seconde, alors qu'une démarche RSE part de la première.",
   ],
   "blocks": [
     {"type": "exemple", "titre": "la même entreprise, deux lectures",
      "paras": [
        "Une entreprise de transport routier de 380 salariés.",
        "<em>Lecture de matérialité d'impact :</em> ses camions émettent environ 9 000 tonnes de CO2 par an, elle emploie des conducteurs dont les conditions de travail sont un enjeu majeur, et son activité contribue à la congestion et au bruit dans les zones qu'elle traverse. Ce sont ses impacts.",
        "<em>Lecture de matérialité financière :</em> la hausse du prix du carbone et l'extension des zones à faibles émissions menacent son modèle ; la difficulté de recrutement de conducteurs limite sa croissance ; ses clients cotés commencent à sélectionner leurs transporteurs sur leur intensité carbone. Ce sont ses risques.",
        "Les deux lectures pointent vers les mêmes sujets — c'est fréquent — mais elles ne conduisent pas aux mêmes priorités. La première pousserait à traiter d'abord le bruit et les conditions de travail ; la seconde, l'intensité carbone et l'attractivité employeur. Une démarche solide fait les deux et les confronte, et c'est précisément ce que la double matérialité organise.",
      ]},
     {"type": "pitfall", "titre": "confondre la RSE avec la communication",
      "paras": [
        "L'erreur historique, et elle n'a pas disparu : traiter la RSE comme un sujet de communication, confié au service concerné, produisant un rapport annuel illustré et un partenariat associatif.",
        "Trois raisons rendent cette approche non seulement inefficace mais dangereuse aujourd'hui. Elle ne répond à aucune des demandes réelles — un questionnaire client ou bancaire porte sur des politiques, des procédures et des chiffres, pas sur des intentions. Elle mobilise du budget sans réduire aucun risque. Et depuis l'entrée en vigueur des règles sur les allégations environnementales, elle expose directement à une sanction : une communication non étayée est devenue une pratique commerciale trompeuse, sujet traité au module 4.",
        "Le signe qui ne trompe pas : si le sujet RSE est porté par la communication et non par la direction générale ou les opérations, il produira des supports et aucun changement.",
      ]},
   ]},

  {"titre": "Le socle européen après la révision de mars 2026",
   "paras": [
     "Le paysage réglementaire européen a été profondément remanié. Il faut le connaître dans son état actuel, et savoir qu'il a bougé — parce qu'une bonne partie de ce que vous lirez ailleurs décrit encore l'état antérieur.",
     "<strong>La CSRD</strong> — directive sur la publication d'informations en matière de durabilité, adoptée en 2022 — imposait à un large ensemble d'entreprises un rapport de durabilité normalisé, vérifié par un tiers, intégré au rapport de gestion. Son périmètre initial visait environ 50 000 entreprises européennes, sur des seuils de 250 salariés et 50 millions d'euros de chiffre d'affaires.",
     "<strong>La directive Omnibus I</strong>, publiée au Journal officiel de l'Union européenne le 26 février 2026 et entrée en vigueur le 18 mars 2026, a réduit ce périmètre d'environ 80 %. Les seuils sont désormais cumulatifs : <strong>plus de 1 000 salariés ET plus de 450 millions d'euros de chiffre d'affaires net</strong>. Les deux conditions doivent être remplies, ce qui écarte de fait la quasi-totalité des entreprises de taille intermédiaire.",
     "Le calendrier a suivi : première application aux exercices ouverts à compter de 2027, premiers rapports publiés en 2028. Pour les groupes non européens, le seuil est de 450 millions d'euros de chiffre d'affaires réalisé dans l'Union avec une filiale ou succursale à plus de 200 millions, à compter de l'exercice 2028. La transposition en droit français est attendue au plus tard le 19 mars 2027.",
     "<strong>Les ESRS</strong> — normes européennes de reporting de durabilité — sont le format imposé du rapport. Elles comptent douze normes : deux transversales, cinq environnementales, quatre sociales, une de gouvernance. Leur version révisée, adoptée par acte délégué le 3 juillet 2026, réduit d'environ 61 % le nombre de points de données obligatoires et introduit une analyse de matérialité descendante, où l'on peut conclure qu'un thème entier est non matériel sans l'examiner enjeu par enjeu. Application facultative sur l'exercice 2026, obligatoire à partir de 2027.",
     "<strong>La taxonomie européenne</strong> est un classement des activités économiques selon leur contribution à six objectifs environnementaux. Elle ne crée pas d'obligation d'agir : elle définit un langage commun permettant de dire quelle part du chiffre d'affaires, des investissements et des dépenses d'exploitation est alignée sur des activités considérées comme durables. Son usage principal est financier — elle oriente les décisions d'investissement et le coût du capital.",
     "<strong>La CS3D</strong> — directive sur le devoir de vigilance des entreprises en matière de durabilité — impose d'identifier et de traiter les atteintes aux droits humains et à l'environnement dans sa chaîne d'activités. L'Omnibus l'a également resserrée : seuils portés à 5 000 salariés et 1,5 milliard d'euros, transposition repoussée au 26 juillet 2028, application différée à juillet 2029, obligation de rompre une relation commerciale supprimée au profit de mesures graduées, et plafonnement des sanctions à 3 % du chiffre d'affaires mondial.",
   ],
   "blocks": [
     {"type": "h3", "titre": "Le point le plus utile de toute la réglementation pour une PME : le droit de refus",
      "paras": [
        "L'Omnibus a introduit une disposition qui change directement la vie des entreprises non soumises, et qu'il faut connaître : le <strong>plafond d'information de la chaîne de valeur</strong>.",
        "Une entreprise soumise à la CSRD ne peut pas exiger d'un partenaire de moins de 1 000 salariés des informations allant au-delà du contenu de la norme volontaire pour les PME — la VSME. Si elle demande davantage, elle doit accompagner sa demande de la mention que l'entreprise sollicitée dispose d'un <em>droit statutaire de refuser</em> de fournir ces informations supplémentaires. Le même mécanisme existe pour la CS3D, avec un seuil à 5 000 salariés.",
        "Concrètement, dans la situation d'ouverture : le questionnaire de 180 questions dépasse très largement le périmètre de la VSME, et votre entreprise n'est pas tenue d'y répondre intégralement. Cela ne signifie pas qu'il faille refuser — un client reste un client — mais que vous êtes en position de <strong>négocier le périmètre</strong> plutôt que de subir la demande.",
        "La formulation utile : « nous répondons intégralement sur le périmètre VSME, qui est le standard prévu pour les entreprises de notre taille ; au-delà, dites-nous quelles questions sont réellement décisives pour vous et nous regarderons ce que nous pouvons construire ». Vous passez d'une position de fournisseur pris en défaut à celle d'un interlocuteur qui connaît le cadre — et l'effet sur la relation est considérable.",
      ]},
     {"type": "exemple", "titre": "la VSME, et pourquoi elle est votre meilleure porte d'entrée",
      "paras": [
        "La VSME est la norme volontaire de reporting de durabilité destinée aux petites et moyennes entreprises. Elle n'est pas une obligation légale et ne relève d'aucun acte délégué : c'est un outil de marché, conçu pour normaliser les demandes que les grandes entreprises adressent à leurs fournisseurs.",
        "Son intérêt tient en un point : elle définit un <em>plafond opposable</em>. Une PME qui produit un jeu d'informations VSME peut répondre à la quasi-totalité des sollicitations avec un seul travail, au lieu de refaire un dossier différent pour chaque client, chaque banque et chaque appel d'offres.",
        "Elle se compose d'un module de base — informations générales, énergie et émissions, eau, déchets, effectifs, santé et sécurité, éthique des affaires — et d'un module complémentaire pour les entreprises sollicitées par des acteurs financiers.",
        "Pour l'entreprise de la mise en situation, c'est la réponse structurelle au problème des trois demandes simultanées : au lieu de traiter le questionnaire client, la demande bancaire et l'appel d'offres séparément, on construit une fois un socle VSME et on l'utilise pour les trois. Le coût de la première année est réel ; celui des années suivantes devient marginal.",
      ]},
     {"type": "pitfall", "titre": "s'appuyer sur une source antérieure à mars 2026",
      "paras": [
        "La révision Omnibus a rendu obsolète une grande partie de ce qui est publié sur la CSRD, y compris des guides d'organismes sérieux. Un document décrivant des seuils à 250 salariés, une entrée en vigueur en 2025 ou 2026 pour les grandes entreprises non cotées, ou des normes sectorielles obligatoires, décrit un état du droit qui n'existe plus.",
        "Deux réflexes s'imposent. Vérifier systématiquement la date de mise à jour de toute source sur ce sujet, et ne rien affirmer sur le périmètre d'application sans avoir consulté une source postérieure à mars 2026. Le sujet continuera par ailleurs de bouger : la transposition française est attendue d'ici mars 2027 et précisera plusieurs points laissés ouverts, notamment le sort des entreprises qui avaient commencé à publier sous les anciens seuils.",
        "C'est une bonne habitude de manière générale sur ces sujets : sur une matière aussi mouvante, dater ce qu'on affirme vaut mieux que de l'affirmer. « Au 4 septembre 2026, les seuils sont de… » est une phrase qui ne vous mettra jamais en difficulté.",
      ]},
   ]},

  {"titre": "Les obligations françaises, qui n'ont pas disparu",
   "paras": [
     "Le resserrement européen a produit un effet de bord : beaucoup d'entreprises ont conclu qu'elles n'avaient plus d'obligations. C'est faux, et la confusion est coûteuse, parce que les obligations françaises visent des seuils bien plus bas et sont assorties de sanctions effectives.",
     "<strong>Le BEGES — bilan d'émissions de gaz à effet de serre</strong>, prévu à l'article L. 229-25 du code de l'environnement, s'impose aux entreprises de <strong>plus de 500 salariés</strong> en métropole, 250 dans les outre-mer, aux collectivités de plus de 50 000 habitants et aux établissements publics de plus de 250 agents. Périodicité : quatre ans pour le secteur privé, trois ans pour le public. Depuis la loi Industrie verte du 23 octobre 2023, il doit être accompagné d'un <em>plan de transition</em> comportant des objectifs chiffrés de réduction, faute de quoi il n'est pas conforme. Les émissions indirectes significatives — le scope 3 — sont obligatoires au-delà de 100 millions d'euros de chiffre d'affaires ou de total de bilan, avec une couverture d'au moins 80 %.",
     "La sanction est de 50 000 euros, portée à 100 000 en cas de récidive, et s'accompagne d'une exclusion possible des marchés publics et d'une perte d'accès à certaines aides publiques. Le dépôt se fait sur la plateforme de l'ADEME, et la publication y est publique : tant que le bilan n'y figure pas, l'entreprise est en infraction.",
     "<strong>L'index de l'égalité professionnelle</strong> s'impose à partir de 50 salariés, avec publication annuelle et obligation de mesures correctives en dessous de 75 points sur 100.",
     "<strong>La loi Climat et Résilience de 2021</strong> et son décret d'application de 2022 encadrent strictement les allégations de neutralité carbone : toute mention de ce type dans une publicité exige la publication du bilan d'émissions, d'une trajectoire de réduction et du détail des projets de compensation. Sanction jusqu'à 300 000 euros.",
     "<strong>La directive EmpCo</strong> — dite « pouvoir d'agir des consommateurs », adoptée en février 2024 — s'applique dans l'ensemble des États membres à compter du <strong>27 septembre 2026</strong>, sans seuil de taille. Elle ajoute au droit de la consommation une série de pratiques interdites, dont plusieurs visent directement les allégations environnementales génériques, les labels non vérifiés par un tiers, et la présentation d'une compensation carbone comme une neutralité. Sujet du module 4.",
     "Retenez la hiérarchie qui en découle : <strong>une PME française de 380 salariés n'est pas soumise à la CSRD, mais elle est soumise au droit de la consommation dès qu'elle communique, et le sera au BEGES si elle franchit 500 salariés.</strong> Le raisonnement « nous sommes hors périmètre » ne tient que si l'on précise hors périmètre de quoi.",
   ],
   "blocks": [
     {"type": "method", "titre": "établir sa carte d'obligations en une demi-journée",
      "paras": ["L'exercice à faire une fois, à refaire chaque année, et à conserver dans un document unique daté."],
      "steps": [
        "<strong>Relevez les quatre chiffres qui déterminent tout</strong> : effectif moyen, chiffre d'affaires net, total de bilan, et statut coté ou non. Notez la méthode de calcul de l'effectif retenue, qui varie selon les textes et fait basculer les entreprises proches d'un seuil.",
        "<strong>Passez la liste des obligations françaises</strong> par ordre de seuil croissant : index égalité à 50 salariés, BEGES à 500, obligations de la commande publique selon les marchés visés. Notez pour chacune : soumis ou non, échéance, et responsable interne.",
        "<strong>Passez ensuite les obligations européennes</strong> avec les seuils postérieurs à mars 2026, en distinguant l'entreprise seule et le groupe consolidé — une filiale peut être entraînée par sa maison mère.",
        "<strong>Listez les obligations contractuelles</strong>, qui sont souvent les plus contraignantes en pratique : clauses RSE dans les contrats clients, exigences des appels d'offres publics, covenants bancaires. Elles ne figurent dans aucun texte de loi et personne ne les recense spontanément.",
        "<strong>Ajoutez ce qui s'applique dès la première communication</strong> : droit de la consommation, allégations environnementales, mentions publicitaires. Sans seuil, et c'est ce qu'on oublie systématiquement.",
        "<strong>Datez le document et fixez la date de revue.</strong> Sur une matière qui a changé trois fois en dix-huit mois, un document non daté est un document faux.",
      ]},
     {"type": "exemple", "titre": "la carte de l'entreprise de la mise en situation",
      "paras": [
        "380 salariés, 120 M€ de chiffre d'affaires, non cotée, filiale d'aucun groupe.",
        "<em>CSRD :</em> non soumise, et ne le sera pas avant de franchir simultanément 1 000 salariés et 450 M€. Autant dire jamais dans son modèle actuel.",
        "<em>BEGES :</em> non soumise à 380 salariés — mais l'effectif a progressé de 40 personnes en deux ans. À ce rythme, le seuil de 500 est atteint dans six ans, et le premier bilan devra être prêt l'année du franchissement. Le sujet n'est donc pas « sommes-nous concernés » mais « quand ».",
        "<em>Index égalité :</em> soumise, publication annuelle au 1er mars. Elle le faisait déjà.",
        "<em>Appels d'offres publics :</em> c'est ici que se situe l'obligation la plus immédiate et la plus coûteuse. La perte d'un marché faute de bilan carbone n'est pas une sanction réglementaire, c'est une perte commerciale sèche — et elle ne figure sur aucune carte d'obligations légales.",
        "<em>Contrats clients :</em> le questionnaire de 180 questions relève d'une exigence contractuelle. Non obligatoire au sens de la loi, décisif au sens du chiffre d'affaires.",
        "<em>Communication :</em> le site internet affiche « une démarche éco-responsable » et « des livraisons neutres en carbone ». Cette dernière mention est en infraction au décret de 2022 en l'absence de bilan publié, et l'exposition est immédiate. C'est le point à traiter en premier, et c'est celui que personne n'avait identifié.",
      ]},
   ]},

  {"titre": "Les référentiels volontaires : lequel sert à quoi",
   "paras": [
     "À côté des obligations, une dizaine de référentiels volontaires coexistent. Le réflexe fréquent — « faisons une certification » — produit des dépenses sans effet quand le référentiel choisi ne correspond pas à ce qu'on cherche. Chacun répond à une question différente.",
     "<strong>ISO 26000</strong> est une <em>ligne directrice</em>, et non une norme certifiable — point systématiquement mal compris. On ne peut pas « être certifié ISO 26000 ». Elle structure sept questions centrales : gouvernance, droits de l'homme, relations et conditions de travail, environnement, loyauté des pratiques, questions relatives aux consommateurs, communautés et développement local. Son usage utile est celui d'une grille de cadrage pour ne rien oublier au démarrage.",
     "<strong>EcoVadis</strong> est une <em>évaluation</em>, sur dossier documentaire, débouchant sur une note et une médaille. C'est le référentiel le plus demandé par les donneurs d'ordre dans les relations fournisseurs. Il évalue l'existence de politiques, d'actions et de résultats documentés — pas la performance environnementale réelle. Une entreprise peu émettrice mais mal documentée obtient une note inférieure à une entreprise très émettrice bien documentée. Ce n'est pas un défaut de l'outil, c'est son objet : il mesure la maturité du système de gestion.",
     "<strong>La certification B Corp</strong> évalue l'entreprise dans son ensemble, y compris son modèle d'affaires et sa gouvernance, avec une exigence d'inscription de l'objet social dans les statuts. Exigeante, longue, et pertinente pour une entreprise dont la raison d'être est un argument de positionnement. Sans effet sur un questionnaire fournisseur.",
     "<strong>Le SBTi</strong> — initiative de fixation d'objectifs fondés sur la science — valide des trajectoires de réduction d'émissions compatibles avec l'accord de Paris. Il ne certifie pas l'entreprise, il valide ses <em>objectifs</em>. Sa version 2.0 du standard net zéro pour les entreprises a été publiée le 11 juin 2026, avec des options de fixation d'objectifs différenciées selon la taille et le contexte, une hiérarchie donnant priorité à la réduction directe avant toute compensation, et une exigence renforcée de transparence sur l'avancement.",
     "<strong>Le CDP</strong> est un questionnaire annuel destiné aux investisseurs, portant sur le climat, l'eau et les forêts, avec une notation publique. Utile si votre capital ou votre financement dépend d'acteurs financiers qui l'utilisent ; sans intérêt sinon.",
     "La règle de choix est unique et il faut s'y tenir : <strong>partez de qui vous demande quoi, jamais du référentiel</strong>. Un client industriel demande EcoVadis. Une banque regarde le CDP ou des éléments alignés sur la taxonomie. Un marché public demande un bilan d'émissions et un plan de réduction. Un positionnement de marque justifie B Corp. Adopter un référentiel avant d'avoir identifié le demandeur, c'est acheter une réponse à une question que personne ne pose.",
   ],
   "blocks": [
     {"type": "pitfall", "titre": "empiler les référentiels",
      "paras": [
        "Le scénario classique : un client demande EcoVadis, on s'y met ; l'année suivante un autre demande le CDP, on s'y met aussi ; un troisième réclame un questionnaire maison de 200 lignes. Trois ans plus tard, une personne à temps plein remplit des questionnaires et l'entreprise n'a réduit aucune émission.",
        "C'est la pathologie la plus fréquente du sujet, et elle a un nom dans les entreprises qui l'ont vécue : la RSE de conformité. Elle consomme intégralement la ressource RSE en production de preuves, sans jamais atteindre les opérations.",
        "Deux parades. D'abord, <strong>construire un socle unique de données</strong> — le jeu VSME — et alimenter tous les questionnaires depuis ce socle, plutôt que de traiter chaque demande comme un projet. Ensuite, tenir un ratio explicite : au moins la moitié du temps de la fonction RSE doit aller à des actions qui changent quelque chose, et pas à des réponses. Ce ratio se mesure et se présente en comité de direction — c'est le seul moyen d'obtenir un arbitrage quand une nouvelle demande arrive.",
      ]},
     {"type": "exemple", "titre": "quatre demandeurs, quatre réponses proportionnées",
      "paras": [
        "<em>Le client industriel</em> qui envoie 180 questions : réponse sur le périmètre VSME, mention du droit de refus au-delà, et proposition d'une évaluation EcoVadis si la relation le justifie — elle sera réutilisable pour ses autres clients.",
        "<em>La banque</em> : elle cherche à évaluer un risque, pas une vertu. Un bilan d'émissions, une trajectoire, et l'exposition physique et de transition des activités suffisent. Un rapport RSE illustré ne l'intéresse pas.",
        "<em>L'appel d'offres public</em> : la demande est précise et vérifiable — un bilan d'émissions et un plan de réduction. C'est le besoin le plus concret des quatre, et le seul dont l'absence a déjà coûté un marché.",
        "<em>Les salariés</em>, qui ne demandent rien officiellement mais posent des questions en réunion : c'est le demandeur qu'on oublie, et le plus déterminant pour la réussite d'une démarche. Aucun référentiel n'y répond ; une réunion d'information honnête, oui.",
        "Une lecture transversale de ces quatre demandes fait apparaître qu'un seul livrable — un bilan d'émissions sérieux assorti d'un plan de réduction — sert trois d'entre elles. C'est le travail à engager en premier, et c'est l'objet du module 2.",
      ]},
   ]},

  {"titre": "Où placer la fonction RSE, et ce qui la fait échouer",
   "paras": [
     "Une démarche RSE échoue rarement pour des raisons techniques. Elle échoue pour des raisons de position dans l'organisation, et les schémas d'échec sont peu nombreux et reconnaissables.",
     "<strong>Le rattachement décide de tout.</strong> Une fonction RSE rattachée à la communication produit des supports. Rattachée aux ressources humaines, elle traite le social et laisse l'environnement de côté. Rattachée à la qualité ou aux opérations, elle avance sur le terrain mais peine à obtenir des arbitrages. Rattachée à la direction générale ou à la direction financière, elle a accès aux décisions d'investissement — et c'est le seul rattachement qui permette de peser sur les choix structurants.",
     "Le rattachement financier surprend souvent et il se justifie : les décisions qui déterminent l'empreinte d'une entreprise sont des décisions d'investissement et d'achat. Une fonction RSE qui n'est pas dans la boucle des arbitrages budgétaires découvre les décisions une fois prises.",
     "<strong>La légitimité vient des chiffres, pas des convictions.</strong> C'est le point qui heurte le plus les personnes qui arrivent sur ces sujets par conviction, et il est décisif. Une position défendue par valeur est audible une fois, puis elle est classée comme une opinion parmi d'autres. Une position défendue par un chiffre — la part de nos émissions que représente ce poste, le coût de cette dépendance à un prix du carbone donné, le nombre de marchés perdus faute de bilan — entre dans le débat au même titre que les autres arguments de gestion. Le module 2 et le module 3 portent presque entièrement là-dessus.",
     "<strong>Les alliés réels sont opérationnels.</strong> Les achats, parce qu'ils tiennent la chaîne de valeur, qui représente la majorité des émissions de la plupart des entreprises. La production ou la logistique, qui détiennent les gisements physiques. La direction financière, qui arbitre. Le comité social et économique, dont les attributions incluent l'information sur les conséquences environnementales de l'activité depuis la loi Climat et Résilience — un canal souvent ignoré et pourtant institué.",
     "<strong>Le premier livrable décide de la suite.</strong> Choisissez-le pour qu'il produise un résultat visible dans les six mois et qu'il serve à quelqu'un d'autre que vous. Un bilan d'émissions qui débloque un appel d'offres, une réponse structurée qui sécurise un référencement client : ces livrables donnent une légitimité que trois ans de sensibilisation ne procurent pas. À l'inverse, une charte, une raison d'être ou une fresque en atelier, engagées en premier, laissent la fonction sans preuve de son utilité au moment du premier arbitrage budgétaire.",
   ],
   "blocks": [
     {"type": "pitfall", "titre": "commencer par la stratégie",
      "paras": [
        "L'enchaînement qui paraît logique — définir la raison d'être, puis la stratégie RSE, puis les indicateurs, puis les actions — échoue presque systématiquement en entreprise de taille moyenne.",
        "Pourquoi : ces travaux mobilisent longtemps la direction sans produire de résultat observable, et ils se déroulent avant que quiconque ait une idée chiffrée des enjeux réels. On construit alors une stratégie sur des intuitions, et il est fréquent qu'un bilan d'émissions réalisé ensuite montre que 80 % de l'empreinte se trouve dans un poste que la stratégie n'évoquait même pas.",
        "L'ordre qui fonctionne est inverse : <strong>mesurer, prioriser sur les chiffres, agir sur deux ou trois postes, puis formaliser la stratégie</strong> — laquelle s'écrit alors en quelques jours parce qu'elle décrit ce qu'on fait déjà. C'est aussi l'ordre des quatre modules de cette formation, et ce n'est pas un hasard.",
      ]},
     {"type": "h3", "titre": "Ce que ce parcours va construire",
      "paras": [
        "<strong>Module 1, celui-ci :</strong> savoir qui demande quoi, sur quel fondement, et ce qu'on est tenu de fournir. Une carte d'obligations datée et un choix de référentiel justifié.",
        "<strong>Module 2 :</strong> mesurer. Le bilan d'émissions, les trois scopes, la collecte des données, les facteurs d'émission et leurs incertitudes. C'est le module le plus technique et celui qui fournit la matière de tous les autres.",
        "<strong>Module 3 :</strong> prioriser et agir. La double matérialité comme méthode de sélection, la construction d'un plan d'action chiffré, et la façon d'embarquer les opérations — qui est la vraie difficulté.",
        "<strong>Module 4 :</strong> rendre compte et communiquer sans s'exposer. Le reporting, les allégations environnementales, et le cadre qui rend une communication non étayée juridiquement risquée.",
        "Une idée les traverse : sur ce sujet plus qu'un autre, <em>ce qui n'est pas mesuré n'est pas piloté, et ce qui n'est pas chiffré n'est pas arbitré</em>. C'est la raison pour laquelle une formation RSE sérieuse ressemble davantage à une formation de gestion qu'à un cours d'écologie.",
      ]},
   ]},
 ],

 "etude_cas": {
   "titre": "Traiter les trois demandes simultanées sans tout accepter",
   "html": """
<p>Reprenons la situation : un questionnaire client de 180 questions sous trois semaines, une demande bancaire, un marché public perdu. Voici la conduite tenue sur six mois.</p>
<p><strong>Semaine 1 — établir la carte, et découvrir le vrai risque.</strong> Une demi-journée pour la carte d'obligations décrite plus haut. Conclusion attendue : non soumise à la CSRD, non soumise au BEGES à 380 salariés, soumise à l'index égalité, déjà traité.</p>
<p>Conclusion inattendue, et c'est elle qui compte : le site internet annonce des « livraisons neutres en carbone ». Cette mention tombe sous le décret de 2022, qui exige la publication d'un bilan d'émissions, d'une trajectoire de réduction et du détail des projets de compensation. Aucun de ces trois éléments n'existe. L'entreprise est en infraction, l'exposition est immédiate, et personne n'avait identifié le sujet.</p>
<p>Décision prise le jour même : la mention est retirée du site, remplacée par une formulation factuelle sur les actions engagées. Coût : zéro. C'est le premier livrable de la fonction RSE, et il a supprimé le risque le plus concret du dossier en quelques heures.</p>
<p><strong>Semaine 2 — reprendre la main sur le questionnaire client.</strong> Lecture des 180 questions et classement en trois piles. Quarante questions relèvent du périmètre VSME et sont documentables rapidement. Soixante demandent des données que l'entreprise possède mais n'a jamais consolidées — consommations d'énergie par site, répartition des achats, accidentologie. Quatre-vingts demandent des politiques formalisées, des certifications ou des données de chaîne de valeur qui n'existent pas.</p>
<p>Appel au responsable achats du client, et non réponse par courriel. Message tenu : « nous répondons intégralement sur le périmètre VSME, qui est le standard prévu par la réglementation pour les entreprises de notre taille, et nous vous fournissons en plus les données de consommation par site. Au-delà, la réglementation prévoit un droit de refus pour les entreprises de moins de 1 000 salariés. Dites-nous lesquelles de ces questions sont réellement décisives pour vous et nous regarderons ce que nous pouvons construire d'ici douze mois. »</p>
<p>Réponse du client : douze questions sont déterminantes, les autres relèvent d'un formulaire standard appliqué à tous les fournisseurs sans distinction de taille. Le périmètre passe de 180 à environ 110 questions traitables, avec un engagement à douze mois sur le reste.</p>
<p><strong>Ce que cet échange enseigne :</strong> le questionnaire était surdimensionné et le client le savait. Personne ne l'avait dit parce qu'aucun fournisseur n'avait posé la question. Connaître le cadre a suffi — pas à refuser, mais à ouvrir une conversation que la relation ne permettait pas auparavant.</p>
<p><strong>Semaines 3 à 6 — le socle de données.</strong> Consolidation des données déjà détenues : consommations d'énergie par site sur trois ans, kilomètres parcourus par la flotte, achats par catégorie, effectifs et accidentologie, structure de gouvernance. Rien de nouveau n'est collecté ; tout existait, dispersé dans quatre services.</p>
<p>Ce socle alimente à la fois la réponse client, la demande bancaire et, plus tard, le bilan d'émissions. Le principe est posé pour la suite : <strong>une donnée est collectée une fois et sert partout</strong>.</p>
<p><strong>Mois 2 et 3 — le bilan d'émissions.</strong> Non obligatoire, engagé quand même, et pour une raison purement commerciale : c'est ce qui a coûté un marché public, et c'est ce que la banque cherche à évaluer. La décision se présente en comité de direction sous cette forme, pas sous une forme environnementale — le marché perdu représentait 2,3 M€.</p>
<p>Le bilan couvre les scopes 1, 2 et les postes significatifs du scope 3, avec la méthode du module 2. Résultat : 4 100 tonnes équivalent CO2, dont 71 % sur les achats de marchandises, 14 % sur le transport aval, 9 % sur l'énergie des sites.</p>
<p>Ce chiffre déplace complètement le débat interne. Le plan d'action envisagé jusque-là portait sur l'éclairage des sites et le tri des déchets — soit environ 1 % de l'empreinte. Il portera désormais sur les achats, qui n'avaient jamais été considérés comme un sujet environnemental.</p>
<p><strong>Mois 4 — l'évaluation EcoVadis.</strong> Engagée parce que deux autres clients l'ont demandée depuis, ce qui la rend réutilisable. Le socle de données constitué au mois 1 couvre l'essentiel du dossier. Note obtenue : médaille de bronze, avec un axe faible identifié sur les achats responsables — cohérent avec le bilan d'émissions, ce qui est plutôt rassurant sur la validité des deux.</p>
<p><strong>Mois 6 — le bilan de la séquence.</strong> Un risque juridique supprimé la première semaine. Un référencement client sécurisé avec un périmètre négocié. Une demande bancaire satisfaite. Un bilan d'émissions qui rouvre l'accès aux marchés publics. Une évaluation EcoVadis réutilisable. Et une priorité d'action identifiée sur les achats, qui n'aurait jamais été trouvée par intuition.</p>
<p>Charge réelle : environ 0,4 équivalent temps plein sur six mois, plus 8 000 euros d'accompagnement externe sur le bilan d'émissions.</p>
<p><strong>La leçon transposable.</strong> Aucune des cinq actions n'a été engagée parce qu'elle était obligatoire — l'entreprise n'était soumise à rien de tout cela. Elles l'ont été parce qu'un demandeur identifié le réclamait, avec une conséquence chiffrée à la clé. C'est ce qui les a rendues finançables et c'est ce qui les rendra durables.</p>
<p>L'ordre a compté autant que le contenu : traiter d'abord le risque immédiat et gratuit, puis reprendre la main sur la demande la plus lourde, puis construire le socle, puis seulement mesurer. Une démarche qui aurait commencé par une charte ou une raison d'être aurait laissé la mention « neutre en carbone » en ligne pendant tout ce temps.</p>
"""},

 "checklist": {
   "titre": "Checklist — cadrer une démarche RSE",
   "items": [
     "Les termes RSE, ESG et transition écologique sont employés à bon escient selon l'interlocuteur",
     "Les quatre chiffres de seuil sont relevés : effectif, chiffre d'affaires, total de bilan, statut coté",
     "La méthode de calcul de l'effectif retenue est notée, texte par texte",
     "Le périmètre CSRD est vérifié sur une source postérieure à mars 2026",
     "Le cas du groupe consolidé est traité séparément de celui de l'entreprise seule",
     "Les obligations françaises sont passées par ordre de seuil croissant, à partir de 50 salariés",
     "L'échéance de franchissement du seuil BEGES de 500 salariés est anticipée",
     "Les obligations contractuelles sont recensées : clauses clients, appels d'offres, covenants bancaires",
     "Toutes les allégations environnementales publiées ont été relues au regard du décret de 2022",
     "Aucune mention de neutralité carbone ne subsiste sans bilan, trajectoire et projets publiés",
     "Le document de cadrage est daté et une date de revue est fixée",
     "Chaque demande reçue est rattachée à un demandeur identifié et à une conséquence chiffrée",
     "Le droit de refus au-delà du périmètre VSME est connu et mobilisable",
     "Un socle unique de données alimente tous les questionnaires, plutôt qu'un dossier par demande",
     "Le choix d'un référentiel volontaire part du demandeur, jamais du référentiel",
     "La part du temps RSE consacrée aux réponses plutôt qu'aux actions est mesurée",
     "Le rattachement hiérarchique de la fonction donne accès aux arbitrages d'investissement",
     "Les achats, les opérations et la direction financière sont identifiés comme alliés opérationnels",
     "Le premier livrable produit un résultat visible en six mois et sert à quelqu'un d'autre",
     "Aucun travail de stratégie ou de raison d'être n'est engagé avant la première mesure",
   ]},

 "glossaire": [
   ("RSE", "Responsabilité sociétale des entreprises : prise en compte par une organisation des effets de ses décisions sur la société et l'environnement. Concept de management, défini par l'ISO 26000."),
   ("ESG", "Environnement, social, gouvernance : vocabulaire d'investisseur servant à évaluer un risque extra-financier depuis l'extérieur. Explique la forme des questionnaires reçus."),
   ("Double matérialité", "Distinction entre les impacts de l'activité sur le monde et les risques que le monde fait peser sur l'activité. Fondement de la sélection des enjeux."),
   ("CSRD", "Directive européenne de reporting de durabilité. Depuis l'Omnibus de mars 2026 : plus de 1 000 salariés ET plus de 450 M€ de chiffre d'affaires, à partir de l'exercice 2027."),
   ("Omnibus I", "Directive publiée le 26 février 2026, entrée en vigueur le 18 mars 2026, réduisant d'environ 80 % le périmètre de la CSRD et resserrant la CS3D."),
   ("ESRS", "Normes européennes de reporting de durabilité : douze normes fixant le contenu du rapport. Version révisée adoptée le 3 juillet 2026, environ 61 % de points de données en moins."),
   ("VSME", "Norme volontaire de reporting pour les PME. Sans valeur obligatoire, mais plafond opposable aux demandes d'information des grandes entreprises."),
   ("Plafond de chaîne de valeur", "Disposition limitant ce qu'une entreprise soumise peut exiger d'un partenaire de moins de 1 000 salariés, assortie d'un droit statutaire de refus."),
   ("Taxonomie européenne", "Classement des activités selon leur contribution à six objectifs environnementaux. Crée un langage commun, pas une obligation d'agir."),
   ("CS3D", "Directive sur le devoir de vigilance. Après Omnibus : 5 000 salariés et 1,5 Md€, application différée à juillet 2029, sanctions plafonnées à 3 % du chiffre d'affaires mondial."),
   ("BEGES", "Bilan d'émissions de gaz à effet de serre obligatoire en France au-delà de 500 salariés, tous les quatre ans, avec plan de transition. Sanction de 50 000 €."),
   ("EmpCo", "Directive UE 2024/825 applicable au 27 septembre 2026, sans seuil de taille, interdisant plusieurs pratiques d'allégation environnementale."),
   ("ISO 26000", "Ligne directrice structurant sept questions centrales de responsabilité sociétale. Non certifiable, contrairement à une croyance répandue."),
   ("EcoVadis", "Évaluation documentaire de la maturité RSE d'un fournisseur, la plus demandée dans les relations donneur d'ordre. Mesure un système de gestion, pas une performance physique."),
   ("SBTi", "Initiative validant des trajectoires de réduction compatibles avec l'accord de Paris. Standard net zéro version 2.0 publié le 11 juin 2026."),
 ],

 "retenir": [
   "RSE est un mot de management, ESG un mot d'investisseur, transition écologique un mot de politique publique : employez le bon devant le bon interlocuteur.",
   "La matérialité d'impact et la matérialité financière ne conduisent pas aux mêmes priorités : une démarche solide fait les deux et les confronte.",
   "Depuis mars 2026, la CSRD ne vise que les entreprises de plus de 1 000 salariés ET plus de 450 M€ de chiffre d'affaires, à partir de l'exercice 2027.",
   "La question « suis-je soumis ? » est devenue secondaire : la vraie question est qui demande quoi, sur quel fondement.",
   "Une entreprise soumise ne peut exiger d'un partenaire de moins de 1 000 salariés davantage que le périmètre VSME, et doit mentionner son droit de refus.",
   "Un socle de données VSME construit une fois répond à la quasi-totalité des sollicitations : c'est la réponse structurelle aux demandes multiples.",
   "Toute source antérieure à mars 2026 sur le périmètre CSRD est obsolète : datez ce que vous affirmez sur cette matière.",
   "Le resserrement européen n'a pas supprimé les obligations françaises, dont les seuils sont bien plus bas et les sanctions effectives.",
   "Le BEGES s'impose au-delà de 500 salariés, tous les quatre ans, avec plan de transition depuis 2023, sous peine de 50 000 € et d'exclusion des marchés publics.",
   "Le droit de la consommation s'applique sans aucun seuil dès qu'on communique : c'est l'exposition la plus souvent ignorée.",
   "Une mention de neutralité carbone sans bilan, trajectoire et projets publiés est en infraction au décret de 2022, quelle que soit la taille de l'entreprise.",
   "Les obligations contractuelles — clauses clients, appels d'offres, covenants — sont souvent plus contraignantes que les obligations légales, et ne figurent dans aucun texte.",
   "On ne peut pas être certifié ISO 26000 : c'est une ligne directrice, pas une norme certifiable.",
   "EcoVadis mesure la maturité d'un système de gestion, pas une performance environnementale physique : les deux ne coïncident pas.",
   "Choisissez un référentiel à partir du demandeur, jamais l'inverse : sinon vous achetez une réponse à une question que personne ne pose.",
   "La RSE de conformité consomme toute la ressource en production de preuves : tenez un ratio explicite entre temps de réponse et temps d'action.",
   "Le rattachement hiérarchique décide de tout : seule la direction générale ou financière donne accès aux arbitrages d'investissement.",
   "La légitimité vient des chiffres, pas des convictions : une position défendue par valeur est classée comme une opinion.",
   "Ne commencez jamais par la stratégie : mesurez, priorisez sur les chiffres, agissez, puis formalisez.",
   "Choisissez un premier livrable qui produit un résultat visible en six mois et qui sert à quelqu'un d'autre que vous.",
 ],

 "exercices": [
  {"titre": "Établir une carte d'obligations", "niveau": "Débutant",
   "enonce": [
     "Une entreprise française de services aux entreprises compte 620 salariés, réalise 95 millions d'euros de chiffre d'affaires, n'est pas cotée, et est détenue à 100 % par un groupe européen de 4 200 salariés et 1,1 milliard d'euros de chiffre d'affaires. Son site internet annonce « une entreprise engagée pour le climat » et « 100 % de notre électricité est verte ». Elle répond régulièrement à des marchés publics.",
     "Établissez sa carte d'obligations, en distinguant ce qui relève de la loi, du contrat et du risque. Indiquez ce que vous traitez en priorité et pourquoi.",
   ],
   "corrige": """
<p><strong>1. CSRD — l'entreprise seule n'est pas soumise, le groupe l'est.</strong></p>
<p>620 salariés et 95 M€ : les deux seuils de 1 000 salariés et 450 M€ ne sont pas atteints, et ils sont cumulatifs. Non soumise en propre.</p>
<p>Mais le groupe atteint 4 200 salariés et 1,1 Md€ : il dépasse les deux seuils et sera soumis à compter de l'exercice 2027. La filiale sera donc <em>consolidée</em> dans le rapport du groupe, ce qui signifie qu'elle devra fournir ses données au format ESRS, dans les délais du groupe, avec la qualité exigée par la vérification par un tiers.</p>
<p><em>Ce point est le plus important de l'exercice, et il est presque toujours manqué.</em> La contrainte réelle est identique à celle d'une entreprise soumise, mais elle arrive par le canal interne du groupe et non par la loi. Elle n'apparaît pas si l'on raisonne uniquement sur les seuils de l'entité, et elle a une conséquence pratique immédiate : le calendrier est celui du groupe, donc les données de l'exercice 2027 doivent être collectées à partir de janvier 2027, ce qui veut dire que le système de collecte doit exister fin 2026.</p>
<p>Première action : appeler le responsable durabilité du groupe pour connaître le calendrier et le format attendu. Aujourd'hui, pas dans six mois.</p>
<p><strong>2. BEGES — soumise, et c'est peut-être déjà une infraction.</strong></p>
<p>620 salariés dépasse le seuil de 500. L'entreprise doit publier un bilan d'émissions sur la plateforme de l'ADEME, tous les quatre ans, accompagné d'un plan de transition depuis la loi Industrie verte de 2023. Le scope 3 n'est pas obligatoire à ce niveau de chiffre d'affaires, le seuil étant à 100 M€ — mais l'entreprise en est à 95 M€, donc à moins d'une année de croissance du basculement.</p>
<p><em>Vérification immédiate :</em> le bilan a-t-il été déposé, et à quelle date ? S'il manque ou date de plus de quatre ans, l'entreprise est en infraction, encourt 50 000 euros, et — plus grave compte tenu de son activité — peut être exclue des marchés publics. Cette vérification prend cinq minutes sur la plateforme publique de l'ADEME.</p>
<p><strong>3. Index d'égalité professionnelle — soumise.</strong> Au-delà de 50 salariés, publication annuelle. Vérifier la publication et le score : sous 75 points, des mesures correctives sont obligatoires.</p>
<p><strong>4. Marchés publics — obligation contractuelle, pas légale, et la plus coûteuse.</strong> Les critères environnementaux sont de plus en plus fréquents dans les marchés publics, et un bilan d'émissions à jour en est le support habituel. Ce n'est pas une sanction mais une perte de chiffre d'affaires, et elle est silencieuse : on ne sait généralement pas qu'on a perdu pour ce motif.</p>
<p><strong>5. Communication — l'exposition immédiate, sur deux mentions distinctes.</strong></p>
<p><em>« Une entreprise engagée pour le climat »</em> est une allégation générique. La directive EmpCo, applicable au 27 septembre 2026 sans seuil de taille, vise précisément les allégations vagues non étayées par une preuve documentée. Elle devient une pratique commerciale trompeuse. À reformuler ou à étayer.</p>
<p><em>« 100 % de notre électricité est verte »</em> est plus délicat et plus intéressant. Si l'entreprise achète des garanties d'origine sans contrat d'approvisionnement direct, la formulation est contestable : elle laisse entendre une électricité physiquement renouvelable là où il s'agit d'un mécanisme comptable. La formulation défendable serait « notre consommation d'électricité est couverte à 100 % par des garanties d'origine renouvelable ». Moins vendeur, exact, et non attaquable.</p>
<p><strong>Ce que je traite en priorité, et dans quel ordre.</strong></p>
<p><em>Le jour même :</em> vérifier le dépôt du BEGES sur la plateforme ADEME. C'est la seule infraction potentielle assortie d'une amende et d'une exclusion des marchés publics, sur une entreprise dont l'activité en dépend. Cinq minutes.</p>
<p><em>La première semaine :</em> reformuler les deux allégations du site. Coût nul, risque supprimé, et sans attendre septembre 2026 — le droit français de la consommation sanctionne déjà les allégations trompeuses.</p>
<p><em>Le premier mois :</em> appeler le groupe. Le calendrier CSRD 2027 conditionne toute l'organisation de la collecte, et le découvrir tard est le scénario le plus coûteux de la liste.</p>
<p><em>Le premier trimestre :</em> le BEGES s'il manque, avec son plan de transition, et en anticipant le scope 3 puisque le seuil de 100 M€ est proche.</p>
<p><strong>Le raisonnement à retenir :</strong> l'ordre ne suit ni l'importance des textes ni l'ampleur du travail, mais le produit du risque par la facilité de traitement. Deux des quatre priorités coûtent moins d'une heure.</p>
"""},

  {"titre": "Répondre à une demande client disproportionnée", "niveau": "Intermédiaire",
   "enonce": [
     "Votre entreprise, 210 salariés, reçoit d'un client représentant 30 % de son chiffre d'affaires une demande en trois volets : un questionnaire ESG de 140 questions, l'obtention d'une médaille EcoVadis argent sous douze mois, et un objectif de réduction des émissions validé SBTi sous vingt-quatre mois. Le courriel indique que ces éléments conditionneront le renouvellement du contrat-cadre.",
     "Construisez votre réponse et votre plan. Traitez explicitement la question de savoir ce que vous acceptez, ce que vous négociez et ce que vous refusez, et comment vous le dites.",
   ],
   "corrige": """
<p><strong>Point de départ : les trois demandes ne sont pas de même nature, et les traiter en bloc est l'erreur à éviter.</strong> L'une est légitime et faisable, l'une est négociable sur le calendrier, la troisième est disproportionnée au point qu'y consentir vous mettrait en difficulté. Répondre « oui » globalement par crainte de perdre 30 % du chiffre d'affaires est le réflexe naturel et la pire décision : vous vous engagez sur un objectif que vous ne tiendrez pas, et le manquement se constatera dans deux ans, quand la relation aura été construite dessus.</p>
<p><strong>Volet 1 — le questionnaire : accepté, avec un périmètre explicite.</strong></p>
<p>À 210 salariés, vous êtes très en dessous du plafond de chaîne de valeur de 1 000 salariés. Le client ne peut pas exiger au-delà du périmètre VSME sans mentionner votre droit de refus.</p>
<p>Conduite : répondre intégralement sur le périmètre VSME, ajouter les données que vous détenez déjà et qui dépassent ce périmètre — il n'y a aucune raison de les retenir, et les fournir installe la bonne foi — et signaler les questions hors périmètre en indiquant lesquelles pourront être documentées à douze mois.</p>
<p>Ne brandissez pas le droit de refus comme un argument juridique. Mentionnez-le une fois, factuellement, et concentrez l'échange sur ce que vous fournissez. « Voici ce que nous vous donnons » place la conversation bien mieux que « voici ce que vous ne pouvez pas exiger ».</p>
<p><strong>Volet 2 — EcoVadis argent en douze mois : négocié sur le calendrier.</strong></p>
<p>La demande est légitime et le référentiel est le bon pour une relation fournisseur. La difficulté est le niveau et le délai. Une première évaluation aboutit couramment à un bronze ; l'argent suppose des politiques formalisées, des indicateurs suivis et des preuves documentaires sur les quatre thèmes du référentiel.</p>
<p>Ce qui est faisable en douze mois : une première évaluation complète, un plan d'amélioration construit sur le rapport, et un engagement daté sur les axes faibles. Ce qui ne l'est pas de façon fiable : garantir un niveau de médaille, qui dépend d'une notation dont vous ne maîtrisez ni les critères ni les seuils.</p>
<p>Formulation : « nous engageons l'évaluation ce trimestre et nous nous engageons sur le plan d'amélioration issu du rapport. Nous ne pouvons pas garantir contractuellement un niveau de médaille, qui dépend d'un tiers évaluateur — aucun fournisseur sérieux ne le peut. Nous pouvons en revanche nous engager sur la réévaluation à dix-huit mois et sur la communication du rapport complet, y compris s'il est mauvais. »</p>
<p>Cette dernière proposition — la transparence sur un résultat éventuellement décevant — vaut souvent plus qu'un engagement de résultat, parce qu'elle est crédible.</p>
<p><strong>Volet 3 — l'objectif validé SBTi en vingt-quatre mois : refusé en l'état, avec une contre-proposition.</strong></p>
<p>Il faut mesurer ce qui est demandé. Une validation SBTi suppose un inventaire complet des émissions incluant le scope 3, une trajectoire compatible avec l'accord de Paris, un dossier de validation, et un engagement public sur des cibles à cinq et dix ans. Pour une entreprise de 210 salariés sans bilan carbone existant, c'est un projet de deux à trois ans mobilisant des ressources dont vous ne disposez pas, avec des coûts de validation et de suivi récurrents.</p>
<p>Surtout, l'ordre est faux : on ne fixe pas une trajectoire avant de connaître son empreinte. S'engager sur une validation SBTi sans bilan revient à promettre une destination sans savoir d'où l'on part.</p>
<p>Contre-proposition en trois temps, chacun daté : bilan d'émissions complet scopes 1, 2 et postes significatifs du scope 3 à douze mois ; plan de réduction chiffré avec objectif à cinq ans, construit sur ce bilan, à dix-huit mois ; examen de l'opportunité d'une validation SBTi à vingt-quatre mois, au vu de ce que le plan aura produit.</p>
<p>Argument à donner au client, et il est réel : « un objectif validé sans plan d'action derrière ne réduira pas vos émissions de scope 3, et c'est cela qui vous intéresse. Un bilan sérieux suivi d'un plan sur nos deux postes principaux vous apportera davantage à vingt-quatre mois qu'un dossier de validation. »</p>
<p><strong>La forme de la réponse compte autant que le fond.</strong></p>
<p>Ne répondez pas par courriel. Demandez un rendez-vous, présentez un document d'une page en trois colonnes — ce que nous faisons, sous quel délai, et ce que nous ne pouvons pas nous engager à faire — et laissez-le. Un engagement écrit, daté, sur un périmètre réduit, est infiniment mieux reçu qu'un accord de principe sur tout.</p>
<p><strong>Le point décisif :</strong> ces demandes émanent presque toujours d'un service achats appliquant une grille uniforme, sans connaissance de la taille de votre entreprise. Dans la majorité des cas, un fournisseur qui répond de façon structurée, datée et honnête sur un périmètre réduit est mieux noté qu'un fournisseur qui accepte tout et ne livre rien. Le risque que vous croyez prendre en négociant est presque toujours inférieur au risque de l'engagement non tenu.</p>
<p><strong>Ce qu'il ne faut pas faire :</strong> accepter les trois volets pour sécuriser le renouvellement, et traiter le problème dans deux ans. Vous auriez alors un manquement contractuel constaté, sur un sujet où la bonne foi est le principal actif — et vous auriez perdu la possibilité de renégocier, puisque l'engagement aura été pris.</p>
"""},

  {"titre": "Structurer une fonction RSE qui ne se limite pas à répondre", "niveau": "Avancé",
   "enonce": [
     "Vous prenez la responsabilité RSE d'une entreprise de 900 salariés. La fonction existe depuis trois ans, tenue par une personne rattachée à la communication. Le bilan de ces trois ans : une charte, un rapport RSE annuel de 40 pages, une fresque du climat suivie par 120 salariés, un partenariat associatif, et douze questionnaires clients remplis par an. Aucune donnée d'émissions consolidée. Le comité de direction estime que « le sujet est traité ».",
     "Construisez votre plan sur douze mois. Traitez explicitement la question du rattachement, celle de ce que vous arrêtez, et la façon dont vous obtenez un premier arbitrage budgétaire.",
   ],
   "corrige": """
<p><strong>Le diagnostic, à poser sans le dire ainsi : la fonction a produit de la preuve d'intention et aucune preuve d'effet.</strong> Cette formulation est juste et il ne faut surtout pas l'employer devant le comité de direction — elle disqualifie trois ans de travail de personnes présentes, et vous perdrez toute possibilité d'alliance interne. Le travail existant sera votre point d'appui, pas votre repoussoir.</p>
<p><strong>Mois 1 à 2 — comprendre et mesurer, sans rien annoncer.</strong></p>
<p>Résistez à la tentation d'annoncer un nouveau cap dès l'arrivée. Vous ne savez pas encore où sont les émissions, et vous risquez d'annoncer des priorités que le premier bilan démentira. Une réorientation annoncée puis corrigée coûte plus cher que deux mois de silence.</p>
<p>Faites trois choses. <em>Une carte d'obligations datée</em> : à 900 salariés, l'entreprise est soumise au BEGES, à l'index égalité, et approche des seuils CSRD si le chiffre d'affaires suit. Le BEGES est le point à vérifier en premier — s'il manque, vous avez une infraction en cours et un levier immédiat.</p>
<p><em>Un premier ordre de grandeur des émissions</em>, en une semaine, par une méthode grossière : consommations d'énergie, flotte, et achats convertis par ratios monétaires. Le résultat sera imprécis à plus ou moins 30 %, et cela suffit largement à savoir si l'empreinte est concentrée sur les achats, l'énergie ou le transport. La précision viendra plus tard ; la structure, elle, ne changera pas.</p>
<p><em>Huit entretiens</em> : directeur général, directeur financier, directeur des achats, directeur industriel ou des opérations, directeur des ressources humaines, deux clients, un membre du comité social et économique. Une question à chacun : « qu'est-ce que la RSE devrait vous apporter et qu'elle ne vous apporte pas ? ». Vous obtiendrez huit réponses concrètes, et elles constitueront votre feuille de route mieux qu'aucune analyse.</p>
<p><strong>Mois 3 — la présentation qui change le rattachement.</strong></p>
<p>C'est le moment décisif de l'année, et il tient en une réunion de comité de direction. Trois éléments, pas davantage.</p>
<p><em>Où sont réellement les enjeux :</em> le graphique de répartition des émissions. S'il montre, comme c'est probable, que 70 % de l'empreinte est chez les fournisseurs, il démontre en une image que le sujet appartient aux achats et non à la communication. Vous n'avez pas besoin de le dire : le graphique le dit.</p>
<p><em>Ce que cela coûte déjà :</em> chiffrez. Marchés perdus faute de bilan, temps passé aux questionnaires converti en euros, exposition juridique sur les allégations publiées, et si l'entreprise a un financement bancaire, les conditions extra-financières éventuelles. Un chiffre de coût actuel est ce qui transforme le sujet d'un poste de dépense en un poste de risque.</p>
<p><em>Ce que vous proposez :</em> un plan à douze mois, trois priorités, un budget, et une demande explicite de rattachement à la direction générale ou financière.</p>
<p>Sur ce dernier point, la formulation compte. Ne dites pas que le rattachement à la communication est inadapté. Dites : « les décisions qui déterminent notre empreinte sont des décisions d'achat et d'investissement. Pour peser dessus, je dois être dans la boucle des arbitrages. C'est la seule raison de la demande. » Un argument fonctionnel passe là où un argument de statut échoue.</p>
<p><strong>Mois 4 à 12 — trois priorités, et ce que vous arrêtez.</strong></p>
<p><em>Priorité 1 — le bilan d'émissions sérieux et le plan de transition</em>, obligatoires au titre du BEGES et utiles à tout le reste. C'est la matière de toutes vos décisions ultérieures.</p>
<p><em>Priorité 2 — deux actions de réduction sur le poste principal.</em> Deux, pas dix. Choisies pour être achevables dans l'année et mesurables. Si le poste principal est les achats, cela peut être la révision d'une famille d'achats représentant 15 % de l'empreinte, et l'introduction d'un critère carbone dans les consultations au-dessus d'un certain montant. Le résultat mesuré de ces deux actions est ce que vous présenterez dans douze mois, et c'est ce qui décidera de votre budget de l'année suivante.</p>
<p><em>Priorité 3 — industrialiser les réponses.</em> Un socle unique de données, alimenté une fois, servant les douze questionnaires. L'objectif est de faire passer le temps consacré aux réponses de l'essentiel de la fonction à environ un quart.</p>
<p><strong>Ce que vous arrêtez — et c'est la partie délicate.</strong></p>
<p><em>Le rapport RSE de 40 pages :</em> réduit à huit pages factuelles. Personne ne le lit, il coûte plusieurs semaines de travail et de la prestation graphique, et depuis EmpCo il constitue une surface d'exposition sur chaque affirmation non étayée. Argument à donner : « nous publions moins et nous étayons tout ».</p>
<p><em>Le partenariat associatif :</em> maintenu. Il coûte peu, il a du sens pour les salariés, et l'arrêter vous ferait passer pour quelqu'un qui supprime ce qui plaît. Choisissez vos batailles — le coût politique de cet arrêt dépasse largement le gain.</p>
<p><em>La fresque du climat :</em> maintenue mais repositionnée. Elle est utile en sensibilisation et sans effet sur les émissions. Rattachez-la à la formation, avec son budget, et cessez de la présenter comme une action RSE. Vous libérez ainsi votre indicateur d'action sans supprimer un dispositif apprécié.</p>
<p><em>La charte :</em> conservée telle quelle. La réécrire consommerait deux mois pour un gain nul.</p>
<p><strong>Comment obtenir le premier arbitrage budgétaire.</strong></p>
<p>Ne demandez pas un budget RSE. Demandez le financement d'une action précise, chiffrée en coût et en effet, présentée comme n'importe quel investissement : montant, gain attendu, délai, risque évité. Une demande de 40 000 euros pour un bilan d'émissions qui rouvre l'accès à des marchés publics chiffrés à 2 M€ s'arbitre en cinq minutes. Une demande de « budget RSE » de 40 000 euros se reporte au prochain comité.</p>
<p>C'est la différence de traitement la plus nette que vous observerez, et elle ne tient qu'à la formulation.</p>
<p><strong>Ce à quoi vous saurez que ça marche, dans l'ordre d'apparition.</strong></p>
<p><em>Mois 4 :</em> quelqu'un d'un autre service vous sollicite spontanément avant de prendre une décision. C'est le premier signal, il est qualitatif, et il vaut tous les indicateurs.</p>
<p><em>Mois 6 :</em> un critère environnemental apparaît dans un cahier des charges achats sans que vous l'ayez demandé.</p>
<p><em>Mois 9 :</em> le sujet est évoqué en comité de direction hors de votre point à l'ordre du jour.</p>
<p><em>Mois 12 :</em> une décision d'investissement a été arbitrée en tenant compte d'un chiffre que vous avez produit. C'est le seul critère qui compte réellement, et il ne se décrète pas : il se prépare en s'assurant que le chiffre en question est juste.</p>
<p><strong>Ce qui n'est pas un bon signal :</strong> une augmentation du nombre de questionnaires bien notés, ou un rapport RSE mieux illustré. On peut améliorer indéfiniment sa note d'évaluation sans réduire une seule tonne — c'est exactement ce que les trois années précédentes ont produit, et c'est le piège dans lequel il serait facile de retomber sous une forme plus sophistiquée.</p>
"""},
 ],

 "ressources": [
   "<strong>Le Portail RSE de l'État</strong> (portail-rse.beta.gouv.fr) — le point d'entrée officiel pour vérifier les seuils et les obligations françaises. À privilégier sur toute source commerciale, et à consulter systématiquement plutôt que de se fier à un document téléchargé.",
   "<strong>La plateforme des bilans GES de l'ADEME</strong> (bilans-ges.ademe.fr) — dépôt obligatoire du BEGES, et surtout base publique consultable : vous pouvez y lire les bilans de vos concurrents et de vos clients, ce qui est le moyen le plus rapide de calibrer le vôtre.",
   "<strong>La norme VSME publiée par l'EFRAG</strong> — le socle à construire si votre entreprise est sollicitée par des clients soumis à la CSRD. C'est le document qui définit le plafond que l'on peut vous opposer.",
   "<strong>Le module 2 de cette formation</strong> — le bilan d'émissions, qui est le livrable dont dépendent le BEGES, la réponse bancaire, les marchés publics et le plan d'action. N'engagez pas de travail de stratégie avant de l'avoir produit.",
 ],
}

QUIZ["rse-transition-ecologique/module-1"] = {
 "module_id": "formation-rse-transition-ecologique-module-1",
 "version": "2.0", "last_verified": "2026-09-04",
 "questions": [
  {"id":"q1","question":"Quels sont les seuils de la CSRD après la directive Omnibus entrée en vigueur le 18 mars 2026 ?",
   "choices":[{"key":"a","text":"Plus de 1 000 salariés ET plus de 450 M€ de chiffre d'affaires net, cumulativement"},
              {"key":"b","text":"250 salariés ou 50 M€ de chiffre d'affaires, au choix"},
              {"key":"c","text":"500 salariés et 100 M€ de chiffre d'affaires"}],
   "correct_answer":"a","feedback":"Les deux conditions doivent être remplies, ce qui a réduit le périmètre d'environ 80 %. Première application aux exercices ouverts à compter de 2027."},
  {"id":"q2","question":"Un client soumis à la CSRD vous adresse 180 questions. Votre entreprise compte 380 salariés. Que prévoit la réglementation ?",
   "choices":[{"key":"a","text":"Vous devez répondre intégralement, la CSRD s'appliquant par ricochet à toute la chaîne de valeur"},
              {"key":"b","text":"Au-delà du périmètre VSME, vous disposez d'un droit statutaire de refus, que le client doit vous signaler"},
              {"key":"c","text":"Vous n'avez aucune obligation et pouvez ignorer la demande sans conséquence"}],
   "correct_answer":"b","feedback":"Le plafond de chaîne de valeur protège les partenaires de moins de 1 000 salariés. Cela n'oblige pas à refuser : cela permet de négocier le périmètre."},
  {"id":"q3","question":"À partir de quel effectif le bilan d'émissions de gaz à effet de serre est-il obligatoire en France métropolitaine ?",
   "choices":[{"key":"a","text":"500 salariés"},
              {"key":"b","text":"250 salariés"},
              {"key":"c","text":"1 000 salariés, comme la CSRD"}],
   "correct_answer":"a","feedback":"Article L. 229-25 du code de l'environnement, tous les quatre ans, avec plan de transition depuis 2023. Sanction de 50 000 € et exclusion possible des marchés publics."},
  {"id":"q4","question":"Peut-on être certifié ISO 26000 ?",
   "choices":[{"key":"a","text":"Oui, par tout organisme accrédité, comme pour l'ISO 9001"},
              {"key":"b","text":"Non : c'est une ligne directrice, pas une norme certifiable"},
              {"key":"c","text":"Oui, mais uniquement pour les entreprises de plus de 500 salariés"}],
   "correct_answer":"b","feedback":"Confusion très répandue. L'ISO 26000 structure sept questions centrales et sert de grille de cadrage, sans certification possible."},
  {"id":"q5","question":"Comment choisir un référentiel volontaire comme EcoVadis, B Corp ou le CDP ?",
   "choices":[{"key":"a","text":"En prenant le plus exigeant, qui couvrira automatiquement les autres"},
              {"key":"b","text":"En prenant le moins coûteux la première année, quitte à changer ensuite"},
              {"key":"c","text":"En partant du demandeur et de ce qu'il cherche à évaluer"}],
   "correct_answer":"c","feedback":"Un client industriel demande EcoVadis, une banque regarde le CDP, un marché public un bilan d'émissions. Adopter un référentiel sans demandeur identifié, c'est répondre à une question que personne ne pose."},
  {"id":"q6","question":"Dans quel ordre construire une démarche RSE en entreprise de taille moyenne ?",
   "choices":[{"key":"a","text":"Raison d'être, stratégie, indicateurs, puis actions"},
              {"key":"b","text":"Certification d'abord, car elle structure toute la démarche"},
              {"key":"c","text":"Mesurer, prioriser sur les chiffres, agir sur deux ou trois postes, puis formaliser la stratégie"}],
   "correct_answer":"c","feedback":"Une stratégie écrite avant toute mesure repose sur des intuitions : il est fréquent qu'un bilan montre ensuite que 80 % de l'empreinte est dans un poste qu'elle n'évoquait pas."},
 ]}

for k, m in M.items():
    w, full = build(k, m)
    print(f"{k:38s} cours: {w} mots | page: {full} mots")
for k, q in QUIZ.items():
    p = os.path.join("/tmp/out_v2", k, "quiz.json")
    os.makedirs(os.path.dirname(p), exist_ok=True)
    json.dump(q, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    open(p, "a", encoding="utf-8").write("\n")
    print(f"{k}: quiz {len(q['questions'])} questions")
