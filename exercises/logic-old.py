import random


def generate_exercises(niveau, count=5):
    """Génère des exercices de logique"""

    # Pool d'exercices par catégorie
    all_templates = {
        'suites': generate_suites(),
        'enigmes': generate_enigmes(),
        'mensonges_verites': generate_mensonges_verites(),
        'grilles': generate_grilles_logiques(),
        'deductions': generate_deductions(),
        'paradoxes': generate_paradoxes_simples(),
        'problemes': generate_problemes_logiques()
    }

    # Sélectionner des exercices variés
    exercises = []
    categories = list(all_templates.keys())

    choices = []
    for _ in range(count):
        category = random.choice(categories)
        while category in choices:
            category = random.choice(categories)
        choices.append(category)
        exercise = random.choice(all_templates[category])
        exercises.append({'content': exercise['question'] + """

        \\cadreligne"""})

    return exercises


def generate_suites():
    """Suites logiques à compléter"""
    templates = [
        {
            'question': """Quelle est la logique de cette suite et quel est le nombre manquant ?

\\begin{center}
2, 4, 8, 16, ?, 64
\\end{center}

Expliquer le raisonnement."""
        },
        {
            'question': """Compléter la suite logique :

\\begin{center}
1, 1, 2, 3, 5, 8, ?, 21
\\end{center}

Quelle est la règle ?"""
        },
        {
            'question': """Trouver l'intrus dans cette liste et expliquer pourquoi :

\\begin{center}
3, 5, 7, 9, 11, 13
\\end{center}"""
        },
        {
            'question': f"""Quelle lettre vient ensuite ?

\\begin{{center}}
A, C, F, J, O, ?
\\end{{center}}

Indice : compter les intervalles."""
        },
        {
            'question': """Compléter la grille :

\\begin{center}
\\begin{tabular}{|c|c|c|}
\\hline
2 & 4 & 8 \\\\
\\hline
3 & 9 & 27 \\\\
\\hline
4 & ? & 64 \\\\
\\hline
\\end{tabular}
\\end{center}"""
        }
    ]
    return templates


def generate_enigmes():
    """Énigmes classiques adaptées"""
    templates = [
        {
            'question': """\\textbf{Le berger et ses moutons}

Un berger dit : « Si j'avais 4 moutons de plus, j'en aurais deux fois plus que mon voisin. »
Son voisin répond : « Mais si j'en avais 4 de plus, on en aurait le même nombre ! »

Combien chacun a-t-il de moutons ? Expliquer le raisonnement."""
        },
        {
            'question': """\\textbf{Les âges}

Marie a 3 fois l'âge qu'avait Sophie quand Marie avait l'âge de Sophie.
Quand Sophie aura l'âge de Marie, la somme de leurs âges sera 56 ans.

Quel âge ont-elles actuellement ?"""
        },
        {
            'question': """\\textbf{Le passage du pont}

Quatre personnes doivent traverser un pont de nuit. Elles n'ont qu'une lampe et le pont ne peut supporter que deux personnes à la fois.
- Alice traverse en 1 minute
- Bob traverse en 2 minutes
- Charlie traverse en 5 minutes
- David traverse en 10 minutes

Quand deux personnes traversent ensemble, elles vont à la vitesse du plus lent.

Quel est le temps minimum pour que tous traversent ? Détailler la stratégie."""
        },
        {
            'question': """\\textbf{Les pièces}

Vous avez 12 pièces identiques en apparence, mais l'une d'elles est plus légère que les autres.
Vous disposez d'une balance à plateaux (qui indique quel côté est le plus lourd).

Comment trouver la pièce différente en seulement 3 pesées ? Expliquer la méthode."""
        },
        {
            'question': """\\textbf{Les chapeaux}

Trois personnes (A, B, C) sont alignées : C voit A et B, B voit A, A ne voit personne.
On place un chapeau noir ou blanc sur la tête de chacun (ils ne voient pas leur propre chapeau).
On leur dit qu'il y a au moins un chapeau noir.

On demande à C : « Connais-tu la couleur de ton chapeau ? » C répond « Non ».
On demande à B : « Connais-tu la couleur de ton chapeau ? » B répond « Non ».
On demande à A : « Connais-tu la couleur de ton chapeau ? » A répond « Oui ! »

Quelle est la couleur du chapeau de A et comment le sait-il ?"""
        }
    ]
    return templates


