import random


def generate_exercises(niveau, count=5):
    """Génère des exercices de débogage"""
    generators = {
        1: gen_niveau1,
        2: gen_niveau2,
        3: gen_niveau3,
        4: gen_niveau4,
        5: gen_niveau5,
    }
    if niveau not in generators:
        raise ValueError(f"Niveau {niveau} non supporté")
    all_templates = generators[niveau]()
    return random.sample(all_templates, min(count, len(all_templates)))


# ── Formateur LaTeX ───────────────────────────────────────────────────────────

def _fmt(description, code, nb_erreurs=1, erreur_python=None):
    """Formate un exercice de débogage en LaTeX."""
    n_str = "une erreur"  if nb_erreurs == 1 else f"{nb_erreurs} erreurs"
    l_str = "l'erreur"    if nb_erreurs == 1 else "les erreurs"

    if erreur_python:
        intro = (f"La fonction suivante est censée \\textbf{{{description}}}, "
                 f"mais elle provoque une erreur.")
    else:
        intro = (f"La fonction suivante est censée \\textbf{{{description}}}, "
                 f"mais elle contient \\textbf{{{n_str}}}.")

    parts = [
        intro,
        "",
        "\\begin{lstlisting}",
        code,
        "\\end{lstlisting}",
        "",
    ]

    if erreur_python:
        parts += [
            f"\\textbf{{Message d'erreur Python :}} \\texttt{{{erreur_python.replace('_','\\_')}}}",
            "",
        ]

    parts += [
        f"\\textbf{{a)}} Entourez {l_str} dans le code ci-dessus.",
        "",
    ]

    is_syntax = erreur_python and (erreur_python.startswith("SyntaxError")
                                   or erreur_python.startswith("IndentationError"))
    if is_syntax:
        qb = "\\textbf{b)} Écrivez la ligne corrigée :"
    elif erreur_python:
        qb = "\\textbf{b)} Écrivez un appel de la fonction qui déclenche cette erreur :"
    else:
        qb = "\\textbf{b)} Écrivez un appel de la fonction qui met en évidence le problème :"

    parts += [
        qb,
        "",
        "\\fbox{\\parbox{12cm}{\\rule{0pt}{1.5cm}}}",
    ]
    return "\n".join(parts)


# ── Niveau 1 : code if/else, 1 erreur ────────────────────────────────────────

