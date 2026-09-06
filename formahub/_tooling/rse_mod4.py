#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, json, os
sys.path.insert(0, "/tmp")
from fh_builder import build

M = {}
QUIZ = {}
FORM = "RSE &amp; transition écologique en entreprise"

M["rse-transition-ecologique/module-4"] = {
 "formation": FORM,
 "titre": "Reporting, Communication et Greenwashing",
 "num": 4, "total": 4, "duree": "70 min", "niveau": "Intermédiaire",
 "module_id": "formation-rse-transition-ecologique-module-4",
 "situation": [
   "Le plan a produit ses premiers résultats : environ 290 tonnes évitées et 118 000 euros d'économies nettes sur douze mois. Le comité de direction est satisfait, et il souhaite le faire savoir.",
   "Le service marketing revient avec quatre propositions pour le site et les supports commerciaux. « Une entreprise engagée pour le climat. » « Nos livraisons sont neutres en carbone. » « Moins 20 % d'émissions depuis 2024. » « Une gamme éco-responsable. »",
   "Trois de ces quatre formulations vous exposent à une sanction, et la quatrième est contestable. La troisième est la plus délicate parce qu'elle repose sur un chiffre réel : les émissions ont bien baissé de 20 % — mais l'essentiel de cette baisse vient d'un changement de méthode de calcul sur les achats, pas d'une réduction. Le marketing ne le sait pas ; vous, si.",
   "Le directeur général veut un communiqué pour la semaine prochaine. Ce module traite de ce qui se joue à ce moment précis : comment rendre compte honnêtement de résultats réels, dans un cadre juridique qui s'est considérablement resserré, sans renoncer à valoriser un travail qui le mérite.",
 ],
 "objectifs": [
   "Distinguer le reporting, qui rend compte, de la communication, qui valorise",
   "Situer le cadre juridique applicable aux allégations environnementales en France et dans l'Union",
   "Reconnaître les sept formulations qui exposent à une sanction, et leurs versions défendables",
   "Appliquer la règle de la preuve de même profondeur que l'allégation",
   "Traiter honnêtement un objectif annoncé dont l'écart n'est pas comblé",
   "Mettre en place la gouvernance qui fait tenir une démarche au-delà d'une personne",
 ],
 "sections": [
  {"titre": "Rendre compte et communiquer sont deux exercices différents",
   "paras": [
     "La confusion entre les deux est à l'origine de la quasi-totalité des accidents de communication environnementale, et elle mérite d'être posée nettement.",
     "<strong>Le reporting rend compte.</strong> Son destinataire cherche à évaluer, et il est parfois hostile : un client qui référence, une banque qui prête, un vérificateur, un investisseur. Sa qualité se mesure à sa complétude, à sa traçabilité et à la manière dont il traite ses propres faiblesses. Un bon rapport de durabilité contient des chiffres décevants, des postes non couverts et des objectifs manqués — et c'est ce qui le rend utilisable.",
     "<strong>La communication valorise.</strong> Son destinataire est un client, un candidat, le grand public, et l'objectif est de mettre en avant. Elle sélectionne par nature, et cette sélection est légitime : personne ne reproche à une publicité de ne pas tout dire.",
     "Le problème naît quand la communication puise dans le reporting en ne retenant que les bonnes lignes, et quand elle emploie des mots — « neutre », « vert », « durable », « éco-responsable » — dont le sens juridique est désormais bien plus étroit que le sens courant.",
     "<strong>La règle qui évite l'essentiel des accidents :</strong> tout ce qui est communiqué à l'extérieur doit pouvoir être retrouvé, dans le même sens et avec le même périmètre, dans un document de reporting accessible. Si une affirmation ne peut pas être adossée à une ligne d'un document que vous accepteriez de montrer à un contradicteur, elle ne sort pas.",
     "Cette règle a un corollaire pratique : <strong>la fonction RSE doit valider toute communication environnementale avant diffusion.</strong> Non par contrôle, mais parce qu'elle est seule à savoir ce que les chiffres recouvrent. Dans la situation d'ouverture, le marketing n'a commis aucune faute : il ignorait que la baisse de 20 % venait d'un changement de méthode. C'est un défaut de processus, pas de personne.",
   ],
   "blocks": [
     {"type": "exemple", "titre": "le même résultat, deux traitements",
      "paras": [
        "Résultat réel : 290 tonnes évitées sur 4 700, soit 6,2 % ; et un total affiché en baisse de 20 % du fait d'un changement de méthode sur les achats.",
        "<em>Version reporting :</em> « Nos émissions 2026 s'établissent à 3 760 tCO2e contre 4 700 en 2025. Cette évolution combine deux effets : une réduction réelle de 290 tonnes liée à quatre actions du plan, et une révision à la baisse de 650 tonnes résultant du passage à des données physiques sur deux familles d'achats. À méthode constante, la réduction est de 6,2 %. L'année de référence a été recalculée en conséquence et s'établit désormais à 4 050 tCO2e. »",
        "<em>Version communication défendable :</em> « Nos actions ont permis d'éviter 290 tonnes de CO2 en 2026, soit 6 % de nos émissions, tout en générant 118 000 euros d'économies. »",
        "<em>Version communication attaquable :</em> « Moins 20 % d'émissions en un an. »",
        "La deuxième version est courte, positive, exacte, et adossée à une ligne du rapport. Elle est moins spectaculaire que la troisième, et c'est le seul reproche qu'on puisse lui faire. La troisième est un chiffre vrai employé pour dire quelque chose de faux — définition assez exacte de ce que le droit sanctionne.",
      ]},
     {"type": "pitfall", "titre": "publier un rapport sans ses faiblesses",
      "paras": [
        "Un rapport de durabilité entièrement positif produit l'effet inverse de celui recherché sur ses lecteurs professionnels. Un analyste, un acheteur ou un banquier sait qu'aucune entreprise n'a que de bons résultats ; un document sans aucune ombre signale soit une sélection, soit une démarche naissante qui se présente comme mature.",
        "À l'inverse, un rapport qui écrit « nous n'avons pas atteint notre objectif sur ce poste, voici pourquoi et ce que nous changeons » obtient une crédibilité qui rejaillit sur tout le reste du document.",
        "La conduite : dans chaque rapport, au moins un objectif manqué expliqué, un poste non couvert avec son ordre de grandeur estimé, et une incertitude affichée. Ce n'est pas de l'humilité, c'est ce qui rend les bons chiffres croyables.",
      ]},
   ]},

  {"titre": "Le cadre juridique s'est considérablement resserré",
   "paras": [
     "Communiquer sur l'environnement relevait, il y a quelques années, de la réputation. C'est désormais une matière encadrée par le droit de la consommation, avec des sanctions proportionnelles au chiffre d'affaires et une administration active. L'état du droit au 4 septembre 2026 se résume en quatre éléments.",
     "<strong>Le droit français de la consommation</strong> sanctionne depuis longtemps la pratique commerciale trompeuse, définie comme toute allégation susceptible d'induire en erreur le consommateur moyen. Les amendes peuvent atteindre 10 % du chiffre d'affaires moyen annuel. La direction générale de la concurrence, de la consommation et de la répression des fraudes conduit chaque année plus d'un millier de contrôles sur les allégations environnementales, avec un taux d'anomalie élevé — de l'ordre de 30 %. Ce cadre s'applique <strong>sans aucun seuil de taille</strong>, à toute entreprise qui communique.",
     "<strong>La loi Climat et Résilience de 2021 et son décret d'application de 2022</strong> encadrent spécifiquement les allégations de neutralité carbone. Toute mention de ce type dans une publicité exige la publication d'un bilan d'émissions couvrant les scopes 1, 2 et les émissions indirectes significatives, d'une trajectoire de réduction avec des objectifs datés, et du détail des projets de compensation financés. Sanction jusqu'à 100 000 euros pour une personne morale (20 000 euros pour une personne physique), montant pouvant être porté au total des dépenses engagées dans l'opération non conforme (article L. 229-69 du code de l'environnement) — à ne pas confondre avec l'amende pour pratique commerciale trompeuse, qui relève du droit de la consommation et dont les plafonds sont autres. En pratique, ces exigences rendent la mention « neutre en carbone » à peu près inutilisable pour la plupart des entreprises.",
     "<strong>La directive européenne 2024/825, dite EmpCo</strong>, s'applique dans l'ensemble des États membres à compter du <strong>27 septembre 2026</strong>, sans seuil de taille. Elle inscrit dans le droit de la consommation une liste de pratiques interdites en toutes circonstances, dont plusieurs visent directement les allégations environnementales : les allégations génériques non étayées par une performance reconnue, l'affirmation qu'un produit a un effet neutre ou positif sur l'environnement en raison d'une compensation, les labels de durabilité non fondés sur un système de certification vérifié par un tiers, et la présentation comme un avantage de ce qui n'est qu'une obligation légale.",
     "<strong>La directive Green Claims</strong>, qui devait imposer une vérification préalable des allégations, est en suspens : la Commission a annoncé en juin 2025 son intention de la retirer, sans que le retrait ait été formalisé, et le texte reste inscrit dans les programmes de travail. Il serait imprudent de parier sur sa disparition définitive, et il serait tout aussi imprudent d'attendre son adoption pour se mettre en conformité — l'essentiel de ce qu'elle prévoyait est déjà couvert par les trois éléments précédents.",
     "<strong>La conséquence pratique tient en une phrase :</strong> une entreprise française qui communique sur l'environnement est déjà soumise à un régime exigeant, quelle que soit sa taille, et indépendamment de la CSRD dont elle relève rarement. C'est l'inverse exact de l'idée reçue selon laquelle la RSE ne concernerait que les grandes entreprises.",
   ],
   "blocks": [
     {"type": "h3", "titre": "Le principe qui sous-tend tout le dispositif",
      "paras": [
        "Toutes ces règles reposent sur une même idée, qu'il vaut mieux comprendre qu'apprendre par cœur : <strong>la preuve doit avoir la même profondeur que l'allégation.</strong>",
        "Une affirmation étroite et vérifiable demande une preuve étroite. « Nos emballages contiennent 60 % de matière recyclée » se prouve par une fiche technique fournisseur, et l'affaire est close.",
        "Une affirmation large demande une preuve large. « Notre entreprise est respectueuse de l'environnement » porte sur l'ensemble des impacts de l'ensemble de l'activité : la prouver supposerait une analyse complète du cycle de vie sur tous les produits et tous les impacts. Personne ne dispose de cela, et c'est exactement pourquoi les allégations génériques sont interdites — non parce qu'elles seraient fausses, mais parce qu'elles sont invérifiables par construction.",
        "Le corollaire est libérateur plutôt que contraignant : <strong>plus vous êtes précis, plus vous êtes en sécurité.</strong> « Nous avons réduit de 18 % la consommation d'énergie de nos trois sites entre 2024 et 2026 » est à la fois plus solide juridiquement et plus convaincant commercialement que « nous sommes engagés pour la planète ». Le droit pousse ici dans le même sens qu'une bonne communication.",
      ]},
     {"type": "exemple", "titre": "ce que la DGCCRF regarde",
      "paras": [
        "Les contrôles portent sur des points précis et répétitifs, connaître leur liste est le meilleur autodiagnostic possible.",
        "<em>L'allégation est-elle étayée par un document daté ?</em> C'est la première demande, et l'absence de dossier de preuve suffit à caractériser le manquement, indépendamment de la véracité de l'affirmation.",
        "<em>Le périmètre de l'allégation correspond-il à celui de la preuve ?</em> Cas fréquent : une preuve portant sur un produit, une allégation portant sur toute la gamme. Ou une preuve sur les scopes 1 et 2, une allégation sur « nos émissions ».",
        "<em>L'allégation compare-t-elle sans dire à quoi ?</em> « Moins d'emballage » ou « plus respectueux » supposent un point de comparaison explicite et une preuve de l'écart.",
        "<em>Le label affiché est-il vérifié par un tiers indépendant ?</em> Un logo créé par l'entreprise elle-même, ou par une association qu'elle finance, tombe sous l'interdiction des labels de durabilité non certifiés.",
        "<em>L'avantage mis en avant est-il une obligation légale ?</em> Présenter comme un engagement le respect d'une norme obligatoire est une pratique explicitement interdite par EmpCo.",
        "<em>La compensation est-elle présentée comme une neutralité ?</em> Point désormais central, et le plus fréquemment sanctionné.",
      ]},
   ]},

  {"titre": "Sept formulations qui exposent, et leurs versions défendables",
   "paras": [
     "Le passage du cadre juridique à la pratique se fait sur des formulations concrètes. Sept reviennent constamment, et chacune a une version défendable qui dit souvent mieux ce qu'on voulait dire.",
     "<strong>1. « Neutre en carbone », « zéro carbone », « climatiquement neutre ».</strong> Interdite si elle repose sur une compensation, ce qui est le cas dans la quasi-totalité des situations. <em>Version défendable :</em> séparer les deux éléments. « Nous avons réduit nos émissions de X % depuis 2024 et nous finançons par ailleurs des projets de séquestration à hauteur de Y tonnes. » La contribution est mentionnée, elle n'est pas présentée comme une annulation.",
     "<strong>2. « Éco-responsable », « vert », « durable », « respectueux de l'environnement ».</strong> Allégations génériques, invérifiables par construction. <em>Version défendable :</em> nommer l'attribut précis et son ampleur. « Emballage contenant 60 % de matière recyclée » plutôt que « emballage éco-responsable ».",
     "<strong>3. « Engagé pour le climat », « acteur de la transition ».</strong> Générique également, et fréquente en communication institutionnelle. <em>Version défendable :</em> l'engagement devient un fait daté. « Nous nous sommes engagés à réduire nos émissions de 18 % d'ici 2030, avec un plan de cinq actions publié. »",
     "<strong>4. « Notre produit est 40 % plus écologique ».</strong> Comparaison sans point de comparaison ni indicateur. <em>Version défendable :</em> dire par rapport à quoi, sur quel indicateur, et sur quel périmètre. « 40 % d'émissions en moins que notre référence précédente, sur le périmètre fabrication et transport. »",
     "<strong>5. « Fabriqué à partir de matériaux recyclés ».</strong> L'ambiguïté porte sur la proportion : le consommateur comprend « majoritairement », la réalité est parfois 5 %. <em>Version défendable :</em> le pourcentage, et la partie du produit concernée.",
     "<strong>6. « Sans produits chimiques », « 100 % naturel ».</strong> La première est scientifiquement fausse ; la seconde ne garantit rien sur l'impact — un produit naturel peut être plus émetteur ou plus toxique qu'un produit de synthèse. <em>Version défendable :</em> nommer ce qui est absent et pourquoi cela compte.",
     "<strong>7. « Conforme à la réglementation environnementale ».</strong> Présenter une obligation comme un avantage est explicitement interdit. <em>Version défendable :</em> ne rien dire — le respect de la loi n'est pas un argument — ou mentionner ce qui va au-delà, en précisant l'écart.",
   ],
   "blocks": [
     {"type": "method", "titre": "valider une allégation avant diffusion, en cinq questions",
      "paras": ["Cinq minutes par allégation. À appliquer à tout élément de communication comportant un terme environnemental, y compris une mention sur une signature de courriel ou un panneau en salle d'attente."],
      "steps": [
        "<strong>Sur quoi porte exactement l'allégation ?</strong> Un produit, une gamme, un site, l'entreprise entière ? Écrivez-le. La plupart des difficultés viennent d'un périmètre implicite plus large que celui de la preuve.",
        "<strong>Quel document daté la prouve ?</strong> Nommez-le et vérifiez qu'il existe et qu'il est accessible. Sans document, l'allégation ne sort pas, même si vous êtes certain de sa véracité.",
        "<strong>Le périmètre de la preuve couvre-t-il celui de l'allégation ?</strong> C'est le point de contrôle le plus productif. Une preuve sur un produit ne couvre pas une gamme ; une preuve sur les scopes 1 et 2 ne couvre pas « nos émissions ».",
        "<strong>Un lecteur de bonne foi pourrait-il comprendre autre chose que ce que nous voulons dire ?</strong> Le critère juridique est le consommateur moyen, pas le spécialiste. Faites relire par quelqu'un du secteur qui ne connaît pas le dossier.",
        "<strong>Que se passe-t-il si un journaliste demande la preuve demain ?</strong> Si la réponse suppose une demi-journée de préparation ou des explications de méthode, l'allégation est trop large pour ce qu'elle repose.",
        "<strong>Archivez le dossier de preuve</strong> avec la date de diffusion et le support. Le contrôle peut porter sur une communication d'il y a deux ans, et personne ne se souvient alors de ce qui la fondait.",
      ]},
     {"type": "pitfall", "titre": "le chiffre exact employé pour dire quelque chose de faux",
      "paras": [
        "C'est le cas de la mise en situation, et c'est le plus difficile à traiter en interne, parce que personne n'a menti. Les émissions ont bien baissé de 20 %. Le chiffre est exact et sa communication serait trompeuse, puisque l'essentiel de la baisse provient d'un changement de méthode.",
        "Le droit ne s'intéresse pas à l'exactitude arithmétique mais à ce que l'affirmation fait comprendre. Un consommateur qui lit « moins 20 % d'émissions » comprend que l'entreprise a réduit ses émissions de 20 %. Ce n'est pas le cas.",
        "La difficulté réelle est relationnelle : le marketing a un chiffre validé par le rapport et ne comprend pas qu'on le lui refuse. Deux choses aident. Expliquer avec la comparaison financière — « c'est comme annoncer une hausse du chiffre d'affaires alors qu'on a changé de méthode de reconnaissance du revenu » — cette analogie fonctionne immédiatement auprès de gens qui connaissent la comptabilité. Et proposer aussitôt la version défendable, qui reste bonne : 290 tonnes évitées et 118 000 euros d'économies est un excellent message.",
        "Ne dites jamais « c'est du greenwashing » à un collègue. Le mot accuse, il ferme la discussion, et il est presque toujours inexact — l'écrasante majorité des allégations problématiques procèdent d'une méconnaissance, pas d'une intention de tromper.",
      ]},
   ]},

  {"titre": "Le rapport : que publier quand on n'y est pas obligé",
   "paras": [
     "Une entreprise non soumise à la CSRD n'a aucune obligation de publier un rapport de durabilité. La question n'est donc pas « que devons-nous publier ? » mais « qu'avons-nous intérêt à publier, et sous quelle forme ? ».",
     "<strong>Le format le plus utile est court.</strong> Huit à douze pages, ou un jeu de données structuré au format VSME. Un rapport de quarante pages illustré coûte plusieurs semaines de travail, n'est lu par personne intégralement, et multiplie la surface d'exposition : chaque affirmation qu'il contient est une allégation à étayer.",
     "<strong>Le contenu minimal utile</strong> tient en six éléments. Ce que fait l'entreprise et son périmètre. Les enjeux retenus comme matériels, et la mention que d'autres ont été écartés. Le bilan d'émissions avec sa méthode, son périmètre et son incertitude. Le plan d'action avec ses résultats de l'année, y compris ce qui n'a pas abouti. Les indicateurs sociaux principaux, dont ceux qui sont déjà publiés par obligation. Et les échéances de l'année suivante.",
     "<strong>Une règle de rédaction domine toutes les autres : chaque affirmation porte un chiffre, une date et un périmètre.</strong> « Nous avons réduit nos déchets » n'est pas publiable. « Les déchets non valorisés de nos deux entrepôts sont passés de 148 à 121 tonnes entre 2025 et 2026 » l'est. La différence n'est pas seulement juridique : la seconde phrase est la seule qui apporte une information.",
     "<strong>La vérification par un tiers</strong> n'est pas obligatoire hors CSRD, et elle mérite d'être envisagée dans un cas précis : lorsque le rapport est utilisé pour obtenir quelque chose — un référencement, un financement, un marché. Elle coûte, et elle transforme la nature du document. Hors de ce cas, un rapport non vérifié mais précis et traçable suffit, et il vaut mieux qu'un rapport vérifié dont le contenu est creux.",
     "<strong>Le sujet le plus délicat est celui de l'objectif annoncé et non tenu.</strong> Une entreprise qui a publié un objectif et constate qu'elle ne l'atteindra pas a trois conduites possibles, et une seule est tenable. Se taire expose : un écart connu et non mentionné dans une communication qui maintient l'objectif est précisément ce que le droit sanctionne. Retirer discrètement l'objectif se remarque et se retourne. Écrire l'écart est la seule voie : « nous avions annoncé moins 40 % en 2030 ; les actions identifiées à ce jour couvrent 22 %, et nous n'avons pas encore de solution pour l'écart. Voici ce que nous engageons pour le réduire. »",
     "Cette dernière formulation paraît coûteuse en image. Elle l'est bien moins que la découverte de l'écart par un tiers deux ans plus tard, et elle a un effet secondaire précieux : elle transforme un objectif décoratif en une demande d'arbitrage adressée à la direction générale.",
   ],
   "blocks": [
     {"type": "exemple", "titre": "deux pages de rapport, ligne à ligne",
      "paras": [
        "<em>« En 2026, nos émissions se sont établies à 3 760 tCO2e sur les scopes 1, 2 et les postes significatifs du scope 3, contre 4 050 tCO2e en 2025 recalculées à méthode constante. La réduction de 290 tonnes, soit 6,2 %, provient de quatre actions du plan détaillées ci-après. »</em> — chiffre, périmètre, date, base de comparaison recalculée, et l'origine de la variation.",
        "<em>« Notre bilan repose sur des données physiques pour les scopes 1 et 2 et pour deux familles d'achats, et sur des ratios monétaires pour le reste des achats. L'incertitude globale est estimée à plus ou moins 30 %, portée principalement par ce dernier poste. »</em> — la méthode et sa faiblesse, en deux phrases.",
        "<em>« Trois postes ne sont pas couverts : l'usage des produits vendus, la fin de vie, et une partie du transport amont. Nous les estimons entre 5 % et 15 % du total et prévoyons de les intégrer en 2027. »</em> — les manques, chiffrés et datés.",
        "<em>« Sur les cinq actions engagées, quatre ont abouti. La cinquième, le basculement de deux familles d'achats sur une gamme à empreinte réduite, a pris six mois de retard pour des raisons de référencement fournisseur. Elle est reportée au premier semestre 2027. »</em> — l'échec, nommé et expliqué.",
        "<em>« L'absentéisme des équipes de nuit de l'entrepôt est passé de 11,2 % à 7,4 % après réorganisation des rotations conduite avec le comité social et économique et le service de santé au travail. »</em> — un indicateur social, avec sa méthode et ses parties prenantes.",
        "Cinq paragraphes, aucune allégation générique, aucun adjectif valorisant, et un document qu'un acheteur ou un banquier lira avec profit. C'est ce qu'il faut viser, et c'est plus facile à écrire qu'un texte de communication.",
      ]},
     {"type": "pitfall", "titre": "le rapport qui devient un exercice annuel autonome",
      "paras": [
        "Une dérive fréquente au bout de deux ou trois ans : le rapport devient le livrable principal de la fonction RSE, il grossit, il mobilise deux mois de travail, et il finit par exister pour lui-même.",
        "Le symptôme est reconnaissable : on commence à mesurer des choses <em>pour le rapport</em>, plutôt que de rapporter ce qu'on mesure pour piloter. Le rapport se met alors à dicter l'agenda, et la fonction RSE redevient une fonction de production documentaire — exactement ce que le module 1 décrivait comme la RSE de conformité.",
        "La parade est simple à énoncer et exigeante à tenir : <strong>le rapport ne contient que ce qui sert déjà en interne.</strong> Aucun indicateur n'est créé pour être publié. Si un indicateur n'aide personne à décider dans l'entreprise, il n'a pas sa place dans le document, quelle que soit sa présence dans les référentiels.",
      ]},
   ]},

  {"titre": "Ce qui fait tenir une démarche au-delà d'une personne",
   "paras": [
     "Une démarche RSE portée par une seule personne s'arrête quand cette personne part, et cela arrive fréquemment. Quatre éléments la rendent indépendante de son porteur, et ils se construisent dès la première année.",
     "<strong>La gouvernance.</strong> Un point RSE inscrit à l'ordre du jour permanent d'une instance de direction, à une fréquence définie. Inscrit, pas sollicité à chaque fois : la différence est considérable, parce qu'un point qu'il faut demander finit par ne plus être demandé. Une revue annuelle du plan qui abandonne explicitement ce qui n'avance pas, plutôt que de le reconduire.",
     "<strong>La répartition des responsabilités.</strong> Chaque enjeu matériel a un responsable opérationnel, et la fonction RSE anime sans porter. C'est le point du module 3, et c'est aussi ce qui rend la démarche robuste : une démarche répartie sur cinq porteurs survit au départ de l'un d'eux.",
     "<strong>La documentation.</strong> Trois documents suffisent, et ils doivent être trouvables sans vous. La carte d'obligations datée du module 1. La note de périmètre du bilan, du module 2. Le tableau de suivi du plan, du module 3. Un successeur qui trouve ces trois documents reprend en une semaine ; sans eux, il recommence, et il recommencera différemment.",
     "<strong>L'intégration dans les processus existants.</strong> C'est le facteur le plus déterminant et le plus lent à obtenir. Un critère environnemental dans la grille de consultation achats, une ligne dans le dossier d'investissement, une rubrique dans la revue de direction : à partir du moment où un processus existant intègre le sujet, celui-ci ne dépend plus de la fonction RSE pour exister. C'est l'objectif de la troisième année, et c'est le seul indicateur fiable de la maturité d'une démarche.",
     "Une dernière chose, moins formelle et qui compte autant. <strong>Une démarche tient si les gens qui l'exécutent y trouvent un intérêt propre.</strong> Le directeur commercial qui a réduit les invendus a gagné 60 000 euros et un argument. Le responsable de l'entrepôt qui a réorganisé les rotations a fait baisser son absentéisme. Aucun des deux n'a agi par conviction environnementale, et cela n'a aucune importance : ils ont agi, les résultats sont réels, et ils recommenceront. Une démarche qui repose sur la conviction de ceux qui l'exécutent est fragile ; une démarche qui repose sur leur intérêt bien compris tient.",
   ],
   "blocks": [
     {"type": "h3", "titre": "Ce que ce parcours a construit",
      "paras": [
        "Quatre modules, et une progression qui est aussi l'ordre dans lequel il faut travailler.",
        "<strong>Module 1 :</strong> savoir qui demande quoi et sur quel fondement, plutôt que de chercher à quoi l'on est soumis. La carte d'obligations, le droit de refus au-delà du périmètre VSME, et le choix d'un référentiel à partir du demandeur.",
        "<strong>Module 2 :</strong> mesurer, parce que rien ne s'arbitre sans chiffres. Les trois scopes, le poids écrasant du scope 3, le périmètre écrit avant le calcul, et l'incertitude affichée plutôt que tue.",
        "<strong>Module 3 :</strong> prioriser et agir. La double matérialité pour sélectionner, y compris sur ce que le carbone ne mesure pas ; les quatre leviers ; le coût de la tonne évitée ; et cinq actions par an avec un porteur qui a dit oui.",
        "<strong>Module 4 :</strong> rendre compte sans s'exposer, dans un cadre juridique qui s'applique sans seuil de taille dès qu'on communique.",
        "Trois idées traversent l'ensemble. <em>Ce qui n'est pas chiffré n'est pas arbitré</em> — c'est pourquoi une formation RSE sérieuse ressemble à une formation de gestion. <em>La précision protège</em> — juridiquement, et aussi dans la conversation interne, où un chiffre daté résiste là qu'une conviction ne résiste pas. Et <em>une démarche tient par l'intérêt de ceux qui l'exécutent</em>, pas par l'adhésion à ses finalités.",
        "Ce qui reste à acquérir n'est pas dans ce parcours : c'est la connaissance fine de votre secteur, de ses gisements réels et de ses contraintes. Elle s'obtient en confrontant ces méthodes à une activité précise, et personne ne peut l'enseigner à l'avance.",
      ]},
     {"type": "pitfall", "titre": "attendre l'adhésion pour agir",
      "paras": [
        "Une erreur de séquence fréquente chez les personnes qui arrivent sur ces sujets par conviction : chercher d'abord à convaincre l'organisation, en supposant qu'une fois les esprits acquis, les actions suivront.",
        "L'expérience va dans l'autre sens. Les actions produisent l'adhésion bien plus sûrement que l'inverse. Une entreprise qui a économisé 118 000 euros en évitant 290 tonnes est beaucoup plus disposée à écouter la suite qu'une entreprise qui a suivi trois ateliers de sensibilisation.",
        "Cela ne disqualifie pas la sensibilisation, qui crée le langage commun rendant les conversations possibles. Cela dit seulement qu'elle ne doit pas être le préalable. Commencez par une action qui rapporte, mesurez-la, faites-la porter par quelqu'un d'autre que vous — et l'adhésion viendra comme conséquence, ce qui est sa place naturelle.",
      ]},
   ]},
 ],

 "etude_cas": {
   "titre": "Refuser trois formulations sur quatre sans bloquer le communiqué",
   "html": """
<p>Reprenons la commande : quatre formulations proposées par le marketing, un communiqué attendu pour la semaine suivante, et un directeur général satisfait de résultats qu'il souhaite valoriser. Voici la conduite tenue.</p>
<p><strong>Jour 1 — instruire avant de répondre.</strong> Ne répondez pas par un refus dans la journée. Reprenez chaque formulation avec les cinq questions de validation, et préparez pour chacune la version défendable. Une heure de travail, et vous arriverez à la conversation avec des propositions plutôt qu'avec des objections.</p>
<p><em>« Une entreprise engagée pour le climat. »</em> Allégation générique. Périmètre implicite : l'entreprise entière. Preuve disponible : un plan de cinq actions et 290 tonnes évitées, ce qui ne prouve pas un engagement global. Version défendable préparée : « Nous nous sommes engagés à réduire nos émissions de 18 % d'ici 2030. Plan et résultats publiés. »</p>
<p><em>« Nos livraisons sont neutres en carbone. »</em> Mention de neutralité reposant sur une compensation, et sans bilan, trajectoire et projets publiés au sens du décret de 2022. Doublement exposée. Version défendable : « Nous avons réduit de 12 % les émissions de nos livraisons depuis 2024 et nous finançons un projet de reforestation à hauteur de 80 tonnes. » Les deux éléments sont séparés, aucun n'annule l'autre.</p>
<p><em>« Moins 20 % d'émissions depuis 2024. »</em> Chiffre exact, message faux. Version défendable : « 290 tonnes de CO2 évitées en 2026 grâce à quatre actions, soit 6 % de nos émissions. »</p>
<p><em>« Une gamme éco-responsable. »</em> Allégation générique appliquée à un périmètre produit. Version défendable, sous réserve de vérification des fiches fournisseur : « Une gamme dont les émissions de fabrication sont inférieures de 30 % à notre gamme standard, sur le périmètre matières et transport. »</p>
<p><strong>Jour 2 — la conversation avec le marketing, seul à seul.</strong> Pas en réunion, et pas par courriel. L'enjeu n'est pas de gagner un arbitrage mais d'installer un réflexe durable, et cela ne se fait pas devant témoins.</p>
<p>Ordre de la conversation, et il compte. D'abord ce qui est possible : « on a un excellent message, 290 tonnes et 118 000 euros, et personne ne peut le contester ». Ensuite le cadre, sans dramatiser : « il y a un texte européen qui s'applique fin septembre, sans seuil de taille, et il vise exactement les formules génériques. Ce n'est pas propre à nous, tout le monde s'y met. » Enfin les quatre reformulations, présentées comme des versions plus fortes et non comme des versions atténuées.</p>
<p><em>La difficulté prévisible</em> est la troisième formulation. Le marketing dispose d'un chiffre validé dans le rapport et ne comprend pas qu'on le lui retire. L'analogie comptable a débloqué la discussion : « c'est comme annoncer une hausse du chiffre d'affaires alors qu'on a changé de méthode de reconnaissance du revenu — le commissaire aux comptes ne laisserait pas passer, et c'est exactement la même logique. »</p>
<p><em>Ce qui n'a pas été dit :</em> le mot greenwashing. Il aurait fermé la conversation et il aurait été inexact — personne n'a cherché à tromper.</p>
<p><strong>Jour 3 — la vérification de la quatrième formulation.</strong> La gamme à empreinte réduite est la seule des quatre dont l'allégation pourrait être maintenue sous une forme précise, à condition que la preuve existe. Vérification auprès du fournisseur : il dispose d'une analyse de cycle de vie sur ses deux références, mais elle porte sur le périmètre matières et fabrication, sans le transport.</p>
<p>Conséquence : l'allégation doit mentionner ce périmètre exact. « 30 % d'émissions de fabrication en moins » et non « 30 % d'émissions en moins ». Trois mots d'écart, et la différence entre une allégation étayée et une allégation dont le périmètre dépasse la preuve.</p>
<p>C'est le point de contrôle le plus productif des cinq questions, et celui qu'on saute le plus volontiers parce qu'il demande d'appeler quelqu'un.</p>
<p><strong>Jour 4 — le communiqué, et l'arbitrage du directeur général.</strong> Le communiqué reprend les versions défendables. Le directeur général trouve le résultat « moins percutant » que les propositions initiales, ce qui est exact.</p>
<p>L'argument qui a emporté la décision n'a pas été juridique. « Nos deux principaux clients ont eux-mêmes des objectifs et des équipes qui savent lire ces chiffres. Une formule générique nous ferait passer pour une entreprise qui découvre le sujet ; un chiffre précis avec son périmètre nous fait passer pour une entreprise qui le maîtrise. C'est ce que nous voulons, et c'est aussi ce qui est vrai. »</p>
<p><em>Le second argument, gardé pour la fin :</em> l'exposition. 10 % du chiffre d'affaires moyen annuel en sanction maximale, une administration qui contrôle plus d'un millier d'allégations par an avec un taux d'anomalie de l'ordre de 30 %. Présenté après l'argument commercial, il a confirmé la décision sans la fonder — l'ordre importe, un argument de risque présenté en premier fait passer la fonction RSE pour un service de contrôle.</p>
<p><strong>Semaine 2 — installer le processus, qui est le vrai livrable.</strong> Le communiqué n'est qu'un épisode ; ce qui compte est que le suivant ne pose plus le problème.</p>
<p>Trois mesures. Une règle écrite en deux lignes : toute communication comportant un terme environnemental passe par une validation avant diffusion. Une grille d'une page reprenant les cinq questions, remise au marketing pour qu'il puisse s'autovalider. Et un dossier de preuves partagé, une allégation par ligne, avec le document qui l'étaye, sa date et le support de diffusion.</p>
<p><em>Le dossier de preuves est la mesure la plus importante des trois</em>, et la moins spectaculaire. En cas de contrôle portant sur une communication d'il y a deux ans, il est la seule chose qui permette de répondre. Sans lui, l'entreprise se retrouve à devoir reconstituer a posteriori la justification d'une phrase que plus personne ne se rappelle avoir écrite.</p>
<p><strong>Résultat à six mois.</strong> Quatre demandes de validation ont été traitées, dont trois validées sans modification — le marketing avait appliqué la grille de lui-même. La quatrième, une mention « emballage écologique » sur une fiche produit, a été reformulée en « emballage contenant 70 % de matière recyclée ».</p>
<p>Un client a par ailleurs demandé les justificatifs de la mention sur la gamme à empreinte réduite, dans le cadre de son propre reporting. Le dossier de preuves a permis de répondre en vingt minutes.</p>
<p><strong>La leçon transposable.</strong> Le refus de trois formulations sur quatre s'est passé sans conflit parce que chaque refus est arrivé accompagné d'une version de remplacement au moins aussi bonne. Un veto sans proposition crée un adversaire ; une reformulation crée un processus.</p>
<p>La seconde leçon porte sur l'ordre des arguments. Le risque juridique est réel et il ne convainc personne en premier — il fait de la fonction RSE une contrainte. L'argument commercial, présenté d'abord, obtient la décision ; le risque, présenté ensuite, la verrouille. C'est vrai bien au-delà de ce sujet.</p>
"""},

 "checklist": {
   "titre": "Checklist — rendre compte et communiquer sans s'exposer",
   "items": [
     "Toute affirmation communiquée est retrouvable, au même périmètre, dans un document de reporting accessible",
     "La fonction RSE valide toute communication comportant un terme environnemental avant diffusion",
     "Le périmètre exact de chaque allégation est écrit avant sa validation",
     "Chaque allégation dispose d'un document de preuve daté et accessible",
     "Le périmètre de la preuve couvre celui de l'allégation, produit par produit et scope par scope",
     "Aucune allégation générique n'est employée : vert, durable, éco-responsable, engagé",
     "Aucune mention de neutralité carbone n'est faite sans bilan, trajectoire et projets publiés",
     "La contribution carbone est mentionnée à part, jamais comme une annulation d'émissions",
     "Toute comparaison précise à quoi elle se compare, sur quel indicateur et sur quel périmètre",
     "Aucun label affiché n'est auto-décerné ou non vérifié par un tiers indépendant",
     "Aucune obligation légale n'est présentée comme un engagement volontaire",
     "Un changement de méthode n'est jamais présenté comme une réduction d'émissions",
     "Un lecteur non spécialiste a relu les formulations pour vérifier ce qu'elles font comprendre",
     "Le dossier de preuves est archivé avec date de diffusion et support, allégation par ligne",
     "Le rapport publié contient au moins un objectif manqué expliqué et un poste non couvert chiffré",
     "L'incertitude du bilan figure dans le rapport",
     "Chaque affirmation du rapport porte un chiffre, une date et un périmètre",
     "Tout écart à un objectif annoncé est écrit plutôt que tu ou discrètement retiré",
     "Aucun indicateur n'est créé pour le rapport : le rapport ne contient que ce qui sert en interne",
     "Un point RSE est inscrit à l'ordre du jour permanent d'une instance de direction",
     "Les trois documents de référence sont trouvables sans le responsable RSE",
     "Au moins un processus existant intègre un critère environnemental",
   ]},

 "glossaire": [
   ("Allégation environnementale", "Toute affirmation sur les qualités environnementales d'un produit, d'un service ou d'une entreprise. Soumise au droit de la consommation sans seuil de taille."),
   ("Allégation générique", "Affirmation large et non spécifique — vert, durable, éco-responsable. Invérifiable par construction, et à ce titre interdite."),
   ("Pratique commerciale trompeuse", "Allégation susceptible d'induire en erreur le consommateur moyen. Sanction pouvant atteindre 10 % du chiffre d'affaires moyen annuel."),
   ("EmpCo", "Directive UE 2024/825, applicable au 27 septembre 2026 sans seuil de taille. Interdit notamment les allégations génériques, les labels non certifiés et la neutralité par compensation."),
   ("Décret neutralité carbone", "Décret de 2022 pris en application de la loi Climat et Résilience. Conditionne toute mention de neutralité à la publication d'un bilan, d'une trajectoire et des projets financés."),
   ("Green Claims", "Proposition de directive sur la vérification préalable des allégations, en suspens depuis l'annonce de retrait de juin 2025 sans formalisation. Ne pas parier sur sa disparition."),
   ("Preuve de même profondeur", "Principe selon lequel l'étendue de la preuve doit correspondre à celle de l'allégation. Fondement de tout le dispositif juridique."),
   ("Dossier de preuves", "Registre listant chaque allégation diffusée, le document qui l'étaye, sa date et son support. Seul moyen de répondre à un contrôle portant sur une communication ancienne."),
   ("Contribution carbone", "Financement d'une réduction hors du périmètre de l'entreprise. Se mentionne à part, jamais comme une annulation de ses propres émissions."),
   ("VSME", "Norme volontaire de reporting pour les PME. Format court adapté à une entreprise qui publie sans y être obligée."),
   ("Vérification par un tiers", "Contrôle externe du rapport. Non obligatoire hors CSRD ; pertinente quand le rapport sert à obtenir un référencement, un financement ou un marché."),
   ("Écart à l'objectif", "Différence entre un objectif annoncé et la somme des actions identifiées. À écrire : un écart connu et tu dans une communication qui maintient l'objectif est sanctionnable."),
 ],

 "retenir": [
   "Le reporting rend compte devant un lecteur qui évalue ; la communication valorise devant un lecteur qu'on veut convaincre. Les confondre produit la plupart des accidents.",
   "Tout ce qui est communiqué doit être retrouvable, au même périmètre, dans un document de reporting que vous accepteriez de montrer à un contradicteur.",
   "La fonction RSE valide toute communication environnementale avant diffusion : elle seule sait ce que les chiffres recouvrent.",
   "Le droit de la consommation s'applique sans aucun seuil de taille dès qu'une entreprise communique.",
   "La directive EmpCo s'applique au 27 septembre 2026 dans tous les États membres, sans seuil, et vise directement les allégations génériques.",
   "Une mention de neutralité carbone sans bilan, trajectoire et projets publiés est en infraction au décret de 2022.",
   "La preuve doit avoir la même profondeur que l'allégation : c'est le principe qui sous-tend tout le dispositif.",
   "Plus vous êtes précis, plus vous êtes en sécurité — et plus vous êtes convaincant : le droit pousse ici dans le même sens qu'une bonne communication.",
   "Un chiffre exact peut servir à dire quelque chose de faux : le droit s'intéresse à ce que l'affirmation fait comprendre, pas à son exactitude arithmétique.",
   "Un changement de méthode de calcul n'est jamais une réduction d'émissions.",
   "La contribution carbone se mentionne à part et ne s'appelle jamais une neutralité.",
   "Une comparaison sans point de comparaison explicite n'est pas défendable.",
   "Un label auto-décerné, ou décerné par une structure que l'on finance, tombe sous l'interdiction des labels non certifiés.",
   "Présenter le respect d'une obligation légale comme un engagement est explicitement interdit.",
   "Archivez un dossier de preuves : un contrôle peut porter sur une communication d'il y a deux ans.",
   "Un rapport entièrement positif décrédibilise : publiez au moins un objectif manqué et un poste non couvert chiffré.",
   "Chaque affirmation d'un rapport porte un chiffre, une date et un périmètre. Sans les trois, elle n'apporte aucune information.",
   "Un écart à un objectif annoncé s'écrit : se taire expose, retirer discrètement se remarque.",
   "Le rapport ne contient que ce qui sert déjà en interne : aucun indicateur n'est créé pour être publié.",
   "Ne dites jamais greenwashing à un collègue : le mot accuse, ferme la discussion, et est presque toujours inexact.",
   "Un refus sans version de remplacement crée un adversaire ; une reformulation crée un processus.",
   "Présentez l'argument commercial avant l'argument de risque : le second verrouille la décision, il ne l'obtient pas.",
   "Une démarche tient par l'intérêt bien compris de ceux qui l'exécutent, pas par leur adhésion à ses finalités.",
 ],

 "exercices": [
  {"titre": "Corriger six allégations", "niveau": "Débutant",
   "enonce": [
     "Pour chacune des six formulations suivantes, dites ce qui pose problème, quelle règle est en cause, et proposez une version défendable.",
     "1. « Notre entreprise est neutre en carbone depuis 2025. » — 2. « Un packaging respectueux de l'environnement. » — 3. « Nos produits sont 100 % naturels. » — 4. « Nous respectons scrupuleusement la réglementation environnementale. » — 5. « Label Entreprise Verte, décerné par notre fédération professionnelle. » — 6. « Notre nouvelle formule est 30 % plus écologique. »",
   ],
   "corrige": """
<p><strong>1. « Neutre en carbone depuis 2025. »</strong></p>
<p><em>Le problème :</em> la neutralité repose presque certainement sur l'achat de crédits de compensation. Deux textes s'appliquent. Le décret de 2022 exige, pour toute mention de ce type, la publication du bilan d'émissions, d'une trajectoire de réduction et du détail des projets financés — sanction jusqu'à 100 000 euros pour une personne morale. Et la directive EmpCo interdit, à compter du 27 septembre 2026, d'affirmer un effet neutre en raison d'une compensation, sans possibilité de régularisation par la publication.</p>
<p><em>La difficulté supplémentaire :</em> même une entreprise ayant publié les trois éléments exigés par le décret se trouve exposée au titre d'EmpCo si la neutralité repose sur la compensation. Autrement dit, la formulation devient à peu près inutilisable.</p>
<p><em>Version défendable :</em> « Nous avons réduit nos émissions de 14 % depuis 2024 et nous finançons des projets de séquestration à hauteur de 800 tonnes par an. » Les deux faits sont exacts, ils sont présentés séparément, et le second n'annule pas le premier.</p>
<p><strong>2. « Un packaging respectueux de l'environnement. »</strong></p>
<p><em>Le problème :</em> allégation générique. Aucun indicateur, aucun périmètre, aucun point de comparaison. Elle est invérifiable par construction — prouver qu'un emballage est « respectueux » supposerait une analyse complète sur tous les impacts, que personne ne détient.</p>
<p><em>Version défendable :</em> nommer l'attribut et le quantifier. « Emballage contenant 70 % de carton recyclé, recyclable dans la filière papier. » Deux faits vérifiables par une fiche technique.</p>
<p><em>Le point qui rend cet exemple instructif :</em> la version défendable est plus informative pour le client. L'allégation générique ne lui apprend rien, et il le sait — d'où sa faible efficacité commerciale, indépendamment de son illégalité.</p>
<p><strong>3. « 100 % naturels. »</strong></p>
<p><em>Le problème :</em> double. D'abord, l'affirmation est presque toujours inexacte au sens strict dès qu'il y a transformation. Ensuite et surtout, elle laisse entendre un bénéfice environnemental que le caractère naturel ne garantit pas : un ingrédient naturel peut avoir une empreinte supérieure à son équivalent de synthèse, en particulier s'il suppose des surfaces cultivées importantes ou un transport lointain.</p>
<p><em>Version défendable :</em> « Formule composée à 94 % d'ingrédients d'origine végétale », si c'est exact et documenté. Le fait est vérifiable et ne suggère plus de bénéfice environnemental non prouvé.</p>
<p><em>Nuance :</em> l'origine végétale d'un ingrédient est un fait, et il est légitime de le mentionner. Ce qui ne l'est pas est de le présenter comme un avantage environnemental sans preuve d'un moindre impact.</p>
<p><strong>4. « Nous respectons scrupuleusement la réglementation environnementale. »</strong></p>
<p><em>Le problème :</em> présenter comme un avantage ce qui est une obligation légale figure explicitement parmi les pratiques interdites par EmpCo. L'adverbe « scrupuleusement » aggrave le cas en suggérant un niveau d'exigence supérieur à ce que la loi impose, sans que cela soit prouvé.</p>
<p><em>Version défendable :</em> ne rien dire. Le respect de la loi n'est pas un argument commercial, et le mentionner suggère au contraire que ce n'est pas évident. Si l'entreprise va réellement au-delà, dire précisément en quoi : « nos rejets sont maintenus 40 % en dessous du seuil réglementaire, contrôlé annuellement par un organisme agréé. »</p>
<p><strong>5. « Label Entreprise Verte, décerné par notre fédération professionnelle. »</strong></p>
<p><em>Le problème :</em> EmpCo interdit d'afficher un label de durabilité qui ne repose pas sur un système de certification vérifié par un tiers indépendant. Un label attribué par une fédération dont l'entreprise est membre et cotisante ne remplit pas la condition d'indépendance, quelle que soit la sincérité de la démarche.</p>
<p><em>Version défendable :</em> deux options. Soit ne plus afficher le label. Soit décrire ce qu'il recouvre sans le présenter comme une certification : « membre de la démarche X de notre fédération professionnelle, qui engage sur trois critères : … ». La nature de la démarche est alors transparente pour le lecteur.</p>
<p><em>Cas fréquent et coûteux :</em> beaucoup d'entreprises affichent de bonne foi des logos sectoriels dont elles n'ont jamais vérifié le mode d'attribution. L'inventaire des logos figurant sur les supports est un contrôle rapide et souvent productif.</p>
<p><strong>6. « 30 % plus écologique. »</strong></p>
<p><em>Le problème :</em> trois manques cumulés. Plus écologique <em>que quoi</em> — la formule précédente, un concurrent, une moyenne de marché ? <em>Sur quel indicateur</em> — émissions, eau, toxicité, déchets ? <em>Sur quel périmètre</em> — fabrication seule, ou cycle de vie complet ? Une comparaison sans ces trois éléments est indéfendable, même si le chiffre repose sur une étude sérieuse.</p>
<p><em>Version défendable :</em> « Émissions de fabrication réduites de 30 % par rapport à notre formule précédente, sur le périmètre matières premières et production, selon une analyse de cycle de vie réalisée en 2026. »</p>
<p><em>Ce que cet exemple enseigne :</em> l'entreprise détient probablement une étude solide. Le problème n'est pas l'absence de preuve, c'est l'écart entre l'étendue de la preuve — un indicateur, un périmètre, une référence — et l'étendue de l'allégation, qui porte sur « l'écologie » en général. C'est le cas de figure le plus courant, et le plus facile à corriger : il suffit de dire ce que l'étude dit.</p>
<p><strong>Le fil conducteur des six réponses.</strong> Dans cinq cas sur six, la version défendable est plus informative que l'originale, et dans le sixième la bonne réponse est de se taire. Le cadre juridique ne demande pas de communiquer moins : il demande de dire ce qu'on sait au lieu de suggérer ce qu'on ne peut pas prouver.</p>
"""},

  {"titre": "Traiter un écart à un objectif public", "niveau": "Intermédiaire",
   "enonce": [
     "Votre entreprise a publié en 2024 un engagement de réduction de 40 % de ses émissions d'ici 2030, mentionné sur le site, dans le rapport annuel et dans deux réponses à appels d'offres. Nous sommes en 2026 : les émissions ont baissé de 5 %, et la somme des actions identifiées atteindrait 22 % en 2030. L'écart est de 18 points, sans solution identifiée.",
     "Que faites-vous ? Traitez la dimension juridique, la dimension interne et la dimension externe, et rédigez la formulation que vous proposeriez pour le prochain rapport.",
   ],
   "corrige": """
<p><strong>D'abord, mesurer le risque juridique, car il détermine l'urgence.</strong></p>
<p>L'engagement a été mentionné dans deux réponses à appels d'offres. C'est le point le plus sérieux du dossier, et il est souvent négligé au profit du site internet. Un engagement figurant dans une réponse à un marché peut avoir été un élément d'appréciation de l'offre ; le maintenir en connaissance d'un écart non comblé expose bien au-delà du droit de la consommation, et potentiellement sur le terrain contractuel.</p>
<p>Sur le site et le rapport, l'exposition relève des allégations environnementales : maintenir publiquement un objectif dont on sait qu'il n'est pas atteignable, sans mentionner l'écart, est susceptible d'induire en erreur.</p>
<p><em>Conclusion sur ce point :</em> le sujet ne peut pas attendre le prochain rapport. Il doit être porté à la direction générale dans le mois.</p>
<p><strong>Ensuite, vérifier que l'écart est réel avant de l'annoncer.</strong></p>
<p>Deux vérifications, une semaine de travail. La première : les 22 % sont-ils la somme de tout ce qui est identifiable, ou seulement de ce qui a été chiffré ? Un plan comporte presque toujours des pistes écartées faute de temps d'instruction, et les reprendre ajoute quelques points.</p>
<p>La seconde : l'objectif porte-t-il sur les émissions absolues ou sur l'intensité, et à quel périmètre ? Si l'entreprise a crû de 15 % depuis 2024, une baisse de 5 % en absolu correspond à une baisse d'intensité bien supérieure. Cela ne supprime pas l'écart — un engagement en absolu reste un engagement en absolu — mais cela change le récit et cela peut ouvrir une révision de la formulation de l'objectif, à condition de la dire.</p>
<p>Ces vérifications ne sont pas une manœuvre dilatoire : annoncer un écart de 18 points qui se révélerait être de 11 après instruction serait un dommage inutile.</p>
<p><strong>La dimension interne : transformer l'écart en demande d'arbitrage.</strong></p>
<p>C'est le cœur du traitement, et c'est aussi ce qui rend l'exercice utile plutôt que pénible.</p>
<p>Présentez au comité de direction trois éléments. L'écart, chiffré en points et en tonnes. Ce qu'il faudrait pour le combler : quelles actions, à quel coût de la tonne, avec quel investissement total. Et la question posée nettement : « finançons-nous cet écart, ou révisons-nous l'objectif ? »</p>
<p>Cette formulation a une propriété précieuse : elle rend la décision impossible à ne pas prendre. Un comité peut reporter une demande de budget ; il ne peut pas laisser sans réponse une question qui porte sur un engagement public déjà pris et sur un risque juridique identifié.</p>
<p><em>Anticipez la troisième réponse, qui viendra :</em> « on compense l'écart ». Elle doit être écartée immédiatement, et l'argument est double. La compensation ne réduit aucune émission propre, donc elle ne permet pas d'atteindre un objectif de réduction — sauf à avoir défini l'objectif comme un objectif net, ce qui doit alors être écrit. Et présenter une compensation comme l'atteinte d'un objectif de réduction est précisément ce que le droit sanctionne. Cette objection est prévisible : préparez-la.</p>
<p><strong>La dimension externe : la formulation.</strong></p>
<p>Voici ce que je proposerais pour le rapport, et le raisonnement derrière chaque phrase.</p>
<p><em>« En 2024, nous avons annoncé un objectif de réduction de 40 % de nos émissions d'ici 2030. Deux ans plus tard, nos émissions ont baissé de 5 % et les actions identifiées à ce jour représentent 22 % de réduction à l'horizon 2030. »</em> — Les trois chiffres, sans atténuation, dans l'ordre chronologique.</p>
<p><em>« L'écart de 18 points n'a pas aujourd'hui de solution identifiée. Il porte principalement sur nos achats, dont la décarbonation dépend en partie de nos fournisseurs et de l'évolution de leurs propres procédés. »</em> — L'écart est nommé, et sa cause est expliquée sans être invoquée comme excuse. La nuance tient au « en partie ».</p>
<p><em>« Nous engageons trois actions pour le réduire : un travail avec nos cinq premiers fournisseurs sur les données et les alternatives disponibles ; l'instruction de deux substitutions de matières identifiées mais non chiffrées à ce jour ; et une revue de notre politique d'investissement pour y intégrer un critère d'émissions. Nous rendrons compte de l'avancement de ces trois actions dans le rapport 2027. »</em> — Trois actions concrètes et une échéance de reddition de comptes.</p>
<p><em>« Nous maintenons à ce stade notre objectif de 40 %, en indiquant que son atteinte suppose des ruptures que nous n'avons pas encore identifiées. »</em> — La position est explicite, et le lecteur dispose de tout pour juger.</p>
<p><strong>Pourquoi maintenir plutôt que réviser à la baisse.</strong></p>
<p>Trois raisons. L'écart porte sur un horizon de quatre ans, pendant lesquels des solutions peuvent apparaître, en particulier chez les fournisseurs. Réviser à la baisse dès la première difficulté enseigne à l'organisation que les objectifs sont négociables, ce qui a un coût durable. Et une révision à la baisse est en pratique plus commentée à l'extérieur qu'un écart documenté.</p>
<p><em>La condition de cette position :</em> elle n'est tenable que parce que l'écart est écrit. Maintenir l'objectif en silence serait la pire des trois conduites ; le maintenir en publiant l'écart est défendable et honnête.</p>
<p><strong>Le cas particulier des appels d'offres.</strong> Pour les deux marchés concernés, vérifiez avec la direction juridique si l'engagement figure dans les pièces contractuelles ou seulement dans le mémoire technique. Dans le premier cas, une information du client s'impose, et il vaut infiniment mieux qu'elle vienne de vous. C'est désagréable et c'est nettement moins coûteux que la même information découverte par le client dans votre rapport.</p>
"""},

  {"titre": "Installer une gouvernance qui survit à votre départ", "niveau": "Avancé",
   "enonce": [
     "Vous avez conduit la démarche RSE d'une entreprise de 900 salariés pendant trois ans : bilan à jour, plan exécuté à 80 %, rapport annuel court, communication maîtrisée. Vous annoncez votre départ dans six mois. Il n'y a pas de successeur identifié et la direction envisage de « répartir le sujet entre les fonctions existantes ».",
     "Construisez votre plan de transmission. Traitez explicitement le scénario où aucun successeur n'est nommé, et dites ce que vous faites des sujets dont vous êtes le seul à connaître l'histoire.",
   ],
   "corrige": """
<p><strong>Le diagnostic à poser d'emblée : la répartition entre fonctions existantes n'est pas absurde, et elle est plus fragile qu'il n'y paraît.</strong></p>
<p>Elle n'est pas absurde parce que c'est l'état final souhaitable de toute démarche : quand le sujet est intégré aux processus, il n'a plus besoin d'une fonction dédiée. Beaucoup de démarches matures fonctionnent ainsi.</p>
<p>Elle est fragile parce que trois choses ne se répartissent pas naturellement : la vision d'ensemble qui permet de prioriser, la mémoire des arbitrages passés, et la veille sur un cadre réglementaire qui a changé trois fois en deux ans. Sans porteur, ces trois éléments disparaissent en dix-huit mois, et l'entreprise redécouvre le sujet à la prochaine demande client.</p>
<p>Votre travail des six mois consiste à rendre la répartition viable, pas à plaider contre elle. Plaider contre elle depuis la position de celui qui part serait à la fois inefficace et suspect.</p>
<p><strong>Mois 1 et 2 — l'inventaire de ce qui n'existe que dans votre tête.</strong></p>
<p>C'est l'exercice le plus utile et le plus inconfortable. Listez tout ce que vous savez et qui n'est écrit nulle part. La liste comporte typiquement quatre catégories.</p>
<p><em>Les arbitrages et leur raison.</em> Pourquoi les commandes sans région sont classées en export, pourquoi tel poste a été écarté du bilan, pourquoi tel enjeu a été jugé non matériel, pourquoi l'objectif est en absolu et non en intensité. Chacun de ces arbitrages sera un jour rediscuté, et sans sa raison écrite il sera repris différemment — rendant les séries de données incomparables.</p>
<p><em>Les relations.</em> Qui, chez le client principal, pilote réellement le sujet ; quel fournisseur dispose de données utiles ; à qui s'adresser à l'ADEME ou dans la fédération. Un carnet de six ou huit noms avec le contexte de la relation.</p>
<p><em>Les fragilités connues.</em> Le poste dont l'incertitude est plus élevée que ce que le rapport laisse entendre, la donnée qui vient d'un fichier maintenu par une seule personne, l'allégation ancienne dont le dossier de preuve est mince. Écrivez-les. C'est désagréable et c'est ce qui évitera à votre successeur de découvrir un problème en réunion.</p>
<p><em>Les échéances qui ne figurent nulle part.</em> La revalidation quadriennale du bilan, la demande client attendue dans dix-huit mois, l'échéance de transposition de la CSRD en mars 2027, la mise à jour du dossier de preuves.</p>
<p>Ce document fait cinq à huit pages. Il est le livrable principal de votre transmission, davantage que tous les autres.</p>
<p><strong>Mois 2 et 3 — la répartition, construite avec les fonctions concernées.</strong></p>
<p>Prenez la répartition au sérieux et proposez-en une, plutôt que d'attendre qu'elle vous soit imposée.</p>
<p><em>Le bilan d'émissions</em> va à la direction financière ou au contrôle de gestion. C'est un exercice de collecte et de consolidation périodique, sur des données majoritairement comptables : le rattachement est naturel, et il assure la continuité de la méthode.</p>
<p><em>Le plan d'action et son suivi</em> restent chez les porteurs, avec le tableau de suivi tenu par le contrôle de gestion dans le même mouvement que les autres plans d'action de l'entreprise.</p>
<p><em>Les critères achats</em> restent aux achats, où ils sont déjà intégrés à la grille de consultation.</p>
<p><em>La validation des allégations</em> va à la direction juridique, avec la grille des cinq questions et le dossier de preuves. C'est un travail de conformité, et c'est le rattachement le plus solide.</p>
<p><em>La veille réglementaire</em> est le point orphelin, et il faut le dire. Personne ne se l'attribue spontanément. Deux solutions : la confier à la direction juridique avec une revue semestrielle inscrite, ou la souscrire auprès de la fédération professionnelle ou d'un prestataire. La seconde option coûte peu et a l'avantage d'exister sans dépendre d'une charge de travail interne.</p>
<p><strong>Mois 3 et 4 — le point qui ne se répartit pas, et ce qu'on en fait.</strong></p>
<p>La priorisation transversale — arbitrer entre un enjeu social et un enjeu carbone, décider ce qui entre au plan de l'année — ne peut pas être répartie sans devenir une somme de décisions locales.</p>
<p>Proposez un dispositif léger : une revue annuelle de deux heures, en comité de direction, avec un ordre du jour fixe — avancement du plan, résultats du bilan, écart à l'objectif, arbitrage des actions de l'année suivante, revue des allégations diffusées. Inscrite au calendrier des instances, pas à convoquer.</p>
<p>Deux heures par an. C'est le minimum viable, et c'est ce qui remplace la fonction. Sans cette revue, la répartition produira cinq sujets suivis séparément et aucune priorisation.</p>
<p><strong>Mois 4 et 5 — la passation active, et non documentaire.</strong></p>
<p>Ne vous contentez pas de transmettre des documents : faites exécuter une fois chaque tâche par celui qui la reprend, pendant que vous êtes là.</p>
<p>Le contrôle de gestion produit la mise à jour du bilan avec vous en observateur. La direction juridique traite une demande de validation d'allégation avec la grille. Les achats mènent une consultation avec le critère environnemental. Chaque question posée pendant ces exercices révèle un trou dans votre documentation — notez-la et complétez.</p>
<p>C'est le seul test valable de la transmission. Un document que personne n'a essayé d'appliquer n'est pas un document transmis.</p>
<p><strong>Mois 6 — ce que vous laissez, et ce que vous dites.</strong></p>
<p>Quatre documents, pas davantage : la carte d'obligations datée, la note de périmètre du bilan, le tableau de suivi du plan, et le document de mémoire des arbitrages. Plus le dossier de preuves et le carnet de contacts.</p>
<p>Et une note d'une page à la direction générale, factuelle, disant ce qui tient et ce qui ne tient pas. « La collecte du bilan, le suivi du plan et la validation des allégations sont répartis et testés. Deux points restent fragiles : la veille réglementaire, qui n'a pas de titulaire clair, et la priorisation transversale, qui repose entièrement sur la revue annuelle. Si un seul point devait être renforcé, c'est le premier — la matière a changé trois fois en deux ans. »</p>
<p><em>Cette note est importante pour une raison qui vous dépasse :</em> dans dix-huit mois, si le sujet a décroché, elle sera relue. Elle aura dit ce qu'il fallait renforcer, ce qui vaut mieux qu'un procès en négligence adressé à ceux qui restent — et cela permettra de reprendre au bon endroit plutôt que de tout recommencer.</p>
<p><strong>Ce qu'il ne faut pas faire.</strong></p>
<p><em>Plaider pour un successeur à temps plein en menaçant d'un effondrement.</em> Vous seriez soupçonné de défendre votre poste, et l'argument perdrait toute force. Montrez la répartition, ses conditions de viabilité, et ses deux points faibles. C'est plus efficace et c'est exact.</p>
<p><em>Terminer un maximum de choses avant de partir.</em> La tentation est forte et elle est contre-productive : une action bouclée en urgence par vous est une action que personne n'a appris à mener. Sur les six derniers mois, faites moins et transmettez plus.</p>
<p><em>Emporter la mémoire des sujets sensibles.</em> Le poste dont l'incertitude est sous-estimée, l'allégation mal étayée : ce sont précisément les choses qu'on n'écrit pas et qui coûtent le plus cher. Les écrire est un acte de loyauté envers l'entreprise, et cela ne vous met pas en cause — vous avez fait ce que vous pouviez avec les moyens dont vous disposiez, et le dire est la meilleure preuve que vous saviez où vous en étiez.</p>
"""},
 ],

 "ressources": [
   "<strong>Le guide de la DGCCRF sur les allégations environnementales</strong> — la lecture la plus directement utile de ce module : il liste les pratiques contrôlées et les formulations sanctionnées, avec des exemples concrets tirés de contrôles réels.",
   "<strong>Le texte de la directive UE 2024/825 (EmpCo)</strong> — son annexe listant les pratiques interdites en toutes circonstances tient en deux pages et se lit directement. C'est la source de référence, applicable au 27 septembre 2026 sans seuil de taille.",
   "<strong>Le décret d'application de la loi Climat et Résilience sur la neutralité carbone</strong> — à consulter avant toute mention de ce type, y compris sur un support interne susceptible d'être diffusé.",
   "<strong>Les modules 1 à 3 de cette formation</strong> — une communication n'est défendable que si le bilan, le périmètre et le plan qui la fondent le sont. En cas de doute sur une allégation, la cause est presque toujours en amont : un périmètre non écrit ou un changement de méthode non tracé.",
 ],
}

