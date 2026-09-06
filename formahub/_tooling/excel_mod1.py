#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, json, os
sys.path.insert(0, "/tmp")
from fh_builder import build

M = {}
QUIZ = {}
FORM = "Excel &amp; analyse de données appliquée"

M["excel-analyse-donnees/module-1"] = {
 "formation": FORM,
 "titre": "Structurer une Donnée Exploitable",
 "num": 1, "total": 4, "duree": "65 min", "niveau": "Débutant",
 "module_id": "formation-excel-analyse-donnees-module-1",
 "situation": [
   "Vendredi 14 h. Votre direction vous demande, pour lundi matin, quelle catégorie de produits a le plus reculé sur le dernier trimestre et dans quelles régions. La réponse existe : elle est dans un fichier que le service commercial vient de vous envoyer, nommé <em>extraction_ventes_2025_v3_FINAL.xlsx</em>, 12 400 lignes.",
   "Vous l'ouvrez. La première ligne est un titre étalé sur huit colonnes fusionnées. Les en-têtes sont en ligne 4. La colonne « Région » contient « Sud-Ouest », « sud ouest », « SO » et 340 cellules vides. Les montants sont alignés à gauche, ce qui veut dire qu'Excel les considère comme du texte. Des lignes « Total mensuel » sont intercalées tous les trente enregistrements. Et une colonne « Client / Contact / Téléphone » empile trois informations séparées par des barres obliques.",
   "Vous avez deux options. La première, la plus tentante, est de commencer tout de suite à filtrer et à faire des sommes ; vous obtiendrez un chiffre lundi matin, et il sera faux. La seconde est de consacrer les deux premières heures à rendre ce fichier analysable, et les vingt minutes suivantes à répondre à la question. Ce module traite de ces deux heures — la partie du travail d'analyse dont personne ne parle, et qui décide de tout le reste.",
 ],
 "objectifs": [
   "Reconnaître en une minute si un fichier est exploitable ou non",
   "Nommer les cinq défauts de structure qui rendent une analyse impossible",
   "Convertir une plage en tableau structuré et exploiter ses références nommées",
   "Nettoyer une colonne de texte, de nombres ou de dates selon une chaîne de contrôle fixe",
   "Séparer une colonne multi-valeurs sans perdre d'enregistrements",
   "Documenter un nettoyage pour qu'il soit reproductible le mois suivant",
 ],
 "sections": [
  {"titre": "Un tableau lisible n'est pas un tableau exploitable",
   "paras": [
     "La confusion de départ, celle qui produit tous les fichiers que l'on vient de décrire, est de croire qu'un tableau bien présenté est un tableau bien construit. Ce sont deux objectifs opposés, et ils ne peuvent pas être servis par le même document.",
     "Un tableau <strong>lisible</strong> est fait pour l'œil humain. Il porte un titre, des totaux visibles, des sous-groupes séparés par des lignes vides, des cellules fusionnées pour indiquer qu'une valeur couvre plusieurs lignes. Il se lit d'un coup et se comprend sans explication.",
     "Un tableau <strong>exploitable</strong> est fait pour la machine. Il n'a qu'une seule ligne d'en-têtes, une observation par ligne, une variable par colonne, aucune cellule vide porteuse de sens implicite, aucun total intercalé. Il est souvent laid, répétitif, et personne n'a envie de le lire directement.",
     "Toute la difficulté du travail sur données en entreprise tient dans le fait que les fichiers circulent sous leur forme lisible, alors qu'ils devraient circuler sous leur forme exploitable, la présentation étant reconstruite à l'arrivée. Vous ne changerez pas cette habitude chez vos interlocuteurs ; vous pouvez en revanche systématiser la conversion, et c'est exactement l'objet de ce module.",
     "La règle qui résume tout, formalisée en statistique sous le nom de <em>données rangées</em> : <strong>une ligne est une observation, une colonne est une variable, une cellule est une valeur</strong>. Trois phrases, et 90 % des problèmes rencontrés dans un fichier d'entreprise sont une violation de l'une d'elles.",
   ],
   "blocks": [
     {"type": "exemple", "titre": "le même contenu, deux structures",
      "paras": [
        "<em>Version lisible</em> — un tableau où les mois sont en colonnes : une colonne « Produit », puis douze colonnes « Janvier », « Février »… jusqu'à « Décembre », et une colonne « Total ». Quatre-vingts lignes, une page, parfaitement compréhensible en réunion.",
        "<em>Version exploitable</em> — trois colonnes seulement : « Produit », « Mois », « Montant ». Neuf cent soixante lignes, aucune envie de la lire.",
        "La question qui tranche : « quel a été le chiffre d'affaires du produit X entre mars et juin ? ». Sur la version exploitable, c'est une somme conditionnelle en une formule. Sur la version lisible, il faut sélectionner quatre colonnes à la main, et refaire l'opération à chaque nouvelle question. Ajoutez maintenant une année : la version exploitable gagne 960 lignes et rien d'autre ne bouge ; la version lisible demande de restructurer tout le fichier.",
      ]},
     {"type": "pitfall", "titre": "vouloir garder les deux à la fois",
      "paras": [
        "La tentation naturelle est de construire un fichier qui soit à la fois beau et calculable : on garde les mois en colonnes mais on ajoute des formules pour compenser, on garde les totaux intercalés mais on les exclut « en faisant attention ».",
        "Cela fonctionne pendant trois semaines, puis quelqu'un insère une ligne, et vos plages de calcul se décalent sans qu'aucun message d'erreur n'apparaisse. C'est le pire scénario possible : un fichier qui produit des chiffres faux sans jamais signaler qu'il est cassé.",
        "La bonne architecture sépare toujours trois choses, dans trois onglets distincts : <strong>les données brutes</strong> telles qu'elles ont été reçues, qu'on ne modifie jamais ; <strong>les données nettoyées</strong>, au format exploitable ; <strong>la présentation</strong>, qui ne contient que des formules pointant vers l'onglet nettoyé. Vous verrez au module 4 que cette séparation en trois est aussi ce qui rend un tableau de bord fiable.",
      ]},
   ]},

  {"titre": "Les cinq défauts qui rendent un fichier inanalysable",
   "paras": [
     "Sur des centaines de fichiers d'entreprise, les problèmes se ramènent à cinq familles. Les reconnaître en une minute, dès l'ouverture, est la compétence la plus rentable de tout ce parcours : elle vous dit combien de temps le nettoyage va coûter avant que vous n'ayez promis une date.",
     "<strong>1. Les cellules fusionnées.</strong> Une cellule fusionnée sur trois lignes contient en réalité une valeur et deux vides. Tout filtre, tout tri, tout tableau croisé dynamique perdra les deux lignes vides ou les traitera comme des enregistrements sans région, sans client, sans catégorie. C'est le défaut le plus destructeur parce qu'il est invisible : le fichier a l'air complet à l'écran.",
     "<strong>2. Les valeurs multiples dans une cellule.</strong> Une colonne « Client / Contact / Téléphone » ou une colonne « Tags » contenant « urgent ; export ; grand compte » empêche tout regroupement. Vous ne pourrez jamais compter les affaires « urgent » de façon fiable, puisque la valeur n'existe pas en tant que telle.",
     "<strong>3. Les totaux et sous-totaux intercalés.</strong> Une ligne « Total mars » au milieu des données est un enregistrement du point de vue d'Excel. Si vous sommez la colonne, vous comptez deux fois. L'erreur est d'autant plus dangereuse que le résultat reste plausible : un doublement est visible, un sur-comptage de 8 % ne l'est pas.",
     "<strong>4. Les nombres et les dates stockés comme du texte.</strong> Le symptôme est visuel et immédiat : dans une cellule non formatée, Excel aligne les nombres et les dates à droite, le texte à gauche. Une colonne de montants alignée à gauche est une colonne de texte : la somme renverra zéro, ou pire, un total partiel si certaines cellules sont bien typées et d'autres non.",
     "<strong>5. Les en-têtes qui ne sont pas en première ligne, ou qui n'existent pas.</strong> Un titre, une date d'extraction, une ligne vide, puis les vrais en-têtes en ligne 4 : tant que la structure n'est pas ramenée à une ligne d'en-têtes unique en ligne 1, aucun outil ne saura ce qu'il manipule.",
   ],
   "blocks": [
     {"type": "method", "titre": "le diagnostic d'ouverture en six gestes, moins de deux minutes",
      "paras": ["À faire systématiquement avant de promettre un délai. Chacun de ces gestes prend quelques secondes et vous évite de découvrir le problème après trois heures de travail."],
      "steps": [
        "<strong>Ctrl + Fin</strong> pour aller à la dernière cellule utilisée. Elle vous donne les dimensions réelles du fichier. Si elle se situe très au-delà de vos données, le fichier traîne des lignes ou colonnes fantômes qui fausseront toutes vos plages.",
        "<strong>Regardez l'alignement de chaque colonne numérique ou de date.</strong> Aligné à gauche sans formatage explicite = c'est du texte. Notez les colonnes concernées, ce sera votre première conversion.",
        "<strong>Sélectionnez tout, puis Accueil &gt; Fusionner et centrer.</strong> Si le bouton apparaît actif, il y a des cellules fusionnées. Le repérage visuel ne suffit pas : une fusion horizontale sur deux colonnes étroites se voit à peine.",
        "<strong>Activez le filtre automatique (Ctrl + Maj + L) et déroulez chaque colonne catégorielle.</strong> La liste des valeurs distinctes vous montre immédiatement les variantes d'écriture, les espaces parasites et les vides. C'est le geste le plus informatif des six.",
        "<strong>Cherchez les mots « Total », « Sous-total », « TOTAL »</strong> (Ctrl + F). S'ils apparaissent ailleurs qu'en fin de fichier, vous avez des lignes de synthèse intercalées à supprimer.",
        "<strong>Comptez.</strong> Un NBVAL sur la première colonne et sur chaque autre colonne : des écarts entre colonnes révèlent les vides, et le total vous donne le nombre d'enregistrements que vous devrez retrouver après nettoyage. Notez ce chiffre : c'est votre garde-fou pour tout le reste du travail.",
      ]},
     {"type": "exemple", "titre": "ce que coûte un défaut non détecté",
      "paras": [
        "Un fichier de 12 400 lignes contient 410 lignes « Total mensuel » intercalées, non détectées. L'analyste somme la colonne Montant et annonce 8,7 M€ de chiffre d'affaires. Le vrai chiffre est 4,4 M€ : les totaux mensuels représentent exactement le double de comptage sur les mois concernés.",
        "Ici l'erreur est spectaculaire et sera repérée, parce que le chiffre est presque doublé. Modifions à peine le scénario : les lignes intercalées ne sont pas des totaux mensuels mais des lignes « Remise commerciale », déjà déduites par ailleurs. Elles représentent 6 % du volume. L'analyse annonce alors une hausse de 4 % là où il y a en réalité une baisse de 2 %, et personne ne s'en apercevra — le chiffre est plausible, il est présenté avec assurance, et une décision sera prise dessus.",
        "La leçon n'est pas que les erreurs de données sont graves : c'est que <strong>les erreurs graves sont celles qui restent plausibles</strong>. Un diagnostic d'ouverture systématique est la seule protection, parce qu'il ne dépend pas de votre capacité à trouver le résultat suspect.",
      ]},
     {"type": "pitfall", "titre": "corriger à la main ce qu'on aurait dû corriger par une règle",
      "paras": [
        "Face à 340 cellules « Région » vides et à quatre orthographes de « Sud-Ouest », le réflexe est d'ouvrir le fichier et de corriger ligne à ligne. Sur 12 000 lignes, cela prend une journée, contient des erreurs de frappe, et sera intégralement à refaire le mois prochain sur la nouvelle extraction.",
        "Toute correction manuelle est une correction perdue. La règle : dès qu'un même geste doit être répété plus de dix fois, il devient une opération — recherche-remplacer, formule de normalisation, ou requête Power Query (module 3). Le temps de mise en place est presque toujours inférieur au temps du geste manuel, et il est capitalisé.",
        "La seule exception légitime est le cas véritablement unique — trois valeurs aberrantes identifiées et arbitrées une par une. Dans ce cas, notez-les dans votre journal de transformation, sinon personne, y compris vous dans six mois, ne saura d'où vient la correction.",
      ]},
   ]},

  {"titre": "Le tableau structuré : le seul réflexe de mise en forme qui compte",
   "paras": [
     "Une plage de cellules ordinaire n'a aucune identité pour Excel : c'est un rectangle de coordonnées. Un <strong>tableau structuré</strong> — obtenu par Ctrl + L, ou Insertion &gt; Tableau — transforme cette plage en objet nommé, doté de colonnes nommées, et qui connaît ses propres limites.",
     "Ce changement paraît cosmétique. Il modifie en réalité le comportement de tout ce que vous construirez ensuite, sur quatre points décisifs.",
     "<strong>Les plages s'étendent seules.</strong> Ajoutez une ligne à la fin d'un tableau structuré : toutes les formules, tous les tableaux croisés dynamiques et tous les graphiques qui s'y réfèrent l'intègrent automatiquement. Avec une plage ordinaire, chacun de ces objets pointe vers un rectangle figé, et vous devrez tous les mettre à jour à la main — travail que l'on oublie systématiquement de faire, ce qui produit des rapports silencieusement incomplets.",
     "<strong>Les formules deviennent lisibles.</strong> <code>=SOMME.SI.ENS(Ventes[Montant];Ventes[Région];\"Sud-Ouest\")</code> se relit un an plus tard ; <code>=SOMME.SI.ENS(F2:F12400;C2:C12400;\"Sud-Ouest\")</code> ne se relit pas, et surtout ne se vérifie pas.",
     "<strong>Les formules se propagent d'elles-mêmes.</strong> Saisissez une formule dans une cellule d'une colonne de tableau : elle se recopie instantanément sur toute la colonne, et sur chaque ligne ajoutée ensuite. Cela supprime la première cause d'incohérence des fichiers Excel — la colonne calculée où trois cellules contiennent une formule différente des autres, généralement parce que quelqu'un a fait un copier-coller malheureux.",
     "<strong>Les en-têtes restent visibles</strong> au défilement, sans avoir à figer les volets. Détail de confort, mais qui évite l'erreur bien réelle consistant à lire une valeur dans la mauvaise colonne à la ligne 3 000.",
     "Le coût de cette conversion est de deux secondes. Il n'existe aucune raison sérieuse de travailler sur une plage ordinaire, et pourtant la majorité des fichiers d'entreprise n'en contient aucun. Prenez l'habitude : le premier geste après le nettoyage est Ctrl + L, puis nommer le tableau dans le champ prévu à gauche du ruban — <em>Ventes</em>, <em>Clients</em>, <em>Budget2025</em>, jamais <em>Tableau1</em>.",
   ],
   "blocks": [
     {"type": "method", "titre": "convertir et nommer proprement un tableau",
      "steps": [
        "<strong>Assurez-vous d'abord qu'il n'y a qu'une ligne d'en-têtes</strong>, en ligne 1 de la plage, sans ligne vide ni titre au-dessus. Supprimez les lignes parasites avant la conversion, pas après.",
        "<strong>Vérifiez qu'aucune cellule n'est fusionnée</strong> : Excel refusera la conversion ou produira un résultat incohérent. Défusionnez tout, puis remplissez les vides créés (voir la méthode de la section suivante).",
        "<strong>Placez le curseur dans la plage et faites Ctrl + L.</strong> Cochez « Mon tableau comporte des en-têtes ». Excel détecte la plage seul ; vérifiez tout de même qu'elle correspond à ce que vous attendez.",
        "<strong>Nommez le tableau</strong> dans Création de tableau &gt; Nom du tableau. Un nom court, sans espace, qui dit ce que contient l'objet. Ce nom apparaîtra dans toutes vos formules : il vaut la peine d'y réfléchir cinq secondes.",
        "<strong>Renommez les colonnes</strong> si nécessaire : des en-têtes courts, sans retour à la ligne, sans unité entre parenthèses si vous pouvez l'éviter. <em>Montant_HT</em> plutôt que <em>Montant (en € HT, hors remise)</em> — l'unité se documente ailleurs, elle n'a pas à alourdir chaque formule.",
        "<strong>Vérifiez le typage colonne par colonne</strong> après conversion : le tableau structuré n'a rien converti, il a seulement nommé. Une colonne de texte reste du texte, et c'est l'objet de la section suivante.",
      ]},
     {"type": "pitfall", "titre": "laisser des colonnes vides ou des lignes vides à l'intérieur du tableau",
      "paras": [
        "Une colonne entièrement vide au milieu des données, souvent un vestige d'une ancienne colonne supprimée par effacement plutôt que par suppression, coupe la détection automatique de plage : Excel proposera un tableau qui s'arrête avant elle, et vous perdrez la moitié de vos colonnes sans avertissement.",
        "Même effet pour une ligne entièrement vide : elle coupe le tableau en deux. Le réflexe correct est de supprimer les lignes et colonnes vides — clic droit &gt; Supprimer — et non de les effacer avec la touche Suppr, qui vide le contenu mais laisse la structure en place. Un Ctrl + Fin qui vous emmène en XFD1048576 est le symptôme classique de ce mauvais geste répété.",
      ]},
   ]},

  {"titre": "Nettoyer : la chaîne de contrôle en sept opérations",
   "paras": [
     "Le nettoyage se fait toujours dans le même ordre, et cet ordre n'est pas arbitraire : chaque opération suppose que la précédente est faite. Défusionner avant de remplir les vides, remplir les vides avant de dédoublonner, dédoublonner avant de convertir les types — l'inverse produit des résultats faux à chaque étape.",
     "<strong>Opération 1 — défusionner et remplir.</strong> Sélectionnez tout, désactivez Fusionner et centrer. Les vides apparaissent. Pour les combler avec la valeur du dessus : sélectionnez la colonne, F5 &gt; Cellules &gt; Cellules vides, tapez <code>=</code> puis flèche haut, et validez par <strong>Ctrl + Entrée</strong>. Toutes les cellules vides reçoivent la valeur de leur voisine supérieure en une fois. Convertissez ensuite en valeurs par un collage spécial, sinon la colonne reste une chaîne de formules fragile.",
     "<strong>Opération 2 — supprimer les lignes de synthèse.</strong> Filtrez la colonne concernée sur les libellés « Total », « Sous-total », « Cumul », sélectionnez les lignes visibles, supprimez-les, retirez le filtre. Comparez ensuite votre compte de lignes à celui noté au diagnostic : l'écart doit correspondre exactement au nombre de lignes de synthèse attendues.",
     "<strong>Opération 3 — normaliser les textes.</strong> Trois fonctions font l'essentiel : <code>SUPPRESPACE</code> retire les espaces superflus, y compris les espaces de fin invisibles qui empêchent deux valeurs identiques de se reconnaître ; <code>MAJUSCULE</code> ou <code>NOMPROPRE</code> uniformisent la casse ; <code>SUBSTITUE</code> corrige un caractère précis. Traitez la colonne dans une colonne voisine, vérifiez, puis remplacez par collage spécial en valeurs.",
     "<strong>Opération 4 — traiter les variantes d'écriture.</strong> C'est le seul point qui demande un jugement humain : « SO », « Sud Ouest » et « sud-ouest » sont la même région, mais « Sud » et « Sud-Ouest » ne le sont peut-être pas. Construisez une petite table de correspondance à deux colonnes — valeur reçue, valeur normalisée — placez-la dans un onglet séparé, et allez y chercher la valeur propre par une fonction de recherche (module 2). Cette table est réutilisable le mois suivant : c'est ce qui distingue un nettoyage capitalisé d'un nettoyage jetable.",
     "<strong>Opération 5 — convertir les types.</strong> Pour une colonne de nombres en texte, la méthode la plus sûre est Données &gt; Convertir : sélectionnez la colonne, cliquez Convertir, Suivant, Suivant, choisissez le format Standard et le bon séparateur décimal, Terminer. Pour les dates, la même commande avec le format Date et l'ordre correct — JMA ou MJA selon l'origine du fichier. Vérifiez toujours après conversion : un alignement à droite et une somme non nulle.",
     "<strong>Opération 6 — séparer les colonnes multi-valeurs.</strong> Données &gt; Convertir, option Délimité, en indiquant le séparateur (barre oblique, point-virgule, tabulation). Attention : cette opération écrase les colonnes situées à droite. Insérez d'abord autant de colonnes vides que de valeurs attendues. Si le nombre de valeurs varie d'une ligne à l'autre, ne séparez pas ainsi — c'est un cas pour Power Query, traité au module 3.",
     "<strong>Opération 7 — traiter les doublons en connaissance de cause.</strong> Données &gt; Supprimer les doublons est un bouton dangereux, parce qu'il agit sur les colonnes que vous cochez et détruit sans retour. Avant de l'utiliser, comptez : un <code>NB.SI</code> sur la colonne d'identifiant vous dit combien de lignes sont concernées. Puis demandez-vous si ces doublons sont des erreurs de saisie ou des enregistrements légitimes — deux commandes du même client le même jour ne sont pas un doublon.",
   ],
   "blocks": [
     {"type": "exemple", "titre": "la colonne Région, de bout en bout",
      "paras": [
        "État initial : 12 400 lignes, colonne C. Le filtre automatique révèle onze valeurs distinctes pour six régions réelles, plus 340 vides.",
        "<em>Défusion</em> : deux blocs de cellules fusionnées détectés, correspondant à 180 lignes qui apparaissaient renseignées à l'écran et étaient vides en réalité. Après remplissage par la valeur supérieure, il reste 160 vraies cellules vides.",
        "<em>Normalisation</em> : <code>=SUPPRESPACE(MAJUSCULE(C2))</code> ramène les onze valeurs à huit. Les trois écarts éliminés étaient des espaces de fin — invisibles, et responsables à eux seuls de trois régions fantômes dans le tableau croisé dynamique.",
        "<em>Correspondance</em> : une table de six lignes fait passer « SO » et « SUD OUEST » sur « Sud-Ouest », « IDF » sur « Île-de-France ». On tombe à six valeurs distinctes.",
        "<em>Vides restants</em> : les 160 lignes sans région sont examinées. Elles correspondent toutes à des commandes export. Elles reçoivent la valeur « Export », qui devient une septième modalité légitime — et non une donnée manquante à ignorer. Ce dernier point est le plus important de l'exemple : <strong>un vide a presque toujours un sens, et le comprendre vaut mieux que le supprimer</strong>.",
      ]},
     {"type": "pitfall", "titre": "écraser la source",
      "paras": [
        "Le nettoyage se fait sur une copie, jamais sur le fichier reçu. Cela paraît évident et c'est pourtant l'erreur la plus fréquemment commise, parce qu'elle se produit par inadvertance : on ouvre le fichier reçu, on commence à corriger « juste une colonne », et deux heures plus tard il n'existe plus aucune trace de l'état d'origine.",
        "Sans source intacte, vous ne pouvez plus rien vérifier : ni comparer un total avant et après, ni comprendre d'où vient une valeur surprenante, ni refaire le nettoyage autrement si vous découvrez une erreur de méthode. La discipline minimale : le fichier reçu est copié dans un onglet « source » que l'on ne touche plus, ou conservé tel quel dans un dossier daté, et tout le travail se fait ailleurs.",
      ]},
   ]},

  {"titre": "Rendre le nettoyage reproductible : le journal de transformation",
   "paras": [
     "Un nettoyage n'est jamais fait une fois. L'extraction reviendra le mois prochain, avec les mêmes défauts, parce que le système qui la produit n'a pas changé. Si votre travail ne laisse aucune trace, vous le referez intégralement, et vous ne le referez pas exactement de la même façon — ce qui rendra vos deux mois incomparables.",
     "Le journal de transformation est un onglet du classeur, à quatre colonnes : <strong>date</strong>, <strong>colonne concernée</strong>, <strong>opération effectuée</strong>, <strong>lignes affectées</strong>. Une ligne par opération. Il prend cinq minutes à tenir et il répond aux trois questions qui reviennent toujours.",
     "<em>« Pourquoi ce chiffre a-t-il changé depuis la version précédente ? »</em> — la réponse est dans le journal, pas dans votre mémoire.",
     "<em>« Est-ce qu'on peut reproduire cette analyse sur le trimestre suivant ? »</em> — oui, en rejouant les lignes du journal dans l'ordre.",
     "<em>« Qui a décidé que les commandes sans région étaient de l'export ? »</em> — question redoutable en réunion quand la décision a été prise trois mois plus tôt. Un arbitrage non documenté est un arbitrage indéfendable.",
     "Ce journal est aussi la meilleure preuve de sérieux que vous puissiez présenter. Un analyste qui montre son journal de transformation obtient une confiance qu'aucune qualité de présentation ne procure, parce qu'il rend son travail vérifiable au lieu de demander qu'on le croie.",
   ],
   "blocks": [
     {"type": "h3", "titre": "Quatre chiffres à conserver systématiquement",
      "paras": [
        "En plus du journal, notez quatre valeurs avant et après le nettoyage. Elles constituent votre contrôle de non-destruction, et leur comparaison prend dix secondes.",
        "<strong>Le nombre de lignes.</strong> L'écart doit s'expliquer entièrement par les suppressions documentées. Un écart inexpliqué de trois lignes est un signal aussi sérieux qu'un écart de trois cents.",
        "<strong>La somme de la colonne de montant principale.</strong> Après conversion de type, elle doit augmenter — puisque des cellules texte comptaient pour zéro — et l'augmentation doit correspondre à la somme des cellules converties. Après suppression des lignes de total, elle doit diminuer d'un montant que vous pouvez recalculer.",
        "<strong>Le nombre de valeurs distinctes des colonnes catégorielles.</strong> Il doit diminuer sous l'effet de la normalisation, et se stabiliser sur le nombre réel de modalités. Une colonne qui reste à onze modalités pour six régions n'est pas nettoyée.",
        "<strong>La plage de dates.</strong> Minimum et maximum. Une date en 1900 signale une conversion ratée ; une date en 2087 signale une inversion jour-mois-année. Ces deux anomalies passent inaperçues dans un tableau croisé dynamique et déforment toute analyse temporelle.",
      ]},
     {"type": "exemple", "titre": "un journal réel, six lignes",
      "paras": [
        "<em>14/03 — toutes colonnes — défusion de 2 blocs, remplissage vers le bas — 180 lignes.</em>",
        "<em>14/03 — toutes colonnes — suppression des lignes « Total mensuel » — 410 lignes supprimées, 12 400 → 11 990.</em>",
        "<em>14/03 — Région — SUPPRESPACE + MAJUSCULE + table de correspondance (onglet ref_regions) — 11 modalités → 6.</em>",
        "<em>14/03 — Région — 160 vides affectés à « Export » après vérification que toutes ces commandes ont un pays de livraison hors France — arbitrage validé avec M. B. du service commercial.</em>",
        "<em>14/03 — Montant_HT — conversion texte vers nombre (Données &gt; Convertir, séparateur décimal virgule) — somme 3 950 k€ → 4 402 k€, écart de 452 k€ correspondant aux 1 380 cellules converties.</em>",
        "<em>14/03 — Date_commande — conversion JMA, contrôle min/max : 02/01/2025 – 31/12/2025, cohérent.</em>",
        "Six lignes, cinq minutes. Elles rendent l'analyse défendable, reproductible, et transmissible à quelqu'un d'autre — trois propriétés que la quasi-totalité des fichiers d'entreprise n'ont pas.",
      ]},
   ]},
 ],

 "etude_cas": {
   "titre": "Les deux heures du vendredi soir",
   "html": """
<p>Reprenons le fichier de la mise en situation : 12 400 lignes, huit défauts, une question à traiter pour lundi. Voici le déroulé réel, minuté.</p>
<p><strong>Minutes 0 à 5 — le diagnostic.</strong> Copie du fichier sous un nom daté, ouverture de la copie. Ctrl + Fin renvoie en AB13208 alors que les données s'arrêtent en H12404 : le fichier traîne des colonnes et des lignes fantômes. Le bouton Fusionner apparaît actif : il y a des fusions. Quatre colonnes numériques sont alignées à gauche. Ctrl + F sur « Total » remonte 410 occurrences. Le filtre sur Région montre onze modalités. Diagnostic posé : les cinq défauts sont présents. Estimation annoncée à la direction : réponse lundi matin, pas vendredi soir. Cette phrase est le premier livrable, et elle vaut mieux qu'un chiffre faux dans l'heure.</p>
<p><strong>Minutes 5 à 15 — la structure.</strong> Suppression des lignes 1 à 3 (titre, date d'extraction, ligne vide) pour ramener les en-têtes en ligne 1. Suppression, et non effacement, des colonnes I à AB et des lignes 12405 à 13208. Nouveau Ctrl + Fin : H12401. Le fichier fait maintenant sa taille réelle.</p>
<p><strong>Minutes 15 à 30 — la défusion et les lignes parasites.</strong> Défusion générale, puis remplissage des vides par F5 &gt; Cellules vides et Ctrl + Entrée, colonne par colonne, en vérifiant à chaque fois que la valeur reprise est la bonne. Filtre sur « Total mensuel », suppression des 410 lignes, contrôle du compte : 12 400 - 410 = 11 990. Le compte tombe juste, ce qui confirme qu'aucune ligne utile n'a été emportée.</p>
<p><strong>Minutes 30 à 50 — les types.</strong> Données &gt; Convertir sur les quatre colonnes numériques, séparateur décimal virgule. La somme de Montant_HT passe de 3 950 k€ à 4 402 k€ : l'écart de 452 k€ correspond aux 1 380 cellules qui étaient du texte et comptaient pour zéro. C'est le moment le plus instructif de l'opération — sans cette conversion, l'analyse aurait sous-estimé le chiffre d'affaires de 10 %, uniformément répartis, donc invisibles.</p>
<p>Conversion de Date_commande en JMA. Contrôle min/max : 02/01/2025 et 31/12/2025. Aucune date en 1900, aucune en 2087.</p>
<p><strong>Minutes 50 à 75 — les catégories.</strong> Colonne Région traitée comme décrit plus haut : onze modalités ramenées à six, plus « Export » pour les 160 vides après vérification du pays de livraison. Colonne Catégorie_produit : sept modalités, dont « Accessoires » et « accessoires  » (deux espaces de fin) — SUPPRESPACE les réunit. Colonne « Client / Contact / Téléphone » séparée en trois par Données &gt; Convertir, après insertion de deux colonnes vides à droite. Trente-quatre lignes contiennent une valeur supplémentaire (un second contact) : elles sont isolées, traitées à part, et notées au journal.</p>
<p><strong>Minutes 75 à 85 — la mise en tableau et le journal.</strong> Ctrl + L, tableau nommé <em>Ventes2025</em>. Colonnes renommées sans espaces ni parenthèses. Journal de transformation rempli, huit lignes. Quatre chiffres de contrôle notés.</p>
<p><strong>Minutes 85 à 105 — la réponse à la question.</strong> Un tableau croisé dynamique (module 3), catégories en lignes, trimestres en colonnes, somme des montants en valeurs. La réponse apparaît en trois minutes : la catégorie Mobilier recule de 18 % au quatrième trimestre, et le recul est concentré sur deux régions, Sud-Ouest et Est, les autres étant stables. Vingt minutes suffisent ensuite à recouper ce résultat par un second calcul indépendant.</p>
<p><strong>Le rapport de temps.</strong> Quatre-vingt-cinq minutes de préparation, vingt minutes d'analyse. C'est la proportion normale, et c'est ce qui surprend le plus quand on découvre le travail sur données : l'analyse proprement dite est la partie courte. Un analyste qui annonce une réponse en vingt minutes sur un fichier non préparé n'a pas été plus rapide, il a sauté les quatre-vingt-cinq minutes qui rendent sa réponse vraie.</p>
<p><strong>La leçon transposable.</strong> Ne promettez jamais un délai avant le diagnostic d'ouverture, et ne présentez jamais un chiffre dont vous ne pouvez pas retracer la fabrication. Le journal de transformation n'est pas de la bureaucratie : c'est la seule chose qui vous permettra, lundi, de répondre calmement à la question « tu es sûr de ton chiffre ? ».</p>
"""},

 "checklist": {
   "titre": "Checklist — préparer un fichier avant toute analyse",
   "items": [
     "Le fichier reçu a été copié : la source d'origine reste intacte quelque part",
     "Ctrl + Fin a été fait, les lignes et colonnes fantômes sont supprimées (pas effacées)",
     "Les en-têtes sont sur une ligne unique, en première ligne de la plage",
     "Aucune cellule n'est fusionnée dans la zone de données",
     "Les vides issus des fusions ont été remplis par la valeur du dessus, puis figés en valeurs",
     "Les lignes de total, sous-total et cumul intercalées ont été supprimées",
     "Le nombre de lignes supprimées est expliqué et noté",
     "Chaque colonne numérique s'aligne à droite et sa somme est non nulle",
     "Chaque colonne de date s'aligne à droite, et son minimum et son maximum sont plausibles",
     "Les colonnes de texte ont été passées à SUPPRESPACE et à une casse uniforme",
     "Les variantes d'écriture sont traitées par une table de correspondance, pas à la main",
     "Le nombre de valeurs distinctes de chaque colonne catégorielle correspond à la réalité métier",
     "Les cellules vides ont été comprises avant d'être remplies ou écartées",
     "Les colonnes multi-valeurs ont été séparées, colonnes vides insérées au préalable",
     "Les doublons ont été comptés et qualifiés avant toute suppression",
     "La plage est convertie en tableau structuré et porte un nom explicite",
     "Aucune ligne ni colonne entièrement vide ne subsiste à l'intérieur du tableau",
     "Le journal de transformation est rempli : date, colonne, opération, lignes affectées",
     "Les quatre chiffres de contrôle sont notés avant et après nettoyage",
     "Les données brutes, les données nettoyées et la présentation sont dans trois onglets distincts",
   ]},

 "glossaire": [
   ("Données rangées", "Structure où une ligne est une observation, une colonne une variable, une cellule une valeur. Condition d'exploitabilité de tout fichier."),
   ("Tableau structuré", "Plage convertie en objet nommé par Ctrl + L. Étend ses plages automatiquement, nomme ses colonnes et propage ses formules."),
   ("Cellule fusionnée", "Cellule couvrant plusieurs lignes ou colonnes. Contient une valeur et des vides : détruit filtres, tris et tableaux croisés dynamiques."),
   ("Ligne de synthèse intercalée", "Ligne de total ou de sous-total placée au milieu des données. Comptée comme un enregistrement, elle produit un double comptage."),
   ("Typage", "Nature attribuée par Excel à une valeur : nombre, date ou texte. Un nombre stocké en texte compte pour zéro dans toute somme."),
   ("SUPPRESPACE", "Fonction retirant les espaces superflus d'une chaîne, y compris les espaces de fin invisibles qui empêchent deux valeurs identiques de se reconnaître."),
   ("Table de correspondance", "Table à deux colonnes associant chaque valeur reçue à sa valeur normalisée. Réutilisable d'une extraction à l'autre."),
   ("Données &gt; Convertir", "Commande de conversion de type et de séparation de colonnes. Écrase les colonnes situées à droite : insérer des colonnes vides au préalable."),
   ("Journal de transformation", "Onglet listant chaque opération de nettoyage : date, colonne, opération, lignes affectées. Rend l'analyse reproductible et défendable."),
   ("Chiffres de contrôle", "Nombre de lignes, somme principale, valeurs distinctes, plage de dates. Relevés avant et après nettoyage pour détecter toute destruction involontaire."),
   ("Valeur manquante", "Cellule vide. A presque toujours un sens métier : à comprendre avant d'être remplie ou écartée."),
   ("Ctrl + Entrée", "Validation qui applique la saisie à toute la sélection en cours. Base du remplissage des cellules vides en une opération."),
 ],

 "retenir": [
   "Un tableau lisible et un tableau exploitable sont deux objets différents : ne cherchez jamais à les faire coïncider dans le même onglet.",
   "La règle de structure tient en trois phrases : une ligne est une observation, une colonne une variable, une cellule une valeur.",
   "Séparez toujours trois onglets : données brutes intactes, données nettoyées, présentation par formules.",
   "Cinq défauts rendent un fichier inanalysable : fusions, valeurs multiples, totaux intercalés, mauvais typage, en-têtes déplacés.",
   "Faites le diagnostic d'ouverture en six gestes avant de promettre un délai — jamais après.",
   "Les erreurs graves sont celles qui restent plausibles : un doublement se voit, un écart de 6 % ne se voit pas.",
   "Un montant aligné à gauche est du texte, et compte pour zéro dans toute somme.",
   "Toute correction manuelle est perdue : au-delà de dix répétitions, il faut une règle, pas un geste.",
   "L'ordre des opérations de nettoyage n'est pas arbitraire : défusionner, supprimer les synthèses, normaliser, corriger les variantes, convertir, séparer, dédoublonner.",
   "Ctrl + L après le nettoyage, systématiquement, et un nom de tableau explicite : les plages s'étendent seules et les formules se relisent.",
   "Supprimez les lignes et colonnes vides, ne les effacez pas : l'effacement laisse la structure et coupe la détection de plage.",
   "Un vide a presque toujours un sens : comprenez-le avant de le remplir ou de l'écarter.",
   "Ne cliquez jamais sur Supprimer les doublons avant d'avoir compté et qualifié ce qui est en double.",
   "Le nettoyage se fait sur une copie : sans source intacte, plus rien n'est vérifiable.",
   "Le journal de transformation coûte cinq minutes et rend l'analyse reproductible, défendable et transmissible.",
   "Relevez quatre chiffres de contrôle avant et après : lignes, somme principale, modalités distinctes, plage de dates.",
   "La proportion normale est de quatre-vingts pour cent de préparation et vingt pour cent d'analyse : celui qui répond en vingt minutes n'a pas été rapide, il a sauté la préparation.",
 ],

 "exercices": [
  {"titre": "Diagnostiquer un fichier en deux minutes", "niveau": "Débutant",
   "enonce": [
     "Un collègue vous transmet un fichier « suivi_stocks.xlsx » et vous demande combien d'articles sont en rupture. Vous constatez, dans l'ordre : Ctrl + Fin renvoie en AZ200000 alors que les données semblent s'arrêter vers la ligne 3 000 ; la colonne « Quantité » est alignée à gauche ; la colonne « Entrepôt » compte neuf modalités pour quatre entrepôts réels ; 220 cellules de la colonne « Date_inventaire » sont vides ; le mot « Total » apparaît 45 fois.",
     "Pour chacune de ces cinq observations, dites de quel défaut il s'agit, ce qu'il produirait si vous l'ignoriez, et par quelle opération vous le traitez. Puis annoncez à votre collègue un délai réaliste, en le justifiant.",
   ],
   "corrige": """
<p><strong>1. Ctrl + Fin en AZ200000.</strong> Défaut de structure : lignes et colonnes fantômes, presque toujours produites par des effacements au lieu de suppressions, ou par un export mal borné. <em>Si vous l'ignorez :</em> toute plage automatique — tableau croisé dynamique, graphique, mise en tableau — englobera 197 000 lignes vides. Le tableau croisé dynamique affichera une modalité « (vide) » massive, les graphiques auront un axe illisible, et le fichier pèsera dix fois son poids utile. <em>Traitement :</em> sélectionner de la première ligne vide jusqu'à la fin, clic droit &gt; Supprimer, idem pour les colonnes, puis enregistrer et rouvrir — Excel ne recalcule la dernière cellule utilisée qu'à l'ouverture, donc un Ctrl + Fin fait juste après la suppression peut encore renvoyer l'ancienne position.</p>
<p><strong>2. Colonne Quantité alignée à gauche.</strong> Défaut de typage : les quantités sont stockées en texte. <em>Si vous l'ignorez :</em> c'est le plus grave des cinq, parce qu'il est silencieux. Une somme renverra zéro si toute la colonne est en texte — anomalie visible — mais renverra un total partiel si seule une partie l'est, et rien ne vous alertera. Un test de rupture par <code>=SI(Quantité=0;...)</code> comparera par ailleurs du texte à un nombre et renverra FAUX pour tout le monde. <em>Traitement :</em> Données &gt; Convertir, format Standard, en vérifiant le séparateur décimal. Contrôle : la colonne s'aligne à droite et sa somme est non nulle et plausible.</p>
<p><strong>3. Neuf modalités pour quatre entrepôts.</strong> Défaut de normalisation : espaces parasites, casse, abréviations. <em>Si vous l'ignorez :</em> tout regroupement par entrepôt produira neuf lignes, et les ruptures d'un même entrepôt seront réparties sur deux ou trois d'entre elles. Le total général restera juste, ce qui rend l'erreur particulièrement difficile à repérer — vous ne verrez le problème que si vous regardez le détail. <em>Traitement :</em> SUPPRESPACE plus casse uniforme, ce qui ramènera probablement à cinq ou six modalités, puis table de correspondance pour les abréviations restantes.</p>
<p><strong>4. Deux cent vingt dates d'inventaire vides.</strong> Ce n'est pas encore un défaut : c'est une question à poser. <em>Si vous l'ignorez :</em> vous ne saurez pas si ces 220 articles n'ont jamais été inventoriés — auquel cas leur quantité affichée n'a aucune valeur et ils doivent sortir de l'analyse — ou s'il s'agit d'un champ simplement non renseigné par le système sur certains types d'articles. Les deux cas conduisent à des réponses opposées. <em>Traitement :</em> croiser avec une autre colonne pour comprendre le motif — s'agit-il d'un entrepôt précis, d'une famille d'articles, d'une période ? Puis trancher explicitement et noter l'arbitrage au journal. C'est le seul point des cinq qui exige une conversation avec le métier plutôt qu'une manipulation.</p>
<p><strong>5. Quarante-cinq occurrences de « Total ».</strong> Défaut de structure : lignes de synthèse intercalées, probablement une par entrepôt et par mois. <em>Si vous l'ignorez :</em> double comptage sur les quantités et surtout, dans le contexte précis de la question posée, des lignes « Total » avec une quantité positive seront comptées comme des articles non en rupture, ce qui faussera le dénominateur. <em>Traitement :</em> filtrer, sélectionner les lignes visibles, supprimer, puis contrôler que le compte a diminué d'exactement 45.</p>
<p><strong>Le délai à annoncer.</strong> Ne dites pas « c'est compliqué, je ne sais pas ». Dites : « le fichier demande environ une heure de préparation avant que le chiffre soit fiable ; je te réponds en début d'après-midi. Il y a un point que je ne peux pas trancher seul : 220 articles n'ont pas de date d'inventaire, et selon ce que cela signifie le résultat change. Sais-tu d'où ça vient ? ».</p>
<p><strong>Pourquoi cette formulation est la bonne :</strong> elle annonce un délai, elle en donne la raison sans se plaindre du fichier, et elle transforme le seul point bloquant en question adressée à la bonne personne. Un analyste qui négocie un délai en expliquant ce qu'il va faire obtient presque toujours ce délai ; celui qui dit simplement « ça va prendre du temps » ne l'obtient pas.</p>
"""},

  {"titre": "Restructurer un tableau de suivi mensuel", "niveau": "Intermédiaire",
   "enonce": [
     "Vous héritez d'un fichier de suivi budgétaire construit ainsi : colonne A « Service », colonne B « Poste de dépense », puis douze colonnes de janvier à décembre, puis une colonne « Total année ». Sous chaque service, une ligne « Sous-total service » en gras. En bas, une ligne « TOTAL GÉNÉRAL ». Quarante lignes de données, six services.",
     "On vous demande désormais de produire, chaque mois, le comparatif entre services sur les postes qui dérapent, et de pouvoir remonter à n'importe quel mois de n'importe quelle année.",
     "Décrivez la structure cible, la façon d'y arriver, et ce que vous répondez au contrôleur de gestion qui tient à son tableau actuel.",
   ],
   "corrige": """
<p><strong>Le diagnostic : trois violations de la règle de structure dans un seul fichier.</strong> Les mois en colonnes font qu'une variable — la période — est devenue une série de colonnes, alors qu'elle devrait être une colonne unique. Les sous-totaux intercalés mélangent deux niveaux d'agrégation dans la même plage. La colonne « Total année » est une valeur calculée stockée, qui deviendra fausse à la première modification et ne signalera rien.</p>
<p><strong>La structure cible.</strong> Quatre colonnes et rien d'autre : <em>Service</em>, <em>Poste</em>, <em>Mois</em> (au format date, premier jour du mois), <em>Montant</em>. Les 40 lignes deviennent 480. Aucun total nulle part, aucune ligne en gras, aucune couleur. Ce tableau ne se lit pas — et c'est normal, ce n'est pas ce qu'on lui demande.</p>
<p><strong>Deux façons d'y arriver, selon ce que vous savez faire.</strong></p>
<p><em>Sans Power Query :</em> supprimez d'abord les sous-totaux et le total général, ainsi que la colonne « Total année ». Puis construisez la version longue par copier-coller successifs — bloc de janvier, on ajoute une colonne Mois remplie de 01/01/2025, bloc de février en dessous, etc. Douze opérations, une demi-heure, faisable une fois. Ce n'est pas reproductible, et c'est précisément pour cela que ce n'est pas la bonne réponse à une demande mensuelle.</p>
<p><em>Avec Power Query</em> (module 3, mais posons-le ici) : supprimez les lignes de synthèse et la colonne de total, sélectionnez les douze colonnes de mois, puis Transformer &gt; Dépivoter les colonnes. Vous obtenez la structure cible en un clic. Renommez les deux colonnes produites en Mois et Montant, convertissez Mois en date. Le mois suivant, le rafraîchissement rejoue tout automatiquement. <strong>C'est la seule réponse acceptable à une demande récurrente</strong>, et le mot « Dépivoter » est probablement le plus utile de tout ce parcours.</p>
<p><strong>Ce que vous gagnez concrètement.</strong> Le comparatif entre services devient un tableau croisé dynamique de trois clics. L'ajout de 2026 consiste à empiler 480 lignes de plus, sans toucher à aucune formule ni à aucun graphique. Une question qui n'était pas prévue — « quels postes ont augmenté plus de deux mois de suite ? » — devient traitable, alors qu'elle était pratiquement impossible sur la structure large.</p>
<p><strong>Ce que vous répondez au contrôleur de gestion.</strong> Il n'a pas tort de tenir à son tableau : c'est celui qu'il présente en comité, tout le monde le connaît, et il le lit d'un coup d'œil. L'erreur serait de lui demander de renoncer à sa vue. Ne présentez donc pas votre travail comme un remplacement, mais comme un ajout invisible pour lui :</p>
<p>« Je ne touche pas à ton tableau : je le reconstruis à l'identique, en tableau croisé dynamique, à partir d'une table de détail. Tu continues à l'ouvrir et à le lire comme avant. Ce qui change, c'est qu'il se met à jour tout seul quand on ajoute un mois, et qu'on peut répondre à des questions nouvelles sans reconstruire quoi que ce soit. »</p>
<p>Puis faites-le réellement : reproduisez sa mise en forme, mois en colonnes, sous-totaux par service — un tableau croisé dynamique fait tout cela nativement. La démonstration qui emporte l'adhésion n'est pas l'argument technique, c'est de lui montrer son propre tableau, identique, se remplir seul à l'arrivée d'un nouveau mois.</p>
<p><strong>Ce qu'il ne faut surtout pas faire :</strong> lui expliquer que sa structure est « mal construite ». Elle est bien construite pour l'usage qu'il en a. Le problème n'est pas son tableau, c'est qu'il est à la fois le support de présentation et la base de données — et c'est cette confusion des rôles que vous corrigez, pas son travail.</p>
"""},

  {"titre": "Concevoir un protocole de nettoyage réutilisable", "niveau": "Avancé",
   "enonce": [
     "Vous recevrez désormais chaque mois la même extraction de 12 000 lignes, avec les mêmes défauts, et vous devrez produire le même rapport. Trois autres personnes de l'équipe recevront la même extraction et devront pouvoir faire le travail à votre place pendant vos congés.",
     "Concevez le dispositif complet : organisation des fichiers, protocole écrit, contrôles automatiques, et ce que vous faites le jour où l'extraction arrive avec une colonne supplémentaire.",
   ],
   "corrige": """
<p><strong>Le principe directeur : ce qui est mensuel doit être une procédure, pas un souvenir.</strong> Un nettoyage qui vit dans la tête d'une personne est une dépendance, et elle se révèle toujours au plus mauvais moment. L'objectif n'est pas de gagner du temps — c'est un effet secondaire — mais de rendre le résultat indépendant de qui l'exécute.</p>
<p><strong>1. L'organisation des fichiers.</strong> Trois dossiers, pas plus. <em>01_sources</em> contient les extractions reçues, jamais modifiées, nommées <code>ventes_AAAA-MM.xlsx</code>. <em>02_traitement</em> contient le classeur de travail, unique et réutilisé chaque mois. <em>03_livrables</em> contient les rapports diffusés, datés. La règle absolue : rien ne sort de 01_sources, rien n'entre dans 03_livrables sans passer par 02_traitement.</p>
<p>Le nommage par date au format AAAA-MM n'est pas un détail : il fait que le tri alphabétique du dossier est aussi le tri chronologique, ce qui reste vrai en 2031. <code>ventes_mars.xlsx</code> et <code>ventes_v2_final.xlsx</code> vous coûteront une demi-heure de recherche dans deux ans.</p>
<p><strong>2. Le protocole écrit.</strong> Un document d'une page, pas dix, dans le dossier 02_traitement. Il contient : la liste ordonnée des opérations de nettoyage avec, pour chacune, le geste exact et le résultat attendu ; les arbitrages déjà tranchés et par qui — « les commandes sans région sont classées Export, décision validée par M. B. le 14/03 » ; les quatre chiffres de contrôle attendus et leur ordre de grandeur habituel ; et le nom de la personne à appeler si quelque chose ne correspond pas.</p>
<p>Ce dernier point est celui qu'on oublie et c'est le plus utile. Une procédure dit quoi faire quand tout va bien ; ce qui bloque un remplaçant, c'est de ne pas savoir qui appeler quand ça ne va pas.</p>
<p><strong>3. L'automatisation du nettoyage.</strong> Autant que possible en Power Query (module 3), pour une raison qui dépasse le gain de temps : une requête Power Query <em>est</em> la documentation du nettoyage, sous forme exécutable. Chaque étape y est nommée et lisible dans l'ordre. Un collègue peut ouvrir la requête et voir exactement ce qui est fait, sans avoir à vous croire ni à lire un document qui aura divergé du réel au bout de trois mois.</p>
<p>Le journal de transformation reste utile, mais il change de nature : il ne décrit plus les opérations, il consigne les <em>anomalies du mois</em> et les arbitrages ponctuels.</p>
<p><strong>4. Les contrôles automatiques.</strong> Un onglet « contrôles » avec cinq formules qui s'évaluent seules et affichent OK ou une alerte. Nombre de lignes dans une fourchette attendue. Somme des montants dans une fourchette attendue — un écart de plus de 30 % avec le mois précédent est presque toujours un incident d'extraction, pas une variation d'activité. Nombre de modalités par colonne catégorielle, égal à la valeur de référence. Plage de dates entièrement contenue dans le mois attendu. Nombre de cellules vides par colonne, comparé au mois précédent.</p>
<p>Ces contrôles ne remplacent pas le jugement : ils garantissent qu'on ne livre pas sans avoir regardé. Leur valeur réelle est de rendre l'anomalie <em>impossible à ne pas voir</em>, y compris par quelqu'un qui découvre le dossier.</p>
<p><strong>5. Le jour où l'extraction change.</strong> C'est le vrai test du dispositif, et il arrivera. Trois cas, trois conduites.</p>
<p><em>Une colonne supplémentaire, inutilisée par le rapport.</em> Power Query la fera remonter et pourra la conserver sans dommage, mais un tableau croisé dynamique construit sur une plage figée l'ignorera silencieusement. Ne l'intégrez pas par réflexe : notez son existence au journal, et attendez qu'un besoin la réclame. Une colonne intégrée « au cas où » est une colonne que personne ne maintiendra.</p>
<p><em>Une colonne renommée ou déplacée.</em> C'est le cas dangereux. Power Query référence les colonnes par leur nom : un renommage casse la requête, ce qui est une bonne nouvelle — l'erreur est bruyante. En revanche, un traitement qui référence les colonnes par leur position ne cassera pas, il produira des résultats faux. C'est l'argument décisif en faveur des références nommées, ici comme au module 2.</p>
<p><em>Une colonne supprimée.</em> Arrêtez et appelez l'émetteur avant toute chose. Une colonne qui disparaît signale presque toujours un changement dans le système source, donc une possible rupture de définition sur les colonnes restantes. Le risque n'est pas la colonne manquante : c'est que les autres ne veuillent plus tout à fait dire la même chose. Comparer les chiffres de contrôle du mois avec ceux du mois précédent est alors le seul moyen de le détecter.</p>
<p><strong>Le test final du dispositif.</strong> Faites exécuter le processus complet par un collègue, sans vous, en vous interdisant d'intervenir. Chaque question qu'il pose est un trou dans votre protocole : notez-la et complétez. Deux passages suffisent généralement. Tant que ce test n'a pas été fait, vous n'avez pas un protocole — vous avez un document qui vous décrit vous-même.</p>
"""},
 ],

 "ressources": [
   "<strong>Support Microsoft — « Vue d'ensemble des tableaux Excel »</strong> : la référence officielle sur les tableaux structurés et leurs références nommées, à garder sous la main pendant les premières semaines.",
   "<strong>« Tidy Data », Hadley Wickham</strong> — l'article qui a formalisé la règle une ligne / une observation. Écrit pour les statisticiens, mais les trois premières pages suffisent et changent durablement la façon de regarder un fichier.",
   "<strong>Le module 2 de cette formation</strong> — les fonctions de recherche et de calcul conditionnel, qui supposent toutes un fichier structuré comme ici. N'y allez pas avant d'avoir nettoyé un fichier réel de bout en bout.",
   "<strong>Le module 3 de cette formation</strong> — Power Query, qui automatise la quasi-totalité des sept opérations vues ici et rend le nettoyage rejouable en un clic.",
 ],
}

