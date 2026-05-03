import random

def generate_exercises(niveau, count=5):
    """Génère des exercices d'écriture de code"""
    generators = {
        1: generate_niveau1,
        2: generate_niveau2,
        3: generate_niveau3,
        4: generate_niveau4,
        5: generate_niveau5,
        6: generate_niveau6
    }
    
    if niveau not in generators:
        raise ValueError(f"Niveau {niveau} non supporté")
    
    exercises = []
    for _ in range(count):
        exercises.append(generators[niveau]())
    
    return exercises


def generate_niveau1():
    """Fonction simple avec un if"""
    import string

    # Génération de valeurs aléatoires variées
    a = random.randint(5, 20)
    b = random.randint(5, 20)
    c = random.randint(2, 8)
    d = random.randint(10, 50)

    # Opérateurs variés
    opérateurs = ['+', '-', '*', '//', '%']
    op1 = random.choice(opérateurs)
    opérateurs_copy = opérateurs.copy()
    if op1 in opérateurs_copy:
        opérateurs_copy.remove(op1)
    op2 = random.choice(opérateurs_copy) if opérateurs_copy else random.choice(opérateurs)

    # Comparateurs
    cmp = random.choice(['>', '<', '==', '!=', '>=', '<='])

    # Chaînes aléatoires
    s1 = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(4, 7)))
    s2 = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(3, 6)))
    mots_exemples = ['python', 'algorithme', 'variable', 'fonction', 'liste']
    mot1 = random.choice(mots_exemples)
    mot2 = random.choice([m for m in mots_exemples if m != mot1])

    # Valeurs pour tests
    val_test1 = random.randint(1, 20)
    val_test2 = random.randint(1, 20)

    templates = [
        # Template 1: Pair/Impair
        {
            'question': f"""Écrire une fonction \\texttt{{est\\_pair(n)}} qui renvoie \\texttt{{True}} si \\texttt{{n}} est pair, \\texttt{{False}} sinon.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{est\\_pair({val_test1})}} doit renvoyer \\texttt{{{str(val_test1 % 2 == 0)}}}
\\item \\texttt{{est\\_pair({val_test2})}} doit renvoyer \\texttt{{{str(val_test2 % 2 == 0)}}}
\\end{{itemize}}"""
        },

        # Template 2: Positif/Négatif
        {
            'question': f"""Écrire une fonction \\texttt{{est\\_positif(x)}} qui renvoie \\texttt{{True}} si \\texttt{{x}} est strictement positif, \\texttt{{False}} sinon.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{est\\_positif({a})}} doit renvoyer \\texttt{{True}}
\\item \\texttt{{est\\_positif({-b})}} doit renvoyer \\texttt{{False}}
\\item \\texttt{{est\\_positif(0)}} doit renvoyer \\texttt{{False}}
\\end{{itemize}}"""
        },

        # Template 3: Voyelle
        {
            'question': f"""Écrire une fonction \\texttt{{commence\\_par\\_voyelle(mot)}} qui renvoie \\texttt{{True}} si le mot commence par une voyelle (a, e, i, o, u, y), \\texttt{{False}} sinon.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{commence\\_par\\_voyelle('arbre')}} doit renvoyer \\texttt{{True}}
\\item \\texttt{{commence\\_par\\_voyelle('maison')}} doit renvoyer \\texttt{{False}}
\\item \\texttt{{commence\\_par\\_voyelle('usine')}} doit renvoyer \\texttt{{True}}
\\end{{itemize}}"""
        },

        # Template 4: Liste vide
        {
            'question': f"""Écrire une fonction \\texttt{{est\\_vide(liste)}} qui renvoie \\texttt{{True}} si la liste est vide, \\texttt{{False}} sinon.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{est\\_vide([])}} doit renvoyer \\texttt{{True}}
\\item \\texttt{{est\\_vide([1, 2, 3])}} doit renvoyer \\texttt{{False}}
\\item \\texttt{{est\\_vide([0])}} doit renvoyer \\texttt{{False}}
\\end{{itemize}}"""
        },

        # Template 5: Multiple
        {
            'question': f"""Écrire une fonction \\texttt{{est\\_multiple(n, diviseur)}} qui renvoie \\texttt{{True}} si \\texttt{{n}} est un multiple de \\texttt{{diviseur}}, \\texttt{{False}} sinon.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{est\\_multiple({c * 3}, {c})}} doit renvoyer \\texttt{{True}}
\\item \\texttt{{est\\_multiple({a}, {c})}} doit renvoyer \\texttt{{{str(a % c == 0)}}}
\\end{{itemize}}"""
        },

        # Template 6: Comparaison simple
        {
            'question': f"""Écrire une fonction \\texttt{{est\\_superieur(a, b)}} qui renvoie \\texttt{{True}} si \\texttt{{a}} est strictement supérieur à \\texttt{{b}}, \\texttt{{False}} sinon.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{est\\_superieur({a}, {b})}} doit renvoyer \\texttt{{{str(a > b)}}}
\\item \\texttt{{est\\_superieur({b}, {a})}} doit renvoyer \\texttt{{{str(b > a)}}}
\\end{{itemize}}"""
        },

        # Template 7: Longueur minimale
        {
            'question': f"""Écrire une fonction \\texttt{{longueur\\_min(mot, minimum)}} qui renvoie \\texttt{{True}} si la longueur du mot est au moins égale à \\texttt{{minimum}}, \\texttt{{False}} sinon.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{longueur\\_min('{mot1}', {len(mot1) - 1})}} doit renvoyer \\texttt{{True}}
\\item \\texttt{{longueur\\_min('{mot2}', {len(mot2) + 2})}} doit renvoyer \\texttt{{False}}
\\end{{itemize}}"""
        },

        # Template 8: Maximum de deux nombres
        {
            'question': f"""Écrire une fonction \\texttt{{maximum(a, b)}} qui renvoie le plus grand des deux nombres.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{maximum({a}, {b})}} doit renvoyer \\texttt{{{max(a, b)}}}
\\item \\texttt{{maximum({b}, {a})}} doit renvoyer \\texttt{{{max(b, a)}}}
\\item \\texttt{{maximum(5, 5)}} doit renvoyer \\texttt{{5}}
\\end{{itemize}}"""
        },

        # Template 9: Minimum de deux nombres
        {
            'question': f"""Écrire une fonction \\texttt{{minimum(a, b)}} qui renvoie le plus petit des deux nombres.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{minimum({a}, {b})}} doit renvoyer \\texttt{{{min(a, b)}}}
\\item \\texttt{{minimum({b}, {a})}} doit renvoyer \\texttt{{{min(b, a)}}}
\\end{{itemize}}"""
        },

        # Template 10: Valeur absolue
        {
            'question': f"""Écrire une fonction \\texttt{{valeur\\_absolue(x)}} qui renvoie la valeur absolue de \\texttt{{x}} (sans utiliser la fonction \\texttt{{abs}}).

Exemples :
\\begin{{itemize}}
\\item \\texttt{{valeur\\_absolue({a})}} doit renvoyer \\texttt{{{a}}}
\\item \\texttt{{valeur\\_absolue({-b})}} doit renvoyer \\texttt{{{b}}}
\\item \\texttt{{valeur\\_absolue(0)}} doit renvoyer \\texttt{{0}}
\\end{{itemize}}"""
        },

        # Template 11: Dans un intervalle
        {
            'question': f"""Écrire une fonction \\texttt{{dans\\_intervalle(x, min, max)}} qui renvoie \\texttt{{True}} si \\texttt{{x}} est compris entre \\texttt{{min}} et \\texttt{{max}} (inclus), \\texttt{{False}} sinon.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{dans\\_intervalle({a}, {a - 2}, {a + 2})}} doit renvoyer \\texttt{{True}}
\\item \\texttt{{dans\\_intervalle({b}, {c}, {c + 3})}} doit renvoyer \\texttt{{{str(c <= b <= c + 3)}}}
\\end{{itemize}}"""
        },

        # Template 12: Divisible par 3 ou 5
        {
            'question': f"""Écrire une fonction \\texttt{{divisible(n)}} qui renvoie \\texttt{{True}} si \\texttt{{n}} est divisible par 3 OU par 5, \\texttt{{False}} sinon.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{divisible(15)}} doit renvoyer \\texttt{{True}}
\\item \\texttt{{divisible(9)}} doit renvoyer \\texttt{{True}}
\\item \\texttt{{divisible(10)}} doit renvoyer \\texttt{{True}}
\\item \\texttt{{divisible(7)}} doit renvoyer \\texttt{{False}}
\\end{{itemize}}"""
        },

        # Template 13: Premier caractère majuscule
        {
            'question': f"""Écrire une fonction \\texttt{{majuscule\\_debut(mot)}} qui renvoie \\texttt{{True}} si le premier caractère du mot est une majuscule, \\texttt{{False}} sinon.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{majuscule\\_debut('Python')}} doit renvoyer \\texttt{{True}}
\\item \\texttt{{majuscule\\_debut('python')}} doit renvoyer \\texttt{{False}}
\\item \\texttt{{majuscule\\_debut('NSI')}} doit renvoyer \\texttt{{True}}
\\end{{itemize}}"""
        },

        # Template 14: Longueur paire
        {
            'question': f"""Écrire une fonction \\texttt{{longueur\\_paire(mot)}} qui renvoie \\texttt{{True}} si la longueur du mot est paire, \\texttt{{False}} sinon.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{longueur\\_paire('code')}} doit renvoyer \\texttt{{True}}
\\item \\texttt{{longueur\\_paire('python')}} doit renvoyer \\texttt{{True}}
\\item \\texttt{{longueur\\_paire('nsi')}} doit renvoyer \\texttt{{False}}
\\end{{itemize}}"""
        },

        # Template 15: Même signe
        {
            'question': f"""Écrire une fonction \\texttt{{meme\\_signe(a, b)}} qui renvoie \\texttt{{True}} si \\texttt{{a}} et \\texttt{{b}} ont le même signe (tous les deux positifs ou tous les deux négatifs), \\texttt{{False}} sinon.

Note : on considère que 0 est positif.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{meme\\_signe({a}, {b})}} doit renvoyer \\texttt{{True}}
\\item \\texttt{{meme\\_signe({a}, {-b})}} doit renvoyer \\texttt{{False}}
\\item \\texttt{{meme\\_signe({-a}, {-b})}} doit renvoyer \\texttt{{True}}
\\end{{itemize}}"""
        },

        # Template 16: Année bissextile (simplifié)
        {
            'question': f"""Écrire une fonction \\texttt{{est\\_bissextile\\_simple(annee)}} qui renvoie \\texttt{{True}} si l'année est bissextile, \\texttt{{False}} sinon.

Règle simplifiée : une année est bissextile si elle est divisible par 4.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{est\\_bissextile\\_simple(2024)}} doit renvoyer \\texttt{{True}}
\\item \\texttt{{est\\_bissextile\\_simple(2023)}} doit renvoyer \\texttt{{False}}
\\item \\texttt{{est\\_bissextile\\_simple(2020)}} doit renvoyer \\texttt{{True}}
\\end{{itemize}}"""
        },

        # Template 17: Contient un caractère
        {
            'question': f"""Écrire une fonction \\texttt{{contient\\_caractere(mot, char)}} qui renvoie \\texttt{{True}} si le mot contient le caractère \\texttt{{char}}, \\texttt{{False}} sinon.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{contient\\_caractere('python', 'y')}} doit renvoyer \\texttt{{True}}
\\item \\texttt{{contient\\_caractere('python', 'a')}} doit renvoyer \\texttt{{False}}
\\item \\texttt{{contient\\_caractere('nsi', 's')}} doit renvoyer \\texttt{{True}}
\\end{{itemize}}"""
        },

        # Template 18: Liste non vide
        {
            'question': f"""Écrire une fonction \\texttt{{a\\_des\\_elements(liste)}} qui renvoie \\texttt{{True}} si la liste contient au moins un élément, \\texttt{{False}} sinon.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{a\\_des\\_elements([1, 2, 3])}} doit renvoyer \\texttt{{True}}
\\item \\texttt{{a\\_des\\_elements([])}} doit renvoyer \\texttt{{False}}
\\item \\texttt{{a\\_des\\_elements([0])}} doit renvoyer \\texttt{{True}}
\\end{{itemize}}"""
        },

        # Template 19: Égalité stricte de longueur
        {
            'question': f"""Écrire une fonction \\texttt{{meme\\_longueur(mot1, mot2)}} qui renvoie \\texttt{{True}} si les deux mots ont la même longueur, \\texttt{{False}} sinon.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{meme\\_longueur('code', 'test')}} doit renvoyer \\texttt{{True}}
\\item \\texttt{{meme\\_longueur('python', 'nsi')}} doit renvoyer \\texttt{{False}}
\\item \\texttt{{meme\\_longueur('ab', 'cd')}} doit renvoyer \\texttt{{True}}
\\end{{itemize}}"""
        },

        # Template 20: Borne inférieure
        {
            'question': f"""Écrire une fonction \\texttt{{au\\_moins(valeur, minimum)}} qui renvoie \\texttt{{True}} si \\texttt{{valeur}} est supérieure ou égale à \\texttt{{minimum}}, \\texttt{{False}} sinon.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{au\\_moins({a}, {b})}} doit renvoyer \\texttt{{{str(a >= b)}}}
\\item \\texttt{{au\\_moins({c}, {c})}} doit renvoyer \\texttt{{True}}
\\item \\texttt{{au\\_moins({c}, {d})}} doit renvoyer \\texttt{{{str(c >= d)}}}
\\end{{itemize}}"""
        },

        # Template 21: Chiffre ou lettre
        {
            'question': f"""Écrire une fonction \\texttt{{est\\_chiffre(caractere)}} qui renvoie \\texttt{{True}} si le caractère est un chiffre ('0' à '9'), \\texttt{{False}} sinon.

Indice : utiliser la méthode \\texttt{{isdigit()}} ou comparer avec '0' et '9'.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{est\\_chiffre('5')}} doit renvoyer \\texttt{{True}}
\\item \\texttt{{est\\_chiffre('a')}} doit renvoyer \\texttt{{False}}
\\item \\texttt{{est\\_chiffre('0')}} doit renvoyer \\texttt{{True}}
\\end{{itemize}}"""
        },

        # Template 22: Température
        {
            'question': f"""Écrire une fonction \\texttt{{temperature\\_negative(temp)}} qui renvoie \\texttt{{True}} si la température est strictement négative, \\texttt{{False}} sinon.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{temperature\\_negative(-5)}} doit renvoyer \\texttt{{True}}
\\item \\texttt{{temperature\\_negative(0)}} doit renvoyer \\texttt{{False}}
\\item \\texttt{{temperature\\_negative(15)}} doit renvoyer \\texttt{{False}}
\\end{{itemize}}"""
        },

        # Template 23: Premier élément
        {
            'question': f"""Écrire une fonction \\texttt{{premier\\_est\\_pair(liste)}} qui renvoie \\texttt{{True}} si le premier élément de la liste est pair, \\texttt{{False}} sinon.

On suppose que la liste n'est jamais vide.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{premier\\_est\\_pair([2, 3, 5])}} doit renvoyer \\texttt{{True}}
\\item \\texttt{{premier\\_est\\_pair([1, 4, 6])}} doit renvoyer \\texttt{{False}}
\\item \\texttt{{premier\\_est\\_pair([8])}} doit renvoyer \\texttt{{True}}
\\end{{itemize}}"""
        },

        # Template 24: Palindrome d'un caractère
        {
            'question': f"""Écrire une fonction \\texttt{{est\\_palindrome\\_1char(mot)}} qui renvoie \\texttt{{True}} si le mot est composé d'un seul caractère (donc palindrome), \\texttt{{False}} sinon.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{est\\_palindrome\\_1char('a')}} doit renvoyer \\texttt{{True}}
\\item \\texttt{{est\\_palindrome\\_1char('ab')}} doit renvoyer \\texttt{{False}}
\\item \\texttt{{est\\_palindrome\\_1char('5')}} doit renvoyer \\texttt{{True}}
\\end{{itemize}}"""
        },

        # Template 25: Entre deux bornes
        {
            'question': f"""Écrire une fonction \\texttt{{hors\\_limites(x, limite)}} qui renvoie \\texttt{{True}} si \\texttt{{x}} est en dehors de l'intervalle [-limite, +limite], \\texttt{{False}} sinon.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{hors\\_limites({a}, {b})}} doit renvoyer \\texttt{{{str(abs(a) > b)}}}
\\item \\texttt{{hors\\_limites(0, {c})}} doit renvoyer \\texttt{{False}}
\\item \\texttt{{hors\\_limites({d}, {c})}} doit renvoyer \\texttt{{{str(abs(d) > c)}}}
\\end{{itemize}}"""
        }
    ]

    template = random.choice(templates)
    content = template['question']+"""\\cadreligne"""

    return {'content': content}