def gen_niveau1():
    a    = random.randint(5, 15)
    b    = random.randint(2, 6)
    pair = random.randint(1, 8) * 2

    templates = [
        # ── Logique : condition ou retour inversé ──
        dict(
            description="renvoyer \\texttt{True} si \\texttt{n} est pair, \\texttt{False} sinon",
            code="""def est_pair(n):
    if n % 2 == 1:
        return True
    else:
        return False""",
        ),
        dict(
            description="renvoyer le maximum de deux nombres",
            code="""def maximum(a, b):
    if a > b:
        return b
    else:
        return a""",
        ),
        dict(
            description="calculer la valeur absolue de \\texttt{x} (sans utiliser \\texttt{abs})",
            code="""def valeur_absolue(x):
    if x < 0:
        return x
    else:
        return -x""",
        ),
        dict(
            description="renvoyer \\texttt{True} si \\texttt{a} et \\texttt{b} sont égaux",
            code="""def sont_egaux(a, b):
    if a > b:
        return True
    else:
        return False""",
        ),
        dict(
            description="renvoyer \\texttt{True} si la liste est vide, \\texttt{False} sinon",
            code="""def est_vide(liste):
    if len(liste) > 0:
        return True
    else:
        return False""",
        ),
        dict(
            description="calculer la différence \\texttt{a - b}",
            code="""def difference(a, b):
    return a + b""",
        ),
        dict(
            description="calculer le carré de \\texttt{n}",
            code="""def carre(n):
    return n * 2""",
        ),
        dict(
            description="calculer le produit de \\texttt{a} et \\texttt{b}",
            code="""def produit(a, b):
    return a + b""",
        ),
        dict(
            description="renvoyer \\texttt{True} si \\texttt{x} est strictement positif",
            code="""def est_positif(x):
    if x >= 0:
        return True
    else:
        return False""",
        ),
        dict(
            description="renvoyer \\texttt{True} si \\texttt{a} est strictement supérieur à \\texttt{b}",
            code="""def strictement_superieur(a, b):
    if a >= b:
        return True
    else:
        return False""",
        ),
        dict(
            description="renvoyer l'opposé de \\texttt{n}",
            code="""def oppose(n):
    return n""",
        ),
        dict(
            description="renvoyer \\texttt{True} si deux mots ont la même longueur",
            code="""def meme_longueur(m1, m2):
    if len(m1) != len(m2):
        return True
    else:
        return False""",
        ),
        # ── Erreurs syntaxe / runtime ──
        dict(
            description="renvoyer \\texttt{True} si \\texttt{n} vaut 0, \\texttt{False} sinon",
            code="""def est_nul(n):
    if n = 0:
        return True
    else:
        return False""",
            erreur_python="SyntaxError: invalid syntax",
        ),
        dict(
            description="renvoyer le signe de \\texttt{n} sous forme de chaîne (\\texttt{'+'} ou \\texttt{'-'})",
            code="""def signe(n)
    if n >= 0:
        return '+'
    else:
        return '-'""",
            erreur_python="SyntaxError: expected ':'",
        ),
        dict(
            description="renvoyer \\texttt{True} si \\texttt{n} est strictement positif",
            code="""def est_positif(n):
    if n > 0:
    return True
    else:
        return False""",
            erreur_python="IndentationError: expected an indented block after 'if' statement",
        ),
        dict(
            description="calculer la valeur absolue de \\texttt{n} (sans \\texttt{abs})",
            code="""def valeur_absolue(n):
    if n >= 0:
        return n
    else:
        retrun -n""",
            erreur_python="NameError: name 'retrun' is not defined",
        ),
        dict(
            description="renvoyer le double de \\texttt{n}",
            code="""def double(n):
    if n >= 0:
        return x * 2
    else:
        return -x * 2""",
            erreur_python="NameError: name 'x' is not defined",
        ),
        dict(
            description="renvoyer le carré de \\texttt{n}",
            code="""def carre(n):
    resutat = n * n
    return resultat""",
            erreur_python="NameError: name 'resultat' is not defined",
        ),
        dict(
            description="renvoyer \\texttt{True} si le mot a plus de \\texttt{n} caractères",
            code="""def assez_long(mot, n):
    if len(mot) > "n":
        return True
    else:
        return False""",
            erreur_python="TypeError: '>' not supported between instances of 'int' and 'str'",
        ),
        dict(
            description="renvoyer la longueur de la liste si elle est non vide, 0 sinon",
            code="""def longueur(liste):
    if liste:
        return len[liste]
    else:
        return 0""",
            erreur_python="TypeError: 'builtin_function_or_method' object is not subscriptable",
        ),
        dict(
            description="renvoyer le message '\\texttt{n} est positif' si \\texttt{n} est positif, '\\texttt{n} est negatif' sinon",
            code="""def message_signe(n):
    if n > 0:
        return n + " est positif"
    else:
        return n + " est negatif" """,
            erreur_python="TypeError: unsupported operand type(s) for +: 'int' and 'str'",
        ),
    ]
    return [{'content': _fmt(t['description'], t['code'],
                              t.get('nb_erreurs', 1), t.get('erreur_python'))}
            for t in templates]


# ── Niveau 2 : boucle for (sans if), 1 erreur ────────────────────────────────

