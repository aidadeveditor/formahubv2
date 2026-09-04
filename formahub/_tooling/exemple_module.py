#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, json, os
sys.path.insert(0, "/tmp")
from fh_builder import build

M = {}
FORM = "CRM &amp; Relation Client (Salesforce)"

M["crm-relation-client/module-3"] = {
 "formation": FORM,
 "titre": "Automatisation, Tableaux de Bord &amp; Optimisation de la Relation Client",
 "num": 3, "total": 3, "duree": "55 min", "niveau": "Intermédiaire",
 "module_id": "formation-crm-relation-client-module-3",
 "situation": [
   "Votre CRM est propre et votre pipeline dit la vérité. Deux problèmes subsistent, et ils sont de nature différente.",
   "Le premier : vos commerciaux passent un temps considérable en saisie répétitive — créer la même tâche de relance après chaque proposition, prévenir le manager quand une affaire dépasse un certain montant, changer un statut quand une autre condition est remplie. Ce travail n'a aucune valeur ajoutée et il est le premier motif d'abandon d'un CRM.",
   "Le second : votre direction demande chaque lundi un « point sur l'activité », que quelqu'un prépare à la main dans un tableur en recopiant des chiffres du CRM. Ce document est faux dès qu'il est imprimé, coûte trois heures par semaine, et n'a jamais déclenché la moindre décision.",
   "Ce module traite ces deux points — automatiser ce qui est mécanique, et construire des tableaux de bord qui provoquent des décisions — puis pose la question qui les dépasse tous les deux : à quoi sert, au fond, tout ce que vous avez construit sur ces trois modules ?",
 ],
 "objectifs": [
   "Distinguer ce qui doit être automatisé de ce qui ne doit jamais l'être",
   "Concevoir une règle d'automatisation lisible : déclencheur, condition, action",
   "Choisir entre alerte, tâche automatique et mise à jour de champ selon l'effet recherché",
   "Construire un tableau de bord qui provoque une décision plutôt qu'il ne décrit une situation",
   "Distinguer indicateurs d'activité, d'avancement et de résultat, et savoir lequel piloter",
   "Mettre en place un suivi de la relation après la vente : renouvellement, satisfaction, signaux de risque",
 ],
 "sections": [
  {"titre": "Automatiser : la règle des trois conditions",
   "paras": [
     "L'automatisation d'un CRM est séduisante et facilement excessive. Une entreprise qui découvre les outils d'automatisation en met partout ; six mois plus tard, personne ne sait plus pourquoi un champ change tout seul, les commerciaux reçoivent quinze notifications par jour qu'ils ont appris à ignorer, et modifier quoi que ce soit fait peur.",
     "Un garde-fou simple évite cela. N'automatisez une action que si elle remplit <strong>les trois conditions suivantes</strong> :",
     "<strong>1. Elle est répétitive et prévisible.</strong> Vous pouvez décrire exactement quand elle doit se produire, sans « ça dépend ». Si vous employez « en général » ou « sauf quand », l'action n'est pas automatisable en l'état — commencez par clarifier la règle métier.",
     "<strong>2. Elle ne demande aucun jugement.</strong> Créer une tâche de relance à J+7 ne demande aucun jugement. Décider si une affaire passe en Négociation en demande un, et doit rester humain — c'est précisément ce qui garantit la fiabilité du pipeline vue au module 2.",
     "<strong>3. Son échec serait visible.</strong> Si l'automatisation cesse de fonctionner, quelqu'un doit s'en apercevoir. Une automatisation silencieuse qui tombe en panne produit des données fausses pendant des mois sans que personne ne le sache. C'est le risque le plus sous-estimé du sujet.",
   ],
   "blocks": [
     {"type": "exemple", "titre": "trois cas, trois réponses",
      "paras": [
        "<em>« Créer une tâche de relance 7 jours après le passage en Proposition »</em> → automatisez. Répétitif, aucun jugement, et son absence se verrait (le commercial n'aurait plus de relances planifiées).",
        "<em>« Passer l'opportunité en Perdue après 60 jours sans activité »</em> → n'automatisez pas. Fermer une affaire est une décision commerciale, parfois contestable, et l'automatiser détruirait des affaires vivantes mais lentes. Automatisez plutôt <strong>l'alerte</strong> : une notification au commercial et une entrée dans le rapport de revue. La décision reste humaine.",
        "<em>« Notifier le directeur commercial pour toute opportunité au-dessus de 100 k€ »</em> → automatisez, mais à la création et au changement d'étape seulement, pas à chaque modification. Une alerte qui se déclenche vingt fois pour la même affaire cesse d'être lue au bout d'une semaine.",
      ]},
     {"type": "pitfall", "titre": "l'automatisation qui remplace une conversation",
      "paras": [
        "Le cas typique : un e-mail automatique envoyé au client trois jours après un rendez-vous, signé du commercial. C'est efficace jusqu'au jour où le client répond au message — et découvre qu'il s'adressait à un robot, ou reçoit la relance alors qu'il vous a appelé la veille.",
        "La règle : automatisez ce qui est interne (tâches, alertes, mises à jour de champs) sans réserve ; soyez très prudent avec ce qui sort vers le client. Un e-mail automatique acceptable est un e-mail qui s'assume comme tel — un accusé de réception, une confirmation de rendez-vous — jamais un message qui imite une attention personnelle.",
      ]},
   ]},

  {"titre": "Déclencheur, condition, action : écrire une règle avant de la construire",
   "paras": [
     "Salesforce propose plusieurs outils d'automatisation (Flow, règles de workflow, processus). Leurs noms et leurs interfaces changent au fil des versions ; la logique, elle, ne change pas. Toute règle s'écrit en trois parties, et il faut l'écrire en français avant de la construire dans l'outil.",
     "<strong>Le déclencheur</strong> — quel événement réveille la règle ? Création d'un enregistrement, modification d'un champ, écoulement d'un délai, action de l'utilisateur.",
     "<strong>La condition</strong> — dans quels cas la règle s'applique-t-elle ? C'est la partie qu'on oublie, et l'oubli produit les automatisations qui se déclenchent en boucle ou sur des enregistrements non concernés.",
     "<strong>L'action</strong> — que se passe-t-il ? Créer une tâche, envoyer une notification, mettre à jour un champ, créer un enregistrement lié.",
     "Écrire ces trois lignes en français avant de toucher à l'outil vous fera abandonner une automatisation sur trois — celles dont la condition ne peut pas s'exprimer clairement. C'est un excellent taux de déchet : chacune de ces règles abandonnées aurait été une source de confusion durable.",
   ],
   "blocks": [
     {"type": "method", "titre": "concevoir et déployer une automatisation en six étapes",
      "steps": [
        "<strong>Écrivez la règle en français</strong> : « quand [déclencheur], si [condition], alors [action] ». Si vous n'y arrivez pas en une phrase, la règle est trop complexe : découpez-la ou renoncez.",
        "<strong>Cherchez la boucle.</strong> Si l'action modifie un champ qui est aussi un déclencheur, vous créez une boucle. C'est l'erreur technique la plus fréquente et la plus difficile à diagnostiquer après coup.",
        "<strong>Listez les exceptions</strong> et décidez explicitement de leur sort. Une exception non traitée devient une donnée fausse, pas un cas non couvert.",
        "<strong>Construisez dans un environnement de test</strong> (sandbox ou Developer Edition), jamais directement en production. Une automatisation mal calibrée peut modifier des milliers d'enregistrements en quelques secondes, et il n'y a pas d'annulation.",
        "<strong>Déployez sur un périmètre restreint</strong> — une équipe, un type d'affaire — pendant deux semaines. Observez, corrigez, puis étendez.",
        "<strong>Documentez</strong> : une ligne par automatisation dans un tableau partagé — nom, règle en français, date, auteur, raison. Sans cela, votre successeur n'osera plus rien modifier, et c'est ainsi qu'une instance devient ingérable.",
      ]},
     {"type": "exemple", "titre": "une règle bien écrite et sa version ratée",
      "paras": [
        "<em>Version ratée :</em> « quand une opportunité est modifiée, notifier le manager ». Pas de condition, déclencheur trop large. Résultat : le manager reçoit 200 notifications par jour et filtre tout dans un dossier qu'il ne lit pas. L'automatisation existe et ne sert à rien — le pire des deux mondes, puisqu'elle donne le sentiment que le sujet est traité.",
        "<em>Version corrigée :</em> « quand une opportunité <strong>passe à l'étape Négociation</strong> (déclencheur), <strong>si son montant dépasse 100 000 €</strong> (condition), <strong>notifier le directeur commercial et créer une tâche « valider la remise »</strong> (action) ». Trois à cinq déclenchements par semaine, chacun lu et suivi d'effet.",
        "La différence entre les deux versions n'est pas technique : c'est le fait d'avoir répondu à la question « qui doit faire quoi en recevant cela ? ». Une alerte qui n'appelle aucune action précise ne doit pas exister.",
      ]},
     {"type": "pitfall", "titre": "empiler les automatisations sans jamais en retirer",
      "paras": [
        "Les automatisations s'ajoutent, ne se retirent jamais, et finissent par interagir de façon imprévisible. Au bout de deux ans, plus personne n'ose modifier un champ de peur de déclencher quelque chose d'inconnu.",
        "Instaurez une revue annuelle : pour chaque automatisation, une question — « si je la supprime aujourd'hui, qui s'en apercevrait et en combien de temps ? ». Si la réponse est « personne », supprimez. Vous en retirerez systématiquement un tiers.",
      ]},
   ]},

  {"titre": "Un tableau de bord doit provoquer une décision",
   "paras": [
     "La plupart des tableaux de bord CRM sont des tableaux de contemplation : beaux, complets, consultés une fois par mois, et sans effet. Le test pour savoir si un indicateur mérite d'y figurer tient en une question : <strong>quelle décision prendrai-je différemment selon sa valeur ?</strong> Si vous ne pouvez pas y répondre, l'indicateur est décoratif, quelle que soit sa pertinence apparente.",
     "Ce test élimine généralement la moitié des indicateurs demandés. Le chiffre d'affaires cumulé depuis janvier, par exemple, est une information légitime mais ne déclenche aucune décision : on ne fait rien de différent selon qu'il vaut 2,1 ou 2,3 M€. En revanche, « nombre d'opportunités engagées sans activité depuis 15 jours » déclenche immédiatement une action nommée sur des affaires nommées.",
   ],
   "blocks": [
     {"type": "h3", "titre": "Trois familles d'indicateurs, trois usages",
      "paras": [
        "<strong>Les indicateurs d'activité</strong> mesurent ce que fait l'équipe : appels passés, rendez-vous tenus, propositions envoyées. Ils sont immédiatement disponibles et immédiatement manipulables — un commercial évalué sur le nombre d'appels passera des appels. À utiliser pour détecter une anomalie individuelle, jamais comme objectif.",
        "<strong>Les indicateurs d'avancement</strong> mesurent l'état du processus : conversion par étape, durée par étape, âge moyen du pipeline. Ce sont les plus utiles au pilotage, parce qu'ils sont difficiles à manipuler et qu'ils préviennent : ils bougent avant le chiffre d'affaires.",
        "<strong>Les indicateurs de résultat</strong> mesurent l'issue : chiffre d'affaires signé, taux de transformation global, panier moyen. Ils sont les seuls qui comptent vraiment et les seuls sur lesquels on ne peut plus agir quand on les découvre. Ils servent à évaluer, pas à piloter.",
        "Un bon tableau de bord mélange les trois dans cette proportion : un ou deux résultats en haut pour le cadrage, trois à quatre indicateurs d'avancement au centre — c'est là que se prennent les décisions — et l'activité en dernier, en accès à la demande plutôt qu'affichée en permanence.",
      ]},
     {"type": "method", "titre": "construire un tableau de bord commercial utile",
      "paras": ["Un tableau par audience : celui du commercial et celui de la direction n'ont ni le même contenu ni la même fréquence de lecture."],
      "steps": [
        "<strong>Nommez l'audience et la fréquence</strong> avant tout : « le commercial, chaque lundi matin » ou « le comité de direction, une fois par mois ». Un tableau pour tout le monde n'est lu par personne.",
        "<strong>Limitez-vous à six blocs.</strong> Au-delà, l'œil ne hiérarchise plus et le tableau devient une page de consultation, pas un outil de décision.",
        "<strong>Placez en haut à gauche l'indicateur qui déclenche le plus d'actions</strong> — généralement les anomalies du pipeline, pas le chiffre d'affaires. La position dit ce qui compte.",
        "<strong>Rendez chaque bloc cliquable vers la liste des enregistrements concernés.</strong> Un chiffre sans accès aux affaires derrière lui ne permet aucune action ; c'est ce détail qui sépare un tableau de bord d'un poster.",
        "<strong>Affichez systématiquement une comparaison</strong> : période précédente ou objectif. Un chiffre isolé n'est pas interprétable — 34 % de conversion n'est ni bon ni mauvais sans référence.",
        "<strong>Testez pendant un mois, puis retirez ce que personne n'a regardé.</strong> Salesforce permet de suivre la consultation des rapports ; servez-vous-en pour élaguer.",
      ]},
     {"type": "exemple", "titre": "le tableau de bord du lundi matin",
      "paras": [
        "Six blocs, pour un responsable commercial, consulté avant la revue hebdomadaire :",
        "<strong>1. Engagé du trimestre vs objectif</strong> (résultat, cadrage) — <strong>2. Opportunités à date de clôture dépassée</strong> : nombre et montant, cliquable (avancement, action immédiate) — <strong>3. Opportunités engagées sans activité depuis 15 jours</strong>, cliquable (avancement, c'est le bloc qui alimente la revue) — <strong>4. Conversion Proposition → Négociation sur 90 jours glissants, avec la valeur du trimestre précédent</strong> (avancement, tendance) — <strong>5. Affaires gagnées et perdues du mois avec motifs</strong> (résultat, apprentissage) — <strong>6. Nouvelles opportunités créées cette semaine</strong> (activité, alimentation du haut du pipeline).",
        "Chaque bloc répond à la question du test. Le bloc 2 déclenche des fermetures ou des reports justifiés ; le bloc 3 fixe l'ordre du jour de la revue ; le bloc 4 déclenche une action sur le processus si la tendance baisse deux trimestres de suite ; le bloc 6 alerte si le haut du pipeline se tarit, trois mois avant que le chiffre d'affaires n'en souffre.",
      ]},
     {"type": "pitfall", "titre": "le tableau de bord qui devient un instrument de surveillance",
      "paras": [
        "Un tableau affichant le nombre d'appels par commercial, projeté en réunion, produit exactement ce qu'il mesure : des appels courts et nombreux. C'est la loi de Goodhart — quand une mesure devient un objectif, elle cesse d'être une bonne mesure.",
        "Gardez les indicateurs d'activité au niveau de l'équipe pour le pilotage, et au niveau individuel pour les entretiens d'accompagnement, jamais projetés collectivement. Le coût d'un classement affiché n'est pas la vexation : c'est la dégradation silencieuse de la qualité des données, puisque chacun apprend à optimiser le chiffre plutôt que le travail.",
      ]},
   ]},

  {"titre": "Après la vente : la relation ne s'arrête pas à la signature",
   "paras": [
     "Les trois quarts de ce que contient un CRM concernent la conquête. C'est un déséquilibre coûteux : dans la plupart des activités B2B, l'essentiel de la marge vient du renouvellement et de l'extension chez des clients existants, dont l'acquisition est déjà payée.",
     "Suivre la relation après la vente demande peu de choses, mais ces choses doivent exister <strong>dans le CRM</strong> et non dans la tête du commercial ou dans un tableur du service client.",
     "<strong>Une date d'échéance ou de renouvellement</strong> sur le Compte, avec une opportunité de renouvellement créée automatiquement quelques mois avant. Un renouvellement qui se prépare trois semaines avant l'échéance est déjà en position défavorable.",
     "<strong>Les requêtes ouvertes visibles depuis le Compte.</strong> Appeler un client pour lui vendre une extension alors qu'il a deux réclamations non traitées est le meilleur moyen de perdre les deux sujets à la fois.",
     "<strong>Un signal de risque simple</strong>, même rudimentaire : baisse d'usage, absence de contact depuis six mois, changement d'interlocuteur principal. Ce dernier point est le plus prédictif de tous — le départ de votre interlocuteur principal chez un client est le premier facteur de non-renouvellement, et c'est une information que le CRM peut faire remonter automatiquement.",
   ],
   "blocks": [
     {"type": "method", "titre": "mettre en place un suivi client en quatre automatisations",
      "steps": [
        "<strong>Création anticipée du renouvellement</strong> : quand une opportunité est gagnée sur un contrat d'un an, créer automatiquement une opportunité de renouvellement à date de clôture J+10 mois, étape Qualification. Le renouvellement devient visible dans le pipeline dix mois à l'avance.",
        "<strong>Alerte contact inactif</strong> : quand un Compte client n'a aucune activité depuis 120 jours, créer une tâche « prendre des nouvelles » pour son propriétaire. Pas d'e-mail automatique au client : une tâche pour un humain.",
        "<strong>Alerte requêtes multiples</strong> : quand un Compte a trois requêtes ouvertes ou plus, notifier son propriétaire commercial. Il doit être au courant avant le client.",
        "<strong>Alerte changement d'interlocuteur</strong> : quand le Contact principal d'un Compte client est marqué inactif ou parti, créer une tâche de reprise de contact prioritaire. C'est l'automatisation au meilleur rendement de la liste.",
      ]},
     {"type": "exemple", "titre": "ce que coûte l'absence de suivi",
      "paras": [
        "Un éditeur de logiciel constate 22 % de non-renouvellement annuel. Analyse des comptes perdus sur douze mois : dans 61 % des cas, l'interlocuteur principal avait changé dans l'année, et personne ne l'avait su. Dans 40 % des cas, aucune activité n'était enregistrée sur le compte dans les six mois précédant l'échéance.",
        "Les quatre automatisations ci-dessus sont mises en place. Un an plus tard, le taux de non-renouvellement est à 14 %. Aucun produit n'a changé, aucun prix n'a bougé, aucun recrutement n'a été fait.",
        "Le mécanisme n'a rien de mystérieux : le CRM n'a pas retenu les clients, il a simplement rendu visible à temps une information que l'entreprise possédait déjà et n'exploitait pas. C'est en une phrase la valeur d'un CRM correctement tenu — et le résumé de ces trois modules.",
      ]},
   ]},

  {"titre": "Ce qui fait vivre un CRM dans la durée",
   "paras": [
     "Trois modules pour arriver ici : un modèle de données propre, un pipeline qui dit la vérité, une automatisation sobre et des tableaux de bord qui déclenchent des décisions. Reste la question qui décide de tout — pourquoi certaines entreprises tiennent cela pendant des années et d'autres retombent en six mois ?",
     "L'observation constante est que la différence n'est presque jamais technique. Elle tient à trois choses.",
     "<strong>Le CRM rend service à celui qui le remplit.</strong> C'est la condition principale. Tant qu'un commercial saisit pour que d'autres puissent le contrôler, il saisira le minimum. À partir du moment où il y trouve son historique, ses relances, ses chiffres, il saisit sans qu'on le lui demande. Chaque fois que vous ajoutez un champ obligatoire, posez la question : à qui sert ce champ ? Si la réponse n'est pas « à celui qui le remplit », au moins en partie, prévoyez qu'il sera mal rempli.",
     "<strong>Quelqu'un en est responsable.</strong> Pas un comité : une personne nommée, avec du temps identifié — souvent une demi-journée par semaine suffit. Un CRM sans propriétaire dérive en dix-huit mois, quels que soient les moyens investis au départ.",
     "<strong>Les décisions visibles s'appuient dessus.</strong> Si la direction pilote sur un tableur parallèle, tout le monde comprend que le CRM est un formulaire administratif, et il le devient. Inversement, une seule décision importante prise publiquement sur la foi d'un chiffre du CRM fait plus pour l'adoption que six mois de formation.",
   ],
   "blocks": [
     {"type": "pitfall", "titre": "croire que le problème est l'outil",
      "paras": [
        "Quand un CRM ne prend pas, la conclusion la plus fréquente est qu'il est mal adapté et qu'il faut en changer. Les migrations d'un CRM vers un autre pour ce motif se soldent presque toujours par la reproduction des mêmes symptômes sur un outil différent, deux ans et beaucoup d'argent plus tard.",
        "Avant d'envisager un changement d'outil, vérifiez les trois points ci-dessus. Dans la grande majorité des cas, le problème est un modèle de données mal posé, des étapes de pipeline invérifiables, ou l'absence d'un propriétaire — trois choses qu'aucun changement de logiciel ne corrige, et que vous savez maintenant traiter.",
      ]},
   ]},
 ],

 "etude_cas": {
   "titre": "Supprimer le point du lundi préparé à la main",
   "html": """
<p>Reprenons le second problème de la mise en situation : trois heures par semaine passées à recopier des chiffres du CRM dans un tableur, pour un document que personne n'utilise pour décider.</p>
<p><strong>Étape 1 — comprendre ce que le document sert réellement à faire.</strong> Avant d'automatiser un rapport, il faut savoir ce qu'on en attend. Question posée à son destinataire : « la semaine dernière, qu'avez-vous décidé après l'avoir lu ? ». La réponse est presque toujours « rien de précis », et c'est le vrai diagnostic. Deuxième question, plus utile : « qu'est-ce que vous aimeriez savoir chaque lundi et que vous n'avez pas ? ». Ici : quelles affaires risquent de glisser sur le trimestre, et pourquoi.</p>
<p><strong>Étape 2 — constater que le document ne répondait pas à cette attente.</strong> Le tableur contenait le chiffre d'affaires cumulé, le nombre d'affaires par commercial et le pipeline total. Aucun de ces trois chiffres ne dit quelles affaires risquent de glisser. Le document était donc à la fois coûteux et hors sujet — cas plus fréquent qu'on ne croit, et qui explique pourquoi l'automatiser tel quel aurait été une erreur : on aurait produit plus vite quelque chose d'inutile.</p>
<p><strong>Étape 3 — construire le tableau de bord autour de la vraie question.</strong> Six blocs, celui du lundi matin décrit plus haut. Le bloc central est « opportunités engagées sans activité depuis 15 jours », cliquable vers la liste des affaires. C'est celui qui répond à la question posée à l'étape 1.</p>
<p><strong>Étape 4 — automatiser l'alimentation, pas le document.</strong> Deux automatisations soutiennent le tableau : une tâche de relance créée sept jours après le passage en Proposition, et une notification au responsable quand une opportunité engagée dépasse quinze jours sans activité. Les données du tableau se maintiennent ainsi d'elles-mêmes, sans que personne n'ait à « préparer » quoi que ce soit.</p>
<p><strong>Étape 5 — supprimer le tableur, et le dire.</strong> Point important et souvent négligé : un rapport manuel ne s'éteint pas tout seul, il faut annoncer explicitement qu'il s'arrête et à quelle date. Sinon il continue en parallèle « au cas où », et vous avez ajouté un tableau de bord à une charge de travail au lieu de l'avoir remplacée.</p>
<p><strong>Résultat à trois mois.</strong> Trois heures hebdomadaires libérées. Mais l'effet principal est ailleurs : la réunion du lundi a changé de nature. Elle ne commence plus par la lecture d'un état des lieux, elle commence par une liste de six affaires nommées à traiter. Sa durée est passée de 75 à 30 minutes et elle produit des décisions.</p>
<p><strong>La leçon transposable.</strong> On n'automatise pas un rapport existant : on part de la décision à prendre, on construit l'indicateur qui la déclenche, et on supprime ce qui ne sert plus. Automatiser un document inutile ne fait que le rendre inutile plus vite — c'est le piège le plus courant de tout ce module.</p>
"""},

 "checklist": {
   "titre": "Checklist — automatisation et pilotage",
   "items": [
     "Chaque automatisation remplit les trois conditions : répétitive, sans jugement, dont l'échec serait visible",
     "Aucune décision commerciale (fermeture, changement d'étape) n'est automatisée",
     "Chaque règle est écrite en français — quand / si / alors — avant d'être construite",
     "Aucune action d'une règle ne modifie un champ qui est aussi son déclencheur",
     "Toute automatisation a été testée hors production avant déploiement",
     "Le déploiement s'est fait sur un périmètre restreint pendant deux semaines",
     "Un tableau partagé documente chaque automatisation : règle, date, auteur, raison",
     "Une revue annuelle supprime les automatisations que personne ne remarquerait",
     "Aucun e-mail automatique sortant n'imite une attention personnelle",
     "Chaque indicateur affiché passe le test : quelle décision change selon sa valeur ?",
     "Chaque tableau de bord a une audience et une fréquence de consultation nommées",
     "Aucun tableau de bord ne dépasse six blocs",
     "Chaque bloc est cliquable vers la liste des enregistrements concernés",
     "Chaque chiffre est affiché avec une comparaison : période précédente ou objectif",
     "Les indicateurs d'activité individuels ne sont jamais projetés collectivement",
     "Une date de renouvellement existe sur les comptes clients",
     "Les requêtes ouvertes sont visibles depuis le Compte par le commercial",
     "Un changement d'interlocuteur principal déclenche une tâche de reprise de contact",
     "Une personne nommée est responsable du CRM, avec du temps identifié",
     "Les rapports manuels remplacés ont été explicitement arrêtés, à une date annoncée",
   ]},

 "glossaire": [
   ("Automatisation", "Règle exécutée par le système sans intervention humaine. Doit être répétitive, sans jugement, et son échec doit être détectable."),
   ("Flow", "Principal outil d'automatisation de Salesforce, permettant de définir déclencheurs, conditions et actions. Les outils antérieurs (règles de workflow, Process Builder) suivent la même logique."),
   ("Déclencheur", "Événement qui réveille une règle d'automatisation : création, modification d'un champ, délai écoulé."),
   ("Condition", "Filtre déterminant les cas où la règle s'applique. Partie la plus souvent oubliée, à l'origine des automatisations parasites."),
   ("Boucle d'automatisation", "Situation où l'action d'une règle modifie un champ qui déclenche cette même règle ou une autre. Cause fréquente de comportements incompréhensibles."),
   ("Sandbox", "Copie de l'environnement de production servant aux tests. Passage obligé avant tout déploiement d'automatisation."),
   ("Indicateur d'activité", "Mesure de ce que fait l'équipe (appels, rendez-vous). Facilement manipulable : à utiliser pour détecter, jamais comme objectif."),
   ("Indicateur d'avancement", "Mesure de l'état du processus (conversion par étape, durée, âge du pipeline). Le plus utile au pilotage car il bouge avant le résultat."),
   ("Indicateur de résultat", "Mesure de l'issue (chiffre d'affaires, taux de transformation). Sert à évaluer, pas à piloter : quand on le découvre, on ne peut plus agir dessus."),
   ("Loi de Goodhart", "Principe selon lequel une mesure cesse d'être une bonne mesure dès qu'elle devient un objectif. Justifie de ne pas afficher les indicateurs d'activité individuels."),
   ("Opportunité de renouvellement", "Opportunité créée à l'avance sur un contrat arrivant à échéance, pour que le renouvellement se prépare plusieurs mois avant."),
   ("Signal de risque", "Indice de dégradation d'une relation client : absence d'activité, requêtes multiples, changement d'interlocuteur principal — le plus prédictif des trois."),
 ],

 "retenir": [
   "N'automatisez que ce qui est répétitif, sans jugement, et dont l'échec serait visible. Les trois conditions sont cumulatives.",
   "Une décision commerciale ne s'automatise jamais : automatisez l'alerte, laissez la décision à un humain.",
   "Écrivez toute règle en français — quand / si / alors — avant de la construire. Un tiers des règles seront abandonnées à ce stade, et c'est un bon taux.",
   "La condition est la partie qu'on oublie ; son absence produit les alertes que personne ne lit plus.",
   "Une alerte qui n'appelle aucune action précise ne doit pas exister.",
   "Ne construisez jamais une automatisation directement en production : elle peut modifier des milliers d'enregistrements sans annulation possible.",
   "Documentez chaque automatisation en une ligne : sans cela, votre successeur n'osera plus rien modifier.",
   "Automatisez sans réserve ce qui est interne ; soyez très prudent avec ce qui sort vers le client, et n'imitez jamais une attention personnelle.",
   "Le test d'un indicateur : quelle décision prendrai-je différemment selon sa valeur ? Sinon, il est décoratif.",
   "Les indicateurs d'avancement sont les plus utiles au pilotage : difficiles à manipuler, ils bougent avant le chiffre d'affaires.",
   "Six blocs maximum par tableau de bord, chacun cliquable vers les enregistrements concernés et assorti d'une comparaison.",
   "N'affichez jamais collectivement les indicateurs d'activité individuels : vous obtiendrez ce que vous mesurez, pas ce que vous voulez.",
   "L'essentiel de la marge vient des clients existants : une date de renouvellement, les requêtes visibles et un signal de risque suffisent à la protéger.",
   "Le changement d'interlocuteur principal est le premier facteur de non-renouvellement, et le CRM peut le signaler automatiquement.",
   "N'automatisez pas un rapport existant : partez de la décision à prendre, construisez l'indicateur qui la déclenche, supprimez le reste — et annoncez la suppression.",
   "Un CRM tient dans la durée s'il rend service à celui qui le remplit, s'il a un propriétaire nommé, et si des décisions visibles s'appuient dessus.",
   "Quand un CRM ne prend pas, le problème est presque toujours le modèle de données, les étapes ou le propriétaire — jamais l'outil.",
 ],

 "exercices": [
  {"titre": "Trier l'automatisable", "niveau": "Débutant",
   "enonce": [
     "Pour chacune des six demandes ci-dessous, indiquez si vous l'automatisez telle quelle, si vous la transformez, ou si vous la refusez — en justifiant par les trois conditions.",
     "1. « Envoyer un e-mail de remerciement personnalisé au client 48 h après chaque rendez-vous. » — 2. « Créer une tâche de relance 7 jours après l'envoi d'une proposition. » — 3. « Passer automatiquement en Perdue toute opportunité sans activité depuis 90 jours. » — 4. « Notifier le manager à chaque modification d'une opportunité. » — 5. « Remplir automatiquement le secteur d'activité d'un compte à partir de son nom de domaine. » — 6. « Créer une opportunité de renouvellement 10 mois après chaque affaire gagnée sur contrat annuel. »",
   ],
   "corrige": """
<p><strong>1. E-mail de remerciement « personnalisé » — refus, ou transformation.</strong> Répétitive : oui. Sans jugement : non — le contenu pertinent dépend de ce qui s'est dit. Échec visible : non. Surtout, elle imite une attention personnelle, ce qui se retourne dès que le client répond ou vous a appelé la veille. <em>Transformation acceptable :</em> une tâche « envoyer un mot de suivi » pour le commercial à J+2. L'automatisation porte sur le rappel, pas sur le message.</p>
<p><strong>2. Tâche de relance à J+7 — automatiser telle quelle.</strong> Les trois conditions sont remplies : parfaitement répétitive, aucun jugement, et son absence se verrait immédiatement (plus de relances planifiées). C'est le cas d'école.</p>
<p><strong>3. Fermeture automatique à 90 jours — refus, transformation obligatoire.</strong> Fermer une affaire est une décision commerciale. Automatisée, elle détruirait des affaires vivantes mais lentes — cycles longs, secteur public — et pire, elle apprendrait aux commerciaux à faire une modification cosmétique tous les 89 jours pour l'éviter. <em>Transformation :</em> alerte au commercial à 60 jours et entrée automatique dans le rapport de revue de pipeline. La décision reste humaine, mais elle est provoquée.</p>
<p><strong>4. Notification à chaque modification — refus en l'état.</strong> Le déclencheur est trop large et la condition absente. Le manager filtrera tout au bout d'une semaine, et l'automatisation donnera l'illusion trompeuse que le sujet est couvert. <em>Transformation :</em> définir ce que le manager doit réellement savoir — par exemple, changement d'étape sur une affaire de plus de 100 k€, ou recul d'étape quel que soit le montant. Un recul d'étape est d'ailleurs l'information la plus utile et la moins souvent remontée.</p>
<p><strong>5. Remplissage automatique du secteur — piège.</strong> Techniquement faisable, et pourtant à refuser dans cette forme. La condition « sans jugement » n'est pas remplie : un nom de domaine ne détermine pas un secteur de façon fiable, et l'automatisation produirait des données <em>fausses</em> — bien pires que des données vides, puisqu'invisibles. Elle échoue aussi à la troisième condition : personne ne s'apercevrait qu'elle se trompe. <em>Alternative :</em> pré-remplir la valeur en proposition modifiable à la création, avec un marquage de l'origine. Une suggestion n'est pas une donnée.</p>
<p><strong>6. Opportunité de renouvellement à J+10 mois — automatiser telle quelle.</strong> Répétitive, sans jugement (créer n'est pas décider), et son échec serait visible puisque le pipeline de renouvellement se viderait. Une des automatisations au meilleur rendement, précisément parce qu'elle rend visible longtemps à l'avance quelque chose qu'on traite habituellement trop tard.</p>
<p><strong>Le fil conducteur des six réponses :</strong> les cas refusés le sont soit parce qu'ils automatisent un jugement (3, 5), soit parce qu'ils simulent une attention humaine (1), soit parce qu'ils manquent de condition (4). Les cas acceptés créent tous un <em>rappel</em> ou une <em>structure</em>, jamais une décision ni une donnée.</p>
"""},

  {"titre": "Concevoir un tableau de bord pour une audience", "niveau": "Intermédiaire",
   "enonce": [
     "Votre directeur général vous demande « un tableau de bord commercial ». Il le consultera une fois par mois, avant le comité de direction, et son rôle est d'arbitrer des moyens : recruter ou non, investir en marketing ou non, agir ou non sur les prix.",
     "Concevez son tableau de bord — six blocs maximum — et expliquez pourquoi vous écartez trois indicateurs qu'il vous demandera probablement.",
   ],
   "corrige": """
<p><strong>Point de départ : ce ne sont pas les mêmes décisions.</strong> Le tableau du responsable commercial sert à agir sur des affaires nommées cette semaine ; celui du DG sert à arbitrer des moyens sur plusieurs mois. Un même indicateur peut donc figurer dans l'un et pas dans l'autre. Concevoir « un » tableau de bord commercial sans préciser l'audience est la première erreur.</p>
<p><strong>Les six blocs.</strong></p>
<p><em>1. Chiffre d'affaires signé sur le trimestre, contre objectif et contre même trimestre de l'année précédente</em> (résultat). Le cadrage indispensable. Il ne déclenche rien seul, mais il conditionne la lecture de tout le reste — c'est la seule exception admise au test de la décision.</p>
<p><em>2. Prévision du trimestre en cours : Engagé et cible, avec l'écart constaté sur les quatre derniers trimestres</em> (avancement). Bloc central. Il permet d'arbitrer un engagement de dépense, et l'historique d'écart lui donne sa crédibilité : une prévision sans historique de fiabilité n'est pas décisionnable.</p>
<p><em>3. Nouvelles opportunités créées par mois sur 12 mois glissants</em> (activité, mais au niveau de l'entreprise). C'est l'indicateur avancé du chiffre d'affaires : il baisse trois à six mois avant lui. C'est le bloc qui déclenche une décision d'investissement marketing, et il doit être lu comme une tendance, jamais comme une valeur ponctuelle.</p>
<p><em>4. Taux de conversion par étape, trimestre courant contre précédent</em> (avancement). Déclenche l'arbitrage entre « il nous faut plus d'affaires » et « il nous faut mieux traiter celles que nous avons » — deux décisions de moyens opposées, que rien d'autre ne permet de départager.</p>
<p><em>5. Répartition des motifs de perte sur 12 mois</em> (résultat, apprentissage). C'est le bloc qui informe le produit et la politique de prix. Précaution à afficher : rappeler que « prix trop élevé » est structurellement surreprésenté dans les motifs déclaratifs.</p>
<p><em>6. Chiffre d'affaires nouveaux clients contre clients existants, et taux de renouvellement</em> (résultat). Arbitrage entre effort de conquête et effort de fidélisation. Presque toujours absent des tableaux de bord, et presque toujours celui qui change le plus une allocation de moyens.</p>
<p><strong>Trois indicateurs à écarter, et comment le dire.</strong></p>
<p><em>a) Le classement des commerciaux par chiffre d'affaires.</em> Demandé dans neuf cas sur dix. Argument : il ne sert aucun arbitrage de moyens — les décisions individuelles relèvent du responsable commercial, dans un autre cadre. Argument décisif : projeté en comité, il pousse chacun à optimiser son chiffre affiché plutôt que la qualité de ses données, et vous perdez la fiabilité de tout le reste du tableau. Proposez-le en accès à la demande, hors comité.</p>
<p><em>b) Le nombre d'appels et de rendez-vous.</em> Indicateur d'activité pur, aisément manipulable, et sans lien avec un arbitrage de moyens. S'il indique quelque chose d'utile, cela apparaîtra dans le bloc 3 sous une forme non manipulable.</p>
<p><em>c) La valeur totale du pipeline.</em> Le plus difficile à écarter parce qu'il paraît fondamental. Argument : ce chiffre agrège des affaires dont les probabilités sont incomparables ; il monte quand on qualifie mal et baisse quand on assainit, ce qui en fait un indicateur au signal inversé. La prévision du bloc 2 dit la même chose en mieux. Si le DG y tient, affichez-le décomposé par étape — jamais en total unique.</p>
<p><strong>La règle générale à retenir de l'exercice :</strong> refuser un indicateur demandé par un dirigeant ne se fait pas en invoquant une bonne pratique, mais en montrant quelle décision il ne permet pas de prendre et quel bloc la permet mieux. Un refus argumenté par la décision passe presque toujours ; un refus argumenté par la méthode, presque jamais.</p>
"""},

  {"titre": "Plan de relance d'un CRM abandonné", "niveau": "Avancé",
   "enonce": [
     "Deux ans après son déploiement, le CRM est déserté : la saisie n'est faite qu'en fin de mois, la direction pilote sur un tableur, et deux personnes réclament un changement d'outil. Vous avez trois mois et aucun budget de licence supplémentaire.",
     "Construisez votre plan. Traitez explicitement la demande de changement d'outil et dites à quoi vous saurez, à trois mois, que le redressement fonctionne.",
   ],
   "corrige": """
<p><strong>D'abord, traiter la demande de changement d'outil — mais sans la balayer.</strong> Ne répondez pas « le problème n'est pas l'outil », même si c'est presque toujours vrai : vous passeriez pour quelqu'un qui défend l'existant. Répondez : « avant de migrer, listons ce qui ne va pas ; si ce sont des manques fonctionnels, la migration se justifie ; si ce sont des symptômes de données et d'usage, ils migreront avec nous ». Puis faites réellement la liste avec les demandeurs. Dans la quasi-totalité des cas, elle contient des symptômes — « on ne trouve rien », « les chiffres sont faux », « c'est trop long à remplir » — et non des manques. Cette liste devient votre feuille de route, et les demandeurs deviennent vos alliés parce qu'elle est faite de leurs mots.</p>
<p><strong>Mois 1 — comprendre, et ne rien changer.</strong></p>
<p>Six entretiens de 20 minutes : quatre utilisateurs, dont les deux mécontents, le responsable commercial, le DG. Une question chacun : « qu'est-ce qui vous fait perdre du temps ? » pour les uns, « sur quoi décidez-vous aujourd'hui ? » pour les autres. Résistez à la tentation de corriger quoi que ce soit pendant ce mois : chaque correction faite avant d'avoir compris consomme votre crédit de changement, qui est limité.</p>
<p>En parallèle, les six mesures de santé du module 1 et du module 2 : complétude, doublons, orphelins, fraîcheur, zombies, adoption. Datez-les — ce sont vos points de départ, sans lesquels vous ne pourrez rien démontrer à trois mois.</p>
<p><strong>Mois 2 — rendre service avant de demander.</strong> C'est le principe central du redressement, et l'ordre est non négociable : <strong>on ne demande rien de nouveau tant qu'on n'a pas rendu quelque chose</strong>. Trois actions dans cet ordre :</p>
<p>a) <em>Retirer.</em> Supprimez les champs obligatoires qui ne servent à personne. Sur une instance de deux ans, on en retire toujours plusieurs. Chaque champ retiré est un gain immédiat et visible pour l'utilisateur — et c'est la première fois depuis longtemps que le CRM lui donne quelque chose.</p>
<p>b) <em>Donner.</em> Construisez à chaque commercial sa vue personnelle : ses affaires, ses relances du jour, son historique par compte. Pas un tableau de contrôle : son outil de travail quotidien. C'est ici que se joue l'adoption, bien plus que dans la formation.</p>
<p>c) <em>Alléger.</em> Deux ou trois automatisations qui suppriment de la saisie répétitive — tâche de relance automatique, création anticipée du renouvellement. Choisissez celles dont le bénéfice est ressenti par celui qui saisit, pas par celui qui contrôle.</p>
<p><strong>Mois 3 — déplacer la décision dans l'outil.</strong> C'est l'étape que la plupart des plans de relance omettent, et sans elle tout le reste retombe.</p>
<p>a) Redéfinir les étapes du pipeline <em>avec</em> l'équipe (module 2), critères vérifiables. Puis le nettoyage annoncé des affaires zombies.</p>
<p>b) Construire le tableau de bord du DG et obtenir de lui qu'il abandonne son tableur, publiquement et à une date annoncée. Sans cet abandon explicite, rien ne tient : tant que la décision se prend ailleurs, la saisie restera un formulaire administratif.</p>
<p>c) Instaurer la revue de pipeline hebdomadaire sur les anomalies. Le rituel est ce qui fait vivre l'ensemble entre deux plans de relance.</p>
<p>d) Nommer un propriétaire du CRM avec une demi-journée par semaine identifiée. Sans propriétaire, vous relancerez à nouveau dans dix-huit mois.</p>
<p><strong>Ce à quoi vous saurez que ça marche — dans l'ordre d'apparition.</strong></p>
<p><em>Semaine 4 :</em> le premier signal est qualitatif — quelqu'un vous demande spontanément un champ ou une vue. Cela signifie que l'outil est redevenu le sien. C'est le meilleur indicateur précoce, et il ne se mesure pas.</p>
<p><em>Semaine 6-8 :</em> la <strong>fraîcheur</strong> s'améliore — part des opportunités modifiées dans les 7 derniers jours. C'est le premier indicateur chiffré à bouger, parce qu'il mesure l'usage réel et non le résultat.</p>
<p><em>Semaine 8-10 :</em> la saisie cesse d'être concentrée en fin de mois. Mesurez la répartition des créations d'activités par jour du mois : une courbe qui s'aplatit vaut tous les discours d'adoption.</p>
<p><em>Semaine 12 :</em> une décision visible a été prise sur la foi d'un chiffre du CRM, en réunion, devant tout le monde. C'est le seul critère qui compte réellement, et il ne se décrète pas — il se prépare en s'assurant que le chiffre en question est juste.</p>
<p><strong>Ce qui n'est pas un bon signal :</strong> une hausse du nombre d'enregistrements créés. On peut remplir un CRM sans l'utiliser, et c'est même exactement ce que produit une pression à la saisie. Ne prenez jamais le volume pour de l'adoption.</p>
"""},
 ],

 "ressources": [
   "<strong>Salesforce Trailhead</strong> — parcours « Flow Builder » et « Reports &amp; Dashboards » : la voie la plus rapide pour construire ses premières automatisations et ses premiers tableaux de bord sans risque.",
   "<strong>Un environnement Developer Edition</strong> (developer.salesforce.com/signup) — indispensable pour tester toute automatisation avant production. Le seul conseil technique de ce module qu'il ne faut jamais négliger.",
   "<strong>Les modules 1 et 2 de cette formation</strong> — l'automatisation et les tableaux de bord n'ont de valeur que sur un modèle de données propre et un pipeline sincère. En cas de doute, revenez-y avant d'automatiser.",
   "<strong>« Measure What Matters », John Doerr</strong> — sur la distinction entre indicateurs qui déclenchent des décisions et indicateurs qui décrivent. Pas un livre sur le CRM, mais le meilleur appui pour arbitrer ce qu'on affiche.",
 ],
}

QUIZ = {
 "crm-relation-client/module-3": {
  "module_id": "formation-crm-relation-client-module-3",
  "version": "2.0", "last_verified": "2026-09-02",
  "questions": [
   {"id":"q1","question":"Faut-il automatiser le passage en Perdue d'une opportunité inactive depuis 90 jours ?",
    "choices":[{"key":"a","text":"Oui, cela garantit un pipeline toujours propre"},
               {"key":"b","text":"Non : fermer est une décision commerciale. On automatise l'alerte, pas la décision"},
               {"key":"c","text":"Oui, à condition d'en informer le commercial par e-mail"}],
    "correct_answer":"b","feedback":"Automatisée, la règle détruirait des affaires vivantes mais lentes, et apprendrait aux commerciaux à faire une modification cosmétique tous les 89 jours."},
   {"id":"q2","question":"Quelle partie d'une règle d'automatisation est le plus souvent oubliée ?",
    "choices":[{"key":"a","text":"Le déclencheur"},
               {"key":"b","text":"La condition"},
               {"key":"c","text":"L'action"}],
    "correct_answer":"b","feedback":"Son absence produit les alertes trop larges : le manager en reçoit deux cents par jour et les filtre dans un dossier qu'il ne lit pas."},
   {"id":"q3","question":"Quel test permet de décider si un indicateur mérite sa place dans un tableau de bord ?",
    "choices":[{"key":"a","text":"Est-il facile à calculer automatiquement ?"},
               {"key":"b","text":"La direction l'a-t-elle demandé ?"},
               {"key":"c","text":"Quelle décision prendrai-je différemment selon sa valeur ?"}],
    "correct_answer":"c","feedback":"Ce test élimine généralement la moitié des indicateurs demandés — le chiffre d'affaires cumulé, par exemple, est légitime mais ne déclenche aucune action."},
   {"id":"q4","question":"Pourquoi ne pas projeter en réunion le nombre d'appels par commercial ?",
    "choices":[{"key":"a","text":"Parce que la donnée est difficile à collecter de façon fiable"},
               {"key":"b","text":"Parce qu'une mesure devenue objectif cesse d'être une bonne mesure : on obtient des appels courts et nombreux"},
               {"key":"c","text":"Parce que le règlement intérieur l'interdit généralement"}],
    "correct_answer":"b","feedback":"C'est la loi de Goodhart. Le coût réel n'est pas la vexation, c'est la dégradation silencieuse de la qualité des données."},
   {"id":"q5","question":"Quel signal prédit le mieux le non-renouvellement d'un client ?",
    "choices":[{"key":"a","text":"Le changement de l'interlocuteur principal chez le client"},
               {"key":"b","text":"Une hausse du nombre de connexions au produit"},
               {"key":"c","text":"Un délai de paiement allongé sur la dernière facture"}],
    "correct_answer":"a","feedback":"C'est le premier facteur de non-renouvellement, et le CRM peut le signaler automatiquement par une tâche de reprise de contact."},
   {"id":"q6","question":"Un CRM est déserté deux ans après son déploiement. Par quoi commencer ?",
    "choices":[{"key":"a","text":"Par une nouvelle session de formation des utilisateurs"},
               {"key":"b","text":"Par retirer des champs obligatoires inutiles et donner à chacun sa vue de travail"},
               {"key":"c","text":"Par rendre la saisie obligatoire avant la validation des commissions"}],
    "correct_answer":"b","feedback":"On ne demande rien de nouveau tant qu'on n'a pas rendu quelque chose. Un CRM tient s'il rend service à celui qui le remplit."},
  ]},
}

for k, m in M.items():
    w, full = build(k, m)
    print(f"{k:30s} cours: {w} mots | page: {full} mots")
for k, q in QUIZ.items():
    p = os.path.join("/tmp/out_v2", k, "quiz.json")
    os.makedirs(os.path.dirname(p), exist_ok=True)
    json.dump(q, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    open(p, "a", encoding="utf-8").write("\n")
    print(f"{k}: quiz {len(q['questions'])} questions")