def generate_mensonges_verites():
    """Problèmes de logique avec menteurs et vérité"""
    templates = [
        {
            'question': """\\textbf{Les trois frères}

Trois frères ont des comportements différents :
\\begin{itemize}
\\item Antoine dit toujours la vérité
\\item Benoît ment toujours
\\item Charles alterne : vérité, mensonge, vérité, mensonge...
\\end{itemize}

Ils font chacun deux déclarations :

\\textbf{Premier frère :}
\\begin{enumerate}
\\item « Je suis Antoine »
\\item « Le deuxième est Benoît »
\\end{enumerate}

\\textbf{Deuxième frère :}
\\begin{enumerate}
\\item « Je ne suis pas Antoine »
\\item « Le troisième est Charles »
\\end{enumerate}

\\textbf{Troisième frère :}
\\begin{enumerate}
\\item « Je ne suis pas Charles »
\\item « Le premier est Benoît »
\\end{enumerate}

Qui est qui ? Justifier le raisonnement."""
        },
        {
            'question': """\\textbf{L'île des chevaliers et menteurs}

Sur une île, il y a deux types d'habitants :
\\begin{itemize}
\\item Les chevaliers disent toujours la vérité
\\item Les menteurs mentent toujours
\\end{itemize}

Vous rencontrez deux habitants, A et B.

A dit : « Au moins l'un de nous deux est un menteur. »

Que sont A et B ? Expliquer."""
        },
        {
            'question': """\\textbf{Les déclarations contradictoires}

Quatre élèves sont interrogés sur qui a cassé la fenêtre :

\\begin{itemize}
\\item Alice : « C'est Bob »
\\item Bob : « C'est Carla »
\\item Carla : « Bob ment »
\\item David : « Ce n'est pas moi »
\\end{itemize}

On sait qu'exactement trois d'entre eux disent la vérité.

Qui a cassé la fenêtre ? Justifier."""
        }
    ]
    return templates


def generate_grilles_logiques():
    """Sudoku simplifiés et grilles logiques"""
    templates = [
        {
            'question': """\\textbf{Mini-Sudoku 4×4}

Remplir la grille avec les chiffres 1, 2, 3, 4.
Chaque ligne, colonne et carré 2×2 doit contenir tous les chiffres de 1 à 4.

\\begin{center}
\\begin{tabular}{|c|c||c|c|}
\\hline
1 & ~ & ~ & 4 \\\\
\\hline
~ & 3 & 1 & ~ \\\\
\\hline
\\hline
~ & 1 & 4 & ~ \\\\
\\hline
4 & ~ & ~ & 1 \\\\
\\hline
\\end{tabular}
\\end{center}"""
        },
        {
            'question': """\\textbf{Grille logique : Les voisins}

Quatre personnes habitent des maisons côte à côte (positions 1, 2, 3, 4).
Chacune a un animal différent : chat, chien, poisson, oiseau.

Indices :
\\begin{itemize}
\\item Le propriétaire du chat habite à côté de celui du chien
\\item Le poisson est en position 2
\\item L'oiseau est à une extrémité (position 1 ou 4)
\\item Le chien n'est pas en position 1
\\end{itemize}

Qui habite où avec quel animal ?"""
        },
        {
            'question': """\\textbf{Le carré magique}

Placer les nombres de 1 à 9 dans cette grille 3×3 de sorte que :
\\begin{itemize}
\\item Chaque ligne somme à 15
\\item Chaque colonne somme à 15
\\item Chaque diagonale somme à 15
\\end{itemize}

\\begin{center}
\\begin{tabular}{|c|c|c|}
\\hline
~ & ~ & ~ \\\\
\\hline
~ & 5 & ~ \\\\
\\hline
~ & ~ & ~ \\\\
\\hline
\\end{tabular}
\\end{center}

Indice : Le 5 est déjà placé au centre."""
        }
    ]
    return templates


def generate_deductions():
    """Exercices de déduction logique"""
    templates = [
        {
            'question': """\\textbf{Déduction}

Dans une classe de 30 élèves :
\\begin{itemize}
\\item 18 font du sport
\\item 15 jouent d'un instrument
\\item 5 ne font ni sport ni musique
\\end{itemize}

Combien d'élèves font à la fois du sport ET de la musique ? Expliquer le raisonnement."""
        },
        {
            'question': """\\textbf{Les cartes}

On vous présente 4 cartes posées sur une table :

\\begin{center}
A ~ ~ ~ ~ K ~ ~ ~ ~ 4 ~ ~ ~ ~ 7
\\end{center}

Règle à vérifier : « Si une carte a une voyelle sur une face, alors elle a un nombre pair sur l'autre face. »

Quelles cartes MINIMUM devez-vous retourner pour vérifier cette règle ? Justifier."""
        },
        {
            'question': """\\textbf{Le calendrier mystère}

« Mon anniversaire est ce mois-ci. »
« Si aujourd'hui on était demain, il ne resterait que 2 jours avant mon anniversaire. »
« Si aujourd'hui on était hier, il resterait 4 jours. »

Dans combien de jours est l'anniversaire ?"""
        },
        {
            'question': """\\textbf{Les suspects}

Un vol a eu lieu. Trois suspects sont interrogés :

\\begin{itemize}
\\item Suspect A : « C'est B ou C »
\\item Suspect B : « Ce n'est ni A ni moi »
\\item Suspect C : « A ment »
\\end{itemize}

Sachant qu'exactement deux suspects disent la vérité et qu'il n'y a qu'un seul coupable, qui est le voleur ?"""
        }
    ]
    return templates