def gen_niveau2():
    m      = random.randint(3, 5)
    c      = random.randint(2, 4)
    lst    = [random.randint(1, 8) for _ in range(4)]
    mot    = random.choice(['python', 'boucle', 'code', 'algo'])
    petite = [random.randint(1, 4) for _ in range(3)]

    templates = [
        # ── Erreur courante : range(liste) ──
        dict(
            description="calculer la somme des éléments d'une liste",
            code="""def somme_liste(liste):
    total = 0
    for i in range(liste):
        total += liste[i]
    return total""",
            erreur_python="TypeError: 'list' object cannot be interpreted as an integer",
        ),
        dict(
            description="renvoyer une liste où chaque élément est doublé",
            code="""def doubler(liste):
    resultat = []
    for i in range(liste):
        resultat.append(liste[i] * 2)
    return resultat""",
            erreur_python="TypeError: 'list' object cannot be interpreted as an integer",
        ),
        # ── Cas limite : range(n) au lieu de range(1, n+1) ──
        dict(
            description=f"calculer la somme des entiers de 1 à \\texttt{{n}}",
            code="""def somme_n(n):
    total = 0
    for i in range(n):
        total += i
    return total""",
        ),
        dict(
            description="renvoyer la liste des entiers de 1 à \\texttt{n}",
            code="""def liste_entiers(n):
    resultat = []
    for i in range(n):
        resultat.append(i)
    return resultat""",
        ),
        # ── Cas limite : range(len - 1) oublie le dernier élément ──
        dict(
            description="calculer la somme de tous les éléments d'une liste",
            code="""def somme_liste(liste):
    total = 0
    for i in range(len(liste) - 1):
        total += liste[i]
    return total""",
        ),
        dict(
            description="inverser une chaîne de caractères",
            code=f"""def inverser(texte):
    resultat = ""
    for i in range(1, len(texte)):
        resultat = texte[i] + resultat
    return resultat""",
        ),
        # ── Logique : initialisation incorrecte ──
        dict(
            description="compter le nombre d'éléments dans une liste",
            code="""def compter(liste):
    compteur = 1
    for x in liste:
        compteur += 1
    return compteur""",
        ),
        dict(
            description="calculer le produit de tous les éléments d'une liste",
            code="""def produit_liste(liste):
    resultat = 0
    for x in liste:
        resultat *= x
    return resultat""",
        ),
        # ── Logique : = au lieu de += ──
        dict(
            description=f"calculer la somme des carrés des entiers de 1 à \\texttt{{n}}",
            code="""def somme_carres(n):
    total = 0
    for i in range(1, n + 1):
        total = i ** 2
    return total""",
        ),
        # ── Erreur courante : mauvaise variable dans l'accumulateur ──
        dict(
            description="construire la liste des puissances de 2 de $2^0$ à $2^{n-1}$",
            code="""def puissances(n):
    resultat = []
    for i in range(n):
        resultat.append(n ** i)
    return resultat""",
        ),
        dict(
            description="construire la liste des multiples de \\texttt{k} de 1 à \\texttt{n}",
            code=f"""def multiples(n, k):
    resultat = []
    for i in range(1, n + 1):
        resultat.append(i)
    return resultat""",
        ),
        # ── Cas limite : range(n+1) fait une itération de trop ──
        dict(
            description=f"calculer $n!$ (la factorielle de \\texttt{{n}})",
            code="""def factorielle(n):
    resultat = 1
    for i in range(n + 1):
        resultat *= i
    return resultat""",
        ),
        # ── Erreur courante : n'utilise pas la variable de boucle ──
        dict(
            description="renvoyer la liste des indices d'une autre liste",
            code="""def indices(liste):
    resultat = []
    for i in range(len(liste)):
        resultat.append(liste[i])
    return resultat""",
        ),
        # ── Logique : mauvais sens dans la concaténation ──
        dict(
            description="construire une chaîne qui répète chaque lettre deux fois",
            code="""def repeter_lettres(mot):
    resultat = ""
    for c in mot:
        resultat = c * 2 + resultat
    return resultat""",
        ),
        # ── Erreur courante : boucle sur les indices mais avec mauvaise variable ──
        dict(
            description="calculer la somme des éléments d'une liste en utilisant les indices",
            code="""def somme_indices(liste):
    total = 0
    for i in range(len(liste)):
        total += i
    return total""",
        ),
        # ── SyntaxError : deux-points manquants après for ──
        dict(
            description="calculer la somme des éléments d'une liste",
            code="""def somme_liste2(liste):
    total = 0
    for x in liste
        total += x
    return total""",
            erreur_python="SyntaxError: expected ':'",
        ),
        # ── IndentationError : corps de boucle non indenté ──
        dict(
            description="renvoyer la liste des carrés des entiers de 1 à \\texttt{n}",
            code="""def carres(n):
    resultat = []
    for i in range(1, n + 1):
    resultat.append(i ** 2)
    return resultat""",
            erreur_python="IndentationError: expected an indented block after 'for' statement",
        ),
        # ── NameError : mauvaise variable dans le corps de boucle ──
        dict(
            description="calculer la somme des éléments d'une liste",
            code="""def somme_elements(liste):
    total = 0
    for element in liste:
        total += valeur
    return total""",
            erreur_python="NameError: name 'valeur' is not defined",
        ),
        # ── TypeError : concaténation entier + chaîne dans boucle ──
        dict(
            description="construire la chaîne des éléments d'une liste séparés par des virgules",
            code="""def liste_en_chaine(liste):
    resultat = ""
    for x in liste:
        resultat += x + ", "
    return resultat""",
            erreur_python="TypeError: unsupported operand type(s) for +: 'str' and 'int'",
        ),
    ]
    return [{'content': _fmt(t['description'], t['code'],
                              t.get('nb_erreurs', 1), t.get('erreur_python'))}
            for t in templates]


# ── Niveau 3 : for + if, 2 erreurs ───────────────────────────────────────────

def gen_niveau3():
    lst_mix = [random.randint(-5, 8) for _ in range(5)]
    lst_int = [random.randint(1, 12) for _ in range(5)]
    seuil   = random.randint(3, 7)
    c       = random.randint(2, 4)

    templates = [
        # ── range(liste) + mauvaise condition ──
        dict(
            description="compter les éléments strictement positifs d'une liste",
            code="""def compter_positifs(liste):
    compteur = 0
    for i in range(liste):
        if liste[i] >= 0:
            compteur += 1
    return compteur""",
            nb_erreurs=2,
        ),
        # ── initialisation + condition inversée ──
        dict(
            description="compter les éléments pairs dans une liste",
            code="""def compter_pairs(liste):
    compteur = 1
    for x in liste:
        if x % 2 == 1:
            compteur += 1
    return compteur""",
            nb_erreurs=2,
        ),
        # ── range(len-1) + mauvais accumulateur ──
        dict(
            description=f"calculer la somme des éléments d'une liste supérieurs à {seuil}",
            code=f"""def somme_superieurs(liste, seuil):
    total = 0
    for i in range(len(liste) - 1):
        if liste[i] > seuil:
            total = liste[i]
    return total""",
            nb_erreurs=2,
        ),
        # ── range(n) au lieu de range(1,n+1) + condition inclut 0 ──
        dict(
            description="renvoyer la liste des entiers de 1 à \\texttt{n} qui sont des multiples de \\texttt{k}",
            code=f"""def multiples(n, k):
    resultat = []
    for i in range(n):
        if i % k == 0:
            resultat.append(i)
    return resultat""",
            nb_erreurs=2,
        ),
        # ── condition inversée ──
        dict(
            description="renvoyer une liste avec uniquement les éléments négatifs d'une liste",
            code="""def garder_negatifs(liste):
    resultat = []
    for x in liste:
        if x > 0:
            resultat.append(x)
    return resultat""",
            nb_erreurs=1,
        ),
        # ── initialisation + condition inversée ──
        dict(
            description="renvoyer le plus petit élément d'une liste (sans utiliser \\texttt{min})",
            code="""def trouver_min(liste):
    mini = 0
    for x in liste:
        if x > mini:
            mini = x
    return mini""",
            nb_erreurs=2,
        ),
        # ── range(liste) + = au lieu de += ──
        dict(
            description="calculer la somme des éléments pairs d'une liste",
            code="""def somme_pairs(liste):
    total = 0
    for i in range(liste):
        if liste[i] % 2 == 0:
            total = liste[i]
    return total""",
            nb_erreurs=2,
        ),
        # ── else manquant + condition trop large ──
        dict(
            description="renvoyer la liste des éléments remplacés par 0 s'ils sont négatifs, "
                        "inchangés sinon",
            code="""def remplacer_negatifs(liste):
    resultat = []
    for x in liste:
        if x <= 0:
            resultat.append(0)
    return resultat""",
            nb_erreurs=2,
        ),
        # ── itération sur les valeurs d'un dict au lieu des clés ──
        dict(
            description="renvoyer la liste des élèves ayant une note supérieure ou égale à 10",
            code="""def eleves_reussite(notes):
    resultat = []
    for note in notes:
        if note >= 10:
            resultat.append(note)
    return resultat""",
            nb_erreurs=2,
        ),
        # ── NameError : typo dans variable à l'intérieur d'un for+if ──
        dict(
            description="renvoyer la liste des éléments strictement positifs",
            code="""def filtrer_positifs(liste):
    resultat = []
    for x in liste:
        if x > 0:
            resultat.append(elemnt)
    return resultat""",
            nb_erreurs=1,
            erreur_python="NameError: name 'elemnt' is not defined",
        ),
        # ── IndentationError : if mal indenté dans for ──
        dict(
            description="compter les éléments strictement supérieurs à un seuil",
            code=f"""def compter_superieurs(liste, seuil):
    compteur = 0
    for x in liste:
    if x > seuil:
        compteur += 1
    return compteur""",
            nb_erreurs=1,
            erreur_python="IndentationError: expected an indented block after 'for' statement",
        ),
        # ── TypeError : opération incorrecte dans for+if ──
        dict(
            description="renvoyer la somme des longueurs des mots d'une liste",
            code="""def somme_longueurs(mots):
    total = 0
    for mot in mots:
        if mot:
            total += mot
    return total""",
            nb_erreurs=1,
            erreur_python="TypeError: unsupported operand type(s) for +=: 'int' and 'str'",
        ),
    ]
    return [{'content': _fmt(t['description'], t['code'],
                              t.get('nb_erreurs', 2), t.get('erreur_python'))}
            for t in templates]


