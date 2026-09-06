#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, json, os
sys.path.insert(0, "/tmp")
from fh_builder import build

M = {}
QUIZ = {}
FORM = "Bilan de Compétences &amp; Repositionnement Professionnel"

M["bilan-competences/module-2"] = {
 "formation": FORM,
 "titre": "Cibler : Explorer un Marché et Tester ses Hypothèses",
 "num": 2, "total": 3, "duree": "70 min", "niveau": "Intermédiaire",
 "module_id": "formation-bilan-competences-module-2",
 "situation": [
   "L'inventaire est fait et il a produit quatre hypothèses de cible. Depuis trois semaines, vous consultez les offres tous les matins.",
   "Le résultat est décourageant. Quarante candidatures envoyées, deux réponses négatives automatiques, trente-huit sans réponse, aucun entretien. Vous en tirez la conclusion qui s'impose : le marché est fermé, votre profil ne correspond à rien, et il faudra sans doute vous rabattre sur un poste équivalent au précédent.",
   "Cette conclusion est presque certainement fausse, et elle repose sur une erreur de méthode et non sur une réalité du marché. Vous avez candidaté avant d'avoir compris. Vous ne savez pas comment ces postes sont réellement pourvus, ni ce que recouvrent leurs intitulés, ni pourquoi votre profil est écarté — un désaccord de vocabulaire et une incompétence réelle produisent exactement le même silence.",
   "Ce module traite de l'étape que presque tout le monde saute : comprendre un marché avant de s'y présenter. Elle prend quatre à huit semaines, elle ne produit aucune candidature, et elle détermine l'essentiel de ce qui suit.",
 ],
 "objectifs": [
   "Transformer une hypothèse vague en cible testable et vérifiable",
   "Conduire un entretien exploratoire et en tirer une information exploitable",
   "Lire un marché réel : offres, tensions, canaux de recrutement, rémunération",
   "Traduire vos compétences dans le vocabulaire du secteur visé",
   "Mesurer l'écart entre votre profil et la cible, et choisir comment le combler",
   "Arbitrer entre plusieurs pistes sans y consacrer une année",
 ],
 "sections": [
  {"titre": "D'une hypothèse à une cible testable",
   "paras": [
     "Une hypothèse comme « la formation en entreprise » n'est pas une cible : c'est un domaine. On ne peut ni la tester, ni l'invalider, ni s'y présenter, parce qu'elle recouvre des métiers sans rapport entre eux — concevoir des parcours, animer des sessions, piloter un plan de développement des compétences, vendre de la formation ne demandent ni les mêmes compétences ni les mêmes profils.",
     "<strong>Une cible testable comporte quatre éléments.</strong> Un <em>type de poste</em>, nommé comme le nomment ceux qui recrutent. Un <em>type d'organisation</em> : grande entreprise, PME, organisme de formation, cabinet, secteur public. Une <em>zone géographique</em>. Et un <em>niveau</em>, exprimé en responsabilité et en rémunération.",
     "Ces quatre éléments transforment une intention en question à laquelle on peut répondre : « existe-t-il, dans un rayon d'une heure autour de chez moi, des postes de formateur interne en entreprise de plus de deux cents salariés, à un niveau de rémunération compatible avec mon seuil ? » Cette question a une réponse, et l'obtenir prend deux semaines.",
     "<strong>La difficulté du premier élément est réelle et sous-estimée.</strong> Vous ne connaissez pas les intitulés du secteur que vous visez. Chercher « formateur » sur un site d'offres ne remonte qu'une fraction des postes concernés, qui s'appellent aussi chargé de développement des compétences, responsable pédagogique, ingénieur de formation, animateur de dispositifs, ou consultant formation selon le contexte. Une part importante des candidatures qui n'aboutissent pas ne trouvent tout simplement pas les bonnes offres.",
     "<strong>La méthode pour trouver ces intitulés</strong> ne consiste pas à réfléchir mais à observer. Prenez trois personnes exerçant approximativement ce que vous visez et regardez leur parcours public : quels intitulés ont-elles portés, dans quel ordre, dans quels types d'organisations ? Faites-le sur dix personnes et vous obtiendrez la cartographie du vocabulaire de votre cible, ainsi qu'une information de valeur : les chemins réellement empruntés pour y arriver.",
     "Ce dernier point mérite l'attention. Si sur dix personnes exerçant le métier visé, sept viennent du même métier d'origine et aucune ne vient du vôtre, c'est une information sérieuse — non pas que ce soit impossible, mais que ce sera long et qu'il faudra une raison forte. Si en revanche les dix viennent d'horizons différents, le métier est ouvert aux profils atypiques, ce qui change entièrement la stratégie.",
   ],
   "blocks": [
     {"type": "method", "titre": "transformer une hypothèse en cible en une semaine",
      "steps": [
        "<strong>Trouvez dix personnes</strong> exerçant approximativement ce que vous visez, via un réseau professionnel en ligne, les sites d'entreprises, ou les intervenants d'événements du secteur. Dix suffisent et vingt n'apportent rien de plus.",
        "<strong>Relevez leurs intitulés de poste actuels et précédents</strong>, ainsi que le type et la taille d'organisation. Vous obtiendrez entre cinq et huit intitulés distincts pour ce que vous appeliez d'un seul mot.",
        "<strong>Relevez leur métier d'origine</strong> et le nombre d'étapes intermédiaires. C'est l'information la plus précieuse de l'exercice : elle vous dit si le passage est direct, s'il suppose une étape intermédiaire, ou s'il n'existe pas.",
        "<strong>Lancez une recherche d'offres sur chacun des intitulés relevés</strong>, sur votre zone géographique, et comptez. Vous saurez en une heure si le marché existe près de chez vous — question qu'il vaut mieux trancher avant six mois d'efforts.",
        "<strong>Lisez quinze offres intégralement</strong>, pas en diagonale, et relevez ce qui revient : les compétences exigées, les outils cités, les formulations employées, le niveau d'expérience demandé. C'est votre référentiel de traduction pour le module 3.",
        "<strong>Reformulez votre cible</strong> avec les quatre éléments et le vocabulaire relevé. Vous devez pouvoir l'énoncer en une phrase à quelqu'un du secteur sans qu'il ait besoin de vous faire préciser.",
      ]},
     {"type": "exemple", "titre": "une hypothèse devenue quatre cibles distinctes",
      "paras": [
        "<em>Hypothèse de départ :</em> « la formation en entreprise ».",
        "<em>Après observation de dix parcours</em>, quatre familles apparaissent, et elles n'ont presque rien en commun.",
        "<strong>Formateur ou animateur en organisme de formation</strong> — animation de sessions pour des publics externes, statut souvent indépendant ou en contrat court, rémunération à la journée, forte saisonnalité.",
        "<strong>Chargé de développement des compétences en entreprise</strong> — construction et pilotage du plan de développement, gestion des budgets et des dispositifs, relations avec les organismes. Métier majoritairement administratif et budgétaire, peu d'animation. Vient presque toujours des ressources humaines.",
        "<strong>Formateur interne ou référent métier</strong> — transmission d'un savoir-faire opérationnel aux équipes. Vient presque toujours du métier lui-même, ce qui est le cas ici. C'est la cible la plus accessible des quatre.",
        "<strong>Ingénieur pédagogique</strong> — conception de parcours et de contenus, forte composante numérique. Demande des compétences techniques absentes de l'inventaire, et il faudrait les acquérir.",
        "<em>Ce que cette décomposition change :</em> la troisième cible est directement accessible, la première l'est sous conditions de statut, la deuxième demande un passage par les ressources humaines, la quatrième une formation. Quatre stratégies différentes là où il y avait un mot unique — et trois semaines de candidatures avaient été envoyées sans cette distinction.",
      ]},
     {"type": "pitfall", "titre": "candidater avant d'avoir compris",
      "paras": [
        "Quarante candidatures sans réponse ne vous apprennent rien. C'est le point décisif : le silence est un signal sans contenu, et il peut recouvrir un profil hors sujet, un vocabulaire inadapté, un canal inapproprié, un niveau mal calibré, ou simplement une offre déjà pourvue en interne.",
        "Pire, ces candidatures ont un coût que l'on sous-estime : elles consomment votre énergie et votre confiance à un moment où les deux sont votre ressource principale, et elles vous font conclure à la fermeture d'un marché que vous n'avez pas encore observé.",
        "La règle à tenir, aussi contre-intuitive soit-elle : <strong>pas de candidature pendant les quatre premières semaines.</strong> Ce temps est consacré à comprendre. Les candidatures qui suivront seront moins nombreuses, mieux ciblées, et leur taux de réponse sera sans commune mesure.",
        "Si l'idée de ne pas candidater pendant un mois vous paraît insupportable — et c'est fréquent quand une échéance approche — fixez-vous un quota de deux candidatures par semaine sur les offres réellement adaptées, et consacrez tout le reste du temps à l'exploration. L'important est que l'exploration ne soit pas la variable d'ajustement.",
      ]},
   ]},

  {"titre": "L'entretien exploratoire : la méthode qui remplace un an de réflexion",
   "paras": [
     "L'entretien exploratoire est une conversation de trente minutes avec quelqu'un qui exerce le métier que vous visez, dans le but de comprendre ce métier — et non d'obtenir un emploi. Cette distinction est la condition de son efficacité, et elle doit être explicite dès la prise de contact.",
     "C'est l'outil au meilleur rendement de tout le repositionnement professionnel, et c'est celui que presque personne n'emploie. Quinze conversations coûtent une dizaine d'heures réparties sur deux mois, et elles produisent une information qu'aucune quantité de réflexion solitaire ne remplace.",
     "<strong>Pourquoi les gens acceptent.</strong> La crainte de déranger est le premier obstacle, et elle est largement infondée. Le taux d'acceptation d'une demande claire, courte et non intéressée se situe couramment entre 30 % et 50 %. Les raisons sont simples : parler de son métier est agréable, la demande est flatteuse, elle est courte, et beaucoup de gens ont eux-mêmes bénéficié d'une conversation de ce type.",
     "<strong>Ce qui fait échouer une demande</strong>, en revanche, est identifiable. Un message long. Un CV joint — il transforme immédiatement la demande en candidature déguisée, et la personne, n'ayant pas de poste à offrir, ne répond pas. Une demande floue du type « échanger sur mon projet ». Et l'absence de durée annoncée, qui laisse craindre un engagement indéterminé.",
     "<strong>Le message qui fonctionne tient en quatre lignes</strong> : qui vous êtes en une phrase, ce que vous cherchez à comprendre, la durée demandée, et une question précise qui montre que vous avez travaillé. Pas de CV, pas de pièce jointe, pas de demande d'emploi.",
     "<strong>Ce que vous cherchez</strong> n'est pas une opinion sur votre projet — les gens sont mal placés pour en juger et vous encourageront par politesse. Vous cherchez des faits : à quoi ressemble une semaine, qu'est-ce qui est difficile, comment recrute-t-on, d'où viennent les gens du métier, qu'est-ce qui fait échouer ceux qui arrivent.",
   ],
   "blocks": [
     {"type": "method", "titre": "conduire un entretien exploratoire en trente minutes",
      "paras": ["Les questions comptent moins que l'ordre. On commence par leur parcours, ce qui les met à l'aise et fournit l'essentiel de l'information, et on garde les questions vous concernant pour la fin."],
      "steps": [
        "<strong>Ouvrez sur leur parcours</strong> : « comment êtes-vous arrivé à ce poste ? ». Question généreuse, à laquelle tout le monde aime répondre, et qui vous donne un chemin réel plutôt qu'un chemin théorique.",
        "<strong>Demandez à quoi ressemble une semaine ordinaire</strong>, pas une semaine type. La nuance compte : on vous décrira ce qui prend réellement du temps, qui n'est presque jamais ce que la fiche de poste met en avant.",
        "<strong>Demandez ce qui est difficile</strong> dans ce métier, et ce qui surprend ceux qui y arrivent. C'est la question qui produit le plus d'information exploitable, et c'est la seule qui vous permettra de savoir si le métier vous conviendra réellement.",
        "<strong>Demandez comment on recrute</strong> dans ce métier : par offres, par réseau, par cooptation, par les organismes ? Vous saurez où porter votre effort, et cette réponse à elle seule justifie l'entretien.",
        "<strong>Demandez d'où viennent les gens</strong> et si des profils comme le vôtre existent dans le métier. Formulez-le comme une question ouverte et non comme une demande de validation.",
        "<strong>Terminez par la question qui prolonge</strong> : « qui d'autre me conseilleriez-vous de rencontrer ? ». Une conversation sur deux produit un ou deux noms, ce qui rend la série de quinze entretiens beaucoup plus facile après les cinq premiers.",
        "<strong>Envoyez un remerciement dans les vingt-quatre heures</strong>, en mentionnant un point précis qui vous a été utile. Trois lignes. C'est ce qui fait que la personne se souviendra de vous si un poste se présente — et c'est arrivé dans un cas sur cinq.",
      ]},
     {"type": "exemple", "titre": "le message de prise de contact, et sa version ratée",
      "paras": [
        "<em>Version ratée, envoyée par la plupart des gens :</em> « Bonjour, je suis actuellement en recherche d'opportunités après huit ans dans le secteur X. Mon profil pourrait correspondre à des postes dans votre domaine, et je serais ravi d'échanger avec vous sur mon projet. Vous trouverez mon CV en pièce jointe. Restant à votre disposition. » — Longueur excessive, demande floue, CV joint, et le mot « opportunités » qui annonce une candidature. Taux de réponse proche de zéro.",
        "<em>Version qui fonctionne :</em> « Bonjour, après huit ans à animer un réseau de partenaires, j'envisage de m'orienter vers la formation interne et j'essaie de comprendre ce métier avant de me positionner. Auriez-vous trente minutes à me consacrer, par téléphone ou en visioconférence ? Une question m'intrigue particulièrement : dans les parcours que j'ai regardés, les formateurs internes viennent presque tous du métier qu'ils forment, et j'aimerais comprendre si c'est une condition ou une coïncidence. Je ne cherche pas de poste chez vous, seulement à comprendre. »",
        "<em>Ce qui fait la différence :</em> la durée est annoncée, la demande est claire, la question précise montre un travail préalable, et la dernière phrase lève l'ambiguïté qui bloque la plupart des réponses.",
        "<em>Le détail qui compte le plus :</em> « je ne cherche pas de poste chez vous ». Elle paraît maladroite et elle est décisive — elle libère la personne de l'obligation d'avoir quelque chose à offrir, qui est la première raison de ne pas répondre.",
      ]},
     {"type": "pitfall", "titre": "transformer l'entretien en candidature",
      "paras": [
        "La tentation apparaît vers la vingtième minute, quand la conversation se passe bien : glisser vers « est-ce que vous auriez quelque chose ? ». C'est une erreur, pour trois raisons.",
        "Vous rompez le contrat annoncé, ce qui met la personne dans une position embarrassante. Vous obtenez une réponse polie et négative qui clôt le sujet définitivement. Et vous perdez l'accès à son réseau, qui valait bien davantage que le poste hypothétique.",
        "La conduite qui fonctionne est l'inverse : tenir l'engagement jusqu'au bout, remercier, et laisser la personne faire le lien elle-même. Dans une proportion notable de cas, c'est elle qui dira « d'ailleurs, si vous cherchez, je connais quelqu'un qui recrute » — et cette proposition-là vaut infiniment plus qu'une demande.",
        "Si vous voulez rester présent sans demander, une seule action suffit : trois mois plus tard, un message de trois lignes disant où vous en êtes et ce que la conversation a changé. C'est rare, cela se remarque, et cela réactive le contact sans rien solliciter.",
      ]},
   ]},

  {"titre": "Lire un marché réel",
   "paras": [
     "Parallèlement aux entretiens, un travail d'observation des offres apporte une information différente et complémentaire. Il ne s'agit pas de candidater mais de lire, avec quatre questions en tête.",
     "<strong>Le volume.</strong> Combien d'offres correspondant à vos intitulés paraissent chaque mois dans votre zone ? Comptez sur quatre semaines. Un marché à trois offres par mois et un marché à quarante n'appellent pas la même stratégie : le premier suppose de se rendre visible et d'attendre, le second permet de candidater et d'itérer.",
     "<strong>Les exigences récurrentes.</strong> Lisez quinze offres intégralement et relevez ce qui revient dans plus de la moitié : un diplôme, un outil, une durée d'expérience, une compétence précise. Ce qui revient est réel ; ce qui apparaît une fois est une préférence locale.",
     "Une nuance importante : <strong>une exigence n'est pas un critère éliminatoire</strong>. Les offres sont rédigées en décrivant le candidat idéal, et les recrutements se font sur des candidats réels. Une expérience demandée de cinq ans écarte rarement un candidat de trois ans qui coche tout le reste. En revanche, un diplôme réglementairement requis ou une certification obligatoire pour exercer sont, eux, éliminatoires — la distinction se vérifie en entretien exploratoire.",
     "<strong>Le canal.</strong> Les offres publiées ne représentent qu'une part du marché, variable selon les métiers : élevée pour les fonctions standardisées, faible pour les postes d'expertise ou dans les petites structures, où le recrutement se fait par recommandation. C'est une des questions à poser en entretien exploratoire, et la réponse détermine où porter l'effort. Concentrer 90 % de son énergie sur les annonces dans un métier qui recrute à 70 % par réseau est une erreur d'allocation, pas un manque de chance.",
     "<strong>La rémunération.</strong> Souvent absente des offres. Les sources utiles sont les entretiens exploratoires — la question se pose sans difficulté sous la forme « à quel niveau de rémunération se situe ce type de poste ? », qui ne demande à personne son salaire — les grilles de conventions collectives, et les études sectorielles publiées par les cabinets de recrutement. Connaître la fourchette avant d'être en situation de négocier évite deux erreurs symétriques : se sous-évaluer, et se disqualifier par une demande hors marché.",
   ],
   "blocks": [
     {"type": "h3", "titre": "Les signaux à lire dans une offre",
      "paras": [
        "Une offre contient plus d'information que sa liste d'exigences, à condition de la lire comme un document et non comme une liste de cases à cocher.",
        "<strong>La longueur et la précision des missions</strong> indiquent si le poste est défini. Une offre vague sur les missions et précise sur le profil décrit souvent un besoin mal cerné, et un recrutement qui traînera.",
        "<strong>La date de publication et les republications.</strong> Une offre republiée trois fois en quatre mois signale un poste difficile à pourvoir — ce qui est une bonne nouvelle pour un profil atypique. C'est même le meilleur endroit où se présenter quand on ne coche pas toutes les cases.",
        "<strong>Le rattachement hiérarchique</strong>, quand il est mentionné, dit le niveau réel du poste bien mieux que son intitulé. Un même intitulé rattaché à un directeur ou à un chef d'équipe décrit deux postes différents.",
        "<strong>Ce qui est répété</strong> dans l'offre est ce qui compte vraiment pour l'employeur. Si l'autonomie revient trois fois, c'est que le prédécesseur en manquait ou que le poste est isolé. C'est le point à traiter dans votre candidature.",
        "<strong>Le ton et le vocabulaire</strong> vous renseignent sur la culture de l'organisation, et vous donnent le registre à adopter dans votre réponse.",
      ]},
     {"type": "exemple", "titre": "quatre semaines d'observation, ce qu'elles ont produit",
      "paras": [
        "<em>Cible retenue :</em> formateur interne ou référent métier, entreprises de plus de deux cents salariés, rayon d'une heure.",
        "<em>Volume :</em> onze offres en quatre semaines sur six intitulés différents. Deux seulement seraient apparues sur une recherche « formateur ». Le marché existe et il était largement invisible avec le mauvais vocabulaire — ce qui explique une bonne part des trois semaines de candidatures infructueuses.",
        "<em>Exigences récurrentes :</em> expérience opérationnelle dans le métier formé, citée dans dix offres sur onze — c'est l'exigence réelle, et c'est justement l'atout du profil. Expérience de formation ou d'animation, citée dans sept. Certification de formateur, citée dans deux seulement, donc non déterminante.",
        "<em>Canal :</em> les entretiens exploratoires ont convergé — la majorité des formateurs internes ont été recrutés en interne ou par recommandation, et les postes ouverts à l'externe sont ceux d'entreprises en croissance ou en réorganisation. Conséquence directe sur la stratégie : la visibilité et le réseau comptent davantage que le volume de candidatures.",
        "<em>Rémunération :</em> fourchette obtenue par trois entretiens, cohérente avec le seuil fixé au module 1, avec une réserve sur les organismes de formation externes, nettement en dessous.",
        "<em>Décision qui en découle :</em> la cible est confirmée, l'effort se déplace des candidatures vers la visibilité et le réseau, et la piste « organisme de formation externe » est écartée pour raison de rémunération — après vérification, non par préjugé.",
      ]},
   ]},

  {"titre": "Mesurer l'écart et choisir comment le combler",
   "paras": [
     "À l'issue de l'exploration, vous savez ce que la cible demande et ce que vous avez. L'écart entre les deux se traite, et le choix du traitement détermine des mois de votre calendrier.",
     "<strong>Première chose à faire : distinguer trois types d'écart</strong>, parce qu'ils appellent des réponses opposées.",
     "<strong>L'écart de vocabulaire.</strong> Vous possédez la compétence, vous ne la nommez pas comme le secteur la nomme. C'est l'écart le plus fréquent, le moins coûteux à combler, et celui qu'on prend le plus souvent pour un écart de compétence. Il se traite par la traduction, en quelques heures, à partir des quinze offres lues. « Animation d'un réseau de partenaires » devient « développement des compétences et accompagnement d'un réseau de distributeurs indépendants ».",
     "<strong>L'écart de preuve.</strong> Vous possédez la compétence, vous ne pouvez pas la démontrer dans le contexte visé. Une personne qui a formé des équipes partenaires sait former, et rien dans son parcours ne l'atteste dans un contexte d'entreprise. Cet écart se comble par une <em>démonstration</em> : une mission courte, un bénévolat ciblé, une intervention ponctuelle, une certification légère. Quelques semaines à quelques mois.",
     "<strong>L'écart de compétence réel.</strong> Vous ne savez pas faire. Il se comble par une formation, et c'est le seul cas où une formation est la bonne réponse. Comptez de plusieurs mois à plus d'un an.",
     "<strong>La règle de séquence :</strong> traitez le vocabulaire d'abord, la preuve ensuite, la compétence en dernier — et seulement si l'écart persiste. Beaucoup de gens engagent une formation longue pour combler ce qui était un problème de vocabulaire, et le découvrent après. C'est la décision la plus coûteuse du repositionnement professionnel, et elle est presque toujours prise trop tôt.",
     "<strong>Un test simple permet de trancher :</strong> présentez votre profil traduit à deux personnes du secteur rencontrées en entretien exploratoire, et demandez si le profil est recevable en l'état. Elles vous diront ce qui manque réellement. Cette conversation de dix minutes vaut mieux qu'une décision de formation à plusieurs milliers d'euros.",
   ],
   "blocks": [
     {"type": "method", "titre": "combler un écart de preuve sans attendre",
      "paras": ["L'écart de preuve est le plus fréquent après celui de vocabulaire, et c'est celui qui se traite le plus vite si l'on accepte de commencer petit."],
      "steps": [
        "<strong>Nommez précisément ce qui manque</strong> : non pas « de l'expérience en formation », mais « une intervention de formation dans un contexte d'entreprise, avec un témoignage vérifiable ». Un manque précis se comble ; un manque vague ne se comble pas.",
        "<strong>Cherchez la plus petite démonstration possible.</strong> Une demi-journée d'intervention vaut mieux que rien, et beaucoup mieux qu'un projet de six mois jamais engagé.",
        "<strong>Regardez du côté du bénévolat structuré</strong> : associations, structures d'accompagnement, réseaux professionnels. Beaucoup cherchent des intervenants et acceptent des profils sans référence dans le domaine, ce qui est exactement votre situation.",
        "<strong>Regardez du côté de votre employeur actuel</strong> si vous êtes encore en poste. Proposer d'animer une session interne est souvent accepté, coûte peu à l'entreprise, et fournit une démonstration dans un contexte professionnel réel — la plus recevable de toutes.",
        "<strong>Obtenez une trace.</strong> Un témoignage écrit court, une recommandation en ligne, un support que vous avez conçu. Une démonstration sans trace ne se transmet pas dans une candidature.",
        "<strong>Fixez-vous une échéance de deux mois.</strong> Au-delà, l'écart de preuve devient un prétexte à ne pas se présenter, ce qui est son principal danger.",
      ]},
     {"type": "pitfall", "titre": "la formation comme moyen de repousser la décision",
      "paras": [
        "Engager une formation longue est la façon la plus confortable de repousser le moment où l'on se présente sur un marché. Elle occupe, elle rassure, elle est socialement bien vue, et elle donne le sentiment d'avancer.",
        "Le signal qui doit alerter : si vous ne pouvez pas nommer précisément le poste que la formation vous permettra d'obtenir et l'écart exact qu'elle comble, elle ne comble rien. « Cela m'ouvrira des portes » n'est pas un objectif, c'est une espérance.",
        "Trois questions à se poser avant tout engagement. <em>Quel écart précis cette formation comble-t-elle, et ai-je vérifié auprès de deux professionnels du secteur que c'est bien lui qui bloque ?</em> <em>Combien d'offres, parmi celles que j'ai lues, exigent réellement cette qualification ?</em> <em>Existe-t-il une version plus courte qui comblerait le même écart ?</em>",
        "Il arrive que les réponses confirment la formation, et elle est alors le bon investissement. Il arrive bien plus souvent qu'elles fassent apparaître que l'écart était ailleurs — et l'on a économisé six mois et plusieurs milliers d'euros.",
      ]},
   ]},

  {"titre": "Arbitrer entre plusieurs pistes sans y passer un an",
   "paras": [
     "À l'issue de l'exploration, vous avez de l'information sur trois ou quatre cibles. Il faut choisir, et le choix se fait mal si l'on attend d'être certain — ce qui n'arrive jamais.",
     "<strong>Quatre critères suffisent</strong>, et ils se pondèrent différemment selon votre situation. <em>L'accessibilité :</em> le marché existe-t-il près de chez vous, et un profil comme le vôtre y est-il recevable ? <em>L'écart :</em> quel type d'écart, et combien de temps pour le combler ? <em>L'adéquation :</em> le métier respecte-t-il vos critères rédhibitoires du module 1 ? <em>L'attrait :</em> après avoir compris ce qu'est réellement ce métier, avez-vous envie de l'exercer ?",
     "Le quatrième critère change souvent après l'exploration, et c'est le principal bénéfice des entretiens exploratoires. Un métier fantasmé devient un métier connu, avec ses contraintes réelles — et il arrive qu'il perde son attrait, ce qui est un résultat utile et non un échec.",
     "<strong>La règle d'arbitrage qui fonctionne :</strong> ne choisissez pas une piste, hiérarchisez-en deux. Une piste principale qui reçoit 70 % de votre effort, et une piste secondaire qui en reçoit 30 % et que vous maintenez active. Une seule piste vous rend dépendant d'un marché ; trois pistes menées en parallèle diluent l'effort au point qu'aucune n'aboutit.",
     "<strong>Fixez une échéance de réexamen</strong> — trois mois est un bon ordre de grandeur — avec un critère écrit à l'avance. « Si dans trois mois je n'ai obtenu aucun entretien sur la piste principale malgré une candidature adaptée par semaine et cinq contacts réseau, je bascule sur la seconde. » Ce critère écrit à froid vous évitera deux erreurs opposées : abandonner trop tôt sous l'effet d'un découragement passager, et persister trop longtemps par entêtement.",
     "<strong>Une dernière chose, sur le rythme.</strong> Une recherche de repositionnement se mène comme un travail : des plages définies, un rythme régulier, et des moments où l'on n'en fait pas. Les périodes de recherche longues sont éprouvantes, et l'usure est le principal facteur d'échec — bien avant la compétence ou le marché. Deux protections concrètes : maintenir des activités et des relations sans rapport avec la recherche, et considérer les entretiens exploratoires comme des résultats en soi, parce qu'ils en sont. Si la situation devient pesante, un accompagnement — conseil en évolution professionnelle, réseau de personnes en démarche similaire, ou soutien professionnel si la difficulté déborde le cadre du travail — est utile et se cherche tôt plutôt que tard.",
   ],
   "blocks": [
     {"type": "exemple", "titre": "l'arbitrage, quatre pistes ramenées à deux",
      "paras": [
        "<em>Formateur interne ou référent métier.</em> Accessibilité : marché réel mais restreint, onze offres en quatre semaines, recrutement majoritairement par réseau. Écart : de preuve, comblable en deux mois. Adéquation : conforme aux critères. Attrait : confirmé et renforcé après cinq entretiens exploratoires. <strong>Piste principale.</strong>",
        "<em>Analyse et pilotage de l'activité commerciale.</em> Accessibilité : marché plus large, recrutement majoritairement par annonces. Écart : de vocabulaire principalement, et un écart technique sur un outil décisionnel, comblable par une formation courte. Adéquation : conforme. Attrait : moyen — les entretiens ont révélé une part de reporting récurrent qui figurait dans les journées « qui ne passent pas vite ». <strong>Piste secondaire</strong>, précisément parce que son marché est plus large et qu'elle sécurise l'ensemble.",
        "<em>Support et expertise avant-vente.</em> Écartée. Les entretiens ont montré que le métier comporte, dans la majorité des structures, des objectifs commerciaux indirects — critère rédhibitoire du module 1. Information que seule la conversation avec des praticiens pouvait donner.",
        "<em>Coordination de projet ou d'opérations.</em> Écartée à ce stade. Les parcours observés montrent un passage direct rare depuis un profil commercial, et l'écart de preuve serait long à combler. Conservée comme piste de moyen terme, à réexaminer si la première aboutit et permet un repositionnement ultérieur.",
        "<em>Ce que l'arbitrage a coûté :</em> six semaines, quinze conversations, aucune candidature envoyée. Et il a écarté deux pistes sur quatre pour des raisons factuelles — dont l'une aurait été poursuivie pendant des mois sur une image erronée du métier.",
      ]},
     {"type": "pitfall", "titre": "attendre la certitude",
      "paras": [
        "Aucune quantité d'exploration ne produira la certitude d'avoir choisi la bonne voie. Passé une quinzaine de conversations, les informations nouvelles se raréfient nettement, et prolonger devient une façon de ne pas décider.",
        "Le seuil pratique : quand trois entretiens consécutifs ne vous apprennent rien que vous ne sachiez déjà, l'exploration a produit ce qu'elle pouvait produire. Arrêtez et décidez.",
        "Il faut par ailleurs se rappeler que la décision n'est pas définitive. Un repositionnement n'est pas un engagement à vie : c'est un pas suivant, qui ouvrira lui-même d'autres possibilités. La quatrième piste écartée plus haut redeviendra peut-être accessible dans trois ans depuis le nouveau poste — et elle le sera dans de meilleures conditions qu'aujourd'hui.",
        "Cette perspective allège considérablement la décision présente, et elle est exacte : la plupart des parcours se construisent par étapes successives dont aucune n'était visible depuis le point de départ.",
      ]},
   ]},
 ],

 "etude_cas": {
   "titre": "Six semaines d'exploration après quarante candidatures sans réponse",
   "html": """
<p>Reprenons la situation : quatre hypothèses, quarante candidatures envoyées, aucun entretien, et la conclusion que le marché est fermé. Voici ce qu'a produit un arrêt complet des candidatures pendant six semaines.</p>
<p><strong>Semaine 1 — la cartographie du vocabulaire, et la première explication.</strong> Dix parcours observés sur chacune des deux hypothèses les plus prometteuses. Résultat immédiat : six intitulés différents pour ce qui était appelé « formation en entreprise », dont un seul avait été utilisé dans les recherches d'offres.</p>
<p>Recherche relancée sur les six intitulés : vingt-trois offres en quatre semaines glissantes, contre quatre trouvées jusque-là. <strong>Le marché n'était pas fermé, il était invisible.</strong> Cette découverte, obtenue en trois heures, explique à elle seule une bonne partie des trois semaines précédentes.</p>
<p>Second enseignement de la cartographie : sur les dix formateurs internes observés, huit venaient du métier opérationnel qu'ils formaient, et aucun n'avait de diplôme de formateur. Le profil visé n'était donc pas un handicap — c'était le profil standard.</p>
<p><strong>Semaine 2 — les premiers contacts, et le taux de réponse.</strong> Douze messages envoyés selon le format en quatre lignes. Cinq réponses positives, une négative, six sans réponse. Taux d'acceptation de 42 %, conforme à ce qu'on observe habituellement, et très au-dessus de ce qui était anticipé.</p>
<p><em>Observation faite après coup :</em> les trois premiers messages, envoyés avant d'avoir bien intégré le format, étaient plus longs et mentionnaient une recherche d'emploi. Aucun n'a reçu de réponse. Les neuf suivants, conformes au format, en ont produit cinq. Le format n'est pas un détail de style.</p>
<p><strong>Semaines 2 à 5 — quinze entretiens exploratoires.</strong> Cinq issus des premiers contacts, dix obtenus par la question de fin — « qui d'autre me conseilleriez-vous de rencontrer ? ». À partir du sixième entretien, il n'a plus été nécessaire de solliciter des inconnus.</p>
<p><em>Ce que les entretiens ont produit, par ordre d'importance.</em></p>
<p><strong>1. Le canal réel de recrutement.</strong> Sur quinze personnes, onze avaient obtenu leur poste en interne ou par recommandation. Les postes ouverts à l'externe correspondaient à des entreprises en croissance ou en réorganisation. Cette information a réorienté toute la stratégie : l'effort devait porter sur la visibilité et le réseau, non sur le volume de candidatures — c'est-à-dire exactement l'inverse de ce qui avait été fait pendant trois semaines.</p>
<p><strong>2. L'exigence qui compte réellement.</strong> Interrogés sur ce qui fait échouer ceux qui arrivent dans le métier, sept ont donné la même réponse : la difficulté à faire adhérer un public qui n'a pas demandé la formation et qui la subit. Or c'est précisément ce que la personne faisait depuis huit ans avec des partenaires indépendants, non subordonnés et libres de ne pas venir. <strong>Ce qui semblait un handicap — ne pas avoir de titre de formateur — était secondaire, et la compétence rare était déjà là.</strong></p>
<p><strong>3. L'invalidation d'une piste.</strong> Trois entretiens menés sur l'hypothèse « support et expertise avant-vente » ont fait apparaître que le métier comporte, dans la plupart des structures, des objectifs commerciaux indirects. C'était un critère rédhibitoire. La piste a été écartée en trois conversations, après avoir été considérée comme la plus prometteuse au départ.</p>
<p><strong>4. Deux informations non sollicitées.</strong> Une personne a signalé un poste à venir dans son entreprise, non encore publié. Une autre a proposé une intervention d'une demi-journée dans une association professionnelle, qui a comblé l'écart de preuve. Aucune des deux n'avait été demandée, et les deux sont venues d'entretiens où la règle du « je ne cherche pas de poste chez vous » avait été tenue jusqu'au bout.</p>
<p><strong>Semaine 4, en parallèle — la lecture des offres.</strong> Quinze offres lues intégralement. Relevé du vocabulaire : « accompagnement à la montée en compétences », « transfert de savoir-faire », « animation de dispositifs de formation », « conception de supports pédagogiques ». Aucun de ces termes ne figurait dans le CV, et tous décrivaient des choses que la personne avait faites.</p>
<p><em>Le diagnostic de l'écart, à ce stade :</em> l'écart de vocabulaire était considérable, l'écart de preuve était réel mais étroit — aucune trace d'intervention en contexte d'entreprise — et l'écart de compétence était nul. Aucune formation n'était nécessaire.</p>
<p><strong>Semaine 5 — la vérification du diagnostic.</strong> Le profil traduit a été présenté à deux personnes rencontrées en entretien, avec une question directe : « ce profil est-il recevable en l'état pour un poste de formateur interne ? ».</p>
<p>Les deux réponses ont convergé : oui, à condition de pouvoir montrer une intervention de formation en contexte professionnel, même courte. La demi-journée proposée à la semaine 3 y répondait exactement, et elle a été programmée.</p>
<p><em>Cette vérification en dix minutes a évité une décision qui était sérieusement envisagée :</em> l'inscription à une certification de formateur professionnel, huit mois et un montant significatif, pour combler un écart qui n'existait pas.</p>
<p><strong>Semaine 6 — l'arbitrage.</strong> Deux pistes retenues sur quatre, hiérarchisées à 70 % et 30 %, avec un critère de réexamen écrit à trois mois.</p>
<p><strong>Résultat de la période.</strong> Six semaines, quinze conversations, zéro candidature envoyée. À l'arrivée : un marché passé de quatre à vingt-trois offres visibles, un canal de recrutement identifié qui a réorienté toute la stratégie, deux pistes invalidées sur des faits, une formation de huit mois évitée, un écart de preuve en cours de comblement, et deux contacts qui ont produit des propositions non sollicitées.</p>
<p><strong>La leçon transposable.</strong> Les quarante candidatures n'avaient rien appris parce que le silence n'apprend rien. Quinze conversations ont produit plus d'information exploitable en six semaines que trois mois de candidatures n'en auraient produit — et elles ont coûté moins d'efforts.</p>
<p>La seconde leçon est plus dérangeante : trois des quatre difficultés rencontrées étaient des problèmes de méthode et non de profil. Le mauvais vocabulaire rendait le marché invisible, le mauvais canal rendait les candidatures inefficaces, et un écart imaginaire allait déclencher une formation inutile. Le profil, lui, était adapté depuis le début.</p>
"""},

 "checklist": {
   "titre": "Checklist — explorer et cibler",
   "items": [
     "Aucune candidature n'a été envoyée pendant les quatre premières semaines d'exploration",
     "Chaque cible comporte ses quatre éléments : type de poste, type d'organisation, zone, niveau",
     "Dix parcours de personnes exerçant le métier visé ont été observés",
     "Les intitulés de poste réellement employés par le secteur ont été relevés, pas devinés",
     "Les recherches d'offres ont été relancées sur chacun de ces intitulés",
     "Le métier d'origine des personnes en poste a été relevé, et le nombre d'étapes intermédiaires",
     "Quinze offres au moins ont été lues intégralement, et leur vocabulaire relevé",
     "Le volume d'offres mensuel de la zone géographique est connu",
     "Les exigences apparaissant dans plus de la moitié des offres sont distinguées des mentions isolées",
     "Les exigences réglementaires ou éliminatoires sont distinguées des exigences souhaitées",
     "Le canal de recrutement dominant du métier a été identifié en entretien exploratoire",
     "La fourchette de rémunération a été obtenue avant toute situation de négociation",
     "Au moins dix entretiens exploratoires ont été menés",
     "Chaque message de contact tient en quatre lignes, sans CV joint, avec une durée annoncée",
     "Chaque message précise explicitement qu'il ne s'agit pas d'une candidature",
     "Aucun entretien exploratoire n'a été transformé en demande d'emploi",
     "Chaque entretien s'est terminé par la question « qui d'autre me conseilleriez-vous de rencontrer ? »",
     "Un remerciement a été envoyé dans les vingt-quatre heures, mentionnant un point précis",
     "L'écart est qualifié : vocabulaire, preuve, ou compétence réelle",
     "Le vocabulaire a été traité avant la preuve, et la preuve avant toute formation",
     "Toute décision de formation a été validée auprès de deux professionnels du secteur",
     "Deux pistes sont retenues et hiérarchisées, pas une seule ni quatre",
     "Un critère de réexamen à trois mois est écrit avant de commencer",
   ]},

 "glossaire": [
   ("Cible testable", "Formulation d'un projet comportant un type de poste, un type d'organisation, une zone géographique et un niveau. Permet de poser une question à laquelle on peut répondre."),
   ("Entretien exploratoire", "Conversation de trente minutes avec un praticien du métier visé, destinée à comprendre ce métier et non à obtenir un emploi. Outil au meilleur rendement du repositionnement."),
   ("Écart de vocabulaire", "Compétence possédée mais nommée autrement que dans le secteur visé. Le plus fréquent, le moins coûteux, et le plus souvent pris pour un écart de compétence."),
   ("Écart de preuve", "Compétence possédée mais non démontrable dans le contexte visé. Se comble par une démonstration courte, pas par une formation."),
   ("Écart de compétence", "Incapacité réelle à faire. Seul cas où une formation est la bonne réponse, et il faut l'avoir vérifié."),
   ("Canal de recrutement", "Voie par laquelle un métier recrute réellement : annonces, réseau, cooptation, interne. Détermine où porter l'effort."),
   ("Marché caché", "Part des postes pourvus sans publication d'offre. Élevée dans les petites structures et les postes d'expertise."),
   ("Exigence éliminatoire", "Condition réglementaire ou de certification sans laquelle l'exercice est impossible. À distinguer des exigences souhaitées, qui décrivent un candidat idéal."),
   ("Piste principale et secondaire", "Répartition de l'effort à 70 % et 30 % entre deux cibles. Une seule piste crée une dépendance, trois diluent l'effort."),
   ("Critère de réexamen", "Condition écrite à l'avance déterminant quand basculer d'une piste à l'autre. Protège du découragement passager comme de l'entêtement."),
   ("Démonstration", "Réalisation courte destinée à attester une compétence dans le contexte visé : intervention, mission, bénévolat ciblé. Doit laisser une trace transmissible."),
 ],

 "retenir": [
   "Quarante candidatures sans réponse n'apprennent rien : le silence est un signal sans contenu.",
   "Pas de candidature pendant les quatre premières semaines : ce temps sert à comprendre le marché.",
   "Une hypothèse comme « la formation » n'est pas une cible : une cible comporte un poste, une organisation, une zone et un niveau.",
   "Vous ne connaissez pas les intitulés du secteur visé : une part importante des offres reste invisible avec le mauvais vocabulaire.",
   "Observez dix parcours réels plutôt que de réfléchir : ils donnent le vocabulaire et les chemins effectivement empruntés.",
   "Si personne dans le métier ne vient de votre profil, ce n'est pas impossible mais ce sera long ; si les origines sont variées, le métier est ouvert.",
   "L'entretien exploratoire est l'outil au meilleur rendement du repositionnement, et presque personne ne l'emploie.",
   "Le taux d'acceptation d'une demande claire et non intéressée se situe couramment entre 30 % et 50 %.",
   "Quatre lignes, pas de CV joint, une durée annoncée, une question précise, et « je ne cherche pas de poste chez vous ».",
   "Ne demandez pas d'opinion sur votre projet : demandez des faits — une semaine ordinaire, ce qui est difficile, comment on recrute.",
   "Ne transformez jamais un entretien exploratoire en candidature : vous perdez la conversation et l'accès au réseau.",
   "Terminez toujours par « qui d'autre me conseilleriez-vous de rencontrer ? » : c'est ce qui rend la série possible.",
   "Une exigence d'offre n'est pas un critère éliminatoire : les offres décrivent un candidat idéal, les recrutements se font sur des candidats réels.",
   "Une offre republiée trois fois signale un poste difficile à pourvoir : c'est le meilleur endroit où se présenter quand on ne coche pas toutes les cases.",
   "Identifiez le canal de recrutement dominant : concentrer son effort sur les annonces dans un métier qui recrute par réseau est une erreur d'allocation.",
   "Connaissez la fourchette de rémunération avant d'être en situation de négocier.",
   "Qualifiez l'écart avant de le traiter : vocabulaire, preuve, ou compétence réelle. Les trois appellent des réponses opposées.",
   "Traitez le vocabulaire d'abord, la preuve ensuite, la formation en dernier — et seulement après vérification auprès de deux professionnels.",
   "Une formation dont vous ne pouvez pas nommer le poste visé et l'écart comblé ne comble rien.",
   "Cherchez la plus petite démonstration possible : une demi-journée vaut mieux qu'un projet de six mois jamais engagé.",
   "Retenez deux pistes hiérarchisées à 70 % et 30 %, et écrivez le critère de bascule avant de commencer.",
   "Quand trois entretiens consécutifs ne vous apprennent plus rien, l'exploration a produit ce qu'elle pouvait : décidez.",
   "L'usure est le premier facteur d'échec d'une recherche longue : maintenez des activités sans rapport, et comptez les entretiens exploratoires comme des résultats.",
 ],

 "exercices": [
  {"titre": "Rédiger un message de prise de contact", "niveau": "Débutant",
   "enonce": [
     "Voici trois messages réellement envoyés. Pour chacun, dites ce qui empêchera la réponse et proposez une réécriture.",
     "<strong>A.</strong> « Bonjour, votre parcours m'intéresse beaucoup. Je suis actuellement en reconversion et je cherche à intégrer votre secteur. Auriez-vous des conseils à me donner ? Merci d'avance. »",
     "<strong>B.</strong> « Bonjour Madame, je me permets de vous contacter car après quinze ans dans l'industrie agroalimentaire, où j'ai occupé successivement des postes de technicien qualité puis de responsable qualité sur deux sites de production, je souhaite aujourd'hui donner un nouveau sens à mon parcours professionnel en m'orientant vers les métiers de l'environnement, domaine qui me passionne depuis longtemps et pour lequel je viens d'entamer une formation. Je serais très heureux de pouvoir échanger avec vous afin de bénéficier de votre expérience et de vos conseils avisés sur les opportunités de ce secteur. Je me tiens à votre entière disposition pour convenir d'un rendez-vous à votre convenance. Vous trouverez ci-joint mon CV. Dans l'attente de votre retour, je vous prie d'agréer... »",
     "<strong>C.</strong> « Bonjour, je vois que vous recrutez régulièrement des chargés de projet. Je suis disponible immédiatement et très motivé. Pouvons-nous échanger ? »",
   ],
   "corrige": """
<p><strong>A — trop vague pour appeler une réponse.</strong></p>
<p><em>Ce qui bloque :</em> aucune information sur qui vous êtes, aucune question précise, aucune durée annoncée. « Des conseils » ne dit pas sur quoi. La personne ne sait pas ce qu'on lui demande, ni combien de temps cela lui coûtera, ni si elle est capable d'y répondre — trois raisons de ne pas répondre plutôt que de risquer de mal répondre.</p>
<p><em>Le mot le plus problématique est « reconversion »</em>, employé seul. Il signale une situation sans indiquer une direction, et il suggère une demande d'aide générale plutôt qu'une question précise.</p>
<p><em>Réécriture :</em> « Bonjour, après huit ans en logistique industrielle, j'envisage de m'orienter vers la qualité fournisseurs et j'essaie de comprendre ce métier avant de me positionner. Auriez-vous trente minutes, par téléphone ? Une question en particulier : dans les parcours que j'ai regardés, ce poste est occupé soit par des profils qualité, soit par des profils achats, et j'aimerais comprendre ce que ces deux origines changent au quotidien. Je ne cherche pas de poste chez vous. »</p>
<p><strong>B — trop long, et il annule sa propre demande.</strong></p>
<p><em>Ce qui bloque, par ordre de gravité.</em></p>
<p>La longueur : dix lignes se lisent en diagonale, et une demande lue en diagonale n'obtient pas de réponse.</p>
<p>Le CV joint : c'est le point rédhibitoire. Il transforme la demande en candidature, quelle que soit la formulation. La personne, n'ayant pas de poste à proposer, ne répond pas — non par désintérêt, mais parce qu'elle croit devoir répondre à une candidature.</p>
<p>Le mot « opportunités » : il confirme la lecture précédente.</p>
<p>L'absence de durée et de question précise, comme en A.</p>
<p><em>Ce qui est bon dans ce message et qu'il faut garder :</em> le parcours est précis, la direction est nommée, et la formation en cours est une information utile. Le matériau est là ; il faut en supprimer les trois quarts.</p>
<p><em>Réécriture :</em> « Bonjour, après quinze ans en qualité dans l'agroalimentaire, je m'oriente vers les métiers de l'environnement et j'ai entamé une formation en ce sens. J'essaie de comprendre comment ce secteur recrute des profils venus de l'industrie. Auriez-vous trente minutes à me consacrer ? Ce qui m'intrigue : les offres que je lis demandent presque toutes une expérience environnement, et pourtant plusieurs personnes du secteur viennent de l'industrie — j'aimerais comprendre par quel chemin. Je ne joins pas de CV, il ne s'agit pas d'une candidature. »</p>
<p><em>La dernière phrase mérite d'être notée :</em> mentionner explicitement l'absence de CV lève l'ambiguïté qu'un message de reconversion crée toujours.</p>
<p><strong>C — c'est une candidature, pas une demande d'entretien exploratoire.</strong></p>
<p><em>Ce qui bloque :</em> tout, mais autrement que dans les deux cas précédents. Ce message ne cherche pas à comprendre, il cherche un poste. « Disponible immédiatement » et « très motivé » sont des formules de candidature, et « pouvons-nous échanger » ne trompe personne.</p>
<p><em>Le vrai problème est en amont :</em> ce message confond deux démarches distinctes. Si l'entreprise recrute effectivement, il faut candidater sur l'offre, correctement, avec le module 3. Si l'on veut comprendre le métier, il faut le dire et ne pas mentionner sa disponibilité.</p>
<p><em>Réécriture, version exploratoire :</em> « Bonjour, je vois que votre équipe compte plusieurs chargés de projet. Je viens de la coordination logistique et j'envisage cette évolution ; j'essaie de comprendre ce que ce poste recouvre concrètement chez vous, qui semble différent de ce que j'ai lu ailleurs. Auriez-vous vingt minutes ? Je ne postule pas — je cherche à comprendre avant de me positionner. »</p>
<p><em>Réécriture, version candidature :</em> ce n'est plus l'objet de ce module, et c'est le module 3.</p>
<p><strong>Ce que les trois cas ont en commun.</strong> Aucun n'annonce de durée, aucun ne pose de question précise, et aucun ne lève l'ambiguïté sur la nature de la demande. Ces trois manques expliquent la quasi-totalité des messages sans réponse.</p>
<p>À l'inverse, les quatre éléments qui font répondre sont toujours les mêmes : une phrase sur qui vous êtes, ce que vous cherchez à comprendre, une durée, et une question qui montre que vous avez travaillé. Le reste peut être supprimé.</p>
"""},

  {"titre": "Qualifier un écart et choisir comment le combler", "niveau": "Intermédiaire",
   "enonce": [
     "Quatre personnes ont identifié leur cible et constatent un écart. Pour chacune, qualifiez l'écart, dites comment le combler, et indiquez ce que vous déconseillez.",
     "<strong>A.</strong> Dix ans d'assistanat de direction, vise la coordination de projet. Les offres demandent « gestion de projet » et une méthode qu'elle ne connaît pas de nom, alors qu'elle a piloté trois déménagements de site et le déploiement d'un logiciel.",
     "<strong>B.</strong> Six ans en support informatique, vise l'administration de bases de données. Ne connaît pas le langage de requête utilisé dans toutes les offres.",
     "<strong>C.</strong> Douze ans en vente en magasin, vise la formation en entreprise. A formé tous les nouveaux arrivants de son magasin pendant huit ans, sans que cela figure dans sa fiche de poste ni dans aucun document.",
     "<strong>D.</strong> Quinze ans en comptabilité dans une PME, vise un poste de responsable administratif et financier. Les offres demandent toutes une expérience du contrôle de gestion et de la relation bancaire, qu'elle n'a jamais exercées.",
   ],
   "corrige": """
<p><strong>A — écart de vocabulaire, presque exclusivement.</strong></p>
<p><em>Qualification :</em> piloter trois déménagements de site et le déploiement d'un logiciel <em>est</em> de la gestion de projet. Il y a eu un objectif, des contraintes de délai, des parties prenantes multiples, un budget probablement, et un résultat. La compétence existe ; ce qui manque est son nom.</p>
<p><em>Comment le combler :</em> par la traduction. Reprendre chaque projet et le décrire dans le vocabulaire du domaine — cadrage, parties prenantes, jalons, arbitrages, gestion des risques, conduite du changement. Ce vocabulaire s'acquiert en lisant quinze offres et un ouvrage d'introduction, en quelques heures.</p>
<p><em>Ce qu'il reste, éventuellement :</em> une méthode formalisée. Si les offres visées la citent réellement dans la majorité des cas, une certification courte de quelques jours comble l'écart. Vérifier d'abord dans les offres : ces méthodes sont souvent citées par réflexe de rédaction plutôt que par exigence réelle, et un entretien exploratoire tranche en dix minutes.</p>
<p><em>Ce que je déconseille :</em> un cycle long en gestion de projet. Douze mois pour apprendre à nommer ce qu'elle fait depuis dix ans. C'est le cas type de la formation qui comble un écart inexistant, et il est très fréquent.</p>
<p><strong>B — écart de compétence réel, et c'est le seul des quatre.</strong></p>
<p><em>Qualification :</em> ne pas connaître le langage de requête utilisé par toutes les offres n'est ni un problème de vocabulaire ni un problème de preuve. C'est une compétence technique absente, et elle est vérifiable objectivement.</p>
<p><em>Comment le combler :</em> par une formation, et c'est le bon usage du dispositif. Bonne nouvelle sur ce cas précis : ces compétences s'acquièrent par des formations courtes et certifiantes, et surtout elles se démontrent par la pratique — un projet personnel, une base construite et documentée, une certification d'éditeur. La démonstration compte ici autant que le certificat.</p>
<p><em>Ce que je recommande en plus :</em> commencer par une ressource gratuite avant de financer quoi que ce soit. Deux semaines suffisent à savoir si l'on accroche. Une part non négligeable des reconversions vers les métiers de la donnée s'arrête au premier contact réel avec la matière, et il vaut mieux que ce soit avant l'engagement financier.</p>
<p><em>Ce que je déconseille :</em> candidater sans avoir commencé. C'est le seul cas des quatre où l'écart bloque réellement, et où se présenter trop tôt produit un refus mérité qui abîme la confiance.</p>
<p><strong>C — écart de preuve pur, et c'est le cas le plus fréquent.</strong></p>
<p><em>Qualification :</em> huit ans à former tous les nouveaux arrivants est une expérience de formation substantielle. Elle n'existe dans aucun document et n'a jamais été nommée. La compétence est là, la preuve n'y est pas.</p>
<p><em>Comment le combler, par ordre de coût croissant.</em></p>
<p>D'abord, obtenir des traces de ce qui existe déjà : un témoignage écrit de son responsable ou d'anciens collègues formés, le nombre de personnes formées sur huit ans — un chiffre concret transforme une affirmation en fait. Une trace de support si elle en a conçu. Coût nul, effet immédiat.</p>
<p>Ensuite, une démonstration en contexte élargi : proposer une session structurée dans son magasin ou pour l'enseigne, avec un support et une évaluation. Quelques semaines.</p>
<p>Enfin, si nécessaire, une certification légère de formateur, qui donne un langage et un titre. À n'envisager qu'après avoir vérifié qu'elle est réellement attendue.</p>
<p><em>Ce que je déconseille :</em> considérer que huit ans de formation informelle ne comptent pas parce qu'elles n'étaient pas dans la fiche de poste. C'est l'erreur d'appréciation la plus coûteuse de ce cas, et elle conduit à se présenter comme débutant dans un domaine où l'on a huit ans de pratique.</p>
<p><strong>D — écart mixte, et c'est le cas le plus délicat à traiter.</strong></p>
<p><em>Qualification :</em> il faut décomposer, car les deux exigences citées ne sont pas de même nature.</p>
<p>Le <em>contrôle de gestion</em> est probablement un écart mixte. Quinze ans de comptabilité en PME comportent presque toujours une part d'analyse — suivi de marge, préparation de budget, explication d'écarts — exercée sans être nommée ainsi. Une partie est un écart de vocabulaire et de preuve ; une autre, sur les méthodes formalisées, est un écart réel mais étroit.</p>
<p>La <em>relation bancaire</em> est plus probablement un écart réel. C'est une compétence relationnelle et technique spécifique, et l'exercer suppose d'avoir eu le mandat de le faire.</p>
<p><em>Comment le combler :</em> traiter les deux séparément. Sur le contrôle de gestion, inventorier tout ce qui relève déjà de l'analyse dans ses quinze ans, le traduire, et compléter éventuellement par une formation courte sur les méthodes formalisées. Sur la relation bancaire, chercher à l'exercer avant de changer de poste — dans une PME, une comptable expérimentée peut souvent obtenir de participer aux rendez-vous bancaires, voire de les préparer. Six mois de cette exposition suffisent à transformer un écart réel en compétence démontrable.</p>
<p><em>Ce que je recommande surtout :</em> cibler d'abord des PME plus petites que la cible idéale. Le poste de responsable administratif et financier d'une structure de vingt personnes est nettement plus accessible et il donne accès aux deux compétences manquantes. C'est un chemin en deux étapes plutôt qu'un saut, et c'est presque toujours la bonne réponse quand l'écart porte sur des compétences qui ne s'acquièrent qu'en les exerçant.</p>
<p><em>Ce que je déconseille :</em> une formation diplômante en gestion financière pour combler la relation bancaire. Elle ne comblera pas cet écart, qui est un écart d'exercice et non de savoir.</p>
<p><strong>Le principe qui traverse les quatre cas.</strong> Sur quatre situations décrites par leurs protagonistes comme « il me manque des compétences », une seule relève réellement d'une formation. Les trois autres relèvent de la traduction, de la preuve, ou d'un chemin en deux étapes. La qualification de l'écart, qui prend une heure, est probablement l'heure la plus rentable de tout un projet de repositionnement.</p>
"""},

  {"titre": "Conduire l'exploration complète d'une cible", "niveau": "Avancé",
   "enonce": [
     "Choisissez l'une de vos hypothèses de cible et menez l'exploration complète sur six semaines : cartographie du vocabulaire, dix parcours observés, quinze offres lues, huit à dix entretiens exploratoires, qualification de l'écart.",
     "Puis répondez aux cinq questions de contrôle : combien d'intitulés distincts avez-vous découverts ? Quel est le canal de recrutement dominant ? Qu'est-ce qui fait échouer ceux qui arrivent dans ce métier ? Votre attrait pour la cible a-t-il augmenté ou diminué ? Et quelle information obtenue en entretien n'auriez-vous jamais trouvée seul ?",
   ],
   "corrige": """
<p>Cet exercice porte sur votre projet et n'a pas de corrigé unique. Voici comment lire chacune de vos cinq réponses, et ce que chaque cas indique sur la qualité de l'exploration menée.</p>
<p><strong>Question 1 — combien d'intitulés distincts avez-vous découverts ?</strong></p>
<p><em>Un ou deux :</em> l'observation des parcours a été trop superficielle, ou la cible est un métier très codifié — ce qui existe, notamment dans les professions réglementées. Vérifiez en relançant une recherche d'offres sur les synonymes que vous auriez pu manquer. La plupart des métiers non réglementés portent quatre à huit intitulés.</p>
<p><em>Quatre à huit :</em> résultat attendu. Vérifiez que vous avez relancé vos recherches d'offres sur chacun. C'est le geste que l'on oublie après avoir fait la cartographie, et il annule tout le bénéfice de l'exercice.</p>
<p><em>Plus de dix :</em> votre cible est probablement encore trop large et recouvre plusieurs métiers distincts. Redécoupez comme dans l'exemple de la formation en entreprise — vous avez sans doute deux ou trois cibles, pas une.</p>
<p><strong>Question 2 — quel est le canal de recrutement dominant ?</strong></p>
<p><em>Si vous ne savez pas répondre :</em> c'est le manque le plus grave possible à ce stade, parce que cette réponse détermine l'allocation de tout votre effort des mois suivants. Reprenez trois personnes rencontrées et posez-leur directement la question : « comment avez-vous obtenu votre poste ? ». Trois réponses suffisent à dégager une tendance.</p>
<p><em>Si la réponse est « les annonces » :</em> tant mieux, c'est le canal le plus simple à travailler. Concentrez-vous sur la qualité des candidatures et sur la vitesse de réaction — sur ce canal, répondre dans les quarante-huit heures change sensiblement les chances.</p>
<p><em>Si la réponse est « le réseau et la cooptation » :</em> c'est le cas le plus fréquent sur les postes d'expertise et dans les petites structures, et il impose une stratégie entièrement différente, traitée au module 3. Le nombre de candidatures cesse d'être le bon indicateur d'activité ; le nombre de personnes qui savent ce que vous cherchez le devient.</p>
<p><strong>Question 3 — qu'est-ce qui fait échouer ceux qui arrivent dans ce métier ?</strong></p>
<p>C'est la question la plus précieuse de tout l'exercice, et si vous n'avez pas de réponse précise, c'est que vous ne l'avez pas posée — elle est rarement volontaire.</p>
<p><em>La réponse a deux usages.</em> Elle vous dit si vous risquez d'échouer pour la même raison, ce qui est une information sur votre adéquation réelle au métier, bien plus fiable que votre intuition. Et elle vous donne l'argument central de votre candidature au module 3 : si sept praticiens sur dix citent la même difficulté et que votre parcours démontre que vous savez la traiter, vous tenez le point unique sur lequel construire votre présentation.</p>
<p><em>Si les réponses divergent complètement</em> d'un interlocuteur à l'autre, c'est en soi une information : le métier recouvre probablement des réalités très différentes selon les organisations, et il faudra affiner la cible par type d'organisation.</p>
<p><strong>Question 4 — votre attrait a-t-il augmenté ou diminué ?</strong></p>
<p><em>S'il a augmenté :</em> bon signe, à une réserve près. Vérifiez que vous avez posé la question de ce qui est difficile, et pas seulement de ce qui est intéressant. Un attrait qui augmente après une exploration où l'on n'a entendu que du positif signale une exploration complaisante — les gens décrivent volontiers leur métier sous son meilleur jour si on ne les interroge pas autrement.</p>
<p><em>S'il a diminué sans disparaître :</em> c'est le résultat le plus courant et le plus sain. Vous êtes passé d'un métier imaginé à un métier connu, avec ses contraintes. Un projet qui survit à cette désidéalisation est solide.</p>
<p><em>S'il a disparu :</em> l'exploration a parfaitement fonctionné. Six semaines ont évité deux ans dans un métier qui ne convenait pas. Ce n'est pas un échec, c'est le résultat le plus utile que l'exercice puisse produire — et c'est aussi le plus difficile à accepter, parce qu'il faut recommencer sur une autre hypothèse. Le travail n'est pas perdu : la méthode est acquise et la seconde exploration prendra trois semaines au lieu de six.</p>
<p><strong>Question 5 — quelle information n'auriez-vous jamais trouvée seul ?</strong></p>
<p>C'est le contrôle final, et il porte sur la valeur réelle des entretiens.</p>
<p><em>Si vous n'avez rien à citer :</em> les entretiens ont probablement porté sur des sujets que vous maîtrisiez déjà, ou vous avez surtout parlé de vous. Reprenez deux conversations avec les questions dans l'ordre indiqué — leur parcours d'abord, vos questions à la fin.</p>
<p><em>Si vous pouvez citer une ou deux choses :</em> résultat normal, et ces deux informations valent à elles seules l'exercice.</p>
<p><em>Si vous pouvez en citer cinq :</em> l'exploration a été bien menée, et vous disposez maintenant d'un avantage réel sur les autres candidats — non pas sur le profil, mais sur la compréhension du métier, qui se perçoit immédiatement en entretien.</p>
<p><strong>Le contrôle qui résume tout.</strong> Après six semaines, vous devriez pouvoir expliquer à quelqu'un du métier, en deux minutes, ce que fait un professionnel de cette cible au quotidien, comment on y entre, et ce qui y est difficile. Si vous ne le pouvez pas, l'exploration n'est pas terminée. Si vous le pouvez, vous êtes prêt pour le module 3 — et vous en savez plus sur ce métier que la majorité de ceux qui candidatent sur ses offres.</p>
"""},
 ],

 "ressources": [
   "<strong>Un réseau professionnel en ligne</strong> — non pour candidater, mais pour observer des parcours réels : quels intitulés, dans quel ordre, depuis quel métier d'origine. C'est la source d'information la plus riche et la plus sous-exploitée de tout le repositionnement.",
   "<strong>Les fiches métiers des répertoires publics</strong> (ROME de France Travail, fiches de branches professionnelles) — utiles pour le vocabulaire officiel et les compétences attendues, à croiser avec les offres réelles, qui emploient souvent d'autres termes.",
   "<strong>Les événements professionnels du secteur visé</strong> — salons, conférences, rencontres de réseau. Un après-midi produit souvent trois contacts qu'un mois de messages n'aurait pas obtenus, et la demande d'entretien exploratoire y est naturelle.",
   "<strong>Le module 3 de cette formation</strong> — traduire son profil, se rendre visible sur le canal identifié, et convertir les entretiens. N'y allez pas avant d'avoir identifié le canal de recrutement dominant : il détermine toute la stratégie du module suivant.",
 ],
}

