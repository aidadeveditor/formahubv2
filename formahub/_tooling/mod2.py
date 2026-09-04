#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Formahub — source du module 2 de la formation « Analytics et mesure de la performance ».

Regenerer la page et le quiz :
    python3 mod2.py                       # ecrit dans ../formations/
    FH_OUT=/tmp/essai python3 mod2.py     # ecrit ailleurs

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

M["analytics-mesure/module-2"] = {
 "formation": FORM,
 "titre": "Lire une audience : sessions, sources et attribution",
 "num": 2, "total": 4, "duree": "60 min", "niveau": "Intermédiaire",
 "module_id": "formation-analytics-mesure-module-2",
 "situation": [
   "Jeudi 14 avril, revue mensuelle d'acquisition. Trois chiffres sont posés sur la table pour le même mois et la même campagne. La régie publicitaire annonce 340 conversions. L'outil d'analytics en compte 190. Le CRM, lui, recense 120 demandes réellement arrivées chez les commerciaux.",
   "La réunion s'enlise sur la question de savoir lequel est le bon, chacun défendant l'outil qu'il administre. Elle se conclut sans décision, sur l'idée qu'il faudrait « fiabiliser les données » — formule qui ne veut rien dire et qui garantit qu'on se retrouvera au même point le mois suivant.",
   "Les trois chiffres sont exacts. Ils comptent trois choses différentes, avec trois définitions différentes et trois fenêtres différentes, et personne dans la salle ne sait lesquelles. C'est la situation la plus courante de tout le métier, et elle ne se résout pas en changeant d'outil.",
   "Ce module donne de quoi la traiter : ce qu'un outil d'analytics compte réellement, ce que valent les indicateurs d'engagement qu'il affiche, comment nommer ses campagnes pour pouvoir les comparer, ce qu'est l'attribution et pourquoi aucun modèle n'a raison. L'étude de cas reprendra les trois chiffres de la réunion et les réconciliera — sans les rendre égaux.",
 ],
 "objectifs": [
   "Expliquer ce que comptent réellement une session, un utilisateur et un événement",
   "Écarter les indicateurs d'engagement trompeurs et leur substituer des mesures d'intention",
   "Poser une nomenclature de campagne tenable et repérer les liens qui la cassent",
   "Comparer les modèles d'attribution et choisir celui qui correspond à la décision à prendre",
   "Conduire un rapprochement entre deux outils qui affichent des chiffres différents",
   "Présenter un écart entre outils comme un écart expliqué plutôt que comme une anomalie",
 ],
 "sections": [
  {"titre": "Ce qu'un outil d'analytics compte vraiment",
   "paras": [
     "Les mots employés par les outils de mesure sont trompeurs parce qu'ils empruntent au vocabulaire courant. « Utilisateur » évoque une personne, « session » évoque une visite. Aucun des deux ne désigne ce que le mot suggère, et l'écart explique une part importante des mauvaises lectures.",
     "Une <strong>session</strong> est une suite d'événements provenant d'un même navigateur, close par une période d'inactivité — trente minutes dans la plupart des outils. Elle se termine donc au bout de trente minutes sans activité, même si la personne revient ensuite, et une même visite humaine interrompue par un déjeuner produit deux sessions. Selon les outils, elle peut aussi se clore à minuit ou lors d'un changement de source. La session n'est pas une unité naturelle : c'est une convention de découpage, et il faut savoir laquelle votre outil applique.",
     "Un <strong>utilisateur</strong>, sauf configuration particulière, est un identifiant stocké dans le navigateur. Une même personne consultant votre site depuis son téléphone puis son ordinateur compte pour deux utilisateurs. La même personne qui vide ses cookies, navigue en mode privé, ou dont le navigateur limite la durée de vie des traceurs, compte pour deux, trois ou dix. Le nombre d'utilisateurs uniques surestime donc systématiquement le nombre de personnes, dans un rapport qui va couramment de 1,3 à 2 selon les audiences et les appareils.",
     "Le seul remède est l'<strong>identifiant de compte</strong> : lorsqu'une personne se connecte, on transmet à l'outil un identifiant stable, non nominatif, qui recolle ses appareils. Il ne concerne que les visiteurs connectés, ce qui exclut le haut du parcours, mais il change la nature de tout ce qui se mesure en aval — rétention, cycles longs, valeur par client. Si votre site a une zone connectée et que cet identifiant n'est pas transmis, c'est probablement le chantier au meilleur rendement de votre dispositif.",
   ],
   "blocks": [
     {"type": "exemple", "titre": "un parcours humain, tel que l'outil le voit",
      "paras": [
        "Une responsable achats découvre votre site un mardi soir sur son téléphone via une publicité, lit deux pages, repart. Le jeudi, au bureau, elle cherche votre nom dans un moteur de recherche, consulte la page tarifs, part en réunion, revient une heure plus tard et envoie une demande de démonstration.",
        "Une personne, trois visites au sens humain. L'outil enregistre <strong>deux utilisateurs</strong> (téléphone et ordinateur) et <strong>trois sessions</strong> : la publicitaire du mardi, l'organique du jeudi matin, et une troisième session du jeudi après-midi ouverte par l'inactivité — dont la source sera, selon les outils, « direct » ou l'organique reconduite.",
        "Aucune de ces valeurs n'est fausse, et aucune ne dit ce qu'on croit qu'elle dit. Retenez surtout ceci : la demande sera attribuée à l'organique ou au direct, jamais à la publicité qui a fait connaître l'entreprise. C'est le problème de l'attribution, traité en section 4, et il est ici entièrement contenu dans un parcours de trois jours parfaitement banal.",
      ]},
     {"type": "pitfall", "titre": "dire « personnes » quand on compte des navigateurs",
      "paras": [
        "Le glissement de vocabulaire est minuscule et ses conséquences ne le sont pas. Annoncer « 40 000 personnes ont visité le site » quand l'outil affiche 40 000 utilisateurs, c'est surestimer l'audience d'un facteur inconnu et fournir une base fausse à tout calcul de couverture ou de coût par personne touchée.",
        "La discipline coûte un mot : dites « utilisateurs », ou « navigateurs », ou « visiteurs mesurés ». Le jour où quelqu'un rapproche ce chiffre du nombre de clients réels et trouve un écart de facteur trois, c'est vous qui serez interrogée — et la seule bonne réponse est d'avoir employé le mot juste depuis le début.",
      ]},
   ]},

  {"titre": "Les indicateurs d'engagement et leur sens réel",
   "paras": [
     "Les outils affichent en évidence trois indicateurs d'engagement — taux de rebond, pages par session, durée moyenne — dont aucun ne supporte l'examen. Le module 1 a écarté la durée moyenne ; il faut aller plus loin, parce que ces trois-là occupent une place que devraient tenir des mesures d'intention.",
     "Le <strong>taux de rebond</strong> a d'abord désigné la part des sessions à une seule interaction. Les outils récents ont substitué à cette définition la notion de <strong>session engagée</strong> — une session dépassant une certaine durée, comptant plusieurs pages, ou contenant une conversion — et affichent l'inverse. Les deux chiffres portent le même nom sur les captures d'écran et n'ont pas la même définition : c'est la première chose à vérifier avant de comparer une valeur à une autre trouvée ailleurs, et une source d'erreur permanente dans les comparaisons sectorielles.",
     "Les <strong>pages par session</strong> montent quand la navigation est mauvaise. Un visiteur qui trouve immédiatement l'information consulte une page ; celui qui erre en consulte six. Sur un site de contenu financé par la publicité, l'indicateur a un sens économique direct ; sur un site de service ou d'aide, il mesure surtout la difficulté à trouver, et sa hausse est une mauvaise nouvelle.",
     "La <strong>durée</strong>, enfin, se calcule par différence entre horodatages d'événements. La dernière page d'une session n'ayant pas d'événement suivant, elle compte pour zéro dans la plupart des configurations classiques. Un article lu intégralement puis quitté vaut donc zéro seconde. Les outils fondés sur les événements corrigent partiellement ce défaut, à condition qu'on l'ait configuré — ce qui est rarement le cas par défaut.",
     "Ce qu'il faut mettre à la place tient en une idée : mesurer l'<strong>intention</strong> plutôt que l'agitation. Atteinte d'une page à valeur commerciale, profondeur de lecture réelle sur un article, taux de retour à sept jours, complétion d'un formulaire commencé. Ces quatre mesures se construisent avec les événements du plan de mesure du module 1 et passent toutes le test de la décision.",
   ],
   "blocks": [
     {"type": "method", "titre": "remplacer trois indicateurs d'engagement par trois mesures d'intention",
      "steps": [
        "<strong>Nommez les pages à valeur commerciale</strong> — tarifs, contact, demande, fiche produit — et mesurez la part des sessions qui en atteignent au moins une. C'est le meilleur substitut au taux de rebond, et il se compare d'un mois sur l'autre sans ambiguïté de définition.",
        "<strong>Remplacez la durée par une profondeur de lecture</strong> : un événement déclenché à un seuil de défilement défini une fois pour toutes, sur les pages où la lecture est l'objectif. Fixez le seuil, écrivez-le, et ne le changez plus — le module 1 a montré ce que coûte une redéfinition silencieuse.",
        "<strong>Ajoutez une mesure de retour</strong> : part des visiteurs revenus dans les sept jours. C'est le seul des trois qui dise quelque chose sur la valeur perçue, et il est presque toujours absent des tableaux de bord.",
        "<strong>Conservez les anciens indicateurs trois mois en parallèle</strong>, puis retirez-les explicitement des rapports. Sans retrait annoncé, ils survivent dans les habitudes et continuent d'alimenter les commentaires de réunion.",
      ]},
     {"type": "pitfall", "titre": "comparer son taux de rebond à une moyenne sectorielle",
      "paras": [
        "L'exercice est irrésistible et il n'a aucune valeur. La moyenne trouvée en ligne agrège des sites de nature différente, mesurés par des outils différents, avec des définitions différentes du rebond et des taux de consentement différents. Se situer par rapport à elle revient à comparer sa taille à la moyenne d'une population dont on ignore l'unité de mesure.",
        "La seule comparaison qui a du sens est celle du site avec lui-même, à définition et à collecte constantes. Si une référence externe est réellement exigée, la formuler en écart relatif entre deux périodes plutôt qu'en valeur absolue est la seule forme défendable.",
      ]},
   ]},

  {"titre": "UTM et nomenclature : nommer pour pouvoir comparer",
   "paras": [
     "Sans marquage explicite, un outil d'analytics devine la provenance d'un visiteur à partir de l'adresse de la page précédente. Ce mécanisme fonctionne pour les liens web ordinaires et échoue partout ailleurs : un lien cliqué dans une application de messagerie, dans un client de courriel, dans un document, ou après une redirection, arrive sans provenance et tombe dans la catégorie <strong>direct</strong>. Le direct n'est donc pas « les gens qui connaissent la marque » : c'est le fourre-tout de tout ce que l'outil n'a pas su rattacher.",
     "Les paramètres <strong>UTM</strong> corrigent cela en inscrivant la provenance dans l'adresse du lien. Cinq paramètres existent, trois suffisent presque toujours : <code>utm_source</code> nomme la plateforme d'où vient le clic, <code>utm_medium</code> le type de canal, <code>utm_campaign</code> l'opération. Les deux autres, <code>utm_content</code> et <code>utm_term</code>, servent à distinguer deux variantes d'un même lien ou un mot-clé.",
     "La difficulté n'est pas technique, elle est organisationnelle. Trois personnes qui posent des UTM sans convention produiront <code>Newsletter</code>, <code>newsletter</code> et <code>NL_avril</code> pour la même chose, et l'outil, sensible à la casse, en fera trois canaux distincts. La nomenclature n'existe pas pour faire joli : elle est ce qui rend un rapport agrégeable. Elle tient sur une page, et elle doit être écrite avant la première campagne, parce qu'elle n'est pas rétroactive.",
   ],
   "blocks": [
     {"type": "html", "html": """
<div class="table-responsive">
<table>
  <thead>
    <tr><th>Paramètre</th><th>Ce qu'il nomme</th><th>Vocabulaire recommandé</th><th>Exemple</th></tr>
  </thead>
  <tbody>
    <tr><td><code>utm_source</code></td><td>La plateforme d'où vient le clic</td><td>Nom de la plateforme, en minuscules</td><td><code>linkedin</code>, <code>newsletter</code>, <code>partenaire_x</code></td></tr>
    <tr><td><code>utm_medium</code></td><td>Le type de canal</td><td>Liste fermée, jamais improvisée</td><td><code>cpc</code>, <code>email</code>, <code>social</code>, <code>affiliation</code></td></tr>
    <tr><td><code>utm_campaign</code></td><td>L'opération commerciale</td><td>Objet puis période</td><td><code>livre_blanc_2026_t2</code></td></tr>
    <tr><td><code>utm_content</code></td><td>La variante du lien ou du visuel</td><td>Court et descriptif</td><td><code>banniere_haut</code>, <code>bouton_bas</code></td></tr>
    <tr><td><code>utm_term</code></td><td>Le mot-clé acheté</td><td>Rempli automatiquement par la régie</td><td><code>logiciel_facturation</code></td></tr>
  </tbody>
</table>
</div>
"""},
     {"type": "method", "titre": "poser une nomenclature tenable en cinq étapes",
      "steps": [
        "<strong>Fermez la liste des <code>medium</code>.</strong> Six à huit valeurs, pas une de plus, décidées une fois : c'est le paramètre sur lequel s'agrègent tous vos rapports, et une valeur improvisée crée une ligne orpheline que personne ne remarquera.",
        "<strong>Imposez minuscules et tirets bas, sans espaces ni accents.</strong> L'outil distingue les majuscules ; les accents et les espaces sont réencodés de façon variable selon les plateformes et produisent des doublons illisibles.",
        "<strong>Datez les campagnes dans leur nom</strong> — <code>_2026_t2</code> — pour pouvoir comparer une opération à celle de l'année précédente sans recherche archéologique.",
        "<strong>Centralisez la fabrication des liens</strong> dans un tableau partagé où chaque ligne est un lien produit : destination, paramètres, auteur, date. C'est ce tableau, et non la mémoire des équipes, qui garantit la cohérence quand quelqu'un part.",
        "<strong>Vérifiez chaque mois les valeurs orphelines</strong> : toute source ou tout medium ne représentant qu'une poignée de sessions est presque toujours une faute de frappe. Corrigez la nomenclature, pas le rapport.",
      ]},
     {"type": "pitfall", "titre": "poser des UTM sur des liens internes",
      "paras": [
        "L'idée paraît bonne : marquer une bannière de la page d'accueil avec des UTM pour savoir combien de personnes cliquent dessus. Elle est destructrice. Sur la plupart des outils, l'arrivée d'un paramètre de campagne <strong>ouvre une nouvelle session et réattribue la source</strong>. Le visiteur venu de la publicité qui clique sur votre bannière interne cesse d'être attribué à la publicité et devient attribué à la bannière.",
        "Le dégât est double : vous perdez la vraie source de vos conversions, et vous gonflez artificiellement le nombre de sessions. Les campagnes d'acquisition apparaissent alors moins efficaces qu'elles ne sont, et l'on prend des décisions de budget sur ce constat.",
        "La règle est absolue : <strong>les UTM ne servent qu'aux liens entrants</strong>, venus de l'extérieur du site. Pour mesurer un clic interne, on utilise un événement dédié — ce que le plan de mesure du module 1 prévoit précisément. Le même raisonnement vaut pour les liens d'un courriel interne ou d'un espace connecté renvoyant vers le site public.",
      ]},
   ]},

  {"titre": "L'attribution : à quel canal revient la conversion ?",
   "paras": [
     "Un client a vu une publicité en mars, lu un article en avril, cherché votre nom en mai et signé en juin. Quelle part de la vente revient à chaque canal ? La question n'a pas de réponse vraie : la vente est le produit conjoint des quatre étapes, dont aucune n'aurait suffi seule. L'attribution consiste à choisir une convention de partage, et il faut comprendre qu'elle relève de la convention et non de la vérité — c'est ce qui permet ensuite de discuter calmement du modèle.",
     "Le modèle <strong>dernier clic</strong>, appliqué par défaut par la plupart des outils, attribue tout à la dernière source avant la conversion. Il est simple, stable, indiscutable dans son calcul, et systématiquement favorable aux canaux de fin de parcours — la recherche sur le nom de marque, la publicité de reciblage, le direct. Il sous-évalue mécaniquement tout ce qui fait connaître : notoriété, contenu, partenariats.",
     "Le <strong>premier clic</strong> fait l'erreur symétrique, en attribuant tout à la découverte et rien à ce qui a conclu. Les modèles <strong>linéaire</strong> et à <strong>dépréciation temporelle</strong> répartissent la valeur entre les points de contact, également pour le premier, avec un poids croissant vers la fin pour le second. Les modèles dits <strong>pilotés par les données</strong> estiment statistiquement la contribution de chaque point de contact ; ils demandent un volume important, et leur calcul n'est généralement pas inspectable, ce qui rend délicat de défendre une décision budgétaire devant quelqu'un qui la conteste.",
     "Une notion secondaire pèse autant que le modèle : la <strong>fenêtre de conversion</strong>, c'est-à-dire la durée pendant laquelle un contact reste crédité. Une fenêtre de sept jours et une fenêtre de trente jours donnent des résultats très différents sur un cycle de vente long, et deux outils réglés différemment ne parleront jamais du même chiffre.",
     "La conduite raisonnable tient en trois points. Choisir un modèle en fonction de la décision à prendre, et non parce qu'il flatte le canal qu'on défend. S'y tenir, en ne comparant jamais deux périodes calculées avec des modèles ou des fenêtres différents. Et regarder systématiquement, à côté du modèle retenu, le rôle d'<strong>assistance</strong> des canaux — la fréquence à laquelle un canal apparaît dans un parcours converti sans en être le dernier point. Un canal qui n'obtient presque rien en dernier clic mais figure dans la moitié des parcours convertis n'est pas un mauvais canal : c'est un canal de découverte, et le condamner sur le dernier clic revient à couper la branche sur laquelle repose le reste.",
   ],
   "blocks": [
     {"type": "exemple", "titre": "un parcours, quatre modèles, quatre conclusions",
      "paras": [
        "Parcours : publicité vidéo (mars), article de blog trouvé en recherche organique (avril), courriel de la newsletter (mai), recherche sur le nom de marque puis signature (juin). Valeur : 12 000 €.",
        "<em>Dernier clic</em> : 12 000 € à la recherche de marque, zéro aux trois autres. <em>Premier clic</em> : 12 000 € à la publicité vidéo. <em>Linéaire</em> : 3 000 € chacun. <em>Dépréciation temporelle</em> : environ 1 200, 2 400, 3 600 et 4 800 €.",
        "Les quatre lectures sont défendables et conduisent à quatre budgets différents. Un point mérite d'être noté : la recherche sur le nom de marque, qui rafle tout en dernier clic, n'a rien créé — elle a enregistré une intention produite en amont. C'est l'exemple type du canal que le dernier clic surévalue, et c'est souvent le canal le mieux financé pour cette seule raison.",
      ]},
     {"type": "pitfall", "titre": "changer de modèle d'attribution et comparer avec l'avant",
      "paras": [
        "Le passage du dernier clic à un modèle réparti déplace mécaniquement de la valeur des canaux de fin vers les canaux de découverte. Si le changement n'est pas annoncé, la lecture qui suit est catastrophique : on croit constater que la publicité de reciblage s'effondre et que le contenu décolle, alors que rien n'a bougé dans la réalité.",
        "C'est une rupture de collecte au sens du module 1, et elle se traite de la même façon : repère daté sur les graphiques, aucune comparaison ne traverse le repère, et recalcul de la période précédente avec le nouveau modèle si l'outil le permet. Un changement de modèle non daté est indétectable six mois plus tard.",
      ]},
   ]},

  {"titre": "Diagnostiquer un écart entre deux outils",
   "paras": [
     "Deux outils qui mesurent la même chose ne donneront jamais le même chiffre, et l'objectif d'un rapprochement n'est pas de les rendre égaux. Il est d'obtenir un <strong>écart stable et expliqué</strong> : savoir que la régie compte environ 40 % de plus que l'analytics, savoir pourquoi, et surveiller la stabilité de ce rapport. Un écart stable est exploitable ; c'est sa variation qui doit alerter.",
     "Les causes sont toujours les mêmes, et il suffit de les passer en revue dans l'ordre. <strong>L'unité comptée</strong> d'abord : une régie compte des clics, l'analytics des sessions, le CRM des enregistrements créés — un même visiteur qui clique deux fois donne deux clics et une session. <strong>Le modèle et la fenêtre d'attribution</strong> ensuite : la plupart des régies s'attribuent la conversion selon leur propre modèle, souvent en incluant les conversions dites post-impression, survenues après un simple affichage sans clic. C'est généralement le premier facteur d'écart, et de loin.",
     "Viennent ensuite le <strong>consentement</strong>, qui retire à l'analytics une part de l'activité que la régie voit de son côté, le <strong>filtrage des robots</strong>, appliqué différemment par chaque outil, le <strong>fuseau horaire</strong> et les bornes de journée, et enfin la <strong>déduplication</strong> — le CRM fusionne deux demandes d'une même personne là où l'analytics en compte deux.",
     "La restitution d'un rapprochement obéit à une règle simple : on ne présente jamais trois chiffres côte à côte sans dire ce que chacun compte. Un tableau de rapprochement comporte, pour chaque outil, l'unité comptée, la fenêtre, le modèle et le périmètre. Il est plus long à lire et il met fin aux réunions où l'on discute de la fiabilité des outils au lieu de décider.",
   ],
   "blocks": [
     {"type": "method", "titre": "conduire un rapprochement en six étapes",
      "steps": [
        "<strong>Fixez un périmètre étroit</strong> : une campagne, un mois, un type de conversion. Un rapprochement global n'aboutit jamais, parce que trop de causes s'y additionnent.",
        "<strong>Écrivez, pour chaque outil, ce qu'il compte exactement</strong> : unité, modèle d'attribution, fenêtre, fuseau, filtres appliqués. Cette étape seule explique souvent la moitié de l'écart, et elle ne demande aucun accès technique.",
        "<strong>Alignez ce qui peut l'être</strong> : même fenêtre, même fuseau, même définition de conversion. Ce qui reste après cet alignement est l'écart réel à expliquer.",
        "<strong>Isolez le post-impression</strong> dans les chiffres de la régie, quand l'interface le permet. C'est le poste d'écart le plus important sur les campagnes d'affichage et de vidéo.",
        "<strong>Estimez la part du consentement</strong> à l'aide du coefficient de sous-couverture du module 1, et considérez le reliquat comme irréductible plutôt que de le poursuivre.",
        "<strong>Écrivez la conclusion en une phrase</strong> — « la régie compte environ 40 % de plus que l'analytics, dont l'essentiel s'explique par le post-impression et le consentement ; nous suivons ce rapport chaque mois » — et arrêtez-vous là.",
      ]},
     {"type": "pitfall", "titre": "vouloir réconcilier au chiffre près",
      "paras": [
        "C'est la demande spontanée d'une direction et c'est un piège de temps considérable. Après le rapprochement méthodique, il reste toujours un écart résiduel de quelques points, dû à des mécanismes non inspectables : filtrage propriétaire des robots, déduplication interne des régies, arrondis. Le poursuivre coûte des semaines et n'apporte aucune décision.",
        "La réponse à donner est simple : « aucun des deux chiffres n'est faux, ils ne comptent pas la même chose ; nous décidons sur celui qui correspond à la décision — le CRM pour évaluer un canal, la régie pour piloter une enchère au quotidien ». Désigner l'outil de référence par décision, plutôt que chercher un chiffre unique et vrai, est ce qui débloque durablement ce type de réunion.",
      ]},
   ]},
 ],

 "etude_cas": {
   "titre": "340, 190, 120 : réconcilier trois chiffres sans les rendre égaux",
   "html": """
<p>Reprenons la réunion du 14 avril. Trois outils, trois chiffres, aucune décision. Voici le rapprochement, mené en une demi-journée sur un périmètre volontairement étroit : une seule campagne payante, le mois de mars, une seule conversion — la demande de démonstration.</p>
<p><strong>Étape 1 — écrire ce que compte chaque outil.</strong> La régie annonce 340 <em>conversions attribuées selon son propre modèle, fenêtre de 30 jours après clic et 1 jour après impression</em>. L'analytics compte 190 <em>sessions ayant déclenché l'événement de demande, en dernier clic non direct, fenêtre de 30 jours</em>. Le CRM recense 120 <em>fiches créées, dédoublonnées par adresse électronique</em>. Trois définitions écrites noir sur blanc : la moitié du travail est faite, et personne n'a encore ouvert un tableur.</p>
<p><strong>Étape 2 — isoler le post-impression.</strong> Sur les 340 conversions de la régie, 95 sont post-impression : la personne a vu la publicité sans cliquer, puis est venue par un autre chemin. L'analytics ne peut pas les voir, par construction. Il reste 245 conversions après clic, contre 190 mesurées. Premier écart expliqué, et c'est le plus gros.</p>
<p><strong>Étape 3 — appliquer le consentement.</strong> Le taux de consentement du site est de 72 %, stable depuis janvier. L'analytics ne voit donc qu'environ trois quarts des demandes réellement effectuées. 190 mesurées correspondent à un ordre de grandeur de 260 demandes réelles, ce qui recouvre les 245 de la régie à la précision près de l'exercice. Deuxième écart expliqué : il n'en reste plus.</p>
<p><strong>Étape 4 — comprendre le passage à 120.</strong> C'est l'écart le plus intéressant, et celui que personne n'avait examiné. Entre les 245 demandes envoyées et les 120 fiches CRM, on trouve 38 doublons — même personne, deux envois —, 51 demandes rejetées par le formulaire pour adresse invalide ou champ obligatoire mal rempli, et 36 demandes arrivées en boîte générique sans être saisies dans le CRM, faute de règle claire sur qui les traite.</p>
<p><strong>Le constat qui change la réunion.</strong> Le sujet n'était pas la fiabilité des outils. <strong>87 demandes sur 245 se perdent entre le site et le commercial</strong>, soit plus d'un tiers, et personne ne le savait parce que chacun regardait son propre chiffre. Les 51 rejets de formulaire sont un problème de conception réparable en une journée ; les 36 demandes non saisies sont un problème d'organisation qui se règle par une règle d'affectation. Aucune campagne, aucun budget n'était en cause.</p>
<p><strong>La décision prise.</strong> Trois choses. Un outil de référence par décision : le CRM pour évaluer la rentabilité d'un canal, la régie pour piloter les enchères au quotidien, l'analytics pour comprendre les parcours. Un rapport d'écart mensuel en trois lignes, dont on surveille la stabilité et non la valeur. Et deux chantiers immédiats sur le formulaire et sur l'affectation des demandes, dont l'effet attendu — récupérer une part des 87 demandes perdues — est supérieur à ce qu'aurait rapporté n'importe quel arbitrage de budget publicitaire.</p>
<p><strong>La leçon transposable.</strong> Un écart entre outils n'est pas un problème de données à corriger, c'est un diagnostic à lire. Ce sont les trois définitions écrites à l'étape 1 qui ont rendu le reste possible, et c'est le seul moment de l'exercice qui ne demandait aucun outil. Retenez enfin que la question de départ — lequel des trois chiffres est le bon — était mal posée : les trois étaient justes, et c'est en cherchant à les <em>expliquer</em> plutôt qu'à les <em>égaliser</em> qu'on a trouvé le tiers de demandes perdues.</p>
"""},

 "checklist": {
   "titre": "Checklist — lire une audience sans se tromper",
   "items": [
     "Le vocabulaire employé en réunion dit « utilisateurs » ou « navigateurs », jamais « personnes »",
     "La durée d'inactivité qui clôt une session est connue et écrite",
     "Un identifiant de compte est transmis pour les visiteurs connectés, si le site en a",
     "La définition du rebond ou de la session engagée utilisée par votre outil est écrite",
     "Aucun taux de rebond n'est comparé à une moyenne sectorielle",
     "Au moins une mesure d'intention remplace les indicateurs d'engagement par défaut",
     "Le seuil de la profondeur de lecture est fixé une fois et documenté",
     "La liste des utm_medium est fermée et compte moins de dix valeurs",
     "Tous les paramètres sont en minuscules, sans espaces ni accents",
     "Les noms de campagne portent leur période, pour comparaison d'une année sur l'autre",
     "Un tableau partagé recense chaque lien marqué : destination, paramètres, auteur, date",
     "Aucun lien interne ne porte de paramètres UTM",
     "Les valeurs de source ou de medium orphelines sont vérifiées chaque mois",
     "Le modèle d'attribution et la fenêtre de conversion sont écrits sur chaque rapport",
     "Aucune comparaison de périodes ne traverse un changement de modèle d'attribution",
     "Le rôle d'assistance des canaux est regardé à côté du modèle retenu",
     "Chaque rapprochement d'outils commence par écrire ce que chacun compte",
     "Le post-impression est isolé dans les chiffres des régies publicitaires",
     "Un outil de référence est désigné par type de décision, pas un chiffre unique et vrai",
     "L'écart entre outils est suivi dans sa stabilité, pas dans sa valeur",
   ]},

 "glossaire": [
   ("Session", "Suite d'événements d'un même navigateur, close par une période d'inactivité (souvent 30 minutes). Convention de découpage, pas unité naturelle : une visite humaine peut en produire plusieurs."),
   ("Utilisateur", "Identifiant stocké dans un navigateur. Une personne sur deux appareils compte pour deux ; le nombre d'utilisateurs surestime le nombre de personnes d'un facteur courant de 1,3 à 2."),
   ("Identifiant de compte", "Identifiant stable, non nominatif, transmis à la connexion. Seul moyen de recoller les appareils d'une même personne."),
   ("Session engagée", "Notion remplaçant le rebond dans les outils récents : session dépassant une durée, plusieurs pages, ou contenant une conversion. Définition variable selon les outils."),
   ("Direct", "Catégorie de provenance regroupant tout ce que l'outil n'a pas su rattacher. N'est pas synonyme de notoriété."),
   ("UTM", "Paramètres ajoutés à l'adresse d'un lien entrant pour en déclarer la provenance. Sensibles à la casse, non rétroactifs, réservés aux liens venus de l'extérieur."),
   ("Attribution", "Convention de partage de la valeur d'une conversion entre les points de contact d'un parcours. Question de convention, jamais de vérité."),
   ("Dernier clic", "Modèle attribuant tout à la dernière source. Simple et stable, mais favorable aux canaux de fin de parcours et défavorable à ceux qui font connaître."),
   ("Fenêtre de conversion", "Durée pendant laquelle un point de contact reste crédité. Deux outils réglés différemment ne parleront jamais du même chiffre."),
   ("Post-impression", "Conversion créditée par une régie après un simple affichage publicitaire sans clic. Invisible pour l'analytics, et premier poste d'écart entre les deux."),
   ("Assistance", "Fréquence à laquelle un canal figure dans un parcours converti sans en être le dernier point. Révèle les canaux de découverte que le dernier clic condamne."),
   ("Rapprochement", "Comparaison méthodique de deux outils visant un écart stable et expliqué, jamais l'égalité des chiffres."),
 ],

 "retenir": [
   "Session et utilisateur ne désignent pas ce que les mots suggèrent : une convention de découpage et un identifiant de navigateur.",
   "Le nombre d'utilisateurs surestime toujours le nombre de personnes ; dites « utilisateurs », jamais « personnes ».",
   "Si le site a une zone connectée, transmettre un identifiant de compte est le chantier au meilleur rendement du dispositif.",
   "Rebond et session engagée portent le même nom sur deux définitions opposées : vérifiez laquelle votre outil applique avant toute comparaison.",
   "Les pages par session montent quand la navigation est mauvaise : sur un site de service, leur hausse est une mauvaise nouvelle.",
   "La dernière page d'une session compte zéro seconde dans la plupart des configurations : la durée moyenne est structurellement sous-estimée.",
   "Remplacez l'engagement par l'intention : atteinte d'une page à valeur, profondeur de lecture, retour à sept jours, complétion.",
   "Ne comparez jamais votre taux de rebond à une moyenne sectorielle : ni l'outil, ni la définition, ni la collecte ne sont les mêmes.",
   "Le direct est le fourre-tout de ce que l'outil n'a pas su rattacher, pas la mesure de votre notoriété.",
   "Une nomenclature UTM se décide avant la première campagne : elle n'est pas rétroactive, et l'outil distingue les majuscules.",
   "Les UTM ne servent qu'aux liens entrants : sur un lien interne, ils ouvrent une session et détruisent la vraie source.",
   "L'attribution est une convention de partage, pas une vérité : le dernier clic surévalue systématiquement les canaux de fin de parcours.",
   "Regardez le rôle d'assistance à côté du modèle : un canal absent du dernier clic mais présent dans la moitié des parcours est un canal de découverte.",
   "Un changement de modèle d'attribution est une rupture de collecte : datez-le, et ne comparez pas au travers.",
   "Deux outils ne seront jamais égaux : cherchez un écart stable et expliqué, et surveillez sa stabilité plutôt que sa valeur.",
   "Le post-impression est le premier poste d'écart entre une régie et un analytics : isolez-le avant tout autre calcul.",
   "Désignez un outil de référence par type de décision plutôt qu'un chiffre unique et vrai : c'est ce qui débloque les réunions de rapprochement.",
 ],

 "exercices": [
  {"titre": "Corriger une nomenclature de campagne", "niveau": "Débutant",
   "enonce": [
     "Six liens ont été fabriqués par trois personnes différentes au cours du même trimestre. Repérez pour chacun ce qui ne va pas, et dites quelles conséquences concrètes l'erreur produira dans les rapports.",
     "1. <code>?utm_source=LinkedIn&amp;utm_medium=Social&amp;utm_campaign=Livre blanc</code> — 2. <code>?utm_source=newsletter&amp;utm_medium=newsletter&amp;utm_campaign=avril</code> — 3. <code>?utm_source=google&amp;utm_medium=cpc</code> (sans campagne) — 4. lien de la bannière de la page d'accueil : <code>?utm_source=site&amp;utm_medium=interne&amp;utm_campaign=promo_ete</code> — 5. <code>?utm_source=partenaire&amp;utm_medium=référencement&amp;utm_campaign=oct</code> — 6. <code>?utm_source=linkedin&amp;utm_medium=cpc&amp;utm_campaign=livre_blanc_2026_t2</code>",
   ],
   "corrige": """
<p><strong>1. Majuscules et espace.</strong> <code>LinkedIn</code> et <code>Social</code> créeront des lignes distinctes de <code>linkedin</code> et <code>social</code>, et l'espace de <code>Livre blanc</code> sera réencodé différemment selon les plateformes — produisant parfois <code>Livre%20blanc</code>, parfois <code>Livre+blanc</code>, donc deux campagnes pour une. Conséquence : le rapport par campagne devient une liste de doublons qu'il faudra additionner à la main chaque mois, indéfiniment.</p>
<p><strong>2. Confusion source / medium, et campagne non datée.</strong> <code>newsletter</code> est ici la source ; le medium correct est <code>email</code>. En l'état, la newsletter n'est pas agrégée avec les autres envois de courriel, et toute question du type « que rapporte l'e-mailing ? » devient sans réponse. <code>avril</code> comme nom de campagne rendra la comparaison avec avril de l'année suivante impossible sans archéologie : écrire <code>newsletter_2026_04</code>.</p>
<p><strong>3. Campagne absente — moins grave qu'il n'y paraît, mais à traiter.</strong> Sur la publicité de recherche, la régie remplit souvent automatiquement les paramètres par un mécanisme dédié, et le manque n'est alors qu'apparent. Si ce n'est pas le cas, tout le trafic payant du moteur tombe dans une même ligne sans campagne, et le rapport ne permet plus de distinguer les opérations. Le bon réflexe est de vérifier si le marquage automatique est actif avant de conclure — et de ne jamais cumuler marquage automatique et UTM manuels, qui entrent en conflit.</p>
<p><strong>4. Le cas grave : des UTM sur un lien interne.</strong> C'est la seule erreur de la liste qui détruit des données existantes plutôt que de mal les ranger. Chaque clic sur cette bannière ouvre une nouvelle session et réattribue le visiteur à <code>site / interne</code>. Résultat : les campagnes d'acquisition perdent les conversions des visiteurs qui ont cliqué sur la bannière, le nombre de sessions est artificiellement gonflé, et l'on peut couper un budget publicitaire sur la foi de ce constat. Correction : retirer les paramètres et mesurer le clic par un événement dédié.</p>
<p><strong>5. Accent, et vocabulaire de medium improvisé.</strong> L'accent de <code>référencement</code> sera réencodé de façon variable et produira des doublons. Surtout, <code>référencement</code> n'appartient à aucune liste fermée raisonnable et se confondra avec le trafic organique dans les esprits alors qu'il s'agit d'un partenariat : le medium correct est <code>affiliation</code> ou <code>partenariat</code>, selon la convention retenue. <code>oct</code> pose le même problème de datation que le cas 2.</p>
<p><strong>6. Le seul correct dans sa forme — et pourtant à vérifier.</strong> Minuscules, tirets bas, campagne datée : rien à redire sur l'écriture. Mais <code>cpc</code> désigne un clic payant : si ce lien correspond à une publication non sponsorisée, le medium est <code>social</code>, et le classer en <code>cpc</code> fera apparaître du trafic payant là où il n'y a aucune dépense — ce qui faussera tout calcul de coût par acquisition. La leçon vaut pour l'ensemble de l'exercice : une nomenclature formellement correcte peut être sémantiquement fausse, et seule la relecture par quelqu'un qui connaît la campagne le détecte.</p>
<p><strong>Ce qu'il faut retenir des six cas.</strong> Cinq erreurs sur six ne se voient jamais dans l'outil : elles produisent des lignes qui paraissent normales. Seul un contrôle mensuel des valeurs orphelines et un tableau centralisé de fabrication des liens les font apparaître. C'est pourquoi la nomenclature est un sujet d'organisation avant d'être un sujet technique.</p>
"""},

  {"titre": "Le même trimestre, deux modèles d'attribution", "niveau": "Intermédiaire",
   "enonce": [
     "Sur un trimestre, quatre canaux ont produit 100 conversions au total. En dernier clic : recherche de marque 46, reciblage 24, recherche organique 18, publicité vidéo 12. En premier clic : publicité vidéo 39, recherche organique 31, recherche de marque 18, reciblage 12. Le budget est aujourd'hui alloué à 55 % au reciblage et à 10 % à la vidéo.",
     "Interprétez l'écart entre les deux lectures, dites ce que vous recommandez, et indiquez comment vous vérifieriez votre recommandation avant d'engager le budget.",
   ],
   "corrige": """
<p><strong>Ce que l'écart raconte.</strong> Il ne signale aucune anomalie : il décrit une division du travail entre canaux. La vidéo passe de 12 à 39 selon qu'on regarde la fin ou le début du parcours, la recherche de marque de 46 à 18 dans l'autre sens. Traduction : la vidéo et le contenu organique <em>créent</em> la demande, la recherche de marque et le reciblage l'<em>enregistrent</em>. C'est le schéma le plus courant qui soit, et la première chose à dire en réunion, avant tout chiffre.</p>
<p><strong>Le cas particulier de la recherche de marque.</strong> 46 conversions en dernier clic pour un canal où le visiteur tape le nom de l'entreprise : ce canal ne convainc personne, il capte une intention déjà formée ailleurs. Le piloter comme un canal d'acquisition et augmenter son budget parce qu'il « performe » est l'erreur classique — on paierait pour des clics que l'on obtiendrait en partie gratuitement, et le coût par acquisition apparent resterait excellent tout en n'apportant aucune conversion supplémentaire.</p>
<p><strong>Le cas du reciblage.</strong> 24 en dernier clic, 12 en premier, pour 55 % du budget : c'est le poste le plus discutable de l'allocation actuelle. Le reciblage s'adresse par construction à des visiteurs déjà venus, donc déjà produits par un autre canal. Une partie de ses 24 conversions serait survenue sans lui — la question n'est pas de savoir combien il en revendique, mais combien il en <em>ajoute</em>.</p>
<p><strong>Ce que je recommande, et ce que je ne recommande pas.</strong> Ne pas basculer le budget sur la seule lecture premier clic : ce serait remplacer un biais par le biais symétrique, et la vidéo n'est pas plus méritante que le reciblage sur cette base. Je recommande un mouvement mesuré — ramener le reciblage de 55 % à environ 40 %, porter la vidéo de 10 % à 20 %, ne pas augmenter la recherche de marque — et surtout, <strong>je conditionne la suite à une vérification</strong>. Un déplacement de budget décidé sur un changement de modèle d'attribution n'est pas une décision fondée, c'est un changement de convention comptable.</p>
<p><strong>Comment vérifier, par ordre de robustesse.</strong></p>
<p><em>Le test d'incrémentalité, seule réponse solide.</em> Couper le reciblage sur une part de l'audience — un pourcentage d'utilisateurs, ou une zone géographique comparable — pendant quatre à six semaines, et comparer le volume total de conversions entre les deux groupes. Si le total ne baisse pas, les conversions revendiquées se produisaient de toute façon. Le module 3 traite la mécanique de ce type de test, sa durée et sa lecture ; retenez ici qu'il est le seul dispositif qui réponde à la question « combien ce canal ajoute-t-il ».</p>
<p><em>Le rôle d'assistance, en attendant.</em> Regarder dans combien de parcours convertis chaque canal figure sans être le dernier point. Un canal présent dans la moitié des parcours et absent du dernier clic est un canal de découverte : cela confirme la lecture sans la démontrer.</p>
<p><em>Le décalage temporel.</em> Si la vidéo crée la demande, une hausse de sa pression doit se lire sur le volume de recherches sur le nom de marque quelques semaines plus tard. C'est un contrôle indirect, gratuit, et souvent convaincant en réunion parce qu'il ne dépend d'aucun modèle d'attribution.</p>
<p><strong>Comment présenter tout cela.</strong> Ne présentez jamais les deux tableaux côte à côte sans commentaire : la lecture spontanée est que l'un des deux est faux. Présentez une seule phrase — « ces deux tableaux mesurent deux choses différentes, l'un dit qui conclut, l'autre dit qui fait connaître » — puis la recommandation, puis le test qui la vérifiera. L'ordre compte autant que le contenu, et un déplacement de budget assorti d'un test de vérification est accepté là où le même déplacement sans test est contesté.</p>
"""},

  {"titre": "Défendre un canal que le dernier clic condamne", "niveau": "Avancé",
   "enonce": [
     "Votre direction financière veut supprimer l'intégralité du budget d'affichage et de vidéo, soit 25 % du budget marketing. L'argument est solide en apparence : ce poste représente 4 % des conversions en dernier clic, avec un coût par acquisition huit fois supérieur à celui du reciblage. La décision doit être arbitrée dans trois semaines.",
     "Construisez votre position. Traitez explicitement l'hypothèse où la direction financière a raison, et proposez un dispositif qui permette de trancher plutôt que d'argumenter indéfiniment.",
   ],
   "corrige": """
<p><strong>Première règle : ne contestez pas les chiffres, contestez ce qu'ils mesurent.</strong> Les 4 % et le coût par acquisition sont exacts. Les nier vous décrédibilise en trois minutes. La position tenable est : « ces chiffres sont justes et ils ne répondent pas à la question posée ; ils disent quel canal conclut, la question est de savoir lequel ajoute ». Cette distinction est tout l'exercice.</p>
<p><strong>Pourquoi le dernier clic condamne structurellement ce type de canal.</strong> L'affichage et la vidéo agissent avant l'intention, souvent plusieurs semaines avant, et sans clic. Le dernier clic ne peut par construction leur attribuer que les rares cas où la conversion suit immédiatement. Un canal de notoriété évalué au dernier clic affichera toujours des résultats médiocres, y compris s'il est le principal moteur de l'activité : ce n'est pas une performance qu'on observe, c'est une conséquence mécanique de l'instrument. Le dire ainsi, sans procès d'intention envers la direction financière, est ce qui rend la suite audible.</p>
<p><strong>Ce que vous apportez immédiatement, en trois éléments faciles à réunir.</strong></p>
<p><em>1. Le rôle d'assistance.</em> Part des parcours convertis contenant au moins un contact avec l'affichage ou la vidéo, même ancien. Si ce chiffre est de l'ordre de 30 à 40 % alors que le dernier clic donne 4 %, l'écart est en lui-même l'argument. S'il est de 5 %, votre position est faible et il faut le savoir avant la réunion, pas pendant.</p>
<p><em>2. La corrélation décalée avec la recherche de marque.</em> Superposez la pression publicitaire hebdomadaire et le volume de recherches sur le nom de l'entreprise, avec deux à quatre semaines de décalage. C'est un indice, non une preuve — le module 3 rappellera qu'une corrélation n'établit pas une causalité — mais il ne dépend d'aucun modèle d'attribution, ce qui le rend difficile à écarter.</p>
<p><em>3. L'historique des arrêts passés.</em> Si le budget a déjà été coupé lors d'un trimestre antérieur, regardez ce qui s'est passé sur le volume total de conversions dans les deux à trois mois suivants. C'est une expérience naturelle imparfaite, et souvent l'argument le plus parlant dont vous disposiez sans rien dépenser.</p>
<p><strong>Le dispositif à proposer, qui est la vraie réponse.</strong> Ne demandez pas de conserver le budget en l'état : personne n'accorde trois mois de sursis sur la foi d'une explication méthodologique. Proposez un <strong>test d'incrémentalité géographique</strong> : maintenir la pression sur un ensemble de régions et la couper sur un ensemble comparable, pendant six à huit semaines, puis comparer le volume total de conversions — toutes sources confondues, ce point est essentiel — entre les deux ensembles.</p>
<p>Le test répond exactement à la question posée par la direction financière, et il y répond quel que soit le résultat. Précisez d'emblée les trois conditions de sa validité : des zones comparables en volume et en saisonnalité, une durée supérieure au cycle de vente moyen sans quoi on mesure un retard et non une absence d'effet, et un critère de décision écrit <em>avant</em> le test. Ce dernier point est le plus important — un seuil défini après coup se négocie, un seuil défini avant tranche.</p>
<p><strong>L'hypothèse où la direction financière a raison — et pourquoi il faut la traiter en premier.</strong> Il est parfaitement possible que ce budget n'ajoute rien : marché saturé, mauvais ciblage, création publicitaire inefficace, ou pression trop faible pour produire un effet. Annoncez-le vous-même, avant qu'on ne vous le dise : « si le test montre que la coupure ne fait pas baisser le volume, je recommanderai moi-même la suppression ». Cela transforme la discussion. Vous ne défendez plus un budget, vous proposez un moyen de trancher — et vous devenez la personne dont on croira la conclusion, y compris quand elle sera favorable.</p>
<p><strong>Ce qu'il faut refuser, et savoir nommer.</strong> Refusez le compromis apparemment raisonnable qui consiste à couper de moitié partout : il ne produit aucune information, puisqu'on ne pourra rien comparer, et il dégrade le canal juste assez pour rendre le test suivant ininterprétable. Refusez également de trancher sur un changement de modèle d'attribution : passer au premier clic ferait apparaître ce canal comme excellent, et ce serait une victoire malhonnête, indéfendable au premier examen. La seule position solide sur la durée est celle qui accepte d'être démentie par un dispositif convenu à l'avance.</p>
"""},
 ],

 "ressources": [
   "<strong>La documentation officielle de votre outil d'analytics, section « sessions et utilisateurs »</strong> — c'est le seul endroit où trouver les conventions exactes appliquées par votre configuration : durée d'inactivité, règles de clôture, définition de la session engagée. Un quart d'heure de lecture qui évite des mois de malentendus.",
   "<strong>Un tableau partagé de fabrication des liens marqués</strong> — le livrable le plus rentable de ce module. Une ligne par lien produit, avec destination, paramètres, auteur et date : c'est lui, et non la mémoire des équipes, qui fait tenir une nomenclature.",
   "<strong>Le module 1 de cette formation</strong> — la nomenclature, l'attribution et les rapprochements ne tiennent que sur un plan de mesure écrit et un journal des modifications. Si vous butez sur un écart inexplicable, c'est presque toujours là qu'il faut revenir.",
   "<strong>Le module 3 de cette formation</strong> — les tests d'incrémentalité évoqués dans les exercices 2 et 3 y sont traités en détail : taille d'échantillon, durée, lecture des résultats. N'engagez pas de test avant de l'avoir lu.",
 ],
}