# ── Niveau 4 : double boucle for, 2-3 erreurs ────────────────────────────────

def gen_niveau4():
    n    = random.randint(3, 4)
    mat  = [[random.randint(1, 6) for _ in range(3)] for _ in range(3)]
    lst1 = [random.randint(1, 5) for _ in range(3)]
    lst2 = [random.randint(1, 5) for _ in range(3)]

    templates = [
        # ── 3 erreurs : range(liste), = au lieu de +=, initialisation ──
        dict(
            description="calculer la somme de tous les éléments d'une matrice",
            code="""def somme_matrice(matrice):
    total = 1
    for i in range(matrice):
        for j in range(len(matrice[i])):
            total = matrice[i][j]
    return total""",
            nb_erreurs=3,
        ),
        # ── 2 erreurs : range commence à 0 sur i et j ──
        dict(
            description="construire la table de multiplication de 1 à \\texttt{n}",
            code=f"""def table_mult(n):
    resultat = []
    for i in range(n + 1):
        ligne = []
        for j in range(n + 1):
            ligne.append(i * j)
        resultat.append(ligne)
    return resultat""",
            nb_erreurs=2,
        ),
        # ── 3 erreurs : range(liste), + au lieu de *, = au lieu de += ──
        dict(
            description="calculer le produit scalaire de deux listes de même taille",
            code="""def produit_scalaire(l1, l2):
    total = 0
    for i in range(l1):
        total = l1[i] + l2[i]
    return total""",
            nb_erreurs=3,
        ),
        # ── 2 erreurs : valeurs 0 et 1 inversées dans la matrice identité ──
        dict(
            description="construire une matrice identité de taille \\texttt{n}×\\texttt{n}",
            code="""def matrice_identite(n):
    mat = []
    for i in range(n):
        ligne = []
        for j in range(n):
            if i == j:
                ligne.append(0)
            else:
                ligne.append(1)
        mat.append(ligne)
    return mat""",
            nb_erreurs=2,
        ),
        # ── 2 erreurs : condition i==j au lieu de i<j + indices au lieu de valeurs ──
        dict(
            description="renvoyer tous les couples (a, b) d'une liste tels que a < b",
            code="""def couples_croissants(liste):
    resultat = []
    for i in range(len(liste)):
        for j in range(len(liste)):
            if i == j:
                resultat.append((liste[i], liste[j]))
    return resultat""",
            nb_erreurs=2,
        ),
        # ── 3 erreurs : range(mat), += x impossible, condition inversée ──
        dict(
            description="aplatir une matrice en ne gardant que les éléments positifs",
            code="""def aplatir_positifs(matrice):
    resultat = []
    for ligne in range(matrice):
        for x in ligne:
            if x <= 0:
                resultat += x
    return resultat""",
            nb_erreurs=3,
        ),
        # ── 2 erreurs : range interne utilise len(matrice) au lieu de len(ligne), init à 0 ──
        dict(
            description="trouver le plus grand élément d'une matrice (sans \\texttt{max})",
            code="""def max_matrice(matrice):
    maxi = 0
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if matrice[i][j] > maxi:
                maxi = matrice[i][j]
    return maxi""",
            nb_erreurs=2,
        ),
        # ── 2 erreurs : range(ligne) et append(ligne) au lieu de append(x) ──
        dict(
            description="renvoyer la liste aplatie d'une matrice (liste de listes)",
            code="""def aplatir(matrice):
    resultat = []
    for ligne in matrice:
        for x in range(ligne):
            resultat.append(ligne)
    return resultat""",
            nb_erreurs=2,
        ),
        # ── 2 erreurs : initialisation à 1 et = au lieu de += ──
        dict(
            description="calculer la somme des éléments de la diagonale d'une matrice carrée",
            code="""def somme_diagonale(matrice):
    total = 1
    n = len(matrice)
    for i in range(n):
        for j in range(n):
            if i == j:
                total = matrice[i][j]
    return total""",
            nb_erreurs=2,
        ),
    ]
    return [{'content': _fmt(t['description'], t['code'],
                              t.get('nb_erreurs', 2), t.get('erreur_python'))}
            for t in templates]


# ── Niveau 5 : code complexe, 3 erreurs ──────────────────────────────────────

def gen_niveau5():
    lst = [random.randint(1, 15) for _ in range(6)]
    mat = [[random.randint(1, 9) for _ in range(3)] for _ in range(3)]

    templates = [
        # ── Tri par sélection : condition > au lieu de <, return coupe le premier ──
        dict(
            description="trier une liste par ordre croissant (tri par sélection)",
            code="""def tri_selection(liste):
    for i in range(len(liste) - 1):
        idx_min = i
        for j in range(i, len(liste)):
            if liste[j] > liste[idx_min]:
                idx_min = j
        liste[i], liste[idx_min] = liste[idx_min], liste[i]
    return liste[1:]""",
            nb_erreurs=3,
        ),
        # ── Fusion de deux listes triées : indices commencent à 1, reste non ajouté ──
        dict(
            description="fusionner deux listes triées en une seule liste triée",
            code="""def fusionner(l1, l2):
    resultat = []
    i, j = 1, 1
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            resultat.append(l1[i])
            i += 1
        else:
            resultat.append(l2[j])
            j += 1
    return resultat""",
            nb_erreurs=3,
        ),
        # ── Comptage dans matrice : init à 1, condition inversée, range carré supposé ──
        dict(
            description="renvoyer le nombre de fois qu'une valeur apparaît dans une matrice",
            code="""def compter_valeur(matrice, val):
    compteur = 1
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if matrice[i][j] != val:
                compteur += 1
    return compteur""",
            nb_erreurs=3,
        ),
        # ── Minimums par ligne : range(matrice), resultat = mini, mini mal réinitialisé ──
        dict(
            description="renvoyer la liste des minimums de chaque ligne d'une matrice",
            code="""def mins_lignes(matrice):
    resultat = []
    for ligne in range(matrice):
        mini = ligne[0]
        for x in ligne:
            if x < mini:
                mini = x
        resultat = mini
    return resultat""",
            nb_erreurs=3,
        ),
        # ── Transposition : matrice[j][i] au lieu de matrice[i][j] ──
        dict(
            description="calculer la transposée d'une matrice (les lignes deviennent des colonnes)",
            code="""def transposer(matrice):
    n = len(matrice)
    m = len(matrice[0])
    resultat = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            resultat[j][i] = matrice[j][i]
    return resultat""",
            nb_erreurs=3,
        ),
    ]
    return [{'content': _fmt(t['description'], t['code'],
                              t.get('nb_erreurs', 3), t.get('erreur_python'))}
            for t in templates]