def generate_paradoxes_simples():
    """Paradoxes et situations contre-intuitives"""
    templates = [
        {
            'question': """\\textbf{Le problème de Monty Hall}

Vous participez à un jeu télévisé. Trois portes sont devant vous :
\\begin{itemize}
\\item Derrière une porte : une voiture
\\item Derrière les deux autres : des chèvres
\\end{itemize}

Vous choisissez la porte 1.

Le présentateur (qui sait ce qu'il y a derrière chaque porte) ouvre alors la porte 3, révélant une chèvre.

Il vous propose : « Voulez-vous changer et choisir la porte 2 ? »

Devriez-vous changer de porte ? Quelle est votre probabilité de gagner si vous changez ? Si vous ne changez pas ? Justifier."""
        },
        {
            'question': """\\textbf{Le barbier}

Dans un village, le barbier rase tous les hommes qui ne se rasent pas eux-mêmes, et uniquement ceux-là.

Question : Le barbier se rase-t-il lui-même ?

Analyser ce qui se passe dans les deux cas (s'il se rase / s'il ne se rase pas)."""
        }
    ]
    return templates


def generate_problemes_logiques():
    """Problèmes de logique variés"""
    templates = [
        {
            'question': """\\textbf{La traversée de la rivière}

Un fermier doit traverser une rivière avec un loup, une chèvre et un chou.
Son bateau ne peut transporter que lui et UN seul des trois à la fois.

Problèmes :
\\begin{itemize}
\\item Si le loup reste seul avec la chèvre, il la mange
\\item Si la chèvre reste seule avec le chou, elle le mange
\\end{itemize}

Comment faire traverser tout le monde sans incident ? Décrire les étapes."""
        },
        {
            'question': """\\textbf{Les interrupteurs}

Vous êtes au rez-de-chaussée d'une maison. Au premier étage, il y a une pièce fermée avec une ampoule.
Au rez-de-chaussée, trois interrupteurs : UN SEUL contrôle l'ampoule du premier étage.

Vous pouvez manipuler les interrupteurs autant que vous voulez, mais vous ne pouvez monter qu'UNE SEULE fois au premier étage.

Comment déterminer avec certitude quel interrupteur contrôle l'ampoule ?

Indice : penser aux propriétés physiques d'une ampoule allumée..."""
        },
        {
            'question': """\\textbf{Le problème des poignées de main}

Lors d'une fête avec 10 personnes, chacun serre la main de certaines autres personnes (0, 1, 2... ou jusqu'à 9 autres personnes).

Est-il possible que chacune des 10 personnes ait serré un nombre différent de mains ?
(c'est-à-dire : une personne a serré 0 main, une autre 1 main, une autre 2 mains... jusqu'à une qui a serré 9 mains)

Répondre par oui ou non et justifier."""
        },
        {
            'question': """\\textbf{Les pirates et les pièces d'or}

5 pirates (A, B, C, D, E) doivent se partager 100 pièces d'or.
Ils votent dans l'ordre (A propose, puis vote majoritaire).

Règles :
\\begin{itemize}
\\item Le pirate A fait une proposition de partage
\\item Tous votent (y compris A)
\\item Si au moins 50\\% votent OUI, le partage est accepté
\\item Sinon, A est jeté par-dessus bord et B propose à son tour
\\end{itemize}

Tous les pirates sont intelligents, rationnels, et préfèrent :
1. Rester en vie
2. Gagner le plus d'or possible
3. Si égalité, éliminer les autres

Quelle proposition A doit-il faire pour maximiser son gain ?"""
        },
        {
            'question': """\\textbf{Les faux billets}

Vous avez 10 sacs de pièces. Chaque sac contient un grand nombre de pièces.
9 sacs contiennent des vraies pièces de 10g chacune.
1 sac contient des fausses pièces de 9g chacune.

Vous avez une balance électronique qui affiche le poids exact.

Comment identifier le sac de fausses pièces en UNE SEULE pesée ?

Expliquer la méthode."""
        },
        {
            'question': """\\textbf{Le café et le lait}

Deux tasses identiques : une de café, une de lait (même volume).

Expérience :
\\begin{itemize}
\\item On prend une cuillère de café et on la verse dans le lait
\\item On mélange bien
\\item On reprend une cuillère du mélange et on la remet dans le café
\\end{itemize}

Question : Y a-t-il plus de café dans la tasse de lait, ou plus de lait dans la tasse de café ?

Justifier avec un raisonnement logique (pas de calculs compliqués nécessaires)."""
        }
    ]
    return templates