#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Formahub — source du module 1 de la formation « Analytics et mesure de la performance ».

Regenerer la page et le quiz :
    python3 mod1.py                       # ecrit dans ../formations/
    FH_OUT=/tmp/essai python3 mod1.py     # ecrit ailleurs

Valider ensuite les quatre modules :
    FH_OUT=../formations FH_CSS=../assets/css/style.css python3 validate.py analytics-mesure 4
"""
import sys, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from fh_builder import build, set_out

OUT = os.environ.get("FH_OUT", os.path.join(HERE, "..", "formations"))
set_out(OUT)

M = {}
FORM = "Analytics &amp; mesure de la performance"

M["analytics-mesure/module-1"] = {
 "formation": FORM,
 "titre": "Cadrer la mesure : du besoin de décision au plan de marquage",
 "num": 1, "total": 4, "duree": "60 min", "niveau": "Débutant",
 "module_id": "formation-analytics-mesure-module-1",
 "situation": [
   "Lundi 9 mars, réunion de préparation budgétaire. Le directeur général pose une question simple : « nous avons dépensé 180 000 € en acquisition l'an dernier. Qu'est-ce que cela a rapporté ? »",
   "Vous ouvrez l'outil d'analytics du site. Il affiche 412 000 sessions sur douze mois, en hausse de 18 %, un taux de rebond de 54 %, une durée moyenne de session de 2 minutes 40 et vingt-quatre sources de trafic. Aucun de ces chiffres ne répond à la question posée. Vous avez énormément de données et pas de réponse.",
   "Ce n'est ni un problème d'outil ni un problème de compétence technique : l'outil enregistre consciencieusement ce qu'on lui a demandé d'enregistrer, c'est-à-dire ce qu'il propose par défaut. Personne n'a jamais écrit quelle décision cette mesure devait servir. C'est la cause première de l'inutilité de la plupart des dispositifs de mesure, et elle est antérieure à toute question technique.",
   "Ce module traite l'étape que tout le monde saute : décider ce qu'on mesure, et pourquoi, avant de mesurer. L'étude de cas y répondra concrètement — et montrera pourquoi la réponse honnête au directeur comporte une part d'incertitude qu'il faut savoir assumer.",
 ],
 "objectifs": [
   "Écarter un indicateur inutile en lui appliquant le test de la décision",
   "Rédiger un indicateur exploitable : mesure, segment, période, référence, propriétaire",
   "Traduire une question métier en plan de mesure, jusqu'aux événements à collecter",
   "Nommer et documenter des événements de façon à ce qu'ils restent lisibles dans deux ans",
   "Estimer ce que le consentement et les bloqueurs retirent réellement de vos données",
   "Décider avec des données incomplètes sans nier l'incertitude ni s'en servir d'excuse",
 ],
 "sections": [
  {"titre": "Pourquoi la plupart des tableaux de bord ne déclenchent rien",
   "paras": [
     "Il existe une différence de nature entre <strong>compter</strong> et <strong>mesurer</strong>. Compter, c'est enregistrer ce qui se produit : un outil installé par défaut compte des pages vues, des sessions et des durées sans qu'on le lui demande. Mesurer, c'est produire une information dont on a besoin pour trancher quelque chose. Le premier est gratuit et abondant, le second demande un travail préalable — et c'est ce travail que la facilité d'installation des outils modernes a fait disparaître.",
     "Le symptôme le plus reconnaissable est le rapport mensuel de dix-huit pages que personne ne lit : il n'est pas faux, il est sans effet, et comme il est complet il donne le sentiment rassurant que le sujet est couvert.",
     "Le filtre à appliquer avant d'afficher quoi que ce soit tient en une question : <strong>quelle décision prendrai-je différemment selon sa valeur ?</strong> Si vous ne pouvez pas nommer la décision, l'indicateur est décoratif, quel que soit le sérieux de celui qui le demande. Appliqué honnêtement, ce test élimine la moitié à deux tiers de ce qu'un tableau de bord contient habituellement.",
     "Il a une conséquence inconfortable : des chiffres parfaitement légitimes ne le passent pas. Le nombre total de sessions du mois est vrai, intéressant et sans usage décisionnel — on ne fait rien de différent selon qu'il vaut 34 000 ou 37 000. En revanche, « part des sessions organiques qui atteignent la page tarifs, comparée au trimestre précédent » déclenche une action nommée si elle baisse. Seule exception admise : deux ou trois indicateurs de <strong>cadrage</strong>, dont le chiffre d'affaires, qui ne déclenchent rien seuls mais conditionnent la lecture du reste. Ils sont en haut, et ils ne se commentent pas.",
   ],
   "blocks": [
     {"type": "exemple", "titre": "trois indicateurs passés au test",
      "paras": [
        "<em>« Durée moyenne de session »</em> — échoue, et c'est le cas le plus instructif. Une durée qui augmente peut signifier que le contenu retient, ou que les visiteurs ne trouvent pas ce qu'ils cherchent. Deux causes opposées, même chiffre : aucune décision ne peut s'y appuyer. Elle ne redevient utile que segmentée et rapportée à une intention connue — la durée sur la page d'aide, qu'on cherche à réduire.",
        "<em>« Taux de complétion du formulaire de demande »</em> — passe : s'il baisse, on regarde le formulaire, l'étape précédente et les appareils. La décision est nommée avant même de voir le chiffre, ce qui est le signe d'un bon indicateur.",
        "<em>« Coût d'acquisition par canal, sur 90 jours glissants »</em> — passe, et c'est celui qui répond à la question du directeur. Il exige un travail de plan de mesure que les deux autres n'imposent pas : les indicateurs utiles coûtent plus cher que les indicateurs disponibles.",
      ]},
     {"type": "pitfall", "titre": "mesurer ce que l'outil propose plutôt que ce dont on a besoin",
      "paras": [
        "L'écran d'accueil d'un outil d'analytics est une proposition commerciale : il affiche ce qui se mesure sans configuration, parce que c'est ce qui rend l'outil impressionnant en trente secondes. Presque rien de ce qui s'y trouve ne passe le test de la décision.",
        "Le glissement se fait sans que personne ne le décide : on regarde l'écran d'accueil, on prend l'habitude de le commenter en réunion, et six mois plus tard ces chiffres sont devenus les indicateurs de l'entreprise. Ils n'ont jamais été choisis. Le seul remède est d'écrire les questions avant d'ouvrir l'outil : l'ordre des opérations est ici la totalité de la méthode.",
      ]},
   ]},

  {"titre": "Anatomie d'un indicateur exploitable",
   "paras": [
     "Un indicateur écrit en deux mots — « le trafic », « les conversions » — n'est pas un indicateur, c'est un sujet de conversation. Il ne se calcule pas de la même façon selon qui le demande, et deux réunions successives commenteront deux chiffres différents en croyant parler du même. Un indicateur exploitable tient en une ligne et contient cinq éléments.",
     "<strong>La mesure</strong>, sans ambiguïté de calcul : « les conversions » ne suffit pas, s'agit-il des demandes envoyées ou des demandes qualifiées par un commercial ? Le premier chiffre est trois fois plus élevé que le second et n'appelle pas les mêmes décisions. <strong>Le segment</strong> : un indicateur sans population définie est une moyenne, et une moyenne cache par construction ce qui nous intéresse. <strong>La période</strong> et sa fenêtre : une valeur mensuelle saute en début de mois là où une fenêtre glissante absorbe les jours fériés, et la seconde est presque toujours préférable dès qu'on suit un chiffre plus d'une fois par mois.",
     "<strong>La référence</strong>, c'est-à-dire ce à quoi on compare : 3,2 % de taux de conversion n'est ni bon ni mauvais tant qu'on ignore ce qu'il valait avant ou ce qu'on visait. C'est l'élément le plus souvent oublié, et son absence explique la longueur des réunions de reporting — on y passe le temps à chercher si le chiffre est bon. <strong>Le propriétaire</strong>, enfin : un indicateur sans propriétaire produit une discussion, jamais une action. Nommer quelqu'un au moment de créer l'indicateur, et non au moment où il se dégrade, change la nature de la réunion.",
   ],
   "blocks": [
     {"type": "exemple", "titre": "le même indicateur, mal puis bien écrit",
      "paras": [
        "<em>Version courante :</em> « suivre le taux de conversion du site ». Trois personnes le calculeront de trois façons, et le comité passera vingt minutes à comprendre pourquoi les chiffres diffèrent.",
        "<em>Version exploitable :</em> « part des sessions organiques, sur ordinateur, aboutissant à une demande de démonstration envoyée — sur 30 jours glissants, comparée aux 30 jours précédents et à l'objectif de 2,5 %. Propriétaire : responsable acquisition. »",
        "La seconde est longue, et c'est normal : on ne l'écrit qu'une fois, dans le plan de mesure, et on l'appelle ensuite par un nom court. Ce qui compte est qu'elle existe et fasse autorité en cas de désaccord — la plupart des disputes de chiffres sont des disputes de définitions.",
      ]},
     {"type": "method", "titre": "rédiger un indicateur en six temps",
      "steps": [
        "<strong>Nommez la décision d'abord.</strong> Écrivez « si ce chiffre bouge, nous ferons X ». Si vous n'y arrivez pas, arrêtez : vous venez d'économiser un travail de collecte.",
        "<strong>Écrivez la mesure sans ambiguïté</strong>, en précisant numérateur et dénominateur s'il s'agit d'un taux. La moitié des désaccords sur un taux portent sur le dénominateur.",
        "<strong>Définissez le segment</strong> : quelle population, quels appareils, quelles sources. Un indicateur qui mélange les visiteurs de la page d'accueil et ceux du support ne mesure rien de commun.",
        "<strong>Choisissez la période et la fenêtre</strong>, en privilégiant la fenêtre glissante pour tout ce qui est suivi plus d'une fois par mois.",
        "<strong>Fixez la référence.</strong> Si vous ne savez pas encore ce qui est normal, observez deux à trois mois avant de poser un seuil : un seuil inventé fait plus de dégâts que pas de seuil, car ses fausses alertes apprennent à ignorer l'indicateur.",
        "<strong>Nommez un propriétaire</strong> et notez la définition complète, datée, dans un document partagé. C'est ce document, pas l'outil, qui fait référence.",
      ]},
     {"type": "h3", "titre": "Indicateurs avancés et indicateurs de résultat",
      "paras": [
        "Les <strong>indicateurs de résultat</strong> mesurent l'issue — chiffre d'affaires, clients signés, marge : les seuls qui comptent vraiment, et ceux sur lesquels on ne peut plus rien quand on les découvre. Les <strong>indicateurs avancés</strong> mesurent ce qui le précède et le prédit partiellement : visiteurs qualifiés, taux de complétion, demandes entrantes. Ce décalage de quelques semaines est ce qui les rend pilotables, et un dispositif sans indicateur avancé ne permet que de constater. Le tableau de bord d'un opérationnel en est majoritairement composé, celui d'un dirigeant beaucoup moins — le module 4 reprendra cette répartition.",
        "Une précaution s'impose toutefois : un indicateur avancé n'est utile que si son lien avec le résultat a été vérifié au moins une fois. Beaucoup d'entreprises en pilotent de supposés et découvrent après deux ans que le nombre de téléchargements de leur livre blanc n'a aucune relation avec les ventes. Le module 3 donnera les moyens de vérifier ce lien.",
      ]},
     {"type": "pitfall", "titre": "confondre un ratio qui monte avec une amélioration",
      "paras": [
        "Un taux est une fraction, et une fraction monte aussi bien quand le numérateur augmente que quand le dénominateur diminue. Un taux de conversion passant de 2,1 % à 3,4 % après la coupure d'une campagne publicitaire ne signale aucune amélioration : on a retiré du trafic peu qualifié du dénominateur, et le nombre absolu de conversions a baissé.",
        "La parade est systématique : <strong>ne jamais afficher un taux sans son numérateur</strong>. Cette seule discipline évite une bonne partie des conclusions inversées, et elle coûte une colonne de tableau.",
      ]},
   ]},

  {"titre": "Le plan de mesure : de la question métier aux événements",
   "paras": [
     "Le plan de mesure est le document qui relie ce que l'entreprise veut décider à ce que le site doit enregistrer. Il se lit de gauche à droite et se construit dans cet ordre, jamais l'inverse : une <strong>question métier</strong>, la <strong>décision</strong> qu'elle prépare, l'<strong>indicateur</strong> qui la déclenche, les <strong>événements</strong> à collecter, les <strong>propriétés</strong> qu'ils doivent porter.",
     "Sa vertu principale n'est pas d'organiser le travail technique, même s'il le fait : elle est de rendre visibles, avant toute dépense, les questions auxquelles on ne pourra pas répondre. Une entreprise qui construit son plan découvre en général deux ou trois questions importantes qu'aucun événement ne permet de traiter — et c'est le bon moment pour le découvrir, plutôt qu'un an plus tard en réunion budgétaire.",
     "Il fixe aussi une limite de volume. Un site correctement instrumenté a besoin de quinze à vingt-cinq événements ; au-delà, plus personne ne sait ce que chacun contient, deux équipes en créent des doublons, et le dispositif devient illisible en dix-huit mois. Cette contrainte n'est pas une économie, c'est ce qui garantit qu'il restera compréhensible quand vous ne serez plus là pour l'expliquer. Un plan de mesure se relit d'ailleurs deux fois par an, avec deux questions — quelles décisions ne sont plus prises, quels événements ne sont plus lus — dont les deux réponses conduisent à retirer quelque chose.",
   ],
   "blocks": [
     {"type": "html", "html": """