def generate_niveau2():
    """Boucle for sans if, sur liste/tuple/dict, avec une variable à gérer"""

    a = random.randint(3, 12)
    b = random.randint(2, 8)

    # Listes aléatoires
    liste_int = [random.randint(1, 20) for _ in range(random.randint(4, 6))]
    liste_int2 = [random.randint(-10, 10) for _ in range(random.randint(4, 6))]
    liste_float = [round(random.uniform(1.0, 10.0), 1) for _ in range(random.randint(4, 5))]

    # Tuples aléatoires
    tuple_int = tuple(random.randint(1, 15) for _ in range(random.randint(4, 6)))
    tuple_notes = tuple(random.randint(5, 20) for _ in range(random.randint(4, 6)))

    # Dictionnaires aléatoires
    prenoms = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Hugo']
    random.shuffle(prenoms)
    dict_ages = {prenoms[i]: random.randint(12, 18) for i in range(random.randint(3, 5))}
    dict_notes = {prenoms[i]: random.randint(5, 20) for i in range(random.randint(3, 5))}
    dict_prix = {random.choice(['pomme', 'banane', 'orange', 'kiwi', 'mangue', 'poire']): round(random.uniform(0.5, 5.0), 1) for _ in range(random.randint(3, 5))}
    dict_stock = {random.choice(['stylo', 'cahier', 'gomme', 'regle', 'crayon', 'colle']): random.randint(1, 50) for _ in range(random.randint(3, 5))}

    # Chaînes
    mots_exemples = ['python', 'algorithme', 'variable', 'fonction', 'boucle', 'programme']
    mot1 = random.choice(mots_exemples)

    templates = [
        # --- Sur des listes ---
        {
            'question': f"""Écrire une fonction \\texttt{{somme\\_liste(liste)}} qui renvoie la somme de tous les éléments d'une liste d'entiers, en parcourant la liste avec une boucle \\texttt{{for}}.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{somme\\_liste({liste_int})}} doit renvoyer \\texttt{{{sum(liste_int)}}}
\\item \\texttt{{somme\\_liste([])}} doit renvoyer \\texttt{{0}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{produit\\_liste(liste)}} qui renvoie le produit de tous les éléments d'une liste d'entiers, en parcourant la liste avec une boucle \\texttt{{for}}.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{produit\\_liste([{liste_int[0]}, {liste_int[1]}, {liste_int[2]}])}} doit renvoyer \\texttt{{{liste_int[0] * liste_int[1] * liste_int[2]}}}
\\item \\texttt{{produit\\_liste([1, 2, 3])}} doit renvoyer \\texttt{{6}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{trouver\\_minimum(liste)}} qui renvoie le plus petit élément d'une liste d'entiers, en parcourant la liste avec une boucle \\texttt{{for}} (sans utiliser \\texttt{{min}}).

On suppose que la liste n'est jamais vide.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{trouver\\_minimum({liste_int})}} doit renvoyer \\texttt{{{min(liste_int)}}}
\\item \\texttt{{trouver\\_minimum([5, 3, 8])}} doit renvoyer \\texttt{{3}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{trouver\\_maximum(liste)}} qui renvoie le plus grand élément d'une liste d'entiers, en parcourant la liste avec une boucle \\texttt{{for}} (sans utiliser \\texttt{{max}}).

On suppose que la liste n'est jamais vide.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{trouver\\_maximum({liste_int})}} doit renvoyer \\texttt{{{max(liste_int)}}}
\\item \\texttt{{trouver\\_maximum([2, 9, 4])}} doit renvoyer \\texttt{{9}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{doubler\\_elements(liste)}} qui renvoie une nouvelle liste où chaque élément est le double de l'élément correspondant dans la liste d'entrée.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{doubler\\_elements({liste_int})}} doit renvoyer \\texttt{{{[x * 2 for x in liste_int]}}}
\\item \\texttt{{doubler\\_elements([1, 3, 5])}} doit renvoyer \\texttt{{[2, 6, 10]}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{ajouter\\_valeur(liste, v)}} qui renvoie une nouvelle liste où \\texttt{{v}} a été ajouté à chaque élément.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{ajouter\\_valeur({liste_int}, {b})}} doit renvoyer \\texttt{{{[x + b for x in liste_int]}}}
\\item \\texttt{{ajouter\\_valeur([1, 2, 3], 10)}} doit renvoyer \\texttt{{[11, 12, 13]}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{compter\\_elements(liste)}} qui renvoie le nombre d'éléments d'une liste, en parcourant la liste avec une boucle \\texttt{{for}} (sans utiliser \\texttt{{len}}).

Exemples :
\\begin{{itemize}}
\\item \\texttt{{compter\\_elements({liste_int})}} doit renvoyer \\texttt{{{len(liste_int)}}}
\\item \\texttt{{compter\\_elements([])}} doit renvoyer \\texttt{{0}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{moyenne\\_liste(liste)}} qui renvoie la moyenne des éléments d'une liste d'entiers. On suppose que la liste n'est jamais vide.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{moyenne\\_liste({liste_int})}} doit renvoyer \\texttt{{{round(sum(liste_int) / len(liste_int), 2)}}}
\\item \\texttt{{moyenne\\_liste([10, 20])}} doit renvoyer \\texttt{{15.0}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{carres\\_liste(liste)}} qui renvoie une nouvelle liste contenant le carré de chaque élément.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{carres\\_liste([{liste_int[0]}, {liste_int[1]}, {liste_int[2]}])}} doit renvoyer \\texttt{{{[x**2 for x in liste_int[:3]]}}}
\\item \\texttt{{carres\\_liste([1, 2, 3])}} doit renvoyer \\texttt{{[1, 4, 9]}}
\\end{{itemize}}"""
        },
        # --- Sur des tuples ---
        {
            'question': f"""Écrire une fonction \\texttt{{somme\\_tuple(t)}} qui renvoie la somme des éléments d'un tuple d'entiers, en parcourant le tuple avec une boucle \\texttt{{for}}.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{somme\\_tuple({tuple_int})}} doit renvoyer \\texttt{{{sum(tuple_int)}}}
\\item \\texttt{{somme\\_tuple((1, 2, 3))}} doit renvoyer \\texttt{{6}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{min\\_tuple(t)}} qui renvoie le plus petit élément d'un tuple d'entiers (sans utiliser \\texttt{{min}}). On suppose que le tuple n'est jamais vide.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{min\\_tuple({tuple_notes})}} doit renvoyer \\texttt{{{min(tuple_notes)}}}
\\item \\texttt{{min\\_tuple((8, 3, 5))}} doit renvoyer \\texttt{{3}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{moyenne\\_notes(notes)}} qui prend un tuple de notes et renvoie la moyenne. On suppose que le tuple n'est jamais vide.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{moyenne\\_notes({tuple_notes})}} doit renvoyer \\texttt{{{round(sum(tuple_notes) / len(tuple_notes), 2)}}}
\\item \\texttt{{moyenne\\_notes((10, 15, 20))}} doit renvoyer \\texttt{{15.0}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{tuple\\_en\\_liste(t)}} qui convertit un tuple en liste, en parcourant le tuple avec une boucle \\texttt{{for}} (sans utiliser \\texttt{{list()}}).

Exemples :
\\begin{{itemize}}
\\item \\texttt{{tuple\\_en\\_liste({tuple_int})}} doit renvoyer \\texttt{{{list(tuple_int)}}}
\\item \\texttt{{tuple\\_en\\_liste((1, 2))}} doit renvoyer \\texttt{{[1, 2]}}
\\end{{itemize}}"""
        },
        # --- Sur des dictionnaires ---
        {
            'question': f"""Écrire une fonction \\texttt{{somme\\_valeurs(dico)}} qui renvoie la somme de toutes les valeurs d'un dictionnaire dont les valeurs sont des entiers.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{somme\\_valeurs({dict_notes})}} doit renvoyer \\texttt{{{sum(dict_notes.values())}}}
\\item \\texttt{{somme\\_valeurs({{'a': 1, 'b': 2}})}} doit renvoyer \\texttt{{3}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{liste\\_cles(dico)}} qui renvoie la liste de toutes les clés d'un dictionnaire, en parcourant le dictionnaire avec une boucle \\texttt{{for}} (sans utiliser \\texttt{{.keys()}}).

Exemples :
\\begin{{itemize}}
\\item \\texttt{{liste\\_cles({dict_ages})}} doit renvoyer \\texttt{{{list(dict_ages.keys())}}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{liste\\_valeurs(dico)}} qui renvoie la liste de toutes les valeurs d'un dictionnaire, en parcourant le dictionnaire avec une boucle \\texttt{{for}}.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{liste\\_valeurs({dict_notes})}} doit renvoyer \\texttt{{{list(dict_notes.values())}}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{augmenter\\_prix(dico, pourcentage)}} qui renvoie un nouveau dictionnaire avec tous les prix augmentés du pourcentage donné.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{augmenter\\_prix({{'pomme': 2.0, 'banane': 1.5}}, 10)}} doit renvoyer \\texttt{{{{'pomme': 2.2, 'banane': 1.65}}}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{total\\_stock(dico)}} qui renvoie la quantité totale de produits en stock, à partir d'un dictionnaire dont les clés sont des noms de produits et les valeurs sont les quantités.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{total\\_stock({dict_stock})}} doit renvoyer \\texttt{{{sum(dict_stock.values())}}}
\\item \\texttt{{total\\_stock({{'a': 5, 'b': 3}})}} doit renvoyer \\texttt{{8}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{inverser\\_dico(dico)}} qui renvoie un nouveau dictionnaire où les clés et valeurs sont inversées.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{inverser\\_dico({{'a': 1, 'b': 2, 'c': 3}})}} doit renvoyer \\texttt{{{{1: 'a', 2: 'b', 3: 'c'}}}}
\\end{{itemize}}"""
        },
        # --- Sur des chaînes ---
        {
            'question': f"""Écrire une fonction \\texttt{{longueur\\_mot(mot)}} qui renvoie le nombre de caractères d'un mot, en parcourant le mot avec une boucle \\texttt{{for}} (sans utiliser \\texttt{{len}}).

Exemples :
\\begin{{itemize}}
\\item \\texttt{{longueur\\_mot('{mot1}')}} doit renvoyer \\texttt{{{len(mot1)}}}
\\item \\texttt{{longueur\\_mot('abc')}} doit renvoyer \\texttt{{3}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{inverser\\_chaine(mot)}} qui renvoie le mot inversé, en parcourant le mot avec une boucle \\texttt{{for}} (sans utiliser le slicing \\texttt{{[::-1]}}).

Exemples :
\\begin{{itemize}}
\\item \\texttt{{inverser\\_chaine('{mot1}')}} doit renvoyer \\texttt{{'{mot1[::-1]}'}}
\\item \\texttt{{inverser\\_chaine('abc')}} doit renvoyer \\texttt{{'cba'}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{repeter\\_chaine(mot, n)}} qui renvoie le mot répété \\texttt{{n}} fois en une seule chaîne, en utilisant une boucle \\texttt{{for}} (sans utiliser \\texttt{{*}}).

Exemples :
\\begin{{itemize}}
\\item \\texttt{{repeter\\_chaine('ab', 3)}} doit renvoyer \\texttt{{'ababab'}}
\\item \\texttt{{repeter\\_chaine('{mot1[:3]}', 2)}} doit renvoyer \\texttt{{'{mot1[:3] * 2}'}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{en\\_majuscules(mot)}} qui renvoie une nouvelle chaîne où chaque caractère a été mis en majuscule, en parcourant le mot avec une boucle \\texttt{{for}} et en utilisant \\texttt{{.upper()}} sur chaque caractère.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{en\\_majuscules('{mot1}')}} doit renvoyer \\texttt{{'{mot1.upper()}'}}
\\item \\texttt{{en\\_majuscules('abc')}} doit renvoyer \\texttt{{'ABC'}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{concatener\\_liste(liste)}} qui prend une liste de mots et renvoie une seule chaîne formée de tous les mots mis bout à bout, séparés par un espace (sans utiliser \\texttt{{.join()}}).

Exemples :
\\begin{{itemize}}
\\item \\texttt{{concatener\\_liste(['je', 'suis', 'ici'])}} doit renvoyer \\texttt{{'je suis ici'}}
\\item \\texttt{{concatener\\_liste(['a', 'b'])}} doit renvoyer \\texttt{{'a b'}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{somme\\_n(n)}} qui calcule la somme des entiers de 1 à \\texttt{{n}} en utilisant une boucle \\texttt{{for}} et \\texttt{{range}}.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{somme\\_n({a})}} doit renvoyer \\texttt{{{sum(range(1, a + 1))}}}
\\item \\texttt{{somme\\_n(5)}} doit renvoyer \\texttt{{15}}
\\end{{itemize}}"""
        },
        # --- Boucle sur une chaîne ---
        {
            'question': f"""Écrire une fonction \\texttt{{compter\\_caractere(mot, c)}} qui renvoie le nombre de fois que le caractère \\texttt{{c}} apparaît dans \\texttt{{mot}}, en parcourant le mot avec une boucle \\texttt{{for}} (sans utiliser \\texttt{{.count()}}).

Exemples :
\\begin{{itemize}}
\\item \\texttt{{compter\\_caractere('{mot1}', '{mot1[0]}')}} doit renvoyer \\texttt{{{mot1.count(mot1[0])}}}
\\item \\texttt{{compter\\_caractere('mississippi', 's')}} doit renvoyer \\texttt{{4}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{construire\\_liste\\_chars(mot)}} qui prend une chaîne et renvoie la liste de ses caractères, en parcourant le mot avec une boucle \\texttt{{for}} (sans utiliser \\texttt{{list()}}).

Exemples :
\\begin{{itemize}}
\\item \\texttt{{construire\\_liste\\_chars('{mot1[:4]}')}} doit renvoyer \\texttt{{{list(mot1[:4])}}}
\\item \\texttt{{construire\\_liste\\_chars('abc')}} doit renvoyer \\texttt{{['a', 'b', 'c']}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{concatener\\_majuscule(mot)}} qui renvoie une nouvelle chaîne où chaque caractère du mot est doublé (par exemple \\texttt{{'ab'}} devient \\texttt{{'aabb'}}).

Exemples :
\\begin{{itemize}}
\\item \\texttt{{concatener\\_majuscule('{mot1[:3]}')}} doit renvoyer \\texttt{{'{("".join(c*2 for c in mot1[:3]))}' }}
\\item \\texttt{{concatener\\_majuscule('ab')}} doit renvoyer \\texttt{{'aabb'}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{somme\\_codes(mot)}} qui renvoie la somme des codes ASCII de tous les caractères d'un mot, en utilisant \\texttt{{ord()}} sur chaque caractère.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{somme\\_codes('{mot1[:3]}')}} doit renvoyer \\texttt{{{sum(ord(c) for c in mot1[:3])}}}
\\item \\texttt{{somme\\_codes('abc')}} doit renvoyer \\texttt{{{ord('a') + ord('b') + ord('c')}}}
\\end{{itemize}}"""
        },
        # --- Boucle avec range() sur un entier ---
        {
            'question': f"""Écrire une fonction \\texttt{{produit\\_n(n)}} qui calcule le produit des entiers de 1 à \\texttt{{n}} (la factorielle) en utilisant \\texttt{{range}} et une variable accumulatrice.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{produit\\_n({b})}} doit renvoyer \\texttt{{{__import__('math').factorial(b)}}}
\\item \\texttt{{produit\\_n(4)}} doit renvoyer \\texttt{{24}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{liste\\_pairs\\_jusqu\\_a(n)}} qui renvoie la liste de tous les entiers pairs de 0 à \\texttt{{n}} inclus, en utilisant \\texttt{{range}}.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{liste\\_pairs\\_jusqu\\_a({a * 2})}} doit renvoyer \\texttt{{{list(range(0, a * 2 + 1, 2))}}}
\\item \\texttt{{liste\\_pairs\\_jusqu\\_a(8)}} doit renvoyer \\texttt{{[0, 2, 4, 6, 8]}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{multiples\\_de\\_n(n, limite)}} qui renvoie la liste des \\texttt{{limite}} premiers multiples de \\texttt{{n}} (à partir de \\texttt{{n}}), en utilisant \\texttt{{range}}.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{multiples\\_de\\_n({b}, 5)}} doit renvoyer \\texttt{{{[b * i for i in range(1, 6)]}}}
\\item \\texttt{{multiples\\_de\\_n(3, 4)}} doit renvoyer \\texttt{{[3, 6, 9, 12]}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{somme\\_carres(n)}} qui renvoie la somme des carrés des entiers de 1 à \\texttt{{n}} en utilisant \\texttt{{range}}.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{somme\\_carres({a})}} doit renvoyer \\texttt{{{sum(i**2 for i in range(1, a + 1))}}}
\\item \\texttt{{somme\\_carres(3)}} doit renvoyer \\texttt{{14}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{liste\\_puissances(n)}} qui renvoie la liste des puissances de 2 de $2^0$ à $2^n$, en utilisant \\texttt{{range}}.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{liste\\_puissances({b})}} doit renvoyer \\texttt{{{[2**i for i in range(b + 1)]}}}
\\item \\texttt{{liste\\_puissances(4)}} doit renvoyer \\texttt{{[1, 2, 4, 8, 16]}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{repeter\\_n\\_fois(liste, n)}} qui renvoie une nouvelle liste où chaque élément de la liste apparaît \\texttt{{n}} fois de suite.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{repeter\\_n\\_fois([1, 2], 3)}} doit renvoyer \\texttt{{[1, 1, 1, 2, 2, 2]}}
\\item \\texttt{{repeter\\_n\\_fois(['a', 'b'], 2)}} doit renvoyer \\texttt{{['a', 'a', 'b', 'b']}}
\\end{{itemize}}"""
        },
    ]

    template = random.choice(templates)
    content = template['question'] + """\\cadreligne"""
    return {'content': content}