QUIZ["rse-transition-ecologique/module-4"] = {
 "module_id": "formation-rse-transition-ecologique-module-4",
 "version": "2.0", "last_verified": "2026-09-04",
 "questions": [
  {"id":"q1","question":"À partir de quelle taille d'entreprise le droit des allégations environnementales s'applique-t-il ?",
   "choices":[{"key":"a","text":"À partir de 250 salariés, comme la plupart des obligations extra-financières"},
              {"key":"b","text":"Sans aucun seuil : il s'applique dès qu'une entreprise communique"},
              {"key":"c","text":"À partir des seuils CSRD, soit 1 000 salariés et 450 M€"}],
   "correct_answer":"b","feedback":"C'est l'inverse exact de l'idée reçue. Une PME non soumise à la CSRD est pleinement soumise au droit de la consommation dès qu'elle communique."},
  {"id":"q2","question":"Quel principe sous-tend l'ensemble du dispositif juridique sur les allégations ?",
   "choices":[{"key":"a","text":"Toute allégation doit être validée par un organisme certificateur avant diffusion"},
              {"key":"b","text":"Aucune allégation environnementale ne peut porter sur l'entreprise dans son ensemble"},
              {"key":"c","text":"La preuve doit avoir la même profondeur que l'allégation"}],
   "correct_answer":"c","feedback":"Corollaire libérateur : plus vous êtes précis, plus vous êtes en sécurité — et plus vous êtes convaincant. Le droit pousse ici dans le même sens qu'une bonne communication."},
  {"id":"q3","question":"Vos émissions affichent -20 %, dont l'essentiel vient d'un changement de méthode de calcul. Que communiquez-vous ?",
   "choices":[{"key":"a","text":"-20 %, le chiffre étant exact et figurant dans le rapport"},
              {"key":"b","text":"Rien, tant que la série n'est pas homogène"},
              {"key":"c","text":"La réduction réelle obtenue par les actions, en tonnes et en pourcentage à méthode constante"}],
   "correct_answer":"c","feedback":"Le droit s'intéresse à ce que l'affirmation fait comprendre, pas à son exactitude arithmétique. Un chiffre exact peut servir à dire quelque chose de faux."},
  {"id":"q4","question":"Un label attribué par votre fédération professionnelle peut-il être affiché ?",
   "choices":[{"key":"a","text":"Non s'il ne repose pas sur un système de certification vérifié par un tiers indépendant"},
              {"key":"b","text":"Oui, une fédération professionnelle constitue un tiers par rapport à l'entreprise"},
              {"key":"c","text":"Oui, à condition d'indiquer le nom de la fédération à côté du logo"}],
   "correct_answer":"a","feedback":"Une fédération dont l'entreprise est membre et cotisante ne remplit pas la condition d'indépendance. L'inventaire des logos affichés est un contrôle rapide et souvent productif."},
  {"id":"q5","question":"Vous avez publié un objectif de -40 % en 2030 et l'écart de 18 points n'a pas de solution. Que faites-vous ?",
   "choices":[{"key":"a","text":"Vous retirez discrètement l'objectif des supports en attendant d'y voir plus clair"},
              {"key":"b","text":"Vous écrivez l'écart, ses causes et les actions engagées pour le réduire"},
              {"key":"c","text":"Vous comblez l'écart par de la compensation carbone"}],
   "correct_answer":"b","feedback":"Se taire expose, retirer discrètement se remarque, et compenser ne réduit aucune émission propre. Écrire l'écart transforme aussi un objectif décoratif en demande d'arbitrage."},
  {"id":"q6","question":"Quel est le meilleur ordre pour obtenir qu'une formulation soit corrigée ?",
   "choices":[{"key":"a","text":"L'argument commercial d'abord, le risque juridique ensuite pour verrouiller"},
              {"key":"b","text":"L'argument de risque juridique d'abord, puis l'argument commercial"},
              {"key":"c","text":"Un refus argumenté par la réglementation, sans proposer d'alternative"}],
   "correct_answer":"a","feedback":"Un argument de risque présenté en premier fait de la fonction RSE un service de contrôle. Et un refus sans version de remplacement crée un adversaire au lieu d'un processus."},
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
