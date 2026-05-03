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
    return [generators[niveau]() for _ in range(count)]


# ── Formateur LaTeX ───────────────────────────────────────────────────────────

def _fmt(description, code, appel, attendu, obtenu, nb_erreurs):
    """Formate un exercice de débogage en LaTeX."""
    n_str  = "une erreur"  if nb_erreurs == 1 else f"{nb_erreurs} erreurs"
    l_str  = "l'erreur"    if nb_erreurs == 1 else "les erreurs"

    parts = [
        f"La fonction suivante est censée \\textbf{{{description}}}, "
        f"mais elle contient \\textbf{{{n_str}}}.",
        "",
        "\\begin{lstlisting}",
        code,
        "\\end{lstlisting}",
        "",
        f"\\textbf{{Exemple :}} \\texttt{{{appel}}} renvoie \\texttt{{{obtenu}}} "
        f"alors qu'elle devrait renvoyer \\texttt{{{attendu}}}.",
        "",
        f"\\textbf{{a) Identifiez et expliquez {l_str} :}}",
        "",
    ]
    for _ in range(nb_erreurs):
        parts += ["\\cadreligne", ""]
    parts += [
        "\\textbf{b) Réécrivez la version corrigée :}",
        "",
        "\\fbox{\\parbox{14cm}{\\rule{0pt}{4.5cm}}}",
    ]
    return "\n".join(parts)


# ── Niveau 1 : code if/else, 1 erreur ────────────────────────────────────────