def generate_niveau3():
    """Boucle for avec un if à l'intérieur"""

    a = random.randint(3, 12)
    b = random.randint(2, 8)
    seuil = random.randint(5, 15)

    liste_int = [random.randint(1, 20) for _ in range(random.randint(4, 6))]
    liste_mix = [random.randint(-10, 10) for _ in range(random.randint(4, 6))]
    liste_notes = [random.randint(0, 20) for _ in range(random.randint(4, 6))]

    tuple_int = tuple(random.randint(1, 20) for _ in range(random.randint(4, 6)))

    prenoms = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Frank', 'Grace', 'Hugo']
    random.shuffle(prenoms)
    dict_notes = {prenoms[i]: random.randint(5, 20) for i in range(random.randint(3, 5))}
    dict_ages = {prenoms[i]: random.randint(12, 18) for i in range(random.randint(3, 5))}
    dict_stock = {random.choice(['stylo', 'cahier', 'gomme', 'regle', 'crayon', 'colle']): random.randint(0, 50) for _ in range(random.randint(3, 5))}

    mots_exemples = ['python', 'algorithme', 'variable', 'fonction', 'boucle', 'programme']
    mot1 = random.choice(mots_exemples)

    templates = [
        # --- Listes avec if ---
        {
            'question': f"""Écrire une fonction \\texttt{{compter\\_pairs(liste)}} qui renvoie le nombre d'éléments pairs dans une liste d'entiers.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{compter\\_pairs({liste_int})}} doit renvoyer \\texttt{{{len([x for x in liste_int if x % 2 == 0])}}}
\\item \\texttt{{compter\\_pairs([1, 3, 5])}} doit renvoyer \\texttt{{0}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{filtrer\\_positifs(liste)}} qui renvoie une nouvelle liste contenant uniquement les nombres strictement positifs.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{filtrer\\_positifs({liste_mix})}} doit renvoyer \\texttt{{{[x for x in liste_mix if x > 0]}}}
\\item \\texttt{{filtrer\\_positifs([-1, -2, 0])}} doit renvoyer \\texttt{{[]}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{garder\\_grands(liste, seuil)}} qui renvoie une nouvelle liste contenant uniquement les éléments strictement supérieurs à \\texttt{{seuil}}.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{garder\\_grands({liste_int}, {seuil})}} doit renvoyer \\texttt{{{[x for x in liste_int if x > seuil]}}}
\\item \\texttt{{garder\\_grands([1, 2, 3], 5)}} doit renvoyer \\texttt{{[]}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{somme\\_pairs(liste)}} qui renvoie la somme des éléments pairs d'une liste d'entiers.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{somme\\_pairs({liste_int})}} doit renvoyer \\texttt{{{sum(x for x in liste_int if x % 2 == 0)}}}
\\item \\texttt{{somme\\_pairs([1, 3, 5])}} doit renvoyer \\texttt{{0}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{compter\\_superieurs(liste, seuil)}} qui renvoie le nombre d'éléments strictement supérieurs à \\texttt{{seuil}} dans une liste.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{compter\\_superieurs({liste_int}, {seuil})}} doit renvoyer \\texttt{{{len([x for x in liste_int if x > seuil])}}}
\\item \\texttt{{compter\\_superieurs([1, 2, 3], 10)}} doit renvoyer \\texttt{{0}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{remplacer\\_negatifs(liste)}} qui renvoie une nouvelle liste où tous les nombres négatifs sont remplacés par 0.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{remplacer\\_negatifs({liste_mix})}} doit renvoyer \\texttt{{{[x if x >= 0 else 0 for x in liste_mix]}}}
\\item \\texttt{{remplacer\\_negatifs([-3, 5, -1, 2])}} doit renvoyer \\texttt{{[0, 5, 0, 2]}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{premier\\_superieur(liste, seuil)}} qui renvoie le premier élément de la liste strictement supérieur à \\texttt{{seuil}}. Si aucun élément ne convient, renvoyer \\texttt{{None}}.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{premier\\_superieur({liste_int}, {seuil})}} doit renvoyer \\texttt{{{next((x for x in liste_int if x > seuil), None)}}}
\\item \\texttt{{premier\\_superieur([1, 2, 3], 10)}} doit renvoyer \\texttt{{None}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{doubler\\_pairs(liste)}} qui renvoie une nouvelle liste où les nombres pairs sont doublés et les impairs restent inchangés.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{doubler\\_pairs({liste_int})}} doit renvoyer \\texttt{{{[x * 2 if x % 2 == 0 else x for x in liste_int]}}}
\\item \\texttt{{doubler\\_pairs([1, 2, 3, 4])}} doit renvoyer \\texttt{{[1, 4, 3, 8]}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{notes\\_au\\_dessus(notes, minimum)}} qui renvoie la liste des notes supérieures ou égales à \\texttt{{minimum}}.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{notes\\_au\\_dessus({liste_notes}, 10)}} doit renvoyer \\texttt{{{[n for n in liste_notes if n >= 10]}}}
\\item \\texttt{{notes\\_au\\_dessus([5, 15, 8, 12], 10)}} doit renvoyer \\texttt{{[15, 12]}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{indice\\_minimum(liste)}} qui renvoie l'indice du plus petit élément d'une liste (sans utiliser \\texttt{{.index()}} ni \\texttt{{min}}). On suppose la liste non vide.

Indice : utiliser \\texttt{{for i in range(len(liste))}}.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{indice\\_minimum({liste_int})}} doit renvoyer \\texttt{{{liste_int.index(min(liste_int))}}}
\\item \\texttt{{indice\\_minimum([5, 2, 8])}} doit renvoyer \\texttt{{1}}
\\end{{itemize}}"""
        },
        # --- Tuples avec if ---
        {
            'question': f"""Écrire une fonction \\texttt{{compter\\_dans\\_tuple(t, valeur)}} qui renvoie le nombre de fois que \\texttt{{valeur}} apparaît dans le tuple \\texttt{{t}} (sans utiliser \\texttt{{.count()}}).

Exemples :
\\begin{{itemize}}
\\item \\texttt{{compter\\_dans\\_tuple({tuple_int}, {tuple_int[0]})}} doit renvoyer \\texttt{{{tuple_int.count(tuple_int[0])}}}
\\item \\texttt{{compter\\_dans\\_tuple((1, 2, 1, 3), 1)}} doit renvoyer \\texttt{{2}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{max\\_tuple\\_pair(t)}} qui renvoie le plus grand nombre pair dans un tuple d'entiers. Si aucun nombre n'est pair, renvoyer \\texttt{{None}}.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{max\\_tuple\\_pair({tuple_int})}} doit renvoyer \\texttt{{{max([x for x in tuple_int if x % 2 == 0], default=None)}}}
\\item \\texttt{{max\\_tuple\\_pair((1, 3, 5))}} doit renvoyer \\texttt{{None}}
\\end{{itemize}}"""
        },
        # --- Dictionnaires avec if ---
        {
            'question': f"""Écrire une fonction \\texttt{{eleves\\_reussite(notes, minimum)}} qui prend un dictionnaire de notes (clé = nom, valeur = note) et renvoie la liste des noms ayant une note supérieure ou égale à \\texttt{{minimum}}.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{eleves\\_reussite({dict_notes}, 10)}} doit renvoyer \\texttt{{{[k for k, v in dict_notes.items() if v >= 10]}}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{moyenne\\_reussite(notes, minimum)}} qui renvoie la moyenne des notes supérieures ou égales à \\texttt{{minimum}}. Si aucune note ne convient, renvoyer \\texttt{{0}}.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{moyenne\\_reussite({dict_notes}, 10)}} doit renvoyer \\texttt{{{round(sum(v for v in dict_notes.values() if v >= 10) / max(len([v for v in dict_notes.values() if v >= 10]), 1), 2)}}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{produits\\_en\\_stock(dico)}} qui prend un dictionnaire (clé = produit, valeur = quantité) et renvoie la liste des produits ayant une quantité strictement supérieure à 0.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{produits\\_en\\_stock({dict_stock})}} doit renvoyer \\texttt{{{[k for k, v in dict_stock.items() if v > 0]}}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{cles\\_valeur\\_max(dico)}} qui renvoie la clé associée à la plus grande valeur dans un dictionnaire (sans utiliser \\texttt{{max}}). On suppose le dictionnaire non vide.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{cles\\_valeur\\_max({dict_notes})}} doit renvoyer \\texttt{{'{max(dict_notes, key=dict_notes.get)}'}}
\\end{{itemize}}"""
        },
        # --- Chaînes avec if ---
        {
            'question': f"""Écrire une fonction \\texttt{{compter\\_voyelles(mot)}} qui renvoie le nombre de voyelles (a, e, i, o, u, y) dans un mot.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{compter\\_voyelles('{mot1}')}} doit renvoyer \\texttt{{{sum(1 for c in mot1 if c in 'aeiouy')}}}
\\item \\texttt{{compter\\_voyelles('xyz')}} doit renvoyer \\texttt{{1}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{supprimer\\_voyelles(mot)}} qui renvoie le mot sans les voyelles (a, e, i, o, u, y).

Exemples :
\\begin{{itemize}}
\\item \\texttt{{supprimer\\_voyelles('{mot1}')}} doit renvoyer \\texttt{{'{("".join(c for c in mot1 if c not in "aeiouy"))}'}}
\\item \\texttt{{supprimer\\_voyelles('bonjour')}} doit renvoyer \\texttt{{'bnjr'}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{garder\\_lettres(mot)}} qui renvoie une nouvelle chaîne contenant uniquement les lettres (pas les chiffres ni les espaces) d'un mot.

Indice : utiliser \\texttt{{.isalpha()}} sur chaque caractère.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{garder\\_lettres('abc123')}} doit renvoyer \\texttt{{'abc'}}
\\item \\texttt{{garder\\_lettres('a 1 b 2')}} doit renvoyer \\texttt{{'ab'}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{contient\\_doublon(liste)}} qui renvoie \\texttt{{True}} si la liste contient au moins un élément en double, \\texttt{{False}} sinon.

Indice : utiliser une liste de déjà-vus.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{contient\\_doublon([1, 2, 3, 2])}} doit renvoyer \\texttt{{True}}
\\item \\texttt{{contient\\_doublon({liste_int})}} doit renvoyer \\texttt{{{str(len(liste_int) != len(set(liste_int)))}}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{multiples\\_de(liste, n)}} qui renvoie une nouvelle liste contenant uniquement les éléments de \\texttt{{liste}} qui sont des multiples de \\texttt{{n}}.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{multiples\\_de({liste_int}, {b})}} doit renvoyer \\texttt{{{[x for x in liste_int if x % b == 0]}}}
\\item \\texttt{{multiples\\_de([1, 4, 6, 9], 3)}} doit renvoyer \\texttt{{[6, 9]}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{elements\\_uniques(liste)}} qui renvoie une nouvelle liste contenant chaque élément une seule fois, dans l'ordre d'apparition.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{elements\\_uniques([1, 2, 3, 2, 1, 4])}} doit renvoyer \\texttt{{[1, 2, 3, 4]}}
\\item \\texttt{{elements\\_uniques([5, 5, 5])}} doit renvoyer \\texttt{{[5]}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{indice\\_element(liste, valeur)}} qui renvoie l'indice de la première occurrence de \\texttt{{valeur}} dans la liste. Si \\texttt{{valeur}} n'est pas dans la liste, renvoyer \\texttt{{-1}} (sans utiliser \\texttt{{.index()}}).

Exemples :
\\begin{{itemize}}
\\item \\texttt{{indice\\_element([5, 3, 8, 3], 8)}} doit renvoyer \\texttt{{2}}
\\item \\texttt{{indice\\_element([5, 3, 8], 1)}} doit renvoyer \\texttt{{-1}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{nb\\_majuscules(mot)}} qui renvoie le nombre de lettres majuscules dans une chaîne.

Indice : utiliser \\texttt{{.isupper()}} sur chaque caractère.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{nb\\_majuscules('Bonjour NSI')}} doit renvoyer \\texttt{{4}}
\\item \\texttt{{nb\\_majuscules('abc')}} doit renvoyer \\texttt{{0}}
\\end{{itemize}}"""
        },
        # --- Boucle sur une chaîne avec if ---
        {
            'question': f"""Écrire une fonction \\texttt{{remplacer\\_espaces(mot)}} qui renvoie une nouvelle chaîne où chaque espace est remplacé par un tiret bas \\_\\ , les autres caractères restant inchangés.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{remplacer\\_espaces('bonjour monde')}} doit renvoyer \\texttt{{'bonjour\\_monde'}}
\\item \\texttt{{remplacer\\_espaces('nsi')}} doit renvoyer \\texttt{{'nsi'}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{compter\\_chiffres(mot)}} qui renvoie le nombre de chiffres dans une chaîne de caractères.

Indice : utiliser \\texttt{{.isdigit()}} sur chaque caractère.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{compter\\_chiffres('nsi2025')}} doit renvoyer \\texttt{{4}}
\\item \\texttt{{compter\\_chiffres('{mot1}')}} doit renvoyer \\texttt{{0}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{premiere\\_majuscule(mot)}} qui renvoie le premier caractère majuscule trouvé dans la chaîne, ou \\texttt{{None}} si aucun n'est trouvé.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{premiere\\_majuscule('bonjour NSI')}} doit renvoyer \\texttt{{'N'}}
\\item \\texttt{{premiere\\_majuscule('{mot1}')}} doit renvoyer \\texttt{{None}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{alterner\\_casse(mot)}} qui renvoie une nouvelle chaîne où les voyelles (a, e, i, o, u, y) sont mises en majuscule et les consonnes en minuscule.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{alterner\\_casse('python')}} doit renvoyer \\texttt{{''.join(c.upper() if c in 'aeiouy' else c.lower() for c in 'python')}}
\\item \\texttt{{alterner\\_casse('nsi')}} doit renvoyer \\texttt{{''.join(c.upper() if c in 'aeiouy' else c.lower() for c in 'nsi')}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{retirer\\_doublons\\_chaine(mot)}} qui renvoie une nouvelle chaîne ne contenant que la première occurrence de chaque caractère, dans l'ordre d'apparition.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{retirer\\_doublons\\_chaine('mississippi')}} doit renvoyer \\texttt{{''.join(dict.fromkeys('mississippi'))}}
\\item \\texttt{{retirer\\_doublons\\_chaine('aabbcc')}} doit renvoyer \\texttt{{'abc'}}
\\end{{itemize}}"""
        },
        # --- Boucle avec range() et if ---
        {
            'question': f"""Écrire une fonction \\texttt{{pairs\\_jusqu\\_a(n)}} qui renvoie la liste des entiers pairs strictement inférieurs à \\texttt{{n}}, en utilisant \\texttt{{range}} et un \\texttt{{if}}.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{pairs\\_jusqu\\_a({a * 2 + 1})}} doit renvoyer \\texttt{{{[i for i in range(a * 2 + 1) if i % 2 == 0]}}}
\\item \\texttt{{pairs\\_jusqu\\_a(7)}} doit renvoyer \\texttt{{[0, 2, 4, 6]}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{diviseurs(n)}} qui renvoie la liste de tous les diviseurs de \\texttt{{n}} (entiers de 1 à \\texttt{{n}} qui le divisent), en utilisant \\texttt{{range}}.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{diviseurs(12)}} doit renvoyer \\texttt{{[1, 2, 3, 4, 6, 12]}}
\\item \\texttt{{diviseurs({b * 2})}} doit renvoyer \\texttt{{{[i for i in range(1, b * 2 + 1) if (b * 2) % i == 0]}}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{somme\\_impairs\\_jusqu\\_a(n)}} qui renvoie la somme des entiers impairs de 1 à \\texttt{{n}} inclus.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{somme\\_impairs\\_jusqu\\_a({a * 2})}} doit renvoyer \\texttt{{{sum(i for i in range(1, a * 2 + 1) if i % 2 != 0)}}}
\\item \\texttt{{somme\\_impairs\\_jusqu\\_a(5)}} doit renvoyer \\texttt{{9}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{compter\\_multiples(n, limite)}} qui renvoie le nombre d'entiers de 1 à \\texttt{{limite}} qui sont des multiples de \\texttt{{n}}.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{compter\\_multiples({b}, {a * b})}} doit renvoyer \\texttt{{{len([i for i in range(1, a * b + 1) if i % b == 0])}}}
\\item \\texttt{{compter\\_multiples(3, 10)}} doit renvoyer \\texttt{{3}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{indices\\_pairs\\_liste(liste)}} qui renvoie une nouvelle liste ne contenant que les éléments situés aux indices pairs (0, 2, 4, ...) de la liste.

Indice : utiliser \\texttt{{range(0, len(liste), 2)}}.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{indices\\_pairs\\_liste({liste_int})}} doit renvoyer \\texttt{{{liste_int[::2]}}}
\\item \\texttt{{indices\\_pairs\\_liste([10, 20, 30, 40, 50])}} doit renvoyer \\texttt{{[10, 30, 50]}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{premier\\_multiple(n, liste)}} qui renvoie le premier élément de la liste qui est un multiple de \\texttt{{n}}, ou \\texttt{{None}} si aucun ne l'est.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{premier\\_multiple({b}, {liste_int})}} doit renvoyer \\texttt{{{next((x for x in liste_int if x % b == 0), None)}}}
\\item \\texttt{{premier\\_multiple(7, [1, 2, 3])}} doit renvoyer \\texttt{{None}}
\\end{{itemize}}"""
        },
    ]

    template = random.choice(templates)
    content = template['question'] + """\\cadreligne"""
    return {'content': content}

