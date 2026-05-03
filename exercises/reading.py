import random
import string


def generate_exercises(niveau, count=5):
    """Génère des exercices de lecture de code"""
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
    """Code simple avec un if"""
    noms = ['mystere', 'calcul', 'secret', 'operation', 'test', 'enigme', 'traiter', 'evaluer', 'appliquer', 'transformer']
    nom = random.choice(noms)

    a = random.randint(5, 20)
    b = random.randint(5, 20)
    while b == a:
        b = random.randint(5, 20)
    c = random.randint(2, 8)
    while c == a or c == b:
        c = random.randint(2, 8)
    opérateurs = ['+', '-', '*', '**', '//', '%']
    op1 = random.choice(opérateurs)
    opérateurs_copy = opérateurs.copy()
    opérateurs_copy.remove(op1)
    op2 = random.choice(opérateurs_copy)
    opérateurs_copy2 = opérateurs.copy()
    if op1 in opérateurs_copy2:
        opérateurs_copy2.remove(op1)
    if op2 in opérateurs_copy2:
        opérateurs_copy2.remove(op2)
    op3 = random.choice(opérateurs_copy2) if opérateurs_copy2 else random.choice(opérateurs)

    cmp = random.choice(['>', '<', '==', '!=', '>=', '<='])
    cmp2 = random.choice(['>', '<', '==', '!=', '>=', '<='])
    s1 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(4, 5)))
    s2 = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(random.randint(7, 10)))
    s3 = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(3, 6)))
    b1 = random.choice([True, False])
    b2 = not b1

    templates = [
        {
            'code': f"""def {nom}(x):
    if x > {a}:
        return x {op1} 2
    else:
        return x {op2} {b}""",
            'question': f"Que renvoie \\texttt{{{nom}({a - 2})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}} \\ Et \\texttt{{{nom}({a + 3})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        {
            'code': f"""def {nom}(mot):
    if len(mot) > {c}:
        return mot[0]
    else:
        return mot[-1]""",
            'question': f"Que renvoie \\texttt{{{nom}('{s3}')}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}} \\ Et \\texttt{{{nom}('{s1}')}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        {
            'code': f"""def {nom}(x, y):
    if x {cmp} y:
        return x {op1} y
    else:
        return y {op2} x""",
            'question': f"Que renvoie \\texttt{{{nom}({a}, {b})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}} \\ Et \\texttt{{{nom}({b}, {a})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        {
            'code': f"""def {nom}(n):
    if n % {c} == 0:
        return n {op1} {c}
    else:
        return n {op2} {b}""",
            'question': f"Que renvoie \\texttt{{{nom}({c * 3})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}} \\ Et \\texttt{{{nom}({c * 3 + 1})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        {
            'code': f"""def {nom}(x):
    if x {op1} {c} {cmp} {a}:
        return x {op2} {c}
    else:
        return x {op3} {b}""",
            'question': f"Que renvoie \\texttt{{{nom}({a + 2})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}} \\ Et \\texttt{{{nom}({c})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        {
            'code': f"""def {nom}(x):
    if x {cmp} {a}:
        return {b1}
    else:
        return {b2}""",
            'question': f"Que renvoie \\texttt{{{nom}({a - 1})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}} \\ Et \\texttt{{{nom}({a + 1})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        {
            'code': f"""def {nom}(x, y):
    if x + y {cmp} {a + b}:
        return (x + y) {op1} {c}
    else:
        return x {op2} y""",
            'question': f"Que renvoie \\texttt{{{nom}({a}, {b})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}} \\ Et \\texttt{{{nom}({c}, {c})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        {
            'code': f"""def {nom}(n):
    if n {cmp} {a}:
        return n {op1} n
    else:
        return n {op2} {c}""",
            'question': f"Que renvoie \\texttt{{{nom}({a - 2})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}} \\ Et \\texttt{{{nom}({a + 3})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        {
            'code': f"""def {nom}(x, y):
    if x {op1} y {cmp} {a}:
        return x {op2} {b}
    else:
        return y {op3} {c}""",
            'question': f"Que renvoie \\texttt{{{nom}({c}, {c})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}} \\ Et \\texttt{{{nom}({a}, {b})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        {
            'code': f"""def {nom}(n):
    if n {cmp} {a}:
        return n {op1} {c}
    else:
        return n {op2} {b}""",
            'question': f"Que renvoie \\texttt{{{nom}({a - 3})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}} \\ Et \\texttt{{{nom}({a + 2})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        {
            'code': f"""def {nom}(mot, n):
    if n {cmp} len(mot):
        return mot[:n]
    else:
        return mot[n:]""",
            'question': f"Que renvoie \\texttt{{{nom}('{s2}', {c})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}} \\ Et \\texttt{{{nom}('{s1}', {a})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        {
            'code': f"""def {nom}(a, b):
    if a {cmp} b:
        return a {op1} {c}
    else:
        return b {op2} {c}""",
            'question': f"Que renvoie \\texttt{{{nom}({a}, {b})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}} \\ Et \\texttt{{{nom}({b}, {a})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        {
            'code': f"""def {nom}(n):
    if n % {c} {cmp2} 0:
        return n {op1} {b}
    else:
        return n {op2} {a}""",
            'question': f"Que renvoie \\texttt{{{nom}({c * 2})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}} \\ Et \\texttt{{{nom}({c * 2 + 1})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        {
            'code': f"""def {nom}(x, y):
    if x {op1} {c} {cmp} y {op2} {c}:
        return x {op3} y
    else:
        return y {op1} x""",
            'question': f"Que renvoie \\texttt{{{nom}({a}, {b})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}} \\ Et \\texttt{{{nom}({c}, {c})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
    ]

    template = random.choice(templates)
    content = f"\\begin{{lstlisting}}\n{template['code']}\n\\end{{lstlisting}}\n\n{template['question']}"
    return {'content': content}


def generate_niveau2():
    """Code avec une boucle for"""
    noms = ['mystere', 'calcul', 'secret', 'operation', 'test', 'enigme', 'traiter', 'evaluer', 'appliquer', 'transformer']
    nom = random.choice(noms)

    n = random.randint(4, 8)
    m = random.randint(3, 6)
    c = random.randint(2, 5)
    mult = random.randint(2, 4)

    opérateurs = ['+', '-', '*', '//', '%']
    op1 = random.choice(['+', '-', '*'])

    s2 = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(3, 5)))
    mots = ['PYTHON', 'ALGO', 'BOUCLE', 'CODE', 'NSI']
    mot = random.choice(mots)

    petite_liste = [random.randint(1, 4) for _ in range(3)]
    liste_entiers = [random.randint(1, 10) for _ in range(random.randint(4, 5))]

    templates = [
        {
            'code': f"""def {nom}(n):
    resultat = 0
    for i in range(n):
        resultat += i * {mult}
    return resultat""",
            'question': f"Que renvoie \\texttt{{{nom}({n})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        {
            'code': f"""def {nom}(mot):
    resultat = ""
    for lettre in mot:
        resultat = lettre + resultat
    return resultat""",
            'question': f"Que renvoie \\texttt{{{nom}('{mot}')}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        {
            'code': f"""def {nom}(n):
    resultat = []
    for i in range(n):
        resultat.append(i {op1} {c})
    return resultat""",
            'question': f"Que renvoie \\texttt{{{nom}({m})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        {
            'code': f"""def {nom}(texte):
    resultat = ""
    for char in texte:
        resultat += char * {c}
    return resultat""",
            'question': f"Que renvoie \\texttt{{{nom}('{s2}')}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        {
            'code': f"""def {nom}(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** 2
    return total""",
            'question': f"Que renvoie \\texttt{{{nom}({m})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        {
            'code': f"""def {nom}(liste):
    resultat = 1
    for nombre in liste:
        resultat *= nombre
    return resultat""",
            'question': f"Que renvoie \\texttt{{{nom}({petite_liste})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        {
            'code': f"""def {nom}(n):
    resultat = 0
    for i in range(1, n + 1):
        resultat += i {op1} {c}
    return resultat""",
            'question': f"Que renvoie \\texttt{{{nom}({m})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        {
            'code': f"""def {nom}(n):
    resultat = []
    for i in range(n):
        resultat.append({c} ** i)
    return resultat""",
            'question': f"Que renvoie \\texttt{{{nom}({m})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        {
            'code': f"""def {nom}(liste):
    total = 0
    for x in liste:
        total += x
    return total""",
            'question': f"Que renvoie \\texttt{{{nom}({liste_entiers})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        {
            'code': f"""def {nom}(liste):
    resultat = []
    for x in liste:
        resultat.append(x * {mult})
    return resultat""",
            'question': f"Que renvoie \\texttt{{{nom}({liste_entiers[:3]})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        {
            'code': f"""def {nom}(mot):
    resultat = []
    for lettre in mot:
        resultat.append(lettre)
    return resultat""",
            'question': f"Que renvoie \\texttt{{{nom}('{s2}')}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        {
            'code': f"""def {nom}(n):
    resultat = 0
    for i in range(1, n + 1):
        resultat += i
    return resultat""",
            'question': f"Que renvoie \\texttt{{{nom}({n})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
    ]

    template = random.choice(templates)
    content = f"\\begin{{lstlisting}}\n{template['code']}\n\\end{{lstlisting}}\n\n{template['question']}"
    return {'content': content}


def generate_niveau3():
    """Code avec boucle for et if imbriqués"""
    noms = ['mystere', 'calcul', 'secret', 'operation', 'test', 'enigme', 'traiter', 'evaluer', 'appliquer', 'transformer']
    nom = random.choice(noms)

    lst_mix  = [random.randint(-8, 8) for _ in range(random.randint(4, 6))]
    lst_int  = [random.randint(1, 15) for _ in range(random.randint(4, 6))]
    seuil    = random.randint(3, 8)
    mult     = random.randint(2, 4)
    c        = random.randint(2, 5)
    n        = random.randint(8, 15)

    prenoms  = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
    random.shuffle(prenoms)
    dict_notes = {prenoms[i]: random.randint(5, 18) for i in range(4)}

    mots_src = ['python', 'algorithme', 'boucle', 'variable', 'fonction']
    mot      = random.choice(mots_src)

    templates = [
        # --- sur une liste, filtre dans nouvelle liste ---
        {
            'code': f"""def {nom}(liste):
    resultat = []
    for x in liste:
        if x > 0:
            resultat.append(x * {mult})
        else:
            resultat.append(x)
    return resultat""",
            'question': f"Que renvoie \\texttt{{{nom}({lst_mix})}} ? \\fbox{{\\parbox{{9cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        {
            'code': f"""def {nom}(liste):
    resultat = []
    for x in liste:
        if x >= {seuil}:
            resultat.append(x)
    return resultat""",
            'question': f"Que renvoie \\texttt{{{nom}({lst_int})}} ? \\fbox{{\\parbox{{9cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        {
            'code': f"""def {nom}(liste):
    total = 0
    for x in liste:
        if x % 2 == 0:
            total += x
    return total""",
            'question': f"Que renvoie \\texttt{{{nom}({lst_int})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        {
            'code': f"""def {nom}(liste):
    compteur = 0
    for x in liste:
        if x > {seuil}:
            compteur += 1
    return compteur""",
            'question': f"Que renvoie \\texttt{{{nom}({lst_int})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        {
            'code': f"""def {nom}(liste):
    resultat = []
    for x in liste:
        if x % {c} == 0:
            resultat.append(x)
        else:
            resultat.append(0)
    return resultat""",
            'question': f"Que renvoie \\texttt{{{nom}({lst_int})}} ? \\fbox{{\\parbox{{9cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        # --- avec range et if ---
        {
            'code': f"""def {nom}(n):
    resultat = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            resultat.append(i)
    return resultat""",
            'question': f"Que renvoie \\texttt{{{nom}({n})}} ? \\fbox{{\\parbox{{9cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        {
            'code': f"""def {nom}(n):
    total = 0
    for i in range(1, n + 1):
        if i % {c} == 0:
            total += i
    return total""",
            'question': f"Que renvoie \\texttt{{{nom}({n})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        {
            'code': f"""def {nom}(n):
    resultat = []
    for i in range(n):
        if i * i < n:
            resultat.append(i)
    return resultat""",
            'question': f"Que renvoie \\texttt{{{nom}({n})}} ? \\fbox{{\\parbox{{9cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        # --- sur un dictionnaire ---
        {
            'code': f"""def {nom}(dico):
    resultat = []
    for cle in dico:
        if dico[cle] >= 10:
            resultat.append(cle)
    return resultat""",
            'question': f"Que renvoie \\texttt{{{nom}({dict_notes})}} ? \\fbox{{\\parbox{{9cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        {
            'code': f"""def {nom}(dico):
    total = 0
    for cle in dico:
        if dico[cle] > {seuil}:
            total += dico[cle]
    return total""",
            'question': f"Que renvoie \\texttt{{{nom}({dict_notes})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        # --- premier élément trouvé ---
        {
            'code': f"""def {nom}(liste):
    for x in liste:
        if x > {seuil}:
            return x
    return None""",
            'question': f"Que renvoie \\texttt{{{nom}({lst_int})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        # --- liste avec remplacement conditionnel ---
        {
            'code': f"""def {nom}(liste):
    resultat = []
    for x in liste:
        if x < 0:
            resultat.append(0)
        else:
            resultat.append(x)
    return resultat""",
            'question': f"Que renvoie \\texttt{{{nom}({lst_mix})}} ? \\fbox{{\\parbox{{9cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
    ]

    template = random.choice(templates)
    content = f"\\begin{{lstlisting}}\n{template['code']}\n\\end{{lstlisting}}\n\n{template['question']}"
    return {'content': content}

def generate_niveau4():
    """Code avec deux boucles for imbriquées"""
    noms = ['mystere', 'calcul', 'secret', 'operation', 'test', 'enigme', 'traiter', 'evaluer', 'appliquer', 'transformer']
    nom = random.choice(noms)

    n    = random.randint(3, 4)
    c    = random.randint(2, 4)
    mat  = [[random.randint(1, 9) for _ in range(3)] for _ in range(3)]
    mat2 = [[random.randint(-5, 5) for _ in range(3)] for _ in range(3)]
    lst1 = [random.randint(1, 6) for _ in range(3)]
    lst2 = [random.randint(1, 6) for _ in range(3)]

    templates = [
        # --- double range ---
        {
            'code': f"""def {nom}(n):
    resultat = 0
    for i in range(n):
        for j in range(i):
            resultat += 1
    return resultat""",
            'question': f"Que renvoie \\texttt{{{nom}({n})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        {
            'code': f"""def {nom}(n):
    resultat = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            resultat.append(i * j)
    return resultat""",
            'question': f"Que renvoie \\texttt{{{nom}({min(n, 3)})}} ? \\fbox{{\\parbox{{9cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        # --- parcours de matrice sans if ---
        {
            'code': f"""def {nom}(matrice):
    total = 0
    for ligne in matrice:
        for x in ligne:
            total += x
    return total""",
            'question': f"Que renvoie \\texttt{{{nom}({mat})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        {
            'code': f"""def {nom}(matrice):
    resultat = []
    for ligne in matrice:
        for x in ligne:
            resultat.append(x)
    return resultat""",
            'question': f"Que renvoie \\texttt{{{nom}({mat[:2]})}} ? \\fbox{{\\parbox{{9cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        # --- construction de matrice ---
        {
            'code': f"""def {nom}(n):
    resultat = []
    for i in range(n):
        ligne = []
        for j in range(i + 1):
            ligne.append(j)
        resultat.append(ligne)
    return resultat""",
            'question': f"Que renvoie \\texttt{{{nom}({n})}} ? \\fbox{{\\parbox{{9cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        {
            'code': f"""def {nom}(n):
    resultat = []
    for i in range(n):
        ligne = []
        for j in range(n):
            ligne.append(i + j)
        resultat.append(ligne)
    return resultat""",
            'question': f"Que renvoie \\texttt{{{nom}({min(n, 3)})}} ? \\fbox{{\\parbox{{9cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        # --- parcours de matrice avec if ---
        {
            'code': f"""def {nom}(matrice):
    total = 0
    for ligne in matrice:
        for x in ligne:
            if x % 2 == 0:
                total += x
    return total""",
            'question': f"Que renvoie \\texttt{{{nom}({mat})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        {
            'code': f"""def {nom}(matrice):
    compteur = 0
    for ligne in matrice:
        for x in ligne:
            if x > {c}:
                compteur += 1
    return compteur""",
            'question': f"Que renvoie \\texttt{{{nom}({mat})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        {
            'code': f"""def {nom}(matrice):
    resultat = []
    for ligne in matrice:
        for x in ligne:
            if x > 0:
                resultat.append(x)
    return resultat""",
            'question': f"Que renvoie \\texttt{{{nom}({mat2})}} ? \\fbox{{\\parbox{{9cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        # --- produit cartésien / comparaison deux listes ---
        {
            'code': f"""def {nom}(liste1, liste2):
    resultat = []
    for a in liste1:
        for b in liste2:
            resultat.append(a + b)
    return resultat""",
            'question': f"Que renvoie \\texttt{{{nom}({lst1}, {lst2})}} ? \\fbox{{\\parbox{{9cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        {
            'code': f"""def {nom}(liste1, liste2):
    communs = []
    for a in liste1:
        for b in liste2:
            if a == b:
                communs.append(a)
    return communs""",
            'question': f"Que renvoie \\texttt{{{nom}({lst1}, {lst2})}} ? \\fbox{{\\parbox{{9cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
        # --- diagonale ---
        {
            'code': f"""def {nom}(matrice):
    total = 0
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if i == j:
                total += matrice[i][j]
    return total""",
            'question': f"Que renvoie \\texttt{{{nom}({mat})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}"
        },
    ]

    template = random.choice(templates)
    content = f"\\begin{{lstlisting}}\n{template['code']}\n\\end{{lstlisting}}\n\n{template['question']}"
    return {'content': content}

def generate_niveau5():
    """Code avec plusieurs structures imbriquées"""
    lst = [random.randint(1, 20) for _ in range(random.randint(6, 10))]
    
    templates = [
        {
            'code': f"""def fonction(liste):
    resultats = []
    for i in range(len(liste)):
        sous_liste = []
        for j in range(i, len(liste)):
            if liste[j] > liste[i]:
                sous_liste.append(liste[j])
        if len(sous_liste) > 0:
            resultats.append(max(sous_liste))
    return resultats""",
            'question': f"Que renvoie \\texttt{{fonction({lst})}} ?"
        },
        {
            'code': f"""def analyser(texte):
    mots = texte.split()
    resultats = {{}}
    for mot in mots:
        longueur = len(mot)
        if longueur not in resultats:
            resultats[longueur] = []
        resultats[longueur].append(mot)
    return resultats""",
            'question': "Que renvoie \\texttt{analyser('le chat mange la souris')} ?"
        }
    ]
    
    template = random.choice(templates)
    
    content = f"Analysez attentivement le code suivant et répondez à la question :\n\n\\begin{{lstlisting}}\n{template['code']}\n\\end{{lstlisting}}\n\n{template['question']}"
    
    return {'content': content}

def generate_niveau6():
    """Code complexe"""
    templates = [
        {
            'code': """def mystere(liste):
    n = len(liste)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if liste[j] < liste[min_idx]:
                min_idx = j
        liste[i], liste[min_idx] = liste[min_idx], liste[i]
    return liste""",
            'question': f"Que fait cette fonction ? Que renvoie \\texttt{{mystere([{', '.join(map(str, [random.randint(1, 30) for _ in range(6)]))}])}} ?"
        },
        {
            'code': """def fonction(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a""",
            'question': "Quelle suite mathématique cette fonction calcule-t-elle ? Que renvoie \\texttt{fonction(7)} ?"
        }
    ]
    
    template = random.choice(templates)
    
    content = f"Analysez le code suivant :\n\n\\begin{{lstlisting}}\n{template['code']}\n\\end{{lstlisting}}\n\n{template['question']}"
    
    return {'content': content}