QUIZ["excel-analyse-donnees/module-1"] = {
 "module_id": "formation-excel-analyse-donnees-module-1",
 "version": "2.0", "last_verified": "2026-09-04",
 "questions": [
  {"id":"q1","question":"Une colonne de montants apparaît alignée à gauche dans un fichier reçu. Qu'est-ce que cela indique ?",
   "choices":[{"key":"a","text":"Que les valeurs sont stockées en texte : toute somme les comptera pour zéro"},
              {"key":"b","text":"Une simple préférence de mise en forme, sans conséquence"},
              {"key":"c","text":"Que la colonne contient des valeurs négatives"}],
   "correct_answer":"a","feedback":"Sans formatage explicite, Excel aligne nombres et dates à droite, le texte à gauche. Le danger est le typage mixte : la somme renvoie alors un total partiel, plausible et faux."},
  {"id":"q2","question":"Pourquoi les cellules fusionnées sont-elles le défaut le plus destructeur ?",
   "choices":[{"key":"a","text":"Parce qu'elles alourdissent considérablement le fichier"},
              {"key":"b","text":"Parce qu'elles contiennent une valeur et des vides, invisibles à l'écran, que filtres et tableaux croisés perdront"},
              {"key":"c","text":"Parce qu'elles empêchent l'impression du document"}],
   "correct_answer":"b","feedback":"Le fichier a l'air complet à l'écran alors que les lignes concernées sont vides pour Excel. C'est un défaut silencieux, donc coûteux."},
  {"id":"q3","question":"Quel est le premier geste après avoir terminé le nettoyage d'une plage de données ?",
   "choices":[{"key":"a","text":"Appliquer un jeu de couleurs pour distinguer les colonnes"},
              {"key":"b","text":"Ajouter une ligne de total en bas de chaque colonne numérique"},
              {"key":"c","text":"La convertir en tableau structuré par Ctrl + L et la nommer"}],
   "correct_answer":"c","feedback":"Le tableau structuré étend ses plages seul, nomme ses colonnes et propage ses formules. Deux secondes de coût, et tout ce qui suit en dépend."},
  {"id":"q4","question":"Vous découvrez 160 cellules vides dans la colonne Région. Que faites-vous ?",
   "choices":[{"key":"a","text":"Vous supprimez ces lignes pour ne pas fausser l'analyse"},
              {"key":"b","text":"Vous les remplissez avec la valeur la plus fréquente de la colonne"},
              {"key":"c","text":"Vous cherchez d'abord ce que ce vide signifie, puis vous tranchez et documentez l'arbitrage"}],
   "correct_answer":"c","feedback":"Un vide a presque toujours un sens métier. Ici, toutes ces commandes étaient des exports : le vide devenait une modalité légitime, pas une donnée à supprimer."},
  {"id":"q5","question":"Quelle est la proportion de temps normale entre préparation et analyse sur un fichier d'entreprise ?",
   "choices":[{"key":"a","text":"Environ 80 % de préparation pour 20 % d'analyse"},
              {"key":"b","text":"Environ 20 % de préparation pour 80 % d'analyse"},
              {"key":"c","text":"Les deux moitiés sont généralement équivalentes"}],
   "correct_answer":"a","feedback":"L'analyse proprement dite est la partie courte. Celui qui répond en vingt minutes sur un fichier non préparé n'a pas été rapide : il a sauté ce qui rend la réponse vraie."},
  {"id":"q6","question":"À quoi sert principalement le journal de transformation ?",
   "choices":[{"key":"a","text":"À justifier le temps passé auprès de sa hiérarchie"},
              {"key":"b","text":"À rendre l'analyse reproductible et à retracer chaque arbitrage effectué"},
              {"key":"c","text":"À conserver une sauvegarde des données avant nettoyage"}],
   "correct_answer":"b","feedback":"Il répond aux trois questions qui reviennent toujours : pourquoi ce chiffre a changé, peut-on refaire l'analyse, et qui a décidé de cet arbitrage."},
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