def gen_niveau1():
    a  = random.randint(5, 15)
    b  = random.randint(2, 6)
    pair   = random.randint(1, 8) * 2
    impair = random.randint(1, 8) * 2 + 1

    templates = [
        # ── Logique : condition ou retour inversé ──
        dict(
            description="renvoyer \\texttt{True} si \\texttt{n} est pair, \\texttt{False} sinon",
            code="""def est_pair(n):
    if n % 2 == 1:
        return True
    else:
        return False""",
            appel=f"est\\_pair({pair})", attendu="True", obtenu="False",
        ),
        dict(
            description="renvoyer le maximum de deux nombres",
            code="""def maximum(a, b):
    if a > b:
        return b
    else:
        return a""",
            appel=f"maximum({a}, {b})", attendu=str(max(a, b)), obtenu=str(min(a, b)),
        ),
        dict(
            description="renvoyer le minimum de deux nombres",
            code="""def minimum(a, b):
    if a < b:
        return b
    else:
        return a""",
            appel=f"minimum({a}, {b})", attendu=str(min(a, b)), obtenu=str(max(a, b)),
        ),
        dict(
            description="calculer la valeur absolue de \\texttt{x} (sans utiliser \\texttt{abs})",
            code="""def valeur_absolue(x):
    if x < 0:
        return x
    else:
        return -x""",
            appel=f"valeur\\_absolue({-a})", attendu=str(a), obtenu=str(-a),
        ),
        dict(
            description="renvoyer \\texttt{True} si \\texttt{a} et \\texttt{b} sont égaux",
            code="""def sont_egaux(a, b):
    if a > b:
        return True
    else:
        return False""",
            appel=f"sont\\_egaux({a}, {a})", attendu="True", obtenu="False",
        ),
        dict(
            description="renvoyer \\texttt{True} si la liste est vide, \\texttt{False} sinon",
            code="""def est_vide(liste):
    if len(liste) > 0:
        return True
    else:
        return False""",
            appel="est\\_vide([])", attendu="True", obtenu="False",
        ),
        dict(
            description="renvoyer \\texttt{True} si \\texttt{n} est impair, \\texttt{False} sinon",
            code="""def est_impair(n):
    if n % 2 == 0:
        return True
    else:
        return False""",
            appel=f"est\\_impair({impair})", attendu="True", obtenu="False",
        ),
        dict(
            description="renvoyer \\texttt{True} si \\texttt{n} est divisible par \\texttt{d}",
            code="""def est_divisible(n, d):
    if n % d != 0:
        return True
    else:
        return False""",
            appel=f"est\\_divisible({b * 3}, {b})", attendu="True", obtenu="False",
        ),
        dict(
            description="calculer la différence \\texttt{a - b}",
            code="""def difference(a, b):
    return a + b""",
            appel=f"difference({a}, {b})", attendu=str(a - b), obtenu=str(a + b),
        ),
        dict(
            description="calculer le carré de \\texttt{n}",
            code="""def carre(n):
    return n * 2""",
            appel=f"carre({b + 1})", attendu=str((b + 1) ** 2), obtenu=str((b + 1) * 2),
        ),
        dict(
            description="calculer le produit de \\texttt{a} et \\texttt{b}",
            code="""def produit(a, b):
    return a + b""",
            appel=f"produit({a}, {b})", attendu=str(a * b), obtenu=str(a + b),
        ),
        # ── Cas limite : mauvaise borne ou cas manqué ──
        dict(
            description="renvoyer \\texttt{True} si \\texttt{x} est strictement positif",
            code="""def est_positif(x):
    if x >= 0:
        return True
    else:
        return False""",
            appel="est\\_positif(0)", attendu="False", obtenu="True",
        ),
        dict(
            description="renvoyer \\texttt{True} si \\texttt{x} est strictement négatif",
            code="""def est_negatif(x):
    if x <= 0:
        return True
    else:
        return False""",
            appel="est\\_negatif(0)", attendu="False", obtenu="True",
        ),
        dict(
            description="renvoyer \\texttt{True} si \\texttt{a} est strictement supérieur à \\texttt{b}",
            code="""def strictement_superieur(a, b):
    if a >= b:
        return True
    else:
        return False""",
            appel=f"strictement\\_superieur({a}, {a})", attendu="False", obtenu="True",
        ),
        dict(
            description="renvoyer \\texttt{True} si le mot commence par une voyelle (a, e, i, o, u ou y)",
            code="""def commence_par_voyelle(mot):
    if mot[0] in 'aeiou':
        return True
    else:
        return False""",
            appel="commence\\_par\\_voyelle('yeux')", attendu="True", obtenu="False",
        ),
        # ── Erreur courante : mauvaise opération ou variable ──
        dict(
            description="renvoyer l'opposé de \\texttt{n}",
            code="""def oppose(n):
    return n""",
            appel=f"oppose({a})", attendu=str(-a), obtenu=str(a),
        ),
        dict(
            description="convertir un mot en minuscules",
            code="""def en_minuscules(mot):
    return mot.upper()""",
            appel="en\\_minuscules('PYTHON')", attendu="'python'", obtenu="'PYTHON'",
        ),
        dict(
            description="renvoyer le reste de la division de \\texttt{a} par \\texttt{b}",
            code="""def reste(a, b):
    return a // b""",
            appel=f"reste({a}, {b})", attendu=str(a % b), obtenu=str(a // b),
        ),
        dict(
            description="calculer la somme de \\texttt{a} et \\texttt{b}",
            code="""def somme(a, b):
    return a * b""",
            appel=f"somme({a}, {b})", attendu=str(a + b), obtenu=str(a * b),
        ),
        dict(
            description="renvoyer le premier caractère d'un mot",
            code="""def premier_caractere(mot):
    return mot[-1]""",
            appel="premier\\_caractere('python')", attendu="'p'", obtenu="'n'",
        ),
        dict(
            description="renvoyer le dernier caractère d'un mot",
            code="""def dernier_caractere(mot):
    return mot[0]""",
            appel="dernier\\_caractere('python')", attendu="'n'", obtenu="'p'",
        ),
        dict(
            description="renvoyer \\texttt{True} si un mot contient la lettre 'a'",
            code="""def contient_a(mot):
    if 'a' not in mot:
        return True
    else:
        return False""",
            appel="contient\\_a('chat')", attendu="True", obtenu="False",
        ),
        dict(
            description="renvoyer \\texttt{True} si deux mots ont la même longueur",
            code="""def meme_longueur(m1, m2):
    if len(m1) != len(m2):
        return True
    else:
        return False""",
            appel="meme\\_longueur('abc', 'xyz')", attendu="True", obtenu="False",
        ),
    ]
    t = random.choice(templates)
    return {'content': _fmt(t['description'], t['code'], t['appel'],
                            t['attendu'], t['obtenu'], t.get('nb_erreurs', 1))}


# ── Niveau 2 : boucle for (sans if), 1 erreur ────────────────────────────────

def gen_niveau2():
    n   = random.randint(4, 7)
    m   = random.randint(3, 5)
    c   = random.randint(2, 4)
    lst = [random.randint(1, 8) for _ in range(4)]
    mot = random.choice(['python', 'boucle', 'code', 'algo'])
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
            appel=f"somme\\_liste({lst})",
            attendu=str(sum(lst)),
            obtenu="une erreur \\texttt{TypeError} (\\texttt{range()} attend un entier, pas une liste)",
        ),
        dict(
            description="renvoyer une liste où chaque élément est doublé",
            code="""def doubler(liste):
    resultat = []
    for i in range(liste):
        resultat.append(liste[i] * 2)
    return resultat""",
            appel=f"doubler({petite})",
            attendu=str([x * 2 for x in petite]),
            obtenu="une erreur \\texttt{TypeError}",
        ),
        # ── Cas limite : range(n) au lieu de range(1, n+1) ──
        dict(
            description=f"calculer la somme des entiers de 1 à \\texttt{{n}}",
            code="""def somme_n(n):
    total = 0
    for i in range(n):
        total += i
    return total""",
            appel=f"somme\\_n({m})",
            attendu=str(sum(range(1, m + 1))),
            obtenu=str(sum(range(m))),
        ),
        dict(
            description="renvoyer la liste des entiers de 1 à \\texttt{n}",
            code="""def liste_entiers(n):
    resultat = []
    for i in range(n):
        resultat.append(i)
    return resultat""",
            appel=f"liste\\_entiers({m})",
            attendu=str(list(range(1, m + 1))),
            obtenu=str(list(range(m))),
        ),
        # ── Cas limite : range(len - 1) oublie le dernier élément ──
        dict(
            description="calculer la somme de tous les éléments d'une liste",
            code="""def somme_liste(liste):
    total = 0
    for i in range(len(liste) - 1):
        total += liste[i]
    return total""",
            appel=f"somme\\_liste({lst})",
            attendu=str(sum(lst)),
            obtenu=str(sum(lst[:-1])),
        ),
        dict(
            description="inverser une chaîne de caractères",
            code="""def inverser(texte):
    resultat = ""
    for i in range(1, len(texte)):
        resultat = texte[i] + resultat
    return resultat""",
            appel=f"inverser('{mot}')",
            attendu=f"'{mot[::-1]}'",
            obtenu=f"'{mot[1:][::-1]}'",
        ),
        # ── Logique : initialisation incorrecte ──
        dict(
            description="compter le nombre d'éléments dans une liste",
            code="""def compter(liste):
    compteur = 1
    for x in liste:
        compteur += 1
    return compteur""",
            appel=f"compter({lst})",
            attendu=str(len(lst)),
            obtenu=str(len(lst) + 1),
        ),
        dict(
            description=f"calculer le produit de tous les éléments d'une liste",
            code="""def produit_liste(liste):
    resultat = 0
    for x in liste:
        resultat *= x
    return resultat""",
            appel=f"produit\\_liste({petite})",
            attendu=str(petite[0] * petite[1] * petite[2]),
            obtenu="0",
        ),
        # ── Logique : = au lieu de += ──
        dict(
            description=f"calculer la somme des carrés des entiers de 1 à \\texttt{{n}}",
            code="""def somme_carres(n):
    total = 0
    for i in range(1, n + 1):
        total = i ** 2
    return total""",
            appel=f"somme\\_carres({m})",
            attendu=str(sum(i ** 2 for i in range(1, m + 1))),
            obtenu=str(m ** 2),
        ),
        # ── Erreur courante : mauvaise variable dans l'accumulateur ──
        dict(
            description="construire la liste des puissances de 2 de $2^0$ à $2^{n-1}$",
            code="""def puissances(n):
    resultat = []
    for i in range(n):
        resultat.append(n ** i)
    return resultat""",
            appel=f"puissances({m})",
            attendu=str([2 ** i for i in range(m)]),
            obtenu=str([m ** i for i in range(m)]),
        ),
        dict(
            description="construire la liste des multiples de \\texttt{k} de 1 à \\texttt{n}",
            code=f"""def multiples(n, k):
    resultat = []
    for i in range(1, n + 1):
        resultat.append(i)
    return resultat""",
            appel=f"multiples({m}, {c})",
            attendu=str([i * c for i in range(1, m + 1)]),
            obtenu=str(list(range(1, m + 1))),
        ),
        # ── Cas limite : range(n+1) fait une itération de trop ──
        dict(
            description=f"calculer $n!$ (la factorielle de \\texttt{{n}})",
            code="""def factorielle(n):
    resultat = 1
    for i in range(n + 1):
        resultat *= i
    return resultat""",
            appel=f"factorielle({m})",
            attendu=str(__import__('math').factorial(m)),
            obtenu="0",
        ),
        # ── Erreur courante : n'utilise pas la variable de boucle ──
        dict(
            description="renvoyer la liste des indices d'une autre liste",
            code="""def indices(liste):
    resultat = []
    for i in range(len(liste)):
        resultat.append(liste[i])
    return resultat""",
            appel=f"indices({petite})",
            attendu=str(list(range(len(petite)))),
            obtenu=str(petite),
        ),
        # ── Logique : mauvais sens dans la concaténation ──
        dict(
            description="construire une chaîne qui répète chaque lettre deux fois",
            code="""def repeter_lettres(mot):
    resultat = ""
    for c in mot:
        resultat = c * 2 + resultat
    return resultat""",
            appel=f"repeter\\_lettres('{mot[:3]}')",
            attendu="".join(c * 2 for c in mot[:3]),
            obtenu="".join(c * 2 for c in reversed(mot[:3])),
        ),
        # ── Erreur courante : boucle sur les indices mais avec mauvaise variable ──
        dict(
            description="calculer la somme des éléments d'une liste en utilisant les indices",
            code="""def somme_indices(liste):
    total = 0
    for i in range(len(liste)):
        total += i
    return total""",
            appel=f"somme\\_indices({lst})",
            attendu=str(sum(lst)),
            obtenu=str(sum(range(len(lst)))),
        ),
    ]
    t = random.choice(templates)
    return {'content': _fmt(t['description'], t['code'], t['appel'],
                            t['attendu'], t['obtenu'], t.get('nb_erreurs', 1))}