QUIZ = {
 "analytics-mesure/module-2": {
  "module_id": "formation-analytics-mesure-module-2",
  "version": "2.0", "last_verified": "2026-09-03",
  "questions": [
   {"id":"q1","question":"Une personne visite le site depuis son téléphone puis depuis son ordinateur. Que compte l'outil ?",
    "choices":[{"key":"a","text":"Un utilisateur et deux sessions"},
               {"key":"b","text":"Deux utilisateurs, car un utilisateur est un identifiant de navigateur"},
               {"key":"c","text":"Un utilisateur, l'outil recollant automatiquement les appareils"}],
    "correct_answer":"b","feedback":"Seul un identifiant de compte transmis à la connexion permet de recoller les appareils. Sans lui, le nombre d'utilisateurs surestime le nombre de personnes."},
   {"id":"q2","question":"Sur un site de service, les pages par session augmentent nettement. Comment le lire ?",
    "choices":[{"key":"a","text":"C'est un bon signe : les visiteurs explorent davantage le site"},
               {"key":"b","text":"C'est probablement un mauvais signe : ils ne trouvent pas ce qu'ils cherchent"},
               {"key":"c","text":"L'indicateur est neutre et ne s'interprète pas"}],
    "correct_answer":"b","feedback":"Un visiteur qui trouve immédiatement consulte une page ; celui qui erre en consulte six. L'indicateur n'a un sens favorable que sur un site de contenu financé par la publicité."},
   {"id":"q3","question":"Peut-on poser des paramètres UTM sur la bannière de sa propre page d'accueil ?",
    "choices":[{"key":"a","text":"Oui, c'est le moyen normal de mesurer les clics internes"},
               {"key":"b","text":"Non : cela ouvre une session et réattribue le visiteur, détruisant sa vraie source"},
               {"key":"c","text":"Oui, à condition de n'utiliser que utm_content"}],
    "correct_answer":"b","feedback":"Les UTM ne servent qu'aux liens entrants. Pour un clic interne, on utilise un événement dédié prévu au plan de mesure."},
   {"id":"q4","question":"Un canal obtient 4 % des conversions en dernier clic mais figure dans 35 % des parcours convertis. Qu'en conclure ?",
    "choices":[{"key":"a","text":"Les deux chiffres sont incohérents : l'un des outils est mal configuré"},
               {"key":"b","text":"C'est un canal de découverte, que le dernier clic sous-évalue par construction"},
               {"key":"c","text":"Le canal est inefficace : seul le dernier clic mesure une vraie conversion"}],
    "correct_answer":"b","feedback":"Le dernier clic ne crédite que ce qui conclut. Un canal agissant avant l'intention affichera toujours des résultats médiocres avec ce modèle, y compris s'il est le moteur de l'activité."},
   {"id":"q5","question":"Une régie annonce 340 conversions, l'analytics 190. Quel poste d'écart examiner en premier ?",
    "choices":[{"key":"a","text":"Le post-impression, que l'analytics ne peut pas voir"},
               {"key":"b","text":"Le fuseau horaire appliqué par chaque outil"},
               {"key":"c","text":"Le filtrage des robots"}],
    "correct_answer":"a","feedback":"C'est de loin le premier poste d'écart sur les campagnes d'affichage et de vidéo. Fuseau et robots existent, mais pèsent bien moins."},
   {"id":"q6","question":"Quel dispositif répond réellement à la question « combien ce canal ajoute-t-il ? »",
    "choices":[{"key":"a","text":"Passer d'un modèle dernier clic à un modèle multi-touch"},
               {"key":"b","text":"Un test d'incrémentalité : couper le canal sur une part comparable de l'audience et comparer le volume total"},
               {"key":"c","text":"Élargir la fenêtre de conversion à 90 jours"}],
    "correct_answer":"b","feedback":"Changer de modèle ou de fenêtre change la convention comptable, pas la réalité. Seule une coupure comparée mesure ce que le canal ajoute."},
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