<div class="table-responsive">
<table>
  <thead>
    <tr><th>Question métier</th><th>Décision préparée</th><th>Indicateur</th><th>Événements requis</th></tr>
  </thead>
  <tbody>
    <tr>
      <td>Nos campagnes payantes amènent-elles des clients ou seulement du trafic ?</td>
      <td>Reconduire, réduire ou arrêter le budget par canal</td>
      <td>Coût par demande qualifiée, par canal, sur 90 jours glissants</td>
      <td><code>demande_envoyee</code> avec source, rapprochée de la dépense des régies</td>
    </tr>
    <tr>
      <td>Le nouveau formulaire est-il plus simple que l'ancien ?</td>
      <td>Généraliser ou revenir en arrière</td>
      <td>Taux de complétion et abandon par champ, par appareil</td>
      <td><code>formulaire_debut</code>, <code>formulaire_champ_abandon</code>, <code>demande_envoyee</code></td>
    </tr>
    <tr>
      <td>Nos contenus servent-ils à autre chose qu'à faire du volume ?</td>
      <td>Poursuivre ou réorienter la production éditoriale</td>
      <td>Part des demandes dont le parcours contient au moins un article</td>
      <td><code>article_lu</code> (seuil de lecture), <code>demande_envoyee</code></td>
    </tr>
    <tr>
      <td>Perdons-nous des visiteurs sur mobile en particulier ?</td>
      <td>Arbitrer un chantier technique mobile</td>
      <td>Écart de taux de complétion mobile / ordinateur</td>
      <td>Les mêmes, avec la propriété <code>type_appareil</code></td>
    </tr>
  </tbody>