QUIZ["bilan-competences/module-2"] = {
 "module_id": "formation-bilan-competences-module-2",
 "version": "2.0", "last_verified": "2026-09-04",
 "questions": [
  {"id":"q1","question":"Quarante candidatures sont restées sans réponse. Qu'est-ce que cela vous apprend ?",
   "choices":[{"key":"a","text":"Que votre profil ne correspond pas au marché visé"},
              {"key":"b","text":"Que le marché est saturé et qu'il faut élargir la zone géographique"},
              {"key":"c","text":"Rien : le silence peut recouvrir un profil hors sujet, un mauvais vocabulaire, un mauvais canal ou un poste déjà pourvu"}],
   "correct_answer":"c","feedback":"Le silence est un signal sans contenu. C'est pourquoi il ne faut pas candidater pendant les quatre premières semaines : ce temps sert à comprendre."},
  {"id":"q2","question":"Comment trouver les intitulés de poste réellement employés par le secteur visé ?",
   "choices":[{"key":"a","text":"En observant les parcours publics de dix personnes exerçant ce métier"},
              {"key":"b","text":"En consultant les fiches métiers des répertoires officiels"},
              {"key":"c","text":"En demandant à un conseiller en évolution professionnelle"}],
   "correct_answer":"a","feedback":"Vous obtiendrez quatre à huit intitulés là où vous en connaissiez un, plus une information rare : les chemins réellement empruntés pour arriver au métier."},
  {"id":"q3","question":"Qu'est-ce qui fait le plus échouer une demande d'entretien exploratoire ?",
   "choices":[{"key":"a","text":"Le fait de contacter quelqu'un qu'on ne connaît pas du tout"},
              {"key":"b","text":"Le CV joint, qui transforme la demande en candidature déguisée"},
              {"key":"c","text":"Le fait de demander trente minutes plutôt que dix"}],
   "correct_answer":"b","feedback":"La personne, n'ayant pas de poste à offrir, ne répond pas. D'où l'utilité de la phrase « je ne cherche pas de poste chez vous », qui paraît maladroite et qui est décisive."},
  {"id":"q4","question":"Vous possédez la compétence mais ne pouvez pas la démontrer dans le contexte visé. De quel écart s'agit-il et comment le combler ?",
   "choices":[{"key":"a","text":"Un écart de preuve, à combler par une démonstration courte laissant une trace"},
              {"key":"b","text":"Un écart de compétence, à combler par une formation certifiante"},
              {"key":"c","text":"Un écart de vocabulaire, à combler par la traduction du CV"}],
   "correct_answer":"a","feedback":"Une demi-journée d'intervention vaut mieux qu'un projet de six mois jamais engagé. Fixez une échéance de deux mois, sinon l'écart de preuve devient un prétexte."},
  {"id":"q5","question":"Une offre a été republiée trois fois en quatre mois. Comment le lire ?",
   "choices":[{"key":"a","text":"Comme une annonce fictive servant à constituer un vivier de candidatures"},
              {"key":"b","text":"Comme un poste difficile à pourvoir, donc un bon endroit où se présenter avec un profil atypique"},
              {"key":"c","text":"Comme un signe que les exigences sont trop élevées pour être satisfaites"}],
   "correct_answer":"b","feedback":"C'est même le meilleur endroit où se présenter quand on ne coche pas toutes les cases : l'employeur a déjà constaté que le profil idéal ne se présente pas."},
  {"id":"q6","question":"Combien de pistes faut-il retenir à l'issue de l'exploration ?",
   "choices":[{"key":"a","text":"Une seule, pour concentrer tout l'effort"},
              {"key":"b","text":"Toutes celles qui restent valides, pour maximiser les chances"},
              {"key":"c","text":"Deux, hiérarchisées à 70 % et 30 %, avec un critère de bascule écrit à l'avance"}],
   "correct_answer":"c","feedback":"Une seule piste crée une dépendance à un marché ; trois pistes menées en parallèle diluent l'effort au point qu'aucune n'aboutit."},
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