def generate_niveau4():
    """Double boucle for, avec ou sans if"""

    a = random.randint(2, 5)
    b = random.randint(2, 5)

    liste_int = [random.randint(1, 15) for _ in range(random.randint(3, 5))]
    liste_int2 = [random.randint(1, 10) for _ in range(random.randint(3, 4))]

    mat = [[random.randint(1, 9) for _ in range(random.randint(2, 3))] for _ in range(random.randint(2, 3))]
    mat_carree = [[random.randint(1, 9) for _ in range(3)] for _ in range(3)]

    prenoms = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
    matieres = ['maths', 'NSI', 'physique', 'anglais']

    templates = [
        # --- Double boucle sans if ---
        {
            'question': f"""Écrire une fonction \\texttt{{somme\\_matrice(matrice)}} qui calcule la somme de tous les éléments d'une matrice (liste de listes).

Exemples :
\\begin{{itemize}}
\\item \\texttt{{somme\\_matrice({mat})}} doit renvoyer \\texttt{{{sum(sum(row) for row in mat)}}}
\\item \\texttt{{somme\\_matrice([[1, 2], [3, 4]])}} doit renvoyer \\texttt{{10}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{aplatir(matrice)}} qui prend une matrice (liste de listes) et renvoie une seule liste contenant tous les éléments.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{aplatir({mat})}} doit renvoyer \\texttt{{{[x for row in mat for x in row]}}}
\\item \\texttt{{aplatir([[1, 2], [3, 4]])}} doit renvoyer \\texttt{{[1, 2, 3, 4]}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{table\\_multiplication(n)}} qui renvoie une liste de listes représentant la table de multiplication de 1 à \\texttt{{n}}.

L'élément à la ligne \\texttt{{i}} et colonne \\texttt{{j}} vaut \\texttt{{(i+1) * (j+1)}}.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{table\\_multiplication(3)}} doit renvoyer \\texttt{{[[1, 2, 3], [2, 4, 6], [3, 6, 9]]}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{produit\\_cartesien(liste1, liste2)}} qui renvoie la liste de tous les couples (a, b) possibles avec a dans \\texttt{{liste1}} et b dans \\texttt{{liste2}}.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{produit\\_cartesien([1, 2], ['a', 'b'])}} doit renvoyer \\texttt{{[(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{transposer(matrice)}} qui renvoie la transposée d'une matrice (les lignes deviennent des colonnes).

Exemples :
\\begin{{itemize}}
\\item \\texttt{{transposer([[1, 2, 3], [4, 5, 6]])}} doit renvoyer \\texttt{{[[1, 4], [2, 5], [3, 6]]}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{triangle\\_nombres(n)}} qui renvoie une liste de listes formant un triangle : la première sous-liste contient [1], la deuxième [1, 2], ..., la n-ième [1, 2, ..., n].

Exemples :
\\begin{{itemize}}
\\item \\texttt{{triangle\\_nombres({a})}} doit renvoyer \\texttt{{{[[j for j in range(1, i + 1)] for i in range(1, a + 1)]}}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{concatener\\_listes(liste\\_de\\_listes)}} qui concatène toutes les sous-listes en une seule liste, avec une double boucle \\texttt{{for}}.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{concatener\\_listes([[1, 2], [3], [4, 5, 6]])}} doit renvoyer \\texttt{{[1, 2, 3, 4, 5, 6]}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{multiplier\\_matrice\\_scalaire(matrice, k)}} qui renvoie une nouvelle matrice où chaque élément est multiplié par \\texttt{{k}}.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{multiplier\\_matrice\\_scalaire({mat}, 2)}} doit renvoyer \\texttt{{{[[x * 2 for x in row] for row in mat]}}}
\\end{{itemize}}"""
        },
        # --- Double boucle avec if ---
        {
            'question': f"""Écrire une fonction \\texttt{{pairs\\_matrice(matrice)}} qui renvoie la liste de tous les éléments pairs dans une matrice (liste de listes).

Exemples :
\\begin{{itemize}}
\\item \\texttt{{pairs\\_matrice({mat})}} doit renvoyer \\texttt{{{[x for row in mat for x in row if x % 2 == 0]}}}
\\item \\texttt{{pairs\\_matrice([[1, 2], [3, 4]])}} doit renvoyer \\texttt{{[2, 4]}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{max\\_matrice(matrice)}} qui renvoie le plus grand élément d'une matrice (liste de listes), sans utiliser \\texttt{{max}}.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{max\\_matrice({mat})}} doit renvoyer \\texttt{{{max(max(row) for row in mat)}}}
\\item \\texttt{{max\\_matrice([[1, 2], [3, 4]])}} doit renvoyer \\texttt{{4}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{compter\\_valeur\\_matrice(matrice, valeur)}} qui compte le nombre d'occurrences d'une valeur dans une matrice.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{compter\\_valeur\\_matrice({mat_carree}, {mat_carree[0][0]})}} doit renvoyer \\texttt{{{sum(row.count(mat_carree[0][0]) for row in mat_carree)}}}
\\item \\texttt{{compter\\_valeur\\_matrice([[1, 2], [1, 3]], 1)}} doit renvoyer \\texttt{{2}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{positions\\_valeur(matrice, valeur)}} qui renvoie la liste des positions (ligne, colonne) où apparaît \\texttt{{valeur}} dans la matrice.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{positions\\_valeur([[1, 2], [3, 1]], 1)}} doit renvoyer \\texttt{{[(0, 0), (1, 1)]}}
\\item \\texttt{{positions\\_valeur([[5, 5], [5, 5]], 5)}} doit renvoyer \\texttt{{[(0, 0), (0, 1), (1, 0), (1, 1)]}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{paires\\_somme(liste, cible)}} qui renvoie la liste de tous les couples (i, j) avec i < j tels que \\texttt{{liste[i] + liste[j] == cible}}.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{paires\\_somme([1, 2, 3, 4], 5)}} doit renvoyer \\texttt{{[(0, 3), (1, 2)]}}
\\item \\texttt{{paires\\_somme([1, 1, 1], 2)}} doit renvoyer \\texttt{{[(0, 1), (0, 2), (1, 2)]}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{somme\\_diagonale(matrice)}} qui renvoie la somme des éléments sur la diagonale principale d'une matrice carrée (éléments où ligne == colonne).

Exemples :
\\begin{{itemize}}
\\item \\texttt{{somme\\_diagonale({mat_carree})}} doit renvoyer \\texttt{{{sum(mat_carree[i][i] for i in range(len(mat_carree)))}}}
\\item \\texttt{{somme\\_diagonale([[1, 2], [3, 4]])}} doit renvoyer \\texttt{{5}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{elements\\_communs(liste1, liste2)}} qui renvoie la liste des éléments présents dans les deux listes (sans doublons).

Exemples :
\\begin{{itemize}}
\\item \\texttt{{elements\\_communs([1, 2, 3, 4], [3, 4, 5, 6])}} doit renvoyer \\texttt{{[3, 4]}}
\\item \\texttt{{elements\\_communs([1, 2], [3, 4])}} doit renvoyer \\texttt{{[]}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{chercher\\_matrice(matrice, valeur)}} qui renvoie \\texttt{{True}} si \\texttt{{valeur}} est présente quelque part dans la matrice, \\texttt{{False}} sinon.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{chercher\\_matrice({mat}, {mat[0][0]})}} doit renvoyer \\texttt{{True}}
\\item \\texttt{{chercher\\_matrice([[1, 2], [3, 4]], 5)}} doit renvoyer \\texttt{{False}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{doublons\\_entre\\_listes(liste1, liste2)}} qui renvoie \\texttt{{True}} si au moins un élément est présent dans les deux listes, \\texttt{{False}} sinon.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{doublons\\_entre\\_listes({liste_int}, {liste_int2})}} doit renvoyer \\texttt{{{str(bool(set(liste_int) & set(liste_int2)))}}}
\\item \\texttt{{doublons\\_entre\\_listes([1, 2], [3, 4])}} doit renvoyer \\texttt{{False}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{lignes\\_contenant(matrice, valeur)}} qui renvoie la liste des indices des lignes de la matrice qui contiennent \\texttt{{valeur}}.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{lignes\\_contenant([[1, 2], [3, 4], [1, 5]], 1)}} doit renvoyer \\texttt{{[0, 2]}}
\\item \\texttt{{lignes\\_contenant([[1, 2], [3, 4]], 5)}} doit renvoyer \\texttt{{[]}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{couples\\_produit\\_pair(liste1, liste2)}} qui renvoie la liste de tous les couples (a, b) avec a dans \\texttt{{liste1}} et b dans \\texttt{{liste2}} dont le produit est pair.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{couples\\_produit\\_pair([1, 2], [3, 4])}} doit renvoyer \\texttt{{[(1, 4), (2, 3), (2, 4)]}}
\\end{{itemize}}"""
        },
        {
            'question': f"""Écrire une fonction \\texttt{{remplacer\\_dans\\_matrice(matrice, ancien, nouveau)}} qui renvoie une nouvelle matrice où toutes les occurrences de \\texttt{{ancien}} sont remplacées par \\texttt{{nouveau}}.

Exemples :
\\begin{{itemize}}
\\item \\texttt{{remplacer\\_dans\\_matrice([[1, 2], [2, 3]], 2, 0)}} doit renvoyer \\texttt{{[[1, 0], [0, 3]]}}
\\end{{itemize}}"""
        },
    ]

    template = random.choice(templates)
    content = template['question'] + """\\cadreligne"""
    return {'content': content}