# ── Niveau 3 : for + if, 2 erreurs ───────────────────────────────────────────

def gen_niveau3():
    lst_mix = [random.randint(-5, 8) for _ in range(5)]
    lst_int = [random.randint(1, 12) for _ in range(5)]
    seuil   = random.randint(3, 7)
    c       = random.randint(2, 4)
    mot     = random.choice(['programmation', 'algorithme', 'boucle', 'variable'])

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
            appel=f"compter\_positifs({lst_mix})",
            attendu=str(sum(1 for x in lst_mix if x > 0)),
            obtenu="une erreur \\texttt{TypeError} (de plus, la condition \\texttt{>= 0} compte aussi le zéro)",
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
            appel=f"compter\_pairs({lst_int})",
            attendu=str(sum(1 for x in lst_int if x % 2 == 0)),
            obtenu=str(1 + sum(1 for x in lst_int if x % 2 == 1)),
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
            appel=f"somme\_superieurs({lst_int}, {seuil})",
            attendu=str(sum(x for x in lst_int if x > seuil)),
            obtenu=f"seulement le dernier élément trouvé > {seuil} (= au lieu de +=, et dernier élément manqué)",
            nb_erreurs=2,
        ),
        # ── range(n) au lieu de range(1,n+1) + condition manque 0 ──
        dict(
            description="renvoyer la liste des entiers de 1 à \\texttt{n} qui sont des multiples de \\texttt{k}",
            code=f"""def multiples(n, k):
    resultat = []
    for i in range(n):
        if i % k == 0:
            resultat.append(i)
    return resultat""",
            appel=f"multiples({c * 4}, {c})",
            attendu=str([i for i in range(1, c * 4 + 1) if i % c == 0]),
            obtenu=str([i for i in range(c * 4) if i % c == 0]),
            nb_erreurs=2,
        ),
        # ── mauvaise condition voyelle + mauvaise variable dans append ──
        dict(
            description="renvoyer la liste des voyelles présentes dans un mot",
            code="""def lister_voyelles(mot):
    resultat = []
    for i in range(len(mot)):
        if mot[i] in 'aeiou':
            resultat.append(i)
    return resultat""",
            appel=f"lister\_voyelles('{mot[:5]}')",
            attendu=str([c for c in mot[:5] if c in 'aeiouy']),
            obtenu=str([i for i, c in enumerate(mot[:5]) if c in 'aeiou']),
            nb_erreurs=2,
        ),
        # ── condition inversée + mauvais sens de construction ──
        dict(
            description="renvoyer une liste avec uniquement les éléments négatifs d'une liste",
            code="""def garder_negatifs(liste):
    resultat = []
    for x in liste:
        if x > 0:
            resultat.append(x)
    return resultat""",
            appel=f"garder\_negatifs({lst_mix})",
            attendu=str([x for x in lst_mix if x < 0]),
            obtenu=str([x for x in lst_mix if x > 0]),
            nb_erreurs=1,
        ),
        # ── two logic bugs: wrong init + wrong condition ──
        dict(
            description="renvoyer le plus petit élément d'une liste (sans utiliser \\texttt{min})",
            code="""def trouver_min(liste):
    mini = 0
    for x in liste:
        if x > mini:
            mini = x
    return mini""",
            appel=f"trouver\_min({lst_int})",
            attendu=str(min(lst_int)),
            obtenu=f"le maximum de la liste (initialisation à 0 et condition inversée)",
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
            appel=f"somme\_pairs({lst_int})",
            attendu=str(sum(x for x in lst_int if x % 2 == 0)),
            obtenu="une erreur \\texttt{TypeError} (de plus, \\texttt{=} au lieu de \\texttt{+=})",
            nb_erreurs=2,
        ),
        # ── mauvaise comparaison de chaîne + mauvaise variable ──
        dict(
            description="compter le nombre de voyelles dans un mot",
            code="""def compter_voyelles(mot):
    compteur = 0
    for i in range(len(mot)):
        if i in 'aeiouy':
            compteur += 1
    return compteur""",
            appel=f"compter\_voyelles('{mot}')",
            attendu=str(sum(1 for c in mot if c in 'aeiouy')),
            obtenu="0 (on compare un indice entier à une chaîne, jamais vrai)",
            nb_erreurs=2,
        ),
        # ── missing else branch + wrong comparison ──
        dict(
            description="renvoyer la liste des éléments remplacés par 0 s'ils sont négatifs, "
                        "inchangés sinon",
            code="""def remplacer_negatifs(liste):
    resultat = []
    for x in liste:
        if x <= 0:
            resultat.append(0)
    return resultat""",
            appel=f"remplacer\_negatifs({lst_mix})",
            attendu=str([0 if x < 0 else x for x in lst_mix]),
            obtenu="une liste incomplète (pas d'\\texttt{else}, et \\texttt{<= 0} inclut le zéro)",
            nb_erreurs=2,
        ),
        # ── wrong dict iteration + wrong condition ──
        dict(
            description="renvoyer la liste des élèves ayant une note supérieure ou égale à 10",
            code="""def eleves_reussite(notes):
    resultat = []
    for note in notes:
        if note >= 10:
            resultat.append(note)
    return resultat""",
            appel="eleves\_reussite({'Alice': 15, 'Bob': 8, 'Charlie': 12})",
            attendu="['Alice', 'Charlie']",
            obtenu="[15, 12] (on itère sur les valeurs, pas les clés)",
            nb_erreurs=2,
        ),
    ]
    t = random.choice(templates)
    nb = t.get('nb_erreurs', 2)
    return {'content': _fmt(t['description'], t['code'], t['appel'],
                            t['attendu'], t['obtenu'], nb)}


# ── Niveau 4 : double boucle for, 2-3 erreurs ────────────────────────────────

def gen_niveau4():
    n   = random.randint(3, 4)
    mat = [[random.randint(1, 6) for _ in range(3)] for _ in range(3)]
    c   = random.randint(2, 4)
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
            appel=f"somme\_matrice({mat})",
            attendu=str(sum(x for row in mat for x in row)),
            obtenu="une erreur \\texttt{TypeError} (et deux autres erreurs dans le code)",
            nb_erreurs=3,
        ),
        # ── 2 erreurs : range(len) au lieu de range(len-1), mauvaise condition ──
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
            appel=f"table\_mult({n})",
            attendu=f"une matrice {n}×{n} dont l'élément [i][j] vaut (i+1)*(j+1)",
            obtenu=f"une matrice {n+1}×{n+1} incluant une ligne et colonne de zéros (range commence à 0)",
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
            appel=f"produit_scalaire({lst1}, {lst2})",
            attendu=str(sum(a * b for a, b in zip(lst1, lst2))),
            obtenu="une erreur \\texttt{TypeError} (et deux autres erreurs dans le code)",
            nb_erreurs=3,
        ),
        # ── 2 erreurs : matrice identité (mauvaise branche + mauvais else) ──
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
            appel=f"matrice_identite({n})",
            attendu=str([[1 if i == j else 0 for j in range(n)] for i in range(n)]),
            obtenu=str([[0 if i == j else 1 for j in range(n)] for i in range(n)]),
            nb_erreurs=2,
        ),
        # ── 2 erreurs : condition i==j au lieu de i<j + mauvais append ──
        dict(
            description="renvoyer tous les couples (a, b) d'une liste tels que a < b",
            code="""def couples_croissants(liste):
    resultat = []
    for i in range(len(liste)):
        for j in range(len(liste)):
            if i == j:
                resultat.append((liste[i], liste[j]))
    return resultat""",
            appel=f"couples_croissants({lst1})",
            attendu=str([(lst1[i], lst1[j]) for i in range(len(lst1)) for j in range(len(lst1)) if lst1[i] < lst1[j]]),
            obtenu="les couples (x, x) pour chaque élément (diagonale au lieu de triangle supérieur)",
            nb_erreurs=2,
        ),
        # ── 3 erreurs : range(mat) + += au lieu de append + condition inversée ──
        dict(
            description="aplatir une matrice en ne gardant que les éléments positifs",
            code="""def aplatir_positifs(matrice):
    resultat = []
    for ligne in range(matrice):
        for x in ligne:
            if x <= 0:
                resultat += x
    return resultat""",
            appel=f"aplatir_positifs({mat})",
            attendu=str([x for row in mat for x in row if x > 0]),
            obtenu="une erreur \\texttt{TypeError} (et deux autres erreurs dans le code)",
            nb_erreurs=3,
        ),
        # ── 2 erreurs : mauvais range interne + = instead of max update ──
        dict(
            description="trouver le plus grand élément d'une matrice (sans \\texttt{max})",
            code="""def max_matrice(matrice):
    maxi = 0
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if matrice[i][j] > maxi:
                maxi = matrice[i][j]
    return maxi""",
            appel=f"max_matrice({mat})",
            attendu=str(max(x for row in mat for x in row)),
            obtenu=f"peut planter avec \\texttt{{IndexError}} si les lignes ne sont pas carrées, "
                   f"et échoue si tous les éléments sont négatifs",
            nb_erreurs=2,
        ),
        # ── 2 erreurs : += liste au lieu d'append + range(liste) ──
        dict(
            description="renvoyer la liste aplatie d'une matrice (liste de listes)",
            code="""def aplatir(matrice):
    resultat = []
    for ligne in matrice:
        for x in range(ligne):
            resultat.append(ligne)
    return resultat""",
            appel=f"aplatir({mat[:2]})",
            attendu=str([x for row in mat[:2] for x in row]),
            obtenu="une erreur \\texttt{TypeError} (\\texttt{range(ligne)} et \\texttt{append(ligne)} incorrects)",
            nb_erreurs=2,
        ),
        # ── 3 erreurs: init, range, opérateur ──
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
            appel=f"somme_diagonale({mat})",
            attendu=str(sum(mat[i][i] for i in range(len(mat)))),
            obtenu=str(mat[-1][-1]),
            nb_erreurs=2,
        ),
    ]
    t = random.choice(templates)
    nb = t.get('nb_erreurs', 2)
    return {'content': _fmt(t['description'], t['code'], t['appel'],
                            t['attendu'], t['obtenu'], nb)}


# ── Niveau 5 : code complexe, 3 erreurs ──────────────────────────────────────

def gen_niveau5():
    lst = [random.randint(1, 15) for _ in range(6)]
    mat = [[random.randint(1, 9) for _ in range(3)] for _ in range(3)]
    mot = random.choice(['programmation', 'algorithme', 'informatique'])

    templates = [
        # ── Tri par sélection : 3 erreurs ──
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
            appel=f"tri_selection({lst[:4]})",
            attendu=str(sorted(lst[:4])),
            obtenu="une liste partiellement triée par ordre décroissant, sans le premier élément",
            nb_erreurs=3,
        ),
        # ── Inversion de chaîne + suppression voyelles : 3 erreurs ──
        dict(
            description="renvoyer un mot sans voyelles et inversé",
            code="""def transformer(mot):
    resultat = ""
    for i in range(mot):
        if mot[i] not in 'aeiouy':
            resultat = resultat + mot[i]
    return resultat""",
            appel=f"transformer('{mot[:6]}')",
            attendu=f"'{''.join(c for c in mot[:6] if c not in 'aeiouy')[::-1]}'",
            obtenu="une erreur \\texttt{TypeError} (et deux autres erreurs dans le code)",
            nb_erreurs=3,
        ),
        # ── Fusion de deux listes triées : 3 erreurs ──
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
            appel=f"fusionner({sorted(lst[:3])}, {sorted(lst[3:])})",
            attendu=str(sorted(lst)),
            obtenu="une liste incomplète : commence à l'indice 1, et n'ajoute pas les éléments restants",
            nb_erreurs=3,
        ),
        # ── Comptage dans matrice : 3 erreurs ──
        dict(
            description="renvoyer le nombre de fois qu'une valeur apparaît dans une matrice",
            code="""def compter_valeur(matrice, val):
    compteur = 1
    for i in range(len(matrice)):
        for j in range(len(matrice)):
            if matrice[i][j] != val:
                compteur += 1
    return compteur""",
            appel=f"compter_valeur({mat}, {mat[0][0]})",
            attendu=str(sum(row.count(mat[0][0]) for row in mat)),
            obtenu="valeur incorrecte : initialisation à 1, condition inversée, et range(matrice) "
                   "incorrect si lignes non carrées",
            nb_erreurs=3,
        ),
        # ── Recherche du minimum dans chaque ligne : 3 erreurs ──
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
            appel=f"mins_lignes({mat})",
            attendu=str([min(row) for row in mat]),
            obtenu="une erreur \\texttt{TypeError} (\\texttt{range(matrice)}, \\texttt{resultat = mini} "
                   "au lieu de \\texttt{append}, et \\texttt{mini} non réinitialisé correctement)",
            nb_erreurs=3,
        ),
        # ── Transposition de matrice : 3 erreurs ──
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
            appel="transposer([[1, 2, 3], [4, 5, 6]])",
            attendu="[[1, 4], [2, 5], [3, 6]]",
            obtenu="une IndexError ou des valeurs incorrectes : \\texttt{matrice[j][i]} au lieu de "
                   "\\texttt{matrice[i][j]}, et les dimensions \\texttt{n}/\\texttt{m} parfois inversées",
            nb_erreurs=3,
        ),
    ]
    t = random.choice(templates)
    nb = t.get('nb_erreurs', 3)
    return {'content': _fmt(t['description'], t['code'], t['appel'],
                            t['attendu'], t['obtenu'], nb)}