</table>
</div>
"""},
     {"type": "method", "titre": "construire un plan de mesure en sept étapes",
      "steps": [
        "<strong>Collectez les questions, pas les demandes d'indicateurs.</strong> Interrogez trois à cinq décideurs avec une seule question : « qu'aimeriez-vous savoir que vous n'avez pas ? ». Demandez-leur quels indicateurs ils veulent, et vous obtiendrez la liste de ce qu'ils ont vu ailleurs.",
        "<strong>Écartez explicitement les questions qui ne préparent aucune décision.</strong> Formulation qui passe : « si nous avions ce chiffre, que ferions-nous de différent ? ». Une question sans réponse à cela est de la curiosité, et la curiosité ne finance pas une collecte.",
        "<strong>Classez les questions restantes par valeur de la décision</strong> qu'elles préparent, jamais par facilité de mesure. Vous en garderez cinq à huit pour un premier plan.",
        "<strong>Écrivez l'indicateur de chaque question</strong> avec les cinq éléments de la section précédente, puis <strong>descendez aux événements et à leurs propriétés</strong> en regroupant ceux qui servent à plusieurs indicateurs. C'est là que le nombre total se réduit fortement.",
        "<strong>Faites relire le plan par la personne qui l'implémentera</strong> avant validation : elle repérera les propriétés impossibles à collecter, celles qui exigent un identifiant inexistant et celles qui coûtent dix fois le budget prévu.",
        "<strong>Datez le document et inscrivez la date de sa prochaine relecture.</strong> Sans date inscrite, elle n'a jamais lieu.",
      ]},
     {"type": "exemple", "titre": "une question qui ne survit pas à l'étape 2",
      "paras": [
        "Demande reçue en atelier : « je voudrais savoir quelles villes visitent le plus notre site ». Question posée en retour : que feriez-vous de différent selon la réponse ? La première réponse est vague ; en creusant, l'intention réelle apparaît — savoir s'il faut ouvrir une agence dans une deuxième ville. Décision considérable, qui mérite une mesure.",
        "Mais la géographie des visiteurs est alors un très mauvais indicateur pour la trancher : elle reflète surtout où l'entreprise fait de la publicité et où sa notoriété existe déjà. Les bons indicateurs seraient la répartition géographique des <em>demandes qualifiées</em>, celle des clients signés et le taux de transformation par région. C'est le rendement principal de l'étape 2 : elle ne sert pas seulement à écarter des demandes, elle sert surtout à en transformer — une demande mal formulée cache souvent une bonne question.",
      ]},
     {"type": "pitfall", "titre": "tout marquer « au cas où »",
      "paras": [
        "L'argument est séduisant — la donnée non collectée est perdue à jamais, donc autant tout enregistrer et trier plus tard. Il est faux pour trois raisons. Une collecte exhaustive ne se maintient pas : les événements sans usage ne sont vérifiés par personne et cessent silencieusement de fonctionner à la première refonte. Elle alourdit la charge juridique, chaque donnée devant être justifiée, documentée et supprimable, y compris celle que personne n'utilise. Surtout, elle détruit la lisibilité : dans un outil contenant deux cents événements dont trente seulement fonctionnent, le réflexe devient de ne plus rien croire.",
        "La règle inverse est plus sûre : ne collectez que ce que votre plan justifie, et acceptez que l'ajout ultérieur d'un événement coûte quelques semaines de recul. Ce coût est borné ; celui d'un dispositif illisible ne l'est pas.",
      ]},
   ]},

  {"titre": "Comment la donnée arrive : balise, événement, propriété, identifiant",
   "paras": [
     "Il n'est pas nécessaire de savoir programmer pour cadrer une mesure, mais il est indispensable de comprendre par quel chemin un clic devient une ligne dans un rapport : sans cela, on demande des choses impossibles, on accepte des explications techniques qu'on ne peut pas évaluer, et on ne sait pas diagnostiquer un chiffre aberrant.",
     "La <strong>balise</strong> est un fragment de code déposé sur le site, qui écoute ce qui s'y passe et envoie des messages à l'outil de mesure. Elle est généralement pilotée par un <strong>gestionnaire de balises</strong>, qui permet d'ajouter ou modifier des mesures sans repasser par un développeur — commodité réelle, et source de désordre quand plusieurs personnes y interviennent sans convention. L'<strong>événement</strong> est le message envoyé : un nom et un instant. C'est l'unité de base de toute mesure moderne, y compris de celles qui s'affichent ensuite sous forme de pages vues — une page vue n'est qu'un événement parmi d'autres.",
     "Les <strong>propriétés</strong> sont ce que l'événement transporte en plus de son nom : quel formulaire, sur quelle page, depuis quel appareil, avec quelle source. Ce sont elles qui rendront la segmentation possible. Un événement sans propriétés se compte mais ne s'analyse pas, et l'ajout rétroactif d'une propriété est impossible — les données déjà collectées ne la porteront jamais. C'est la décision la moins réversible du dispositif, et elle se prend au moment du plan de mesure. L'<strong>identifiant</strong>, enfin, est ce qui rattache plusieurs événements à la même personne : c'est le maillon le plus fragile de la chaîne, et le module 2 y consacrera une part importante.",
   ],
   "blocks": [
     {"type": "h3", "titre": "Une convention de nommage, écrite une fois pour toutes",
      "paras": [
        "Les noms d'événements sont ce qui reste quand tout le monde a changé de poste. Une convention prend dix minutes à écrire et évite des années de confusion ; trois règles suffisent.",
        "<strong>Une seule langue, un seul format</strong> — minuscules, tirets bas, sans dérogation : un outil contenant <code>demande_envoyee</code>, <code>DemandeEnvoyee</code> et <code>form_submit</code> contient trois événements distincts, dont deux sont des accidents. <strong>Objet puis action, au passé</strong> — <code>formulaire_envoye</code>, <code>article_lu</code>, <code>video_terminee</code> — ce qui range ensemble les événements d'un même objet par ordre alphabétique.",
        "<strong>Ce qui varie est une propriété, pas un nom.</strong> C'est la règle la plus enfreinte. On ne crée pas <code>demande_demo_envoyee</code> et <code>demande_devis_envoyee</code> : on crée <code>demande_envoyee</code> avec une propriété <code>type_demande</code>. Sans quoi le total, dont on a besoin neuf fois sur dix, devient impossible à obtenir sans additionner des événements dont on n'est jamais sûr d'avoir la liste complète.",
      ]},
     {"type": "exemple", "titre": "le même besoin, marqué deux fois",
      "paras": [
        "<em>Marquage naïf :</em> quatre événements — <code>clic_demo_accueil</code>, <code>clic_demo_tarifs</code>, <code>clic_demo_article</code>, <code>clic_demo_mobile</code>. Le besoin réel, combien de demandes au total et d'où elles viennent, exige de les additionner en espérant qu'aucun cinquième n'a été créé depuis par quelqu'un d'autre. Le jour où une page apparaît, le total se met à mentir en silence.",
        "<em>Marquage correct :</em> un seul événement <code>demande_envoyee</code> portant <code>page_origine</code>, <code>type_appareil</code>, <code>type_demande</code> et <code>source</code>. Le total est immédiat, chaque découpage disponible, et une nouvelle page ne demande aucune modification.",
        "Le symptôme qui distingue les deux est fiable et facile à repérer dans un dispositif existant : <strong>si vous vous surprenez à additionner régulièrement plusieurs événements, c'est qu'ils auraient dû n'en former qu'un, découpé par une propriété.</strong>",
      ]},
     {"type": "pitfall", "titre": "renommer ou redéfinir un événement en cours de route",
      "paras": [
        "Un jour, quelqu'un décide que <code>article_lu</code> se déclenchera désormais à 50 % de défilement au lieu de 25 %. L'intention est bonne, le changement n'est annoncé nulle part, et le résultat est une rupture invisible dans l'historique : la courbe fait un saut, que quelqu'un analysera six mois plus tard comme un phénomène réel. C'est l'une des façons les plus courantes de produire une conclusion entièrement fausse à partir de données techniquement exactes.",
        "La discipline tient en deux points. On ne redéfinit pas un événement : on en crée un nouveau et on arrête l'ancien à une date connue. Et tout changement de collecte s'inscrit dans un <strong>journal des modifications</strong> daté, consultable à côté des tableaux de bord. Ce journal est le premier réflexe devant une courbe qui fait un saut — avant toute hypothèse métier, on vérifie qu'on n'a pas simplement changé l'instrument.",
      ]},
   ]},

  {"titre": "Ce que vous n'aurez jamais : consentement, bloqueurs, données manquantes",
   "paras": [
     "Un dispositif de mesure web ne voit pas tout, et l'écart entre ce qui se passe et ce qui est enregistré est bien plus grand que ne le croient ceux qui commentent les chiffres. Le savoir change la façon de conclure ; l'ignorer conduit à décider sur des variations qui n'existent que dans la collecte.",
     "La première cause est le <strong>consentement</strong>. Le dépôt de traceurs à des fins de mesure d'audience non exemptée exige, en France et dans l'Union européenne, un consentement explicite. Le taux observé varie fortement selon le secteur, la présentation du bandeau et le type d'audience : sur un site grand public il est fréquemment compris entre 60 et 80 %, et il peut être nettement plus bas sur une audience technophile. Ce qui est refusé n'est pas mesuré, sauf recours à une solution exemptée dont la configuration est encadrée et le périmètre réduit.",
     "La deuxième est le <strong>blocage technique</strong> : bloqueurs de publicité, navigateurs limitant les traceurs tiers, extensions de confidentialité, réseaux d'entreprise filtrants. L'effet le plus pernicieux n'est pas la perte de volume mais sa <strong>répartition inégale</strong> — les audiences les plus techniques sont les plus sous-comptées, et comparer deux segments dont les taux de blocage diffèrent revient à comparer deux instruments. La troisième est l'<strong>attribution</strong>, à laquelle le module 2 consacre une section entière : retenez dès maintenant que ce n'est pas une imperfection qu'un meilleur outil corrigerait, mais une limite de principe.",
     "La conclusion pratique n'est pas de renoncer à mesurer — ce serait remplacer une donnée imparfaite par une intuition. Elle est de <strong>raisonner en tendances et en comparaisons plutôt qu'en valeurs absolues</strong>. Le nombre exact de visiteurs du mois est faux et le restera ; son évolution à collecte inchangée est fiable, et le rapport entre deux canaux mesurés de la même façon l'est aussi. C'est amplement suffisant pour la quasi-totalité des décisions.",
   ],
   "blocks": [
     {"type": "method", "titre": "travailler avec une collecte partielle en cinq étapes",
      "steps": [
        "<strong>Mesurez votre taux de consentement</strong> et suivez-le dans le temps ; la plupart des plateformes de consentement l'exposent. Sans ce chiffre, vous ignorez de combien votre analytics sous-estime la réalité.",
        "<strong>Recoupez avec une source non soumise au consentement</strong> : journaux du serveur, commandes ou demandes enregistrées en base, chiffres du CRM. Le rapport entre volume métier réel et volume mesuré donne un coefficient de sous-couverture utilisable.",
        "<strong>Traitez ce coefficient comme un ordre de grandeur</strong>, jamais comme une correction exacte. Il sert à dire « nous voyons environ deux tiers de l'activité », pas à multiplier chaque ligne par 1,5 — ce qui produirait une fausse précision plus dangereuse que l'incertitude assumée.",
        "<strong>Ne comparez jamais deux périodes séparées par un changement de collecte</strong> : nouveau bandeau, changement d'outil, refonte du marquage. Marquez la rupture sur vos graphiques et redémarrez la série.",
        "<strong>Écrivez la marge d'incertitude dans vos restitutions</strong>, en une phrase : « ces chiffres couvrent environ 70 % de l'activité réelle, de façon stable depuis janvier ; les évolutions sont fiables, les valeurs absolues sous-estimées. » Elle vous crédibilise bien davantage qu'un chiffre présenté comme exact et démenti trois mois plus tard.",
      ]},
     {"type": "pitfall", "titre": "la chute de trafic qui n'a jamais eu lieu",
      "paras": [
        "Scénario extrêmement fréquent. Une entreprise met son bandeau de consentement en conformité au mois de mai ; en juin, le trafic mesuré affiche moins 30 %. On soupçonne une pénalité de moteur de recherche, on envisage de couper des dépenses. Or le trafic réel n'a pas bougé d'un point : ce qui a changé est la part des visiteurs qui acceptent d'être mesurés. Le contrôle qui aurait évité trois semaines de panique tient en deux minutes — comparer l'évolution du nombre de commandes enregistrées en base, qui ne dépend d'aucun consentement.",
        "La règle à retenir : <strong>devant toute variation brutale, on vérifie l'instrument avant d'interpréter le phénomène.</strong> Journal des modifications, date de la dernière intervention technique, taux de consentement, source non soumise à consentement. Dans une majorité de cas l'explication est là, et l'analyse métier ne commence qu'après avoir écarté cette hypothèse.",
      ]},
   ]},
 ],

 "etude_cas": {
   "titre": "Répondre au directeur : 180 000 € d'acquisition, qu'est-ce que cela a rapporté ?",
   "html": """
<p>Reprenons la question de la mise en situation. Elle est légitime, elle est précise, et le dispositif en place ne permet pas d'y répondre. Voici comment on la traite en six semaines, sans changer d'outil.</p>
<p><strong>Étape 1 — reformuler la question en décision.</strong> Question posée au directeur : « selon la réponse, que ferez-vous ? ». Réponse obtenue : reconduire le budget global mais le redistribuer entre canaux, et arbitrer entre acquisition payante et production de contenu. Cela change tout. La question n'est pas « les 180 000 € ont-ils été rentables », qui appelle un chiffre unique et invérifiable, mais « quels canaux méritent quelle part du budget », qui appelle une comparaison. Une comparaison est infiniment plus atteignable qu'une valeur absolue — et c'est presque toujours le cas.</p>
<p><strong>Étape 2 — écrire l'indicateur.</strong> Il devient : <em>coût par demande qualifiée, par canal, sur 90 jours glissants, comparé au trimestre précédent</em>. Une demande qualifiée est définie avec le responsable commercial comme une demande à laquelle un commercial a donné suite après premier échange — définition qui existe déjà dans le CRM, ce qui évite d'en inventer une. Propriétaire : responsable acquisition.</p>
<p><strong>Étape 3 — descendre aux événements, et constater ce qui manque.</strong> L'indicateur exige trois choses : un événement <code>demande_envoyee</code> portant la source, la dépense par canal (disponible dans les régies) et le statut de qualification (disponible dans le CRM). Le diagnostic tombe vite : l'événement existe mais ne porte pas la source, et rien ne relie une demande du site à sa fiche CRM. Deux manques, corrigeables, aucun rétroactif.</p>
<p><strong>Étape 4 — corriger le marquage et la jonction.</strong> On ajoute à <code>demande_envoyee</code> les propriétés <code>source</code>, <code>campagne</code>, <code>type_appareil</code> et <code>page_origine</code>, et l'on transmet au CRM, à la création de la fiche, un identifiant technique de la demande et sa source. Deux semaines de travail, dont l'essentiel est la coordination avec l'équipe qui administre le CRM : c'est presque toujours la partie longue, et il faut la prévoir comme telle plutôt que la découvrir.</p>
<p><strong>Étape 5 — assumer ce que l'on ne saura pas.</strong> Les visiteurs ayant refusé le consentement ne porteront pas de source : environ un tiers des demandes arriveront sans canal identifié. La tentation est de les répartir au prorata des autres, ce qui produirait un tableau propre et faux. Le choix retenu est inverse — une ligne <em>« source inconnue »</em> affichée telle quelle, avec son volume : elle rend le tableau moins net et la conclusion plus solide.</p>
<p><strong>Étape 6 — restituer.</strong> Le tableau tient en huit lignes : par canal, la dépense, le nombre de demandes, le nombre de demandes qualifiées, le coût par demande qualifiée et la comparaison au trimestre précédent, sous une phrase de périmètre. Deux canaux payants affichent un coût par demande qualifiée de 310 € et de 1 240 € pour des budgets voisins : le second consomme 38 % du budget et produit 9 % des demandes qualifiées. Personne ne le savait — non parce que c'était difficile à voir, mais parce que le chiffre n'avait jamais existé. Constat plus inattendu : la recherche organique, qui ne consomme aucun budget d'acquisition, produit 41 % des demandes qualifiées, ce qui déplace la discussion vers le coût de production du contenu, absent des 180 000 €.</p>
<p><strong>La décision prise.</strong> Le canal à 1 240 € est réduit de deux tiers et non arrêté : on conserve un budget d'observation, parce qu'un canal évalué sur un seul trimestre et sur une définition de qualification récente mérite confirmation. Ce n'est pas de la prudence excessive, c'est la conséquence directe de savoir sur quelle qualité de données on décide.</p>
<p><strong>La leçon transposable.</strong> La question initiale n'était pas mesurable et il ne fallait pas essayer d'y répondre telle quelle. Ramenée à la décision qu'elle préparait, elle est devenue une comparaison entre canaux, atteignable en six semaines avec les outils en place. C'est le mouvement fondamental de ce module : <strong>on ne mesure pas une question, on mesure une décision</strong>. Et l'on gagne plus de crédibilité à afficher une ligne « source inconnue » qu'à produire un tableau parfaitement réparti que le premier recoupement démentira.</p>
"""},

 "checklist": {
   "titre": "Checklist — cadrer un dispositif de mesure",
   "items": [
     "Chaque indicateur affiché a passé le test : quelle décision change selon sa valeur ?",
     "Les indicateurs de cadrage qui ne déclenchent rien sont au maximum deux ou trois, et en haut",
     "Chaque indicateur est écrit avec sa mesure, son segment, sa période, sa référence et son propriétaire",
     "Le numérateur et le dénominateur de chaque taux sont écrits explicitement",
     "Aucun taux n'est affiché sans son numérateur à côté",
     "Le tableau de bord comporte au moins un indicateur avancé, et pas seulement des résultats",
     "Le lien entre chaque indicateur avancé et le résultat a été vérifié au moins une fois",
     "Un plan de mesure écrit relie chaque question métier à ses événements",
     "Les questions qui ne préparent aucune décision ont été écartées ou transformées explicitement",
     "Le site compte entre quinze et vingt-cinq événements, pas davantage",
     "Une convention de nommage est écrite : une langue, un format, objet puis action au passé",
     "Ce qui varie est une propriété et non un nom d'événement distinct",
     "Chaque événement porte les propriétés nécessaires à la segmentation prévue",
     "Un journal des modifications daté consigne tout changement de collecte",
     "Aucun événement existant n'a été redéfini : les changements créent un nouvel événement",
     "Le taux de consentement est mesuré et suivi dans le temps",
     "Une source non soumise au consentement permet de recouper les volumes",
     "Les ruptures de collecte sont marquées sur les graphiques et interdisent la comparaison",
     "Chaque restitution comporte une phrase sur le périmètre et l'incertitude",
     "Le plan de mesure porte une date de prochaine relecture",
   ]},

 "glossaire": [
   ("Test de la décision", "Question à poser à tout indicateur avant de l'afficher : quelle décision prendrai-je différemment selon sa valeur ? Élimine la moitié à deux tiers d'un tableau de bord courant."),
   ("Indicateur avancé", "Mesure qui précède le résultat et le prédit partiellement (demandes entrantes, taux de complétion). Pilotable, parce qu'il bouge avant le chiffre d'affaires."),
   ("Indicateur de résultat", "Mesure de l'issue (chiffre d'affaires, clients signés). Sert à évaluer, pas à piloter : quand on le découvre, on ne peut plus agir dessus."),
   ("Plan de mesure", "Document reliant chaque question métier à la décision qu'elle prépare, à son indicateur, aux événements à collecter et à leurs propriétés. Se relit deux fois par an."),
   ("Balise", "Fragment de code déposé sur le site, qui observe ce qui s'y passe et envoie des messages à l'outil de mesure."),
   ("Gestionnaire de balises", "Outil permettant d'ajouter ou modifier des mesures sans intervention de développement. Commode, et source de désordre sans convention partagée."),
   ("Événement", "Unité de base de la mesure : un nom et un instant. Une page vue est un événement parmi d'autres."),
   ("Propriété", "Information transportée par un événement (page, appareil, source, type). Rend la segmentation possible ; ne peut jamais être ajoutée rétroactivement."),
   ("Identifiant", "Ce qui rattache plusieurs événements à la même personne. Maillon le plus fragile de la chaîne, traité au module 2."),
   ("Consentement", "Accord explicite du visiteur au dépôt de traceurs non exemptés. Ce qui est refusé n'est pas mesuré : le taux de consentement conditionne la couverture réelle."),
   ("Coefficient de sous-couverture", "Rapport entre un volume métier réel (commandes en base, fiches CRM) et le volume mesuré par l'analytics. Ordre de grandeur, jamais facteur de correction ligne à ligne."),
   ("Journal des modifications", "Registre daté de tout changement de collecte. Premier réflexe devant une courbe qui fait un saut, avant toute hypothèse métier."),
   ("Rupture de collecte", "Changement d'outil, de marquage ou de bandeau qui rend incomparables les périodes situées de part et d'autre."),
 ],

 "retenir": [
   "Compter n'est pas mesurer : un outil compte tout seul, mesurer suppose d'avoir décidé à quoi cela sert.",
   "Le test de la décision est le seul filtre qui vaille : si aucune décision ne change, l'indicateur est décoratif.",
   "Deux ou trois indicateurs de cadrage échappent au test, pas davantage, et ils ne se commentent pas.",
   "Un indicateur exploitable tient en une ligne et contient cinq éléments : mesure, segment, période, référence, propriétaire.",
   "La plupart des disputes de chiffres sont des disputes de définitions : c'est le document, pas l'outil, qui fait référence.",
   "N'affichez jamais un taux sans son numérateur : un taux monte aussi quand le dénominateur baisse.",
   "Un dispositif sans indicateur avancé ne permet que de constater, jamais de piloter.",
   "Un indicateur avancé dont le lien avec le résultat n'a jamais été vérifié est une croyance, pas une mesure.",
   "Le plan de mesure se lit de la question métier vers les événements, et se construit dans cet ordre, jamais l'inverse.",
   "Quinze à vingt-cinq événements suffisent : la contrainte de volume est ce qui garde le dispositif lisible dans deux ans.",
   "Ce qui varie est une propriété, pas un nom d'événement : si vous additionnez souvent plusieurs événements, ils auraient dû n'en faire qu'un.",
   "Une propriété ne s'ajoute jamais rétroactivement : c'est la décision la moins réversible du dispositif.",
   "On ne redéfinit pas un événement, on en crée un nouveau et on arrête l'ancien à une date connue.",
   "Devant une variation brutale, on vérifie l'instrument avant d'interpréter le phénomène.",
   "Les valeurs absolues sont fausses et le resteront ; les tendances et les comparaisons à collecte inchangée sont fiables, et suffisent à décider.",
   "Une ligne « source inconnue » assumée vaut mieux qu'une répartition inventée : la fausse précision se paie au premier recoupement.",
   "Une question qui ne prépare aucune décision est de la curiosité — mais elle cache souvent une bonne question, qu'il faut chercher.",
 ],

 "exercices": [
  {"titre": "Passer six indicateurs au test de la décision", "niveau": "Débutant",
   "enonce": [
     "Une direction marketing vous transmet les six indicateurs qu'elle souhaite voir chaque mois. Pour chacun, dites s'il passe le test de la décision, s'il faut le transformer, ou s'il faut l'écarter — en justifiant par la décision concernée ou par son absence.",
     "1. Nombre total de visiteurs du site. — 2. Taux de rebond global. — 3. Nombre de demandes de démonstration envoyées, par canal. — 4. Position moyenne du site dans les résultats de recherche. — 5. Nombre d'abonnés à la newsletter. — 6. Chiffre d'affaires du mois.",
   ],
   "corrige": """
<p><strong>1. Nombre total de visiteurs — à écarter, ou à transformer.</strong> Aucune décision n'en dépend : on ne fait rien de différent selon qu'il vaut 34 000 ou 37 000, et il monte pour de mauvaises raisons comme pour de bonnes. <em>Transformation utile :</em> nombre de visiteurs sur les pages à intention commerciale (tarifs, contact, produit), qui est un indicateur avancé du volume de demandes et déclenche une vérification si la tendance s'inverse.</p>
<p><strong>2. Taux de rebond global — à écarter sans transformation évidente.</strong> C'est le cas le plus intéressant de la liste, parce qu'il est le plus demandé. Le taux de rebond agrège des situations opposées : un visiteur qui arrive sur une page d'aide, trouve sa réponse et repart est un rebond réussi ; un visiteur qui arrive sur la page tarifs et repart est un échec. Additionner les deux produit un chiffre dont la hausse et la baisse sont également ininterprétables. Il peut redevenir utile sur un périmètre restreint et avec une intention connue — le taux de sortie de la page de formulaire, par exemple — mais ce n'est alors plus le même indicateur.</p>
<p><strong>3. Demandes de démonstration par canal — passe, et c'est le meilleur de la liste.</strong> Décision nommée : redistribuer le budget entre canaux. Il faut cependant compléter sa définition avec les cinq éléments, et surtout trancher ce qu'est une « demande » — envoyée, ou qualifiée ? Sans ce point, on comparera des canaux qui apportent du volume avec des canaux qui apportent des clients, ce qui conduit exactement à la mauvaise décision.</p>
<p><strong>4. Position moyenne dans les résultats de recherche — à transformer.</strong> La moyenne est ici particulièrement trompeuse : elle mélange des requêtes stratégiques et des requêtes marginales, et elle peut se dégrader parce qu'on s'est mis à être visible sur davantage de requêtes, ce qui est un progrès. <em>Transformation :</em> positions sur une liste nommée de requêtes prioritaires, suivies individuellement. Décision associée : réviser un contenu identifié. La formation SEO de ce catalogue traite ce point en détail.</p>
<p><strong>5. Abonnés à la newsletter — à transformer.</strong> Le nombre cumulé ne descend jamais et ne déclenche rien ; il donne l'illusion d'une progression permanente. <em>Transformations :</em> nouveaux abonnés du mois, taux de désabonnement, et surtout part des demandes commerciales dont le parcours contient un abonnement. Cette dernière est la seule qui dise si la newsletter sert à autre chose qu'à exister.</p>
<p><strong>6. Chiffre d'affaires du mois — passe au titre du cadrage, sans être un indicateur de pilotage.</strong> Il ne déclenche aucune action en lui-même, puisqu'il décrit un passé fermé, mais il conditionne la lecture de tout le reste. Il appartient aux deux ou trois exceptions admises, et sa place est en haut du tableau, sans commentaire mensuel.</p>
<p><strong>Ce que révèle l'ensemble de la liste.</strong> Un seul des six indicateurs demandés est directement exploitable. Ce n'est pas une critique de la direction marketing : c'est le résultat normal d'une liste construite à partir de ce que les outils affichent par défaut. Point de méthode pour la restitution — ne présentez jamais ce diagnostic comme un désaveu. Présentez pour chaque indicateur écarté sa version transformée et la décision qu'elle permet. Une transformation est acceptée, un refus est contesté ; et sur les six, cinq admettent une transformation qui répond mieux à l'intention initiale que la demande d'origine.</p>
"""},

  {"titre": "Construire le plan de mesure d'un site de formation", "niveau": "Intermédiaire",
   "enonce": [
     "Une école propose des formations professionnelles. Son site présente un catalogue, des fiches de formation, un formulaire de demande d'information et un formulaire d'inscription en ligne. Le directeur veut savoir quelles formations méritent d'être maintenues au catalogue et sur lesquelles investir en communication.",
     "Construisez le plan de mesure : questions retenues, indicateurs correspondants, événements et propriétés. Indiquez ce que vous refusez de mesurer et pourquoi, et signalez la question à laquelle votre plan ne pourra pas répondre.",
   ],
   "corrige": """
<p><strong>D'abord, remonter à la décision.</strong> La demande contient deux décisions distinctes qu'il faut séparer, car elles n'appellent pas les mêmes mesures : <em>maintenir ou retirer une formation du catalogue</em>, et <em>où investir en communication</em>. La première se tranche sur des inscriptions et une rentabilité, la seconde sur des coûts d'acquisition par formation. Traiter les deux avec un seul indicateur est l'erreur qui rend la plupart des plans de mesure inutilisables.</p>
<p><strong>Les quatre questions retenues.</strong></p>
<p><em>Q1 — Quelles formations génèrent de l'intérêt sans générer d'inscriptions ?</em> Décision : retravailler la fiche et le prix, ou retirer la formation. Indicateur : par formation, taux de passage de la consultation de fiche à la demande d'information, puis de la demande à l'inscription, sur 90 jours glissants, comparé à la médiane du catalogue. La médiane comme référence est ici bien meilleure qu'un seuil absolu, parce qu'elle absorbe la saisonnalité commune à toutes les formations.</p>
<p><em>Q2 — Quelles formations sont découvertes sans être cherchées ?</em> Décision : investir en communication sur celles qui convertissent bien mais reçoivent peu de visites. Indicateur : par formation, volume de fiches vues croisé avec le taux d'inscription. Une formation qui convertit à 8 % avec 200 visites vaut mieux qu'une qui convertit à 1 % avec 4 000.</p>
<p><em>Q3 — Où les candidats abandonnent-ils l'inscription en ligne ?</em> Décision : chantier de simplification du formulaire, ou non. Indicateur : taux de complétion et dernier champ atteint avant abandon, par appareil.</p>
<p><em>Q4 — Quels canaux amènent des inscrits, et à quel coût ?</em> Décision : allocation du budget de communication. Indicateur : coût par inscription, par canal et par formation quand le volume le permet.</p>
<p><strong>Les événements, réduits au nécessaire.</strong> <code>fiche_formation_vue</code> (propriétés : <code>formation_id</code>, <code>formation_famille</code>, <code>source</code>, <code>type_appareil</code>) — <code>demande_info_envoyee</code> (mêmes propriétés) — <code>inscription_debut</code> — <code>inscription_champ_abandon</code> (propriété <code>champ</code>) — <code>inscription_terminee</code> (mêmes propriétés, plus <code>montant</code>).</p>
<p>Cinq événements pour quatre questions : c'est le signe d'un plan bien construit, les événements étant partagés entre les indicateurs. <code>formation_id</code> est la propriété qui fait tout le travail ; sans elle, aucune des quatre questions n'est traitable. C'est précisément elle qu'un marquage naïf oublie en créant un événement par formation, ce qui aurait donné soixante événements et un dispositif ingérable.</p>
<p><strong>Ce que je refuse de mesurer, et comment le dire.</strong> Le temps passé sur la fiche sera demandé, presque à coup sûr. À écarter : sa hausse peut signifier de l'intérêt comme de la confusion tarifaire, aucune décision ne s'y appuie, et sa mesure fiable exige un marquage disproportionné. Formulation à employer : « nous ne le collectons pas parce qu'aucune décision n'en dépend, et l'indicateur Q1 répond mieux à ce que vous cherchez ». À écarter également, le suivi individuel nominatif des visiteurs : il n'apporte rien à ces quatre décisions et alourdit la charge de conformité.</p>
<p><strong>La question à laquelle ce plan ne répondra pas, et qu'il faut annoncer d'emblée.</strong> Le plan mesure le parcours en ligne. Il ne dira pas <em>pourquoi</em> une formation ne se vend pas — prix, format, concurrence, réputation, calendrier. Il localisera l'endroit du décrochage, ce qui est déjà beaucoup, mais il faudra trois entretiens avec des candidats non inscrits pour en connaître la cause. L'annoncer au moment de présenter le plan, et non lorsque le directeur le découvrira, fait toute la différence entre un dispositif jugé décevant et un dispositif jugé honnête : un plan de mesure qui prétend tout expliquer perd sa crédibilité au premier constat qu'il ne sait pas commenter.</p>
"""},

  {"titre": "Diagnostiquer une chute de 30 % du trafic mesuré", "niveau": "Avancé",
   "enonce": [
     "Le 4 juin, votre tableau de bord affiche une chute de 31 % des sessions sur les quinze derniers jours par rapport aux quinze précédents. La direction demande un plan d'action pour la fin de semaine. Le responsable acquisition penche pour une pénalité de moteur de recherche et propose de basculer en urgence du budget vers la publicité payante.",
     "Décrivez votre démarche de diagnostic, dans l'ordre, en indiquant ce que chaque vérification permet d'exclure. Dites ce que vous répondez à la proposition de basculer le budget, et ce que vous mettez en place pour que ce diagnostic soit plus rapide la prochaine fois.",
   ],
   "corrige": """
<p><strong>Le réflexe à tenir avant toute chose : on vérifie l'instrument avant d'interpréter le phénomène.</strong> L'ordre des vérifications n'est pas indifférent — il va du moins coûteux et du plus probable vers le plus coûteux et le moins probable.</p>
<p><strong>Vérification 1 — le journal des modifications.</strong> Y a-t-il eu, dans la fenêtre concernée, un déploiement, une refonte, un changement de bandeau de consentement, une migration, une modification du gestionnaire de balises ? C'est la vérification la moins chère et celle qui explique le plus souvent. Elle exclut ou confirme la rupture de collecte. Si l'entreprise n'a pas de journal des modifications, c'est déjà la première conclusion de l'exercice.</p>
<p><strong>Vérification 2 — le recoupement avec une source non soumise au consentement.</strong> Commandes ou demandes enregistrées en base, chiffre d'affaires, appels reçus, fiches créées dans le CRM. C'est la vérification décisive, et elle prend dix minutes. <em>Si l'activité réelle est stable et que le trafic mesuré chute, le phénomène est dans l'instrument et le débat est clos.</em> <em>Si l'activité réelle chute aussi, le phénomène est réel</em> et le diagnostic continue. Aucune autre vérification ne tranche aussi nettement, et c'est pourquoi ce recoupement mérite d'exister en permanence dans le tableau de bord plutôt que d'être bricolé en situation de crise.</p>
<p><strong>Vérification 3 — la décomposition.</strong> La chute est-elle uniforme ou concentrée ? Par canal, par appareil, par type de page, par pays. Une chute uniforme sur tous les canaux à la fois n'a presque jamais de cause métier : c'est la signature d'un problème de collecte, car aucun phénomène réel ne frappe simultanément l'organique, le direct et le payant dans les mêmes proportions. Une chute concentrée oriente au contraire vers une cause réelle et vers l'endroit précis où chercher.</p>
<p><strong>Vérification 4 — seulement maintenant, les sources externes.</strong> Console de recherche pour les impressions et les positions, journaux du serveur, statut des campagnes payantes, disponibilité du site sur la période. La console de recherche est particulièrement utile ici : elle mesure impressions et clics indépendamment du consentement, ce qui en fait un second recoupement pour la part organique.</p>
<p><strong>Ce que je réponds sur le basculement de budget.</strong> Non, et il faut savoir le dire sans passer pour un frein. L'argument n'est pas méthodologique — « il faut d'abord analyser » ne convainc personne dans une réunion tendue — il est factuel et chiffré : « basculer le budget coûte X euros, met trois semaines à produire un effet, et si la chute vient de la collecte, nous aurons dépensé cette somme pour corriger un problème qui n'existe pas. Les deux vérifications qui tranchent prennent une demi-journée. Nous décidons vendredi avec la réponse. » Vous n'opposez pas une méthode à une urgence : vous opposez une demi-journée à trois semaines et à un budget. C'est un arbitrage que n'importe quel dirigeant accepte.</p>
<p><strong>Le cas où le responsable acquisition a raison.</strong> Ne construisez pas le diagnostic pour le contredire. Si les vérifications 2 et 3 confirment une chute réelle concentrée sur le canal organique, avec une baisse d'impressions dans la console de recherche, sa lecture est la bonne et il faut le dire aussi clairement que le contraire. La démarche ne sert pas à défendre une position, elle sert à savoir laquelle des deux est vraie avant de dépenser.</p>
<p><strong>Ce que je mets en place pour la prochaine fois — la vraie livraison de l'exercice.</strong></p>
<p><em>Un journal des modifications</em> partagé entre équipes techniques et marketing, consultable à côté des tableaux de bord : une ligne par changement, date, nature, auteur. C'est la mesure au meilleur rendement de toute la liste.</p>
<p><em>Un indicateur de recoupement affiché en permanence</em> : la courbe du volume métier réel posée à côté de celle du trafic mesuré. Quand les deux divergent, le problème est dans l'instrument ; quand elles bougent ensemble, il est réel. Ce seul graphique aurait rendu la réunion inutile.</p>
<p><em>Le suivi du taux de consentement</em> dans le temps, au même endroit : sa variation explique une part importante des mouvements inexpliqués, et il n'est presque jamais suivi.</p>
<p><em>Des repères visuels sur les graphiques</em> aux dates de rupture de collecte, avec la règle explicite qu'aucune comparaison ne traverse un repère.</p>
<p><strong>Le principe général.</strong> Un dispositif de mesure mature ne se reconnaît pas au nombre d'indicateurs qu'il affiche, mais à sa capacité à distinguer rapidement un problème de mesure d'un problème réel. Cette capacité ne s'improvise pas en situation de crise : elle se construit à froid, et elle tient en trois éléments — un journal, un recoupement permanent et le suivi du consentement.</p>
"""},
 ],

 "ressources": [
   "<strong>Le guide de la CNIL sur les cookies et autres traceurs</strong> — la référence française sur ce qui exige un consentement et sur les conditions d'exemption pour la mesure d'audience. À lire avant toute discussion sur le bandeau de consentement, y compris avec un prestataire.",
   "<strong>« Lean Analytics », Alistair Croll et Benjamin Yoskovitz</strong> — sur l'idée qu'un indicateur ne vaut que par la décision qu'il déclenche, et sur la notion de mesure unique qui compte à un instant donné. Le meilleur appui pour défendre un plan de mesure court.",
   "<strong>Les modules 2 et 3 de cette formation</strong> — le module 2 traite les sources, l'attribution et les écarts entre outils ; le module 3, l'analyse proprement dite. Ne les abordez pas avant d'avoir un plan de mesure écrit : sans lui, ils n'ont rien sur quoi s'appliquer.",
   "<strong>La formation CRM et relation client de ce catalogue, module 3</strong> — sur la construction de tableaux de bord qui déclenchent des décisions, du côté commercial cette fois. Les deux logiques se rejoignent, et la jonction site-CRM décrite dans l'étude de cas y trouve son prolongement naturel.",
 ],
}

QUIZ = {
 "analytics-mesure/module-1": {
  "module_id": "formation-analytics-mesure-module-1",
  "version": "2.0", "last_verified": "2026-09-03",
  "questions": [
   {"id":"q1","question":"Quel test permet de décider si un indicateur mérite d'être affiché ?",
    "choices":[{"key":"a","text":"Est-il disponible sans configuration supplémentaire ?"},
               {"key":"b","text":"Quelle décision prendrai-je différemment selon sa valeur ?"},
               {"key":"c","text":"La direction l'a-t-elle demandé explicitement ?"}],
    "correct_answer":"b","feedback":"Appliqué honnêtement, ce test élimine la moitié à deux tiers d'un tableau de bord courant. Seuls deux ou trois indicateurs de cadrage y échappent."},
   {"id":"q2","question":"Le taux de conversion passe de 2,1 % à 3,4 % après l'arrêt d'une campagne payante. Que s'est-il passé ?",
    "choices":[{"key":"a","text":"Le site convertit mieux : le parcours s'est amélioré"},
               {"key":"b","text":"Du trafic peu qualifié a quitté le dénominateur ; le nombre de conversions a probablement baissé"},
               {"key":"c","text":"Les deux valeurs ne sont pas comparables car la période a changé"}],
    "correct_answer":"b","feedback":"Un taux monte aussi quand son dénominateur diminue. D'où la règle : ne jamais afficher un taux sans afficher son numérateur à côté."},
   {"id":"q3","question":"Vous devez suivre les demandes de démonstration et les demandes de devis. Comment les marquer ?",
    "choices":[{"key":"a","text":"Deux événements distincts, un par type de demande"},
               {"key":"b","text":"Un événement demande_envoyee avec une propriété type_demande"},
               {"key":"c","text":"Un événement par page contenant un formulaire"}],
    "correct_answer":"b","feedback":"Ce qui varie est une propriété, pas un nom. Sinon le total, dont on a besoin neuf fois sur dix, exige d'additionner des événements dont on n'est jamais sûr d'avoir la liste complète."},
   {"id":"q4","question":"Quelle décision d'un plan de mesure est la moins réversible ?",
    "choices":[{"key":"a","text":"Le choix des propriétés portées par chaque événement"},
               {"key":"b","text":"Le choix de l'outil d'analytics"},
               {"key":"c","text":"Le choix de la référence de comparaison des indicateurs"}],
    "correct_answer":"a","feedback":"Une propriété ne peut pas être ajoutée rétroactivement : les données déjà collectées ne la porteront jamais. Outil et référence, eux, se changent."},
   {"id":"q5","question":"Le trafic mesuré chute de 30 % le mois suivant la refonte du bandeau de consentement. Par quoi commencer ?",
    "choices":[{"key":"a","text":"Vérifier les positions dans les moteurs de recherche"},
               {"key":"b","text":"Comparer l'évolution d'un volume métier non soumis au consentement, commandes ou demandes en base"},
               {"key":"c","text":"Basculer du budget vers la publicité payante pour compenser"}],
    "correct_answer":"b","feedback":"On vérifie l'instrument avant d'interpréter le phénomène. Si l'activité réelle est stable, la chute est dans la collecte et le débat est clos en dix minutes."},
   {"id":"q6","question":"Un tiers des demandes arrivent sans source identifiable. Que faire dans le tableau de restitution ?",
    "choices":[{"key":"a","text":"Les répartir au prorata des canaux connus pour obtenir un tableau complet"},
               {"key":"b","text":"Les exclure du tableau et n'afficher que les demandes attribuées"},
               {"key":"c","text":"Afficher une ligne « source inconnue » avec son volume réel"}],
    "correct_answer":"c","feedback":"La répartition au prorata produit un tableau propre et faux. Une incertitude assumée résiste au premier recoupement ; une fausse précision, non."},
  ]},
}

for k, m in M.items():
    w, full = build(k, m)
    print(f"{k:30s} cours: {w} mots | page: {full} mots")
for k, q in QUIZ.items():
    p = os.path.join(OUT, k, "quiz.json")
    os.makedirs(os.path.dirname(p), exist_ok=True)
    json.dump(q, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    open(p, "a", encoding="utf-8").write("\n")
    print(f"{k}: quiz {len(q['questions'])} questions")