def generate_niveau5():
    """Fonction avec plusieurs boucles for et if imbriqués"""
    templates = [
        {
            'question': "Écrire une fonction \\texttt{compter_motifs(matrice, motif)} qui compte le nombre de fois qu'un motif 2×2 apparaît dans une matrice.\n\nLe motif est également une matrice 2×2. La fonction doit parcourir toutes les sous-matrices 2×2 possibles."
        },
        {
            'question': lambda n: f"Écrire une fonction \\texttt{{triplets_pythagoriciens(n)}} qui trouve tous les triplets (a, b, c) tels que a² + b² = c² avec a, b, c ≤ {n}.\n\nExemple : pour n={n}, chercher tous les triplets pythagoriciens."
        },
        {
            'question': "Écrire une fonction \\texttt{mots_croises(grille, mot)} qui vérifie si un mot peut être placé horizontalement ou verticalement dans une grille de mots croisés (liste de listes de caractères).\n\nLa fonction doit vérifier toutes les positions possibles."
        },
        {
            'question': lambda lst: f"Écrire une fonction \\texttt{{sous_suites_croissantes(liste)}} qui trouve toutes les sous-suites strictement croissantes d'au moins 3 éléments.\n\nExemple : \\texttt{{sous_suites_croissantes({lst})}}."
        }
    ]

    template = random.choice(templates)

    if callable(template['question']):
        if 'pythagoriciens' in template['question'](10):
            content = template['question'](random.randint(10, 15))
        else:
            lst = [random.randint(1, 20) for _ in range(random.randint(8, 12))]
            content = template['question'](lst)
    else:
        content = template['question']

    return {'content': content}

