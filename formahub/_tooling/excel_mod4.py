#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, json, os
sys.path.insert(0, "/tmp")
from fh_builder import build

M = {}
QUIZ = {}
FORM = "Excel &amp; analyse de données appliquée"

M["excel-analyse-donnees/module-4"] = {
 "formation": FORM,
 "titre": "Du Tableau au Tableau de Bord : Représenter, Contrôler, Partager",
 "num": 4, "total": 4, "duree": "75 min", "niveau": "Intermédiaire",
 "module_id": "formation-excel-analyse-donnees-module-4",
 "situation": [
   "Votre rapport est automatisé. Huit minutes le premier lundi du mois, quatre tableaux croisés dynamiques justes, des contrôles qui s'évaluent seuls. Techniquement, le travail est fait.",
   "Deux choses vous disent qu'il ne l'est pas. La première : en comité de direction, personne n'ouvre le fichier. On vous demande de « dire l'essentiel », et vous le dites de mémoire, ce qui signifie que quatre tableaux et une journée de construction ont produit un commentaire oral de deux minutes.",
   "La seconde est plus sérieuse. Le mois dernier, un chiffre présenté en comité s'est révélé faux — une région dont l'export avait été rejoué deux fois. Le contrôle existait, dans l'onglet Contrôles, en cellule B7. Personne ne l'avait regardé, vous compris, parce qu'il était huit heures moins le quart et que le fichier « s'était toujours bien comporté ».",
   "Ce module traite de ces deux problèmes, qui n'en font qu'un : un chiffre juste que personne ne lit et un chiffre faux que personne ne détecte échouent de la même façon. Il s'agit de rendre le résultat lisible et l'anomalie visible — et de savoir reconnaître le moment où Excel n'est plus l'outil adapté.",
 ],
 "objectifs": [
   "Choisir le type de graphique à partir de la question posée, et non de l'esthétique",
   "Repérer et éviter les six constructions graphiques qui trompent le lecteur",
   "Construire un tableau de bord d'une page organisé autour des décisions à prendre",
   "Mettre en place les contrôles qui rendent une anomalie impossible à ignorer",
   "Diffuser un fichier sans en perdre la maîtrise ni casser sa mise en forme",
   "Reconnaître les cinq signaux qui indiquent qu'Excel n'est plus le bon outil",
 ],
 "sections": [
  {"titre": "Le graphique découle de la question, jamais de l'esthétique",
   "paras": [
     "Le choix d'un graphique n'est pas une affaire de goût, et c'est la première chose à admettre. Il découle de la question posée, et il n'y a que quatre grandes questions en analyse courante.",
     "<strong>Une évolution dans le temps</strong> appelle une <em>courbe</em>. Le temps se met en abscisse, orienté de gauche à droite, et la ligne rend visible la continuité — c'est justement ce qu'on veut voir. Un histogramme pour une série temporelle longue fonctionne mais fatigue l'œil ; il reste préférable pour un petit nombre de périodes comparées comme des blocs, quatre trimestres par exemple.",
     "<strong>Une comparaison entre catégories</strong> appelle des <em>barres horizontales</em>, triées par valeur décroissante. L'horizontalité permet des libellés lisibles, ce qui règle le problème des noms de catégories tronqués ou inclinés à 45 degrés. Le tri par valeur est ce qui fait le travail : il transforme un tableau en classement, et un classement se lit sans effort.",
     "<strong>Une répartition en parts d'un tout</strong> appelle des <em>barres empilées à 100 %</em> ou, mieux dans la plupart des cas, des barres simples avec le pourcentage en étiquette. Le camembert n'est acceptable que pour deux ou trois parts nettement différentes ; au-delà, l'œil humain compare mal des angles, et le graphique devient décoratif.",
     "<strong>Une relation entre deux variables</strong> appelle un <em>nuage de points</em>. C'est le graphique le plus sous-employé en entreprise, alors qu'il répond à des questions qu'aucun autre ne traite : les clients qui commandent le plus souvent sont-ils ceux qui dépensent le plus ? Le délai de livraison est-il lié au montant ?",
     "Une règle de conception domine toutes les autres : <strong>le titre du graphique doit énoncer la conclusion, pas décrire le contenu</strong>. « CA par catégorie » est une étiquette ; « Le mobilier recule de 18 % au T4, seul segment en baisse » est un titre. Le second fait le travail du lecteur ; le premier le lui laisse, et le lecteur ne le fera pas.",
   ],
   "blocks": [
     {"type": "method", "titre": "construire un graphique lisible en sept gestes",
      "steps": [
        "<strong>Écrivez d'abord la conclusion</strong> en une phrase. Si vous n'y arrivez pas, le graphique n'a pas encore de raison d'exister — vous êtes encore en exploration, et un TCD suffit.",
        "<strong>Choisissez le type selon la question</strong>, parmi les quatre familles ci-dessus. Ne partez jamais de la galerie de graphiques : elle propose des formes, pas des réponses.",
        "<strong>Triez les données</strong> quand l'axe n'est pas temporel. Un graphique en barres non trié gaspille l'essentiel de son pouvoir explicatif.",
        "<strong>Retirez tout ce qui n'informe pas</strong> : quadrillage, bordures, effets, dégradés, légende à une seule série, axe secondaire décoratif. Chaque élément supprimé rend les autres plus lisibles.",
        "<strong>Étiquetez directement</strong> plutôt que par une légende dès que vous avez trois séries ou moins : le nom de la série au bout de sa courbe évite au lecteur l'aller-retour entre le graphique et sa légende.",
        "<strong>Mettez la conclusion en titre</strong>, et employez la couleur pour souligner ce dont parle ce titre — une seule série ou une seule barre en couleur, tout le reste en gris. C'est le geste qui distingue un graphique d'un tableau dessiné.",
        "<strong>Faites le test des cinq secondes</strong> : montrez le graphique à quelqu'un cinq secondes, retirez-le, demandez ce qu'il a compris. S'il ne restitue pas votre titre, le graphique ne dit pas ce que vous croyez.",
      ]},
     {"type": "exemple", "titre": "le même chiffre, trois graphiques, trois messages",
      "paras": [
        "Donnée : le chiffre d'affaires mensuel de six catégories sur vingt-quatre mois.",
        "<em>Six courbes superposées.</em> Illisible dès la quatrième série. C'est pourtant la construction produite par défaut quand on sélectionne toute la plage et qu'on insère une courbe. Elle ne répond à aucune question précise.",
        "<em>Une courbe en couleur, cinq en gris clair.</em> La même donnée, avec Mobilier en évidence. Le message devient immédiat : cette catégorie décroche à partir du dixième mois quand les autres restent stables. Aucune information n'a été retirée, seule la hiérarchie visuelle a changé.",
        "<em>Barres horizontales de l'évolution en pourcentage T4 contre T3, triées.</em> Six barres, une seule négative et nettement plus longue. Le message est encore plus direct, mais l'information temporelle a disparu : on ne voit plus si le recul est brutal ou progressif.",
        "Le troisième convient à une diapositive de comité, le deuxième à un rapport écrit, le premier à rien. Le choix ne dépend pas de la donnée mais de <strong>ce que le lecteur doit pouvoir faire après avoir regardé</strong>.",
      ]},
   ]},

  {"titre": "Six constructions qui trompent le lecteur",
   "paras": [
     "Un graphique peut être exact et trompeur : toutes les valeurs sont justes, et la conclusion que le lecteur en tire est fausse. Six constructions produisent cet effet, et elles apparaissent le plus souvent sans intention de tromper — ce sont les options par défaut ou les réflexes de mise en forme.",
     "<strong>1. L'axe des ordonnées tronqué.</strong> Un axe qui commence à 95 au lieu de 0 transforme une variation de 3 % en une falaise. Excel tronque automatiquement quand les valeurs sont proches. La règle : pour un graphique en <em>barres</em>, l'axe part de zéro sans exception, parce que le lecteur compare des longueurs. Pour une <em>courbe</em>, où l'on lit une variation et non une longueur, un axe tronqué est acceptable à condition d'être signalé — mais soyez conscient qu'il amplifie tout.",
     "<strong>2. Le camembert à sept parts.</strong> L'œil compare mal des angles, et très mal des angles voisins. Sept parts dont quatre entre 10 % et 15 % ne se hiérarchisent pas visuellement. Un camembert en trois dimensions ajoute une distorsion supplémentaire : la part située à l'avant paraît plus grande. Aucune version tridimensionnelle d'un graphique n'améliore jamais sa lisibilité.",
     "<strong>3. Le double axe.</strong> Deux séries d'unités différentes sur un même graphique, chacune avec son axe. Le problème est que <em>l'échelle de chaque axe est arbitraire</em> : en la modifiant, on fait apparaître ou disparaître une corrélation à volonté. Un double axe suggère toujours une relation, qu'elle existe ou non. Deux graphiques empilés partageant le même axe temporel disent la même chose sans induire quoi que ce soit.",
     "<strong>4. La moyenne présentée seule.</strong> « Délai moyen de résolution : 8,4 jours » ne dit rien d'utile si la médiane est à 3 jours. La moyenne est tirée par les valeurs extrêmes, et une distribution asymétrique — ce que sont la plupart des distributions en entreprise — la rend non représentative. Affichez toujours la moyenne accompagnée de la médiane, ou mieux, d'une distribution.",
     "<strong>5. Le pourcentage sans effectif.</strong> « 60 % de satisfaction dans la région Est » n'a pas le même poids selon qu'il porte sur 500 réponses ou sur 5. Un pourcentage sans son dénominateur est une information incomplète, et c'est la construction la plus fréquemment utilisée pour appuyer une conclusion fragile — souvent de bonne foi.",
     "<strong>6. La comparaison sur des périodes de longueurs différentes.</strong> Comparer un trimestre à quatre mois, ou un mois de février à un mois de mars, sans normaliser. L'erreur est banale et passe inaperçue parce que les libellés sont exacts. La parade est systématique : ramenez à une base commune — par jour ouvré, par semaine — ou comparez des périodes strictement identiques.",
   ],
   "blocks": [
     {"type": "pitfall", "titre": "le graphique qui plaît parce qu'il exagère",
      "paras": [
        "Un phénomène désagréable mérite d'être nommé : un graphique à axe tronqué obtient souvent plus d'adhésion qu'un graphique honnête, parce qu'il rend le message spectaculaire. Vous serez tenté de le laisser, et quelqu'un vous demandera peut-être de le faire.",
        "Le coût n'apparaît pas tout de suite. Il apparaît le jour où quelqu'un refait le graphique avec un axe à zéro et constate que la « chute » était une variation de 2 %. À ce moment, ce n'est pas le graphique qui est mis en cause, c'est vous — et rétroactivement, tous vos autres chiffres.",
        "La formulation qui permet de refuser sans conflit : « avec l'axe à zéro on voit que la variation est faible ; si le message est qu'elle est faible, gardons-le ainsi. Si le message est que la tendance s'inverse, montrons plutôt l'évolution sur douze mois, ce sera plus démonstratif et incontestable. » Vous ne refusez pas, vous proposez une construction plus solide qui sert le même objectif.",
      ]},
     {"type": "exemple", "titre": "quatre chiffres exacts, une conclusion fausse",
      "paras": [
        "Une note interne affirme que la région Est surperforme : « satisfaction client de 78 % contre 61 % pour la moyenne nationale, et délai moyen de traitement de 4,2 jours contre 6,8 ». Quatre chiffres, tous exacts, tirés du fichier.",
        "<em>Effectifs :</em> la satisfaction de l'Est porte sur 23 réponses, la moyenne nationale sur 1 840. À 23 réponses, l'incertitude est telle que 78 % et 61 % ne sont pas distinguables.",
        "<em>Périmètre :</em> le délai moyen de l'Est exclut les dossiers non clôturés, qui y sont proportionnellement plus nombreux — précisément parce que les dossiers longs y traînent. La comparaison porte donc sur des populations différentes, et l'écart mesure l'inverse de ce qu'il prétend.",
        "<em>Médiane :</em> au niveau national, la médiane du délai est à 3,1 jours contre une moyenne de 6,8. La moyenne nationale est tirée par une minorité de dossiers très longs, et comparer deux moyennes issues de distributions asymétriques différentes ne veut rien dire.",
        "Aucun chiffre n'est faux, la conclusion est infondée. C'est la forme la plus courante de l'erreur d'analyse en entreprise, et elle ne se détecte par aucun contrôle automatique : seule l'habitude de demander systématiquement l'effectif, le périmètre et la dispersion la fait apparaître.",
      ]},
   ]},

  {"titre": "Un tableau de bord s'organise autour des décisions",
   "paras": [
     "Un tableau de bord n'est pas un rapport en couleurs. C'est un objet dont la fonction est de <strong>provoquer des décisions</strong>, et le test qui décide de la présence d'un indicateur est le même que celui vu dans la formation CRM : quelle décision prendrai-je différemment selon sa valeur ? Un indicateur qui ne change aucune décision est décoratif, quelle que soit sa pertinence apparente.",
     "Ce test élimine la moitié des indicateurs qu'on vous demandera. Le chiffre d'affaires cumulé depuis janvier est une information légitime dont personne ne fait rien : on n'agit pas différemment selon qu'il vaut 4,2 ou 4,4 M€. En revanche, « catégories en recul de plus de 10 % sur deux trimestres consécutifs » désigne des catégories nommées et appelle une action nommée.",
     "<strong>Une page, une audience, une fréquence.</strong> Ces trois contraintes se décident avant de dessiner quoi que ce soit. Un tableau de bord qui sert à la fois au responsable commercial chaque lundi et à la direction chaque trimestre ne sert bien ni l'un ni l'autre : ils n'ont ni les mêmes décisions à prendre ni le même horizon.",
     "<strong>La structure qui fonctionne</strong> tient en trois bandes. En haut, trois à cinq <em>chiffres clés</em>, chacun avec sa comparaison — période précédente ou objectif — car un chiffre isolé n'est pas interprétable. Au centre, deux à trois <em>graphiques</em> qui portent les messages principaux. En bas, un <em>tableau de détail</em> filtrable, qui permet de descendre au niveau des lignes concernées.",
     "Cette dernière bande est celle qu'on oublie et c'est elle qui distingue un tableau de bord d'une affiche. Un chiffre sans accès aux enregistrements qui le composent ne permet aucune action : le lecteur voit que quelque chose ne va pas, et ne peut rien en faire. Les segments et chronologies d'Excel — Insertion &gt; Segment sur un TCD — donnent ce filtrage en quelques clics, et un même segment peut piloter plusieurs TCD à la fois par la commande Connexions de rapport.",
     "<strong>Ce qu'il faut retirer.</strong> Le quadrillage de la feuille, désactivé dans Affichage : c'est le geste qui transforme visuellement une feuille de calcul en document. Les onglets techniques, masqués. Les couleurs, réduites à trois au maximum, dont une seule vive réservée à ce qui doit être vu. Les jauges, compteurs de vitesse et feux tricolores, supprimés — ils occupent une place considérable pour transmettre une seule valeur, et le feu tricolore en particulier remplace un chiffre par un jugement dont le seuil est invisible.",
   ],
   "blocks": [
     {"type": "method", "titre": "construire un tableau de bord d'une page",
      "steps": [
        "<strong>Nommez l'audience et la fréquence</strong> par écrit, en haut de votre brouillon. Toutes les décisions suivantes en découlent, et cette ligne évite les trois quarts des discussions ultérieures.",
        "<strong>Listez les décisions</strong> que cette personne prend à cette fréquence. Trois à cinq, pas plus. Si vous n'arrivez pas à les nommer, allez le lui demander — c'est une conversation de dix minutes qui évite trois versions inutiles.",
        "<strong>Associez un indicateur à chaque décision</strong>, et rejetez tous les autres. Notez les indicateurs rejetés et pourquoi : on vous les redemandera, et une réponse préparée passe bien mieux qu'une hésitation.",
        "<strong>Dessinez la page sur papier</strong> avant de toucher à Excel. Trois bandes, position de chaque bloc, titre de chaque graphique rédigé comme une conclusion. Vingt minutes de papier économisent trois heures de mise en forme abandonnée.",
        "<strong>Construisez sur des TCD</strong> placés dans un onglet masqué, et exposez les chiffres clés par <code>LIREDONNEESTABCROISDYNAMIQUE</code> dans l'onglet visible. Les graphiques peuvent être des graphiques croisés dynamiques liés à ces TCD.",
        "<strong>Ajoutez les segments</strong> sur la bande de détail, et connectez-les à tous les TCD concernés par Connexions de rapport, pour qu'un seul filtre pilote toute la page.",
        "<strong>Testez sur son destinataire</strong>, en silence, sans commenter. Notez chaque question qu'il pose : chacune signale un élément que la page ne dit pas assez clairement. Deux itérations suffisent presque toujours.",
      ]},
     {"type": "exemple", "titre": "la page mensuelle de la direction commerciale",
      "paras": [
        "<em>Audience :</em> le comité de direction, une fois par mois. <em>Décisions :</em> renforcer ou non une région, agir ou non sur une catégorie en recul, arbitrer l'effort entre conquête et fidélisation.",
        "<em>Bande haute, quatre chiffres.</em> CA du mois avec écart au mois précédent et au même mois de l'an dernier. Taux de marge avec son taux de couverture — hérité du module 2, et qui dit sur quelle part du chiffre d'affaires la marge est calculée. Nombre de clients actifs avec sa variation. Panier moyen avec sa variation.",
        "<em>Bande centrale, deux graphiques.</em> Une courbe du CA sur vingt-quatre mois, toutes catégories en gris et la catégorie qui décroche en couleur, titre énonçant la conclusion. Des barres horizontales triées de l'évolution par région, une seule barre en couleur.",
        "<em>Bande basse, un tableau filtrable.</em> Les vingt premières lignes par contribution à la variation, avec segments Région, Catégorie et Trimestre.",
        "<em>Indicateurs demandés et écartés, avec leur justification préparée :</em> le classement des commerciaux — ne sert aucun arbitrage de moyens en comité, et son affichage collectif dégrade la qualité des données saisies ; le CA cumulé depuis janvier — ne déclenche aucune décision, disponible sur demande ; le nombre de devis émis — indicateur d'activité, manipulable, et déjà reflété dans le nombre de clients actifs.",
        "Une page A4 en paysage, quatre couleurs dont une vive, aucune jauge. Le temps de construction a été de trois heures, dont vingt minutes sur papier et deux heures et demie à supprimer des choses.",
      ]},
     {"type": "pitfall", "titre": "le tableau de bord qui grossit à chaque demande",
      "paras": [
        "Chaque lecteur demandera un ajout, et chaque ajout est individuellement raisonnable. Au bout d'un an, la page compte dix-huit blocs, personne ne sait plus où regarder, et le tableau de bord est redevenu un rapport.",
        "La règle qui tient dans la durée : <strong>la page a un nombre de blocs fixe</strong>, décidé au départ. Toute addition exige une suppression, et c'est au demandeur de dire ce qui sort. Cette contrainte paraît rigide ; elle est en réalité la seule chose qui protège l'objet, et elle transforme la conversation — au lieu de « peux-tu ajouter X ? », elle devient « X est-il plus important que Y ? », qui est la vraie question.",
        "Prévoyez en contrepartie une page annexe, non diffusée, où vivent les indicateurs de second rang. Vous pouvez alors répondre « c'est en page 2 » plutôt que « non », ce qui règle la majorité des demandes sans encombrer la page principale.",
      ]},
   ]},

  {"titre": "Les contrôles qui empêchent de livrer un chiffre faux",
   "paras": [
     "L'incident de la mise en situation — un contrôle qui existait, en cellule B7, et que personne n'a lu — est le scénario type. Il enseigne quelque chose de précis : <strong>un contrôle qui demande d'être consulté ne protège de rien</strong>. Il doit s'imposer au regard de quelqu'un qui ne le cherche pas.",
     "La conception d'un dispositif de contrôle efficace repose sur trois principes.",
     "<strong>Le contrôle est visible là où le chiffre est lu.</strong> Un bandeau en haut de l'onglet de diffusion, affichant « Contrôles : 6/6 OK » en vert ou « ATTENTION : 2 contrôles en échec » en rouge, avec le détail juste en dessous. Pas dans un onglet séparé qu'il faut penser à ouvrir. La mise en forme conditionnelle rend ce bandeau impossible à manquer.",
     "<strong>Le contrôle bloque plutôt qu'il n'informe.</strong> La forme la plus efficace : la page de diffusion affiche, à la place du tableau, un message « Contrôles en échec — vérifier avant diffusion » tant que tous les contrôles ne sont pas au vert. C'est brutal et c'est ce qui fonctionne, parce qu'à huit heures moins le quart on ne lit pas, on ne peut que constater.",
     "<strong>Le contrôle porte sur ce qui a réellement mal tourné.</strong> Les contrôles utiles ne s'inventent pas : ils se déduisent des incidents passés. Tenez la liste des anomalies survenues et transformez chacune en contrôle. Un fichier rejoué deux fois donne un contrôle de doublon sur la clé source ; une région manquante donne un contrôle du nombre de sources.",
     "Le jeu de départ, à adapter ensuite : nombre de lignes et sa variation ; nombre de sources lues contre attendu ; somme principale et sa variation ; unicité de la clé ; plage de dates contenue dans la période ; nombre de non-correspondances et son taux ; écart entre chaque total de tableau de bord et un calcul indépendant sur la source ; nombre de valeurs distinctes des colonnes catégorielles.",
     "Ce dernier point mérite une insistance : <strong>tout chiffre affiché sur le tableau de bord doit être recalculé une seconde fois par un chemin différent</strong>, et l'écart affiché en contrôle. Un total de TCD comparé à une somme conditionnelle directe : si les deux chemins donnent la même valeur, la probabilité d'une erreur commune est faible. C'est le contrôle le plus puissant qui existe, et il coûte une formule par chiffre.",
   ],
   "blocks": [
     {"type": "h3", "titre": "Les quatre questions à se poser avant toute diffusion",
      "paras": [
        "Indépendamment des contrôles automatiques, une relecture humaine en quatre questions attrape ce qu'aucune formule ne détecte. Elle prend trois minutes.",
        "<strong>« Ce chiffre est-il vraisemblable ? »</strong> Non pas juste, mais vraisemblable : compatible avec ce que vous savez de l'activité. Un chiffre d'affaires en hausse de 40 % un mois de février est un signal, même si toutes les formules sont exactes. L'invraisemblance est le seul détecteur d'erreurs que vous n'aviez pas anticipées.",
        "<strong>« Sur quelle population porte-t-il ? »</strong> Combien de lignes, quelle période, quelles exclusions. Si vous ne pouvez pas répondre en une phrase, vous ne pouvez pas défendre le chiffre.",
        "<strong>« Qu'est-ce qui a changé depuis la dernière fois ? »</strong> Non pas dans les chiffres, mais dans le processus : une nouvelle source, une règle modifiée, une correction manuelle. Les erreurs se logent dans les changements, pas dans la routine.",
        "<strong>« Quelle est la question qu'on va me poser, et sais-je y répondre ? »</strong> Il y en a presque toujours une, et vous la connaissez. La préparer prend deux minutes et change complètement la position dans laquelle vous vous trouvez en réunion.",
      ]},
     {"type": "exemple", "titre": "l'incident du mois dernier, rejoué avec le bon dispositif",
      "paras": [
        "Rappel des faits : l'export d'une région avait été déposé deux fois, les lignes comptaient double, le CA de cette région était surévalué de 100 %, et le contrôle qui l'aurait détecté dormait en B7.",
        "<em>Avec un contrôle bloquant :</em> à l'ouverture, l'onglet de diffusion affiche « 1 contrôle en échec : nombre de lignes +8,3 % contre moyenne des 6 derniers mois — seuil 5 % ». Le tableau n'est pas affiché. L'incident est réglé en quatre minutes : on ouvre le contrôle par source, la région en double saute aux yeux, on retire le doublon, on actualise.",
        "<em>Le contrôle qui aurait été encore plus direct :</em> un test d'unicité sur la clé de ligne — numéro de commande — qui aurait affiché « 1 042 doublons détectés » et désigné la cause au lieu du symptôme. Il n'existait pas parce que personne n'avait imaginé qu'un fichier puisse être déposé deux fois. Il existe désormais, et c'est ainsi qu'un jeu de contrôles se construit : par sédimentation des incidents réels, jamais par anticipation exhaustive.",
        "<em>Le point qui compte le plus dans cette histoire :</em> le contrôle existait et n'a pas servi. La leçon n'est donc pas « il faut des contrôles » — il y en avait — mais que la conception d'un contrôle inclut la question de savoir <strong>comment il forcera l'attention de quelqu'un de pressé</strong>. Un contrôle qui suppose un lecteur disponible et méthodique est un contrôle qui ne fonctionne que les jours où il est inutile.",
      ]},
   ]},

  {"titre": "Diffuser sans perdre la main, et savoir quand changer d'outil",
   "paras": [
     "Un fichier diffusé cesse de vous appartenir. Il sera renommé, copié, modifié, transmis, et une version de mars circulera encore en septembre. Quatre précautions limitent les dégâts.",
     "<strong>Diffusez le résultat, pas le moteur.</strong> Pour un destinataire qui doit seulement lire, exportez l'onglet de tableau de bord en PDF. Le PDF est daté, non modifiable, léger, et ne peut pas produire de version divergente. C'est la forme de diffusion par défaut, et elle règle la majorité des problèmes avant qu'ils n'existent.",
     "<strong>Si le fichier doit circuler, protégez ce qui est calculé.</strong> Révision &gt; Protéger la feuille sur les onglets calculés, en laissant modifiables les seules cellules de paramètres. Masquez les onglets techniques. Cette protection n'est pas une sécurité — elle se contourne — mais elle empêche les modifications accidentelles, qui sont la totalité des cas réels.",
     "<strong>Datez et versionnez dans le fichier lui-même.</strong> Une cellule visible portant « Données au 31/08/2026, généré le 03/09/2026 ». Sans cette mention, un fichier ancien ressorti d'une boîte de courriels est indiscernable du fichier à jour, et cette confusion coûte plus cher que toutes les erreurs de formule réunies.",
     "<strong>Gardez une trace des versions diffusées.</strong> Le PDF daté dans un dossier de livrables suffit. Le jour où quelqu'un conteste un chiffre présenté en juin, vous pouvez montrer ce qui a effectivement été diffusé, et non ce que le fichier affiche aujourd'hui après quatre actualisations.",
     "Reste la question de fond de ce parcours : <strong>jusqu'où va Excel ?</strong> Cinq signaux indiquent qu'il n'est plus l'outil adapté, et les reconnaître à temps évite deux ans de fichiers qui s'effondrent.",
     "<em>Le volume.</em> Au-delà de quelques centaines de milliers de lignes, un classeur devient lent et instable. La limite théorique du million de lignes n'est jamais la vraie limite : c'est le temps de recalcul qui rend le travail impraticable bien avant.",
     "<em>La concurrence.</em> Dès que plusieurs personnes doivent écrire dans le même fichier en même temps, Excel n'est plus adapté, quel que soit le mode de partage. C'est le signal le plus net des cinq, et c'est une base de données ou un outil métier qu'il faut.",
     "<em>L'historisation.</em> Si vous avez besoin de savoir qui a modifié quoi et quand, il faut un système qui journalise. Un classeur ne le fait pas.",
     "<em>La fréquence.</em> Un rapport quotidien produit à la main est un rapport qui finira par être faux un jour de fatigue. À cette fréquence, il faut une chaîne automatisée de bout en bout.",
     "<em>La criticité.</em> Si une erreur dans le fichier a des conséquences réglementaires, financières ou contractuelles, le niveau de contrôle nécessaire dépasse ce qu'un classeur permet de garantir.",
     "En dehors de ces cinq cas, Excel reste un excellent outil, et il a un avantage que les solutions qui le remplacent perdent presque toujours : <strong>il est lisible par tout le monde</strong>. Une analyse dans un classeur peut être ouverte, comprise et vérifiée par n'importe qui dans l'entreprise. C'est une propriété rare et sous-estimée, et c'est la raison pour laquelle le tableur n'a jamais été remplacé.",
   ],
   "blocks": [
     {"type": "pitfall", "titre": "migrer trop tôt vers un outil plus puissant",
      "paras": [
        "Le mouvement inverse existe et coûte cher : conclure qu'Excel est dépassé et engager une migration vers un outil de visualisation ou une base de données alors qu'aucun des cinq signaux n'est présent.",
        "Ce qui se produit alors est prévisible. Le nouvel outil demande une compétence que l'équipe n'a pas, la maintenance dépend d'une seule personne, les utilisateurs continuent d'exporter vers Excel pour travailler — et l'on se retrouve avec deux systèmes au lieu d'un.",
        "Le critère de décision n'est pas la sophistication de l'outil mais la présence d'un des cinq signaux. Un tableau de bord Excel bien construit, contrôlé et documenté vaut mieux qu'un outil moderne mal maîtrisé, et il est infiniment plus facile à transmettre. La question à se poser n'est jamais « cet outil est-il meilleur ? » mais « quel problème précis résout-il que je n'arrive pas à résoudre ici ? ».",
      ]},
     {"type": "h3", "titre": "Ce que ce parcours a construit",
      "paras": [
        "Quatre modules pour aller d'un fichier illisible à un tableau de bord contrôlé, et la chaîne complète tient en une phrase : <strong>on structure la donnée, on la calcule sans la trahir, on automatise ce qui se répète, on expose ce qui déclenche une décision</strong>.",
        "Une idée traverse les quatre modules et mérite d'être isolée : <em>les erreurs qui comptent sont silencieuses</em>. Un montant en texte qui compte pour zéro, une plage qui se décale, un SIERREUR qui masque 15 % des lignes, un regroupement de dates sans l'année, un axe tronqué — aucun ne produit de message d'erreur, et tous produisent un résultat plausible. C'est pourquoi la compétence centrale de l'analyse n'est pas la maîtrise des fonctions, qui s'acquiert en quelques semaines, mais l'habitude du contrôle systématique.",
        "Une seconde idée les traverse également : <em>tout ce qui n'est pas documenté sera refait, autrement</em>. Le journal de transformation, les étapes de requête nommées, le Lisez-moi, la mention de la période, les indicateurs écartés et leur justification — ce travail paraît accessoire et c'est lui qui décide si votre analyse survit à votre absence.",
        "Ce que vous savez faire à ce stade couvre l'essentiel de ce qu'on demande à un analyste en entreprise. Ce qui reste à acquérir n'est pas technique : c'est le jugement sur ce qui mérite d'être mesuré, et il ne s'apprend qu'en confrontant des analyses à des décisions réelles.",
      ]},
   ]},
 ],

 "etude_cas": {
   "titre": "Transformer quatre tableaux croisés en une page qui déclenche des décisions",
   "html": """
<p>Reprenons la situation : un rapport automatisé et juste, que personne ne lit, et un incident de chiffre faux non détecté. Voici la reprise complète, en une semaine.</p>
<p><strong>Jour 1 — la conversation qui remplace trois versions.</strong> Vingt minutes avec le directeur commercial, une seule question : « le mois dernier, après avoir eu ces chiffres, qu'avez-vous décidé ? ». Réponse : rien de précis. Deuxième question, la vraie : « qu'auriez-vous aimé savoir et que vous n'aviez pas ? ». Réponse : « où on perd, et si c'est en train de s'aggraver ou pas ».</p>
<p>Cette phrase est le cahier des charges complet. Elle contient une localisation — où — et une dynamique — s'aggrave ou pas. Les quatre TCD existants donnaient des niveaux, pas des variations : ils ne pouvaient structurellement pas répondre.</p>
<p><strong>Jour 1, suite — nommer les décisions.</strong> Trois décisions mensuelles émergent de l'entretien : renforcer ou non le soutien à une région, agir ou non sur une catégorie en recul, arbitrer entre conquête de nouveaux clients et fidélisation. Trois décisions, donc trois à cinq indicateurs, pas davantage.</p>
<p><strong>Jour 2 — le brouillon papier.</strong> Trois bandes dessinées à la main. Chiffres clés en haut, avec leur comparaison ; deux graphiques au centre, dont les titres sont rédigés dès le brouillon sous forme de conclusions provisoires ; tableau filtrable en bas.</p>
<p>Ce brouillon fait apparaître une difficulté que la construction directe aurait masquée : « où on perd » demande une contribution à la variation, pas un niveau. Une région qui baisse de 30 % mais pèse 3 % du chiffre d'affaires n'est pas le sujet ; une région qui baisse de 6 % en pesant 35 % l'est. L'indicateur juste est donc la contribution en euros à la variation totale, pas le pourcentage d'évolution — et c'est exactement le genre d'arbitrage qu'on ne fait pas quand on commence par manipuler des champs dans un TCD.</p>
<p><strong>Jour 3 — la construction.</strong> Les quatre TCD existants sont déplacés dans un onglet masqué. Un onglet « Tableau de bord » est créé, quadrillage désactivé, format A4 paysage.</p>
<p><em>Bande haute :</em> quatre chiffres extraits par <code>LIREDONNEESTABCROISDYNAMIQUE</code>, chacun avec son écart au mois précédent et au même mois de l'an dernier. Le taux de marge est affiché avec son taux de couverture, hérité du module 2 — un choix discuté, finalement retenu parce que masquer la couverture reviendrait à laisser croire que la marge porte sur 100 % du chiffre d'affaires.</p>
<p><em>Bande centrale, graphique 1 :</em> courbe du CA sur vingt-quatre mois, six catégories, cinq en gris clair et Mobilier en couleur. Titre : « Le mobilier décroche depuis juin, seule catégorie en recul ». Le titre est une formule qui se met à jour — il compose la phrase à partir de la catégorie ayant la plus forte contribution négative, calculée dans l'onglet masqué. Construction délicate, mais elle évite le titre périmé, qui est l'accident le plus fréquent des tableaux de bord automatisés.</p>
<p><em>Bande centrale, graphique 2 :</em> barres horizontales de la contribution en euros à la variation, par région, triées. Deux barres négatives nettement plus longues. Axe à zéro, sans discussion possible puisqu'il s'agit de barres.</p>
<p><em>Bande basse :</em> les vingt premières lignes par contribution à la variation, avec trois segments — Région, Catégorie, Trimestre — connectés à tous les TCD par Connexions de rapport.</p>
<p><strong>Jour 4 — les contrôles, refondus autour de l'incident.</strong> Le bandeau de contrôle passe en haut de l'onglet de diffusion, en pleine largeur. Sept contrôles, dont deux nouveaux issus directement de l'incident : unicité du numéro de commande, qui aurait désigné la cause du doublon ; et nombre de fichiers sources lus contre attendu.</p>
<p>Surtout, le comportement change : tant qu'un contrôle est en échec, l'onglet affiche un bandeau rouge pleine largeur et les trois bandes sont masquées par mise en forme conditionnelle. On ne peut plus lire les chiffres sans avoir vu l'alerte.</p>
<p>Ce choix a été débattu — il paraît excessif. L'argument qui a tranché : le coût d'un rapport diffusé quatre minutes plus tard est nul ; le coût d'un chiffre faux présenté en comité est une remise en cause de tous les autres chiffres pendant six mois.</p>
<p><strong>Jour 5 — le test silencieux.</strong> La page est montrée au directeur commercial sans commentaire. Trois questions posées, donc trois défauts identifiés : le taux de couverture n'est pas compris — une note de deux mots est ajoutée ; la contribution à la variation est prise pour un pourcentage — l'unité est ajoutée en toutes lettres ; et il demande où sont les commerciaux, ce qui était l'indicateur explicitement écarté. La réponse préparée est donnée telle quelle, et acceptée.</p>
<p><strong>Résultat à trois mois.</strong> La page est projetée en comité, et le comité commence désormais par elle. Deux décisions ont été prises sur la bande basse : un soutien commercial redirigé vers le Sud-Ouest, et une révision de gamme sur le mobilier. Aucun chiffre faux n'a été diffusé — deux fois, le bandeau rouge a bloqué la diffusion, une fois pour un fichier régional manquant, une fois pour un doublon.</p>
<p><strong>La leçon transposable.</strong> Le travail technique de ce module a représenté environ un tiers du temps. Les deux autres tiers ont été la conversation initiale, le brouillon papier et le test silencieux — c'est-à-dire tout ce qui ne se fait pas dans Excel. Un tableau de bord qui déclenche des décisions n'est pas un problème de construction : c'est un problème de compréhension de ce que le lecteur doit pouvoir faire, et la construction n'en est que la conséquence.</p>
"""},

 "checklist": {
   "titre": "Checklist — représenter, contrôler et diffuser",
   "items": [
     "Le type de graphique découle de la question posée, pas de la galerie de graphiques",
     "Le titre de chaque graphique énonce une conclusion, pas un contenu",
     "Les barres sont triées par valeur quand l'axe n'est pas temporel",
     "L'axe des ordonnées part de zéro sur tout graphique en barres",
     "Aucun camembert ne compte plus de trois parts, et aucun graphique n'est en trois dimensions",
     "Aucun double axe ne suggère une corrélation entre deux unités différentes",
     "Toute moyenne est accompagnée de sa médiane ou de sa dispersion",
     "Tout pourcentage est accompagné de son effectif",
     "Les périodes comparées sont de longueur identique, ou ramenées à une base commune",
     "Le tableau de bord tient sur une page, pour une audience et une fréquence nommées",
     "Chaque indicateur affiché passe le test : quelle décision change selon sa valeur ?",
     "Les indicateurs écartés sont listés avec leur justification préparée",
     "Chaque chiffre clé est affiché avec une comparaison : période précédente ou objectif",
     "Une bande de détail filtrable permet de descendre aux lignes concernées",
     "Le quadrillage est désactivé et les onglets techniques sont masqués",
     "Le bandeau de contrôle est en haut de l'onglet lu, pas dans un onglet séparé",
     "Les contrôles en échec bloquent l'affichage plutôt que de simplement informer",
     "Chaque chiffre du tableau de bord est recalculé par un second chemin, et l'écart est affiché",
     "Chaque incident passé a été transformé en un contrôle",
     "Le fichier porte visiblement la date des données et la date de génération",
     "La diffusion se fait en PDF daté, sauf nécessité contraire, et les onglets calculés sont protégés",
   ]},

 "glossaire": [
   ("Axe tronqué", "Axe des ordonnées ne partant pas de zéro. Amplifie visuellement les variations. Interdit sur un graphique en barres, à signaler sur une courbe."),
   ("Double axe", "Deux échelles verticales sur un même graphique. Suggère une corrélation dont l'intensité dépend d'un choix d'échelle arbitraire."),
   ("Étiquetage direct", "Placement du nom d'une série au bout de sa courbe plutôt que dans une légende. Supprime un aller-retour du regard."),
   ("Test des cinq secondes", "Montrer un graphique cinq secondes puis demander ce qui a été compris. Révèle si le message passe réellement."),
   ("Médiane", "Valeur qui sépare la population en deux moitiés. À afficher avec la moyenne : leur écart révèle l'asymétrie de la distribution."),
   ("Contribution à la variation", "Part en valeur absolue qu'un segment apporte à l'évolution totale. Indicateur juste pour répondre à « où perd-on ? », contrairement au pourcentage d'évolution."),
   ("Segment", "Filtre visuel attaché à un ou plusieurs tableaux croisés dynamiques. Connectable à plusieurs TCD par la commande Connexions de rapport."),
   ("Contrôle bloquant", "Contrôle qui masque le tableau de bord tant qu'il est en échec, au lieu d'afficher une alerte que personne ne lit."),
   ("Double calcul", "Vérification d'un chiffre par un second chemin de calcul indépendant. Le contrôle le plus puissant, au coût d'une formule."),
   ("Vraisemblance", "Compatibilité d'un chiffre avec ce que l'on sait de l'activité. Seul détecteur des erreurs qui n'avaient pas été anticipées."),
   ("Onglet Lisez-moi", "Onglet documentant l'origine des données, les onglets protégés, la procédure et l'historique des incidents. Ne diverge pas du fichier, contrairement à un document séparé."),
   ("Feu tricolore", "Représentation d'un état par une couleur. Remplace un chiffre par un jugement dont le seuil est invisible : à éviter sur un tableau de bord."),
 ],

 "retenir": [
   "Le type de graphique découle de la question : courbe pour une évolution, barres triées pour une comparaison, nuage de points pour une relation.",
   "Le titre d'un graphique énonce la conclusion ; une étiquette descriptive laisse au lecteur un travail qu'il ne fera pas.",
   "Un graphique en barres part toujours de zéro : le lecteur y compare des longueurs.",
   "Le double axe suggère une corrélation dont l'intensité dépend d'un choix d'échelle arbitraire : deux graphiques empilés disent la même chose honnêtement.",
   "Une moyenne sans médiane, un pourcentage sans effectif : deux chiffres exacts et deux informations incomplètes.",
   "Un graphique peut être entièrement exact et conduire à une conclusion fausse ; seule l'habitude de demander effectif, périmètre et dispersion le détecte.",
   "Un tableau de bord se conçoit à partir des décisions à prendre, pas des données disponibles.",
   "Une page, une audience, une fréquence : un tableau de bord qui sert à tout le monde ne sert bien personne.",
   "Trois bandes : chiffres clés avec comparaison, graphiques porteurs de message, tableau de détail filtrable.",
   "Un chiffre sans accès aux enregistrements qui le composent ne permet aucune action.",
   "Le nombre de blocs de la page est fixe : toute addition exige une suppression, et c'est au demandeur de choisir.",
   "Un contrôle qui demande d'être consulté ne protège de rien : il doit s'imposer à quelqu'un de pressé.",
   "Un contrôle en échec doit bloquer l'affichage, pas se contenter d'informer.",
   "Les contrôles utiles se déduisent des incidents passés, jamais d'une anticipation exhaustive.",
   "Recalculez chaque chiffre affiché par un second chemin indépendant : c'est le contrôle le plus puissant, au coût d'une formule.",
   "Quatre questions avant diffusion : est-il vraisemblable, sur quelle population, qu'est-ce qui a changé, quelle question va-t-on me poser.",
   "Diffusez le résultat en PDF daté, pas le moteur : un fichier diffusé cesse de vous appartenir.",
   "Cinq signaux disent qu'Excel n'est plus l'outil : volume, écriture concurrente, historisation, fréquence quotidienne, criticité réglementaire.",
   "En dehors de ces cinq cas, l'avantage décisif d'Excel reste qu'il est lisible et vérifiable par tout le monde.",
   "Les erreurs qui comptent sont silencieuses : la compétence centrale de l'analyse est l'habitude du contrôle, pas la maîtrise des fonctions.",
 ],

 "exercices": [
  {"titre": "Repérer ce qui trompe dans quatre graphiques", "niveau": "Débutant",
   "enonce": [
     "Quatre graphiques figurent dans une note de direction. Pour chacun, dites ce qui pose problème, ce que le lecteur va conclure à tort, et par quelle construction vous le remplaceriez.",
     "<strong>A.</strong> Un histogramme du chiffre d'affaires trimestriel, axe vertical de 980 à 1 060 k€. Les quatre barres semblent très différentes.",
     "<strong>B.</strong> Un camembert de la répartition des ventes entre sept commerciaux, en trois dimensions, la part la plus importante placée à l'avant.",
     "<strong>C.</strong> Un graphique combinant, sur deux axes, le budget publicitaire mensuel et le nombre de commandes. Les deux courbes se suivent de près.",
     "<strong>D.</strong> Un tableau comparant la satisfaction client par région : 82 %, 74 %, 91 %, 68 %.",
   ],
   "corrige": """
<p><strong>A — l'axe tronqué sur un graphique en barres.</strong></p>
<p>De 980 à 1 060, l'échelle couvre 80 k€ sur des valeurs d'environ 1 000 k€, soit 8 % d'amplitude. Une barre deux fois plus haute qu'une autre représente en réalité un écart de 4 %.</p>
<p><em>Ce que le lecteur conclut :</em> que l'activité est très volatile d'un trimestre à l'autre, et probablement qu'il faut agir. La conclusion juste est que le chiffre d'affaires est remarquablement stable — l'inverse exact.</p>
<p><em>Correction :</em> axe à zéro. Sur un graphique en barres, la règle ne souffre aucune exception, parce que la barre encode une longueur et que le lecteur compare des longueurs.</p>
<p><em>Ce qu'il faut faire si la variation reste le sujet :</em> ne pas forcer l'axe, mais changer d'objet. Un graphique de la variation en pourcentage d'un trimestre à l'autre, avec zéro au centre, montre honnêtement des écarts de plus ou moins 4 %. Le lecteur voit alors la vraie amplitude et peut décider si elle mérite attention. Vous avez répondu à la question sans déformer.</p>
<p><strong>B — le camembert tridimensionnel à sept parts.</strong></p>
<p>Trois défauts cumulés. Sept parts dépassent largement la capacité de comparaison visuelle d'angles. La perspective agrandit la part avant. Et l'ordre des parts, s'il n'est pas décroissant, empêche tout classement.</p>
<p><em>Ce que le lecteur conclut :</em> que le commercial placé à l'avant domine nettement, ce qui peut être faux de plusieurs points. Sur un sujet de répartition entre personnes, l'erreur n'est pas anodine.</p>
<p><em>Correction :</em> des barres horizontales triées par valeur décroissante, avec le pourcentage en étiquette au bout de chaque barre. Sept barres se lisent instantanément, se classent sans effort, et les libellés sont horizontaux donc lisibles. Le camembert ne conserve un intérêt que pour deux ou trois parts nettement différentes.</p>
<p><em>Remarque :</em> aucune version tridimensionnelle d'un graphique n'améliore jamais sa lisibilité. La troisième dimension n'encode aucune information et ajoute une distorsion. C'est une règle sans exception.</p>
<p><strong>C — le double axe et la corrélation fabriquée.</strong></p>
<p>Le problème est que l'échelle de chaque axe est un choix libre. En modifiant l'un des deux, on rapproche ou on écarte les courbes à volonté. Deux séries quelconques peuvent être rendues visuellement parallèles.</p>
<p><em>Ce que le lecteur conclut :</em> que le budget publicitaire pilote les commandes, et probablement qu'il faut l'augmenter. Rien dans le graphique ne soutient cette conclusion — ni la corrélation, ni la causalité, ni le sens de celle-ci. Il est tout aussi plausible que le budget suive les commandes, si la publicité est calibrée sur le chiffre d'affaires du mois précédent.</p>
<p><em>Correction en trois niveaux.</em> Le minimum : deux graphiques empilés partageant le même axe temporel, chacun avec sa propre échelle partant de zéro. Le lecteur voit les deux séries et forme son jugement. Mieux : un nuage de points, budget en abscisse, commandes en ordonnée, un point par mois — le graphique qui répond réellement à la question, et qui révélera souvent qu'il n'y a pas grand-chose. Encore mieux, si la causalité est le sujet : un nuage de points avec le budget décalé d'un mois, pour vérifier que l'effet suit la cause et non l'inverse.</p>
<p><strong>D — les pourcentages sans effectif.</strong></p>
<p>Quatre pourcentages, aucun dénominateur. Impossible de savoir si 91 % porte sur 400 réponses ou sur 11.</p>
<p><em>Ce que le lecteur conclut :</em> que la troisième région est la meilleure et la quatrième la plus mauvaise, et il agira en conséquence — félicitations d'un côté, plan d'action de l'autre. Si les effectifs sont de 400, 380, 11 et 350, la seule chose qu'on puisse dire est que la troisième région n'a pas assez de réponses pour être évaluée, et que 68 % contre 74 % et 82 % mérite d'être regardé.</p>
<p><em>Correction :</em> ajouter systématiquement l'effectif à côté de chaque pourcentage — « 91 % (n = 11) ». C'est un ajout de deux caractères qui change la lecture du tableau.</p>
<p><em>Ce qu'il faut faire en plus, et qui compte davantage :</em> décider d'un effectif minimal en dessous duquel on n'affiche pas de pourcentage, et l'appliquer. Trente réponses est un seuil usuel et défendable. En dessous, affichez « n. s. » plutôt qu'un chiffre. Vous éviterez que quelqu'un construise une décision sur onze réponses, ce qui arrive régulièrement et coûte plus cher qu'un tableau incomplet.</p>
"""},

  {"titre": "Concevoir un tableau de bord pour une audience précise", "niveau": "Intermédiaire",
   "enonce": [
     "Le responsable du service client vous demande un tableau de bord. Il gère douze personnes, consulte ses chiffres chaque lundi matin avant sa réunion d'équipe, et ses décisions hebdomadaires sont : réaffecter de la charge entre les personnes, décider quels dossiers escalader, et repérer les sujets récurrents qui méritent une action de fond.",
     "Concevez la page. Précisez les indicateurs retenus, ceux que vous écartez et comment vous le justifiez, et traitez explicitement la question du suivi individuel.",
   ],
   "corrige": """
<p><strong>Point de départ : les trois décisions sont hebdomadaires et opérationnelles.</strong> Cela exclut d'emblée tous les indicateurs de niveau et de tendance longue, qui relèvent d'une revue trimestrielle. Chaque bloc de la page doit désigner des dossiers ou des personnes sur lesquels agir <em>cette semaine</em>.</p>
<p><strong>Bande haute — quatre chiffres de cadrage.</strong></p>
<p><em>Dossiers ouverts en fin de semaine</em>, avec la variation contre la semaine précédente. C'est l'indicateur de charge globale : il dit si le service tient ou décroche.</p>
<p><em>Dossiers reçus contre dossiers clôturés dans la semaine.</em> Le rapport entre les deux est plus informatif que chacun séparément : au-dessus de 1, le stock grossit, et c'est le signal avancé d'une saturation qui apparaîtra dans trois semaines dans les délais.</p>
<p><em>Âge du plus ancien dossier ouvert.</em> Indicateur brutal et excellent : il désigne un dossier précis, et il est impossible à améliorer autrement qu'en traitant réellement ce dossier.</p>
<p><em>Dossiers dépassant le délai d'engagement</em>, en nombre. Directement lié à la décision d'escalade.</p>
<p><strong>Bande centrale — deux graphiques.</strong></p>
<p><em>Courbe reçus / clôturés sur douze semaines</em>, deux séries, étiquetées directement. Elle montre si le déséquilibre de la semaine est ponctuel ou installé — distinction qui change complètement la décision à prendre.</p>
<p><em>Barres horizontales triées des motifs de dossier sur quatre semaines glissantes</em>, avec la variation contre les quatre semaines précédentes. C'est le bloc qui alimente la troisième décision : un motif qui progresse fortement signale un problème de fond, souvent en amont du service client. Quatre semaines glissantes plutôt qu'une seule, car sur une semaine les volumes par motif sont trop faibles pour être interprétables.</p>
<p><strong>Bande basse — le tableau qui fait le travail.</strong> Les dossiers ouverts depuis plus de X jours ou dépassant l'engagement, triés par ancienneté décroissante, avec le motif, le client, la personne en charge et la date de dernière action. Segments sur le motif et sur la personne.</p>
<p>C'est la bande qui sert réellement le lundi matin : elle donne l'ordre du jour de la réunion d'équipe sous forme de liste de dossiers nommés. Les trois autres bandes servent à comprendre ; celle-ci sert à agir.</p>
<p><strong>La question du suivi individuel — le point délicat.</strong></p>
<p>Le responsable demandera le nombre de dossiers traités par personne, et il aura une raison légitime : sa première décision est de réaffecter la charge, ce qui suppose de savoir qui en a trop.</p>
<p><em>La distinction qui permet de répondre :</em> mesurer la <strong>charge</strong> est nécessaire, mesurer la <strong>performance</strong> individuelle est un autre sujet et n'a pas sa place ici.</p>
<p><em>Ce que j'affiche :</em> le nombre de dossiers <em>ouverts</em> par personne, et l'âge moyen de ces dossiers. Ces deux chiffres décrivent une charge à un instant donné et servent directement la décision de réaffectation.</p>
<p><em>Ce que je n'affiche pas :</em> le nombre de dossiers clôturés par personne, et le délai moyen par personne. Ce sont des indicateurs de rendement, et ils produisent exactement ce qu'ils mesurent : les dossiers faciles seront pris en premier, les dossiers difficiles éviteront tout le monde, et le délai moyen s'améliorera pendant que le service se dégradera. C'est la loi de Goodhart, et elle est particulièrement forte sur ce type d'indicateur.</p>
<p><em>Comment le dire au responsable :</em> « le nombre de dossiers ouverts et leur âge te disent qui est en surcharge, ce qui est ce dont tu as besoin lundi. Le nombre de dossiers clôturés te dirait qui va vite, et il pousserait chacun à prendre les dossiers rapides en premier — tu aurais un meilleur chiffre et des dossiers difficiles qui traînent. Si tu veux évaluer quelqu'un, ça se fait en entretien, sur des dossiers réels, pas sur un compteur affiché à toute l'équipe. »</p>
<p><em>Et si l'indicateur est affiché malgré tout :</em> qu'il ne le soit jamais collectivement, ni projeté en réunion d'équipe. Un classement affiché produit une dégradation silencieuse de la qualité des données et du travail, et cette dégradation coûte plus cher que l'information gagnée.</p>
<p><strong>Contrôles associés.</strong> Nombre de dossiers importés contre nombre attendu ; unicité du numéro de dossier ; plage de dates couvrant la semaine ; nombre de dossiers sans motif renseigné, qui est le signal d'une dégradation de la saisie et qui rendrait le second graphique trompeur.</p>
<p><strong>Le test :</strong> deux lundis consécutifs, en observant simplement ce qu'il regarde. Ce que personne ne regarde deux semaines de suite sort de la page. C'est le seul critère fiable, et il est plus honnête que toute discussion préalable.</p>
"""},

  {"titre": "Arbitrer entre fiabiliser et changer d'outil", "niveau": "Avancé",
   "enonce": [
     "Le fichier de pilotage commercial que vous maintenez compte désormais 340 000 lignes, met quatre minutes à s'actualiser, et trois personnes voudraient y saisir des commentaires en parallèle. La direction vous demande de « passer sur un vrai outil » et un éditeur a fait une démonstration convaincante d'une solution de tableaux de bord à 18 000 € par an.",
     "Construisez votre recommandation. Traitez la question du volume, celle de la saisie concurrente, et dites ce que vous répondez si la direction veut acheter malgré votre analyse.",
   ],
   "corrige": """
<p><strong>D'abord : deux problèmes différents ont été présentés comme un seul.</strong> Le volume et la lenteur relèvent de la technique et sont peut-être solubles. La saisie concurrente relève de l'usage et ne l'est pas dans Excel. Les traiter ensemble conduit mécaniquement à la conclusion « il faut acheter », alors que séparés ils appellent des réponses différentes et beaucoup moins coûteuses.</p>
<p><strong>1. Le volume et la lenteur — mesurer avant de conclure.</strong></p>
<p>340 000 lignes n'est pas un volume problématique en soi. Quatre minutes d'actualisation sont un symptôme, pas un diagnostic. Avant toute conclusion, identifiez ce qui prend ces quatre minutes, et il y a trois suspects habituels.</p>
<p><em>Des formules volatiles ou des colonnes entières.</em> Une RECHERCHEX sur des colonnes entières, ou des fonctions comme DECALER et INDIRECT, recalculent tout à chaque frappe. Sur 340 000 lignes, une seule formule mal écrite peut expliquer la totalité du temps. C'est le cas le plus fréquent, et le plus facile à corriger.</p>
<p><em>Des calculs qui devraient être dans la requête.</em> Une colonne de formule appliquée à 340 000 lignes recalcule à chaque modification ; la même transformation faite dans Power Query s'exécute une fois à l'actualisation.</p>
<p><em>Le chargement en feuille de ce qui pourrait rester en modèle.</em> Une requête peut être chargée dans le modèle de données plutôt que dans une feuille. Les 340 000 lignes ne sont alors jamais écrites dans une grille, les TCD interrogent le modèle directement, et le gain est souvent d'un facteur cinq à dix.</p>
<p><em>Estimation honnête :</em> deux jours de travail ramènent très probablement l'actualisation sous la minute. À comparer à 18 000 € par an, la question mérite d'être posée avant toute décision.</p>
<p><em>Et si ce n'est pas suffisant :</em> alors le volume est un vrai signal, et la bonne réponse n'est pas un outil de tableaux de bord — c'est une base de données en amont. Un outil de visualisation branché sur des fichiers restera lent, parce que le problème est le stockage, pas l'affichage. C'est une confusion très répandue et coûteuse.</p>
<p><strong>2. La saisie concurrente — le signal qui, lui, est net.</strong></p>
<p>Trois personnes qui saisissent des commentaires dans le même fichier : Excel n'est pas fait pour cela, quel que soit le mode de partage. Les scénarios de perte de données sont nombreux et ils se produiront.</p>
<p>Mais observez ce qu'on demande réellement : saisir des commentaires liés à des lignes, à plusieurs. C'est un besoin de <em>saisie collaborative</em>, pas un besoin de <em>tableau de bord</em>. L'outil à 18 000 € ne le résout probablement pas — la plupart des solutions de visualisation sont en lecture seule.</p>
<p><em>La réponse proportionnée :</em> séparer les deux flux. Les commentaires vont dans un outil de saisie collaborative — un formulaire alimentant une table partagée, une liste dans l'outil collaboratif de l'entreprise, une petite base. Cette table devient une source supplémentaire, lue par Power Query et jointe aux données. Chacun saisit où il faut, le fichier lit, et le problème disparaît. Coût : quelques jours, éventuellement zéro licence supplémentaire si l'entreprise dispose déjà d'un outil collaboratif.</p>
<p><strong>3. La recommandation.</strong></p>
<p>Une page, trois parties. <em>Ce qui ne va pas</em>, en distinguant les deux problèmes et en chiffrant chacun. <em>Ce que je propose</em> : optimisation technique en deux jours, séparation du flux de saisie en trois jours, avec un objectif chiffré — actualisation sous une minute, saisie concurrente supprimée. <em>Ce qui déclencherait un changement d'outil</em>, écrit à l'avance : si après optimisation l'actualisation dépasse deux minutes, si le volume double, si un quatrième besoin apparaît que le fichier ne couvre pas, ou si le maintien du fichier dépasse deux jours par mois.</p>
<p>Cette troisième partie est la plus importante du document. Elle transforme votre position : vous ne dites pas « non », vous dites « pas maintenant, et voici exactement à quoi nous saurons que le moment est venu ». Personne ne peut vous reprocher de freiner, et vous ne serez pas contraint de défendre le fichier indéfiniment.</p>
<p><strong>4. Si la direction achète malgré tout.</strong></p>
<p>C'est une décision légitime qui peut reposer sur des considérations que vous n'avez pas — une stratégie de système d'information, un besoin d'un autre service, une relation commerciale. Ne la combattez pas.</p>
<p>Faites en revanche trois choses. <em>Posez par écrit les questions techniques qui décideront de la réussite</em> : d'où l'outil lit-il les données, comment sont gérées les transformations, qui les maintient, qui a la compétence en interne, et que se passe-t-il à l'arrêt de l'abonnement. Ces cinq questions, posées avant signature, valent plus que toute argumentation.</p>
<p><em>Proposez-vous pour préparer les données</em>, quel que soit l'outil retenu. Aucun outil de visualisation ne nettoie les données à votre place : ils supposent tous une source propre, et c'est précisément ce que vous savez produire. Votre travail des trois premiers modules garde toute sa valeur, et c'est même lui qui décidera si le projet réussit.</p>
<p><em>Maintenez le fichier Excel en parallèle pendant trois mois</em>, et comparez les chiffres. Les écarts entre l'ancien et le nouveau système sont systématiques, toujours instructifs, et c'est le seul moyen de valider la nouvelle chaîne. Une migration sans période de recouvrement est une migration dont personne ne saura si elle a introduit des erreurs.</p>
<p><strong>Le principe général, au-delà de ce cas :</strong> la question n'est jamais « cet outil est-il meilleur ? » — il l'est presque toujours sur au moins un critère — mais « quel problème précis résout-il que je n'arrive pas à résoudre ici, et à quel coût de maintenance ? ». Un outil dont la maintenance dépend d'une seule personne est plus fragile qu'un classeur que dix personnes savent ouvrir, et c'est un arbitrage qu'on ne fait presque jamais explicitement.</p>
"""},
 ],

 "ressources": [
   "<strong>« Storytelling with Data », Cole Nussbaumer Knaflic</strong> — le livre le plus directement applicable sur la conception de graphiques en contexte professionnel : que retirer, comment employer la couleur, comment titrer. Se lit en quelques heures et change durablement la pratique.",
   "<strong>Support Microsoft — « Utiliser des segments pour filtrer les données »</strong> et la commande Connexions de rapport : la mécanique exacte pour piloter plusieurs tableaux croisés dynamiques avec un seul filtre, cœur de la bande de détail d'un tableau de bord.",
   "<strong>Les modules 1 à 3 de cette formation</strong> — un tableau de bord n'est jamais meilleur que la donnée qui l'alimente. En cas de chiffre contesté, la cause est presque toujours en amont : structure, rapprochement ou périmètre de consolidation.",
   "<strong>La formation « Analytics &amp; mesure de la performance » de Formahub</strong> — pour la suite logique : plan de mesure, attribution et tests, c'est-à-dire ce qu'il faut mesurer, quand ce module traite de la façon de le représenter.",
 ],
}

QUIZ["excel-analyse-donnees/module-4"] = {
 "module_id": "formation-excel-analyse-donnees-module-4",
 "version": "2.0", "last_verified": "2026-09-04",
 "questions": [
  {"id":"q1","question":"Sur quel type de graphique l'axe des ordonnées doit-il impérativement partir de zéro ?",
   "choices":[{"key":"a","text":"Sur les nuages de points, où la position encode deux variables"},
              {"key":"b","text":"Sur tous les graphiques, sans aucune exception"},
              {"key":"c","text":"Sur les graphiques en barres, où le lecteur compare des longueurs"}],
   "correct_answer":"c","feedback":"Une barre encode une longueur : la tronquer déforme la comparaison. Sur une courbe, où l'on lit une variation, un axe tronqué est acceptable s'il est signalé."},
  {"id":"q2","question":"Pourquoi le double axe est-il une construction trompeuse ?",
   "choices":[{"key":"a","text":"Parce que l'échelle de chaque axe est arbitraire : on fait apparaître ou disparaître la corrélation à volonté"},
              {"key":"b","text":"Parce qu'Excel ne permet pas d'y afficher de légende correcte"},
              {"key":"c","text":"Parce qu'il ne peut afficher que deux séries au maximum"}],
   "correct_answer":"a","feedback":"Deux séries quelconques peuvent être rendues visuellement parallèles. Deux graphiques empilés sur le même axe temporel disent la même chose sans induire de relation."},
  {"id":"q3","question":"Quel test décide si un indicateur mérite sa place sur un tableau de bord ?",
   "choices":[{"key":"a","text":"Est-il disponible sans travail supplémentaire ?"},
              {"key":"b","text":"Quelle décision prendrai-je différemment selon sa valeur ?"},
              {"key":"c","text":"La direction l'a-t-elle demandé explicitement ?"}],
   "correct_answer":"b","feedback":"Ce test élimine la moitié des indicateurs demandés. Le CA cumulé depuis janvier est légitime et ne déclenche aucune action."},
  {"id":"q4","question":"Un contrôle existait en cellule B7 et personne ne l'a lu avant de diffuser un chiffre faux. Quelle est la bonne conclusion ?",
   "choices":[{"key":"a","text":"Qu'un contrôle doit s'imposer au regard et bloquer l'affichage, pas attendre d'être consulté"},
              {"key":"b","text":"Qu'il faut former les utilisateurs à consulter l'onglet Contrôles"},
              {"key":"c","text":"Qu'il faut multiplier le nombre de contrôles pour augmenter les chances d'en voir un"}],
   "correct_answer":"a","feedback":"Un contrôle qui suppose un lecteur disponible et méthodique ne fonctionne que les jours où il est inutile."},
  {"id":"q5","question":"Lequel de ces signaux indique qu'Excel n'est plus l'outil adapté ?",
   "choices":[{"key":"a","text":"Le fichier dépasse cinquante mille lignes"},
              {"key":"b","text":"Plusieurs personnes doivent écrire dans le même fichier en même temps"},
              {"key":"c","text":"Le fichier comporte plus de dix onglets"}],
   "correct_answer":"b","feedback":"L'écriture concurrente est le signal le plus net des cinq. Cinquante mille lignes ou dix onglets ne posent aucun problème en soi."},
  {"id":"q6","question":"Comment afficher honnêtement un taux de satisfaction de 91 % calculé sur 11 réponses ?",
   "choices":[{"key":"a","text":"En l'affichant tel quel : le pourcentage est exact"},
              {"key":"b","text":"En arrondissant à 90 % pour ne pas suggérer une fausse précision"},
              {"key":"c","text":"En affichant l'effectif à côté, et en n'affichant pas de pourcentage sous un seuil défini à l'avance"}],
   "correct_answer":"c","feedback":"Un pourcentage sans son dénominateur est une information incomplète. Sous le seuil retenu, afficher « n. s. » évite qu'une décision se construise sur onze réponses."},
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