def generate_niveau6():
    """Fonction complexe avec multiples structures imbriquées"""
    templates = [
        {
            'question': "Écrire une fonction \\texttt{analyser_transactions(transactions, seuil)} qui analyse une liste de transactions bancaires.\n\nChaque transaction est un dictionnaire avec 'date', 'montant', 'type' (débit/crédit).\n\nLa fonction doit :\n\\begin{itemize}\n\\item Grouper les transactions par mois\n\\item Pour chaque mois, calculer le solde\n\\item Identifier les mois où le solde dépasse le seuil en valeur absolue\n\\end{itemize}"
        },
        {
            'question': "Écrire une fonction \\texttt{resoudre_sudoku_ligne(grille, ligne)} qui vérifie si une ligne de Sudoku (9 cases) respecte les règles :\n\\begin{itemize}\n\\item Pas de doublons parmi les chiffres de 1 à 9\n\\item Les cases vides sont représentées par 0\n\\item Suggérer les chiffres manquants possibles\n\\end{itemize}"
        },
        {
            'question': "Écrire une fonction \\texttt{chemins_labyrinth(labyrinthe, depart, arrivee)} qui trouve tous les chemins possibles dans un labyrinthe (matrice de 0 et 1).\n\nLes déplacements sont possibles en haut, bas, gauche, droite uniquement sur les cases à 0."
        }
    ]
    
    content = random.choice(templates)['question']
    
    return {'content': content}