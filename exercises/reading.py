import random
import string


# ── Helpers pour le corrigé ───────────────────────────────────────────────────

def _latex_tt(s):
    """Renvoie s encadré de \\texttt{} avec les caractères LaTeX spéciaux échappés."""
    s = str(s)
    s = s.replace('\\', '\\textbackslash{}')
    s = s.replace('{',  '\\{')
    s = s.replace('}',  '\\}')
    s = s.replace('%',  '\\%')
    s = s.replace('#',  '\\#')
    s = s.replace('&',  '\\&')
    s = s.replace('$',  '\\$')
    return f"\\texttt{{{s}}}"


def _compute_answer(code, appels):
    """Exécute le code Python et évalue chaque appel. Renvoie une chaîne LaTeX."""
    env = {}
    try:
        exec(code, env)
    except Exception:
        return " \\quad ".join(f"{_latex_tt(a)} $\\to$ ?" for a in appels)
    parts = []
    for appel in appels:
        try:
            val = eval(appel, env)
            parts.append(f"{_latex_tt(appel)} $\\to$ {_latex_tt(repr(val))}")
        except Exception:
            parts.append(f"{_latex_tt(appel)} $\\to$ ?")
    return " \\quad ".join(parts)


# ── Point d'entrée ────────────────────────────────────────────────────────────

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

    all_templates = generators[niveau]()
    return random.sample(all_templates, min(count, len(all_templates)))


# ── Niveau 1 : if/else simple ─────────────────────────────────────────────────

def generate_niveau1():
    """Code simple avec un if"""
    noms = ['mystere', 'calcul', 'secret', 'operation', 'test', 'enigme',
            'traiter', 'evaluer', 'appliquer', 'transformer']
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

    cmp  = random.choice(['>', '<', '==', '!=', '>=', '<='])
    cmp2 = random.choice(['>', '<', '==', '!=', '>=', '<='])
    s1 = ''.join(random.choice(string.ascii_uppercase + string.digits)
                 for _ in range(random.randint(4, 5)))
    s2 = ''.join(random.choice(string.ascii_uppercase + string.digits)
                 for _ in range(random.randint(7, 10)))
    s3 = ''.join(random.choice(string.ascii_lowercase)
                 for _ in range(random.randint(3, 6)))
    b1 = random.choice([True, False])
    b2 = not b1

    def _t(code, question, appels):
        return {'code': code, 'question': question,
                'answer': _compute_answer(code, appels)}

    templates = [
        _t(
            f"""def {nom}(x):
    if x > {a}:
        return x {op1} 2
    else:
        return x {op2} {b}""",
            f"Que renvoie \\texttt{{{nom}({a - 2})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}} \\ Et \\texttt{{{nom}({a + 3})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}({a - 2})", f"{nom}({a + 3})"],
        ),
        _t(
            f"""def {nom}(mot):
    if len(mot) > {c}:
        return mot[0]
    else:
        return mot[-1]""",
            f"Que renvoie \\texttt{{{nom}('{s3}')}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}} \\ Et \\texttt{{{nom}('{s1}')}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}('{s3}')", f"{nom}('{s1}')"],
        ),
        _t(
            f"""def {nom}(x, y):
    if x {cmp} y:
        return x {op1} y
    else:
        return y {op2} x""",
            f"Que renvoie \\texttt{{{nom}({a}, {b})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}} \\ Et \\texttt{{{nom}({b}, {a})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}({a}, {b})", f"{nom}({b}, {a})"],
        ),
        _t(
            f"""def {nom}(n):
    if n % {c} == 0:
        return n {op1} {c}
    else:
        return n {op2} {b}""",
            f"Que renvoie \\texttt{{{nom}({c * 3})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}} \\ Et \\texttt{{{nom}({c * 3 + 1})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}({c * 3})", f"{nom}({c * 3 + 1})"],
        ),
        _t(
            f"""def {nom}(x):
    if x {op1} {c} {cmp} {a}:
        return x {op2} {c}
    else:
        return x {op3} {b}""",
            f"Que renvoie \\texttt{{{nom}({a + 2})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}} \\ Et \\texttt{{{nom}({c})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}({a + 2})", f"{nom}({c})"],
        ),
        _t(
            f"""def {nom}(x):
    if x {cmp} {a}:
        return {b1}
    else:
        return {b2}""",
            f"Que renvoie \\texttt{{{nom}({a - 1})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}} \\ Et \\texttt{{{nom}({a + 1})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}({a - 1})", f"{nom}({a + 1})"],
        ),
        _t(
            f"""def {nom}(x, y):
    if x + y {cmp} {a + b}:
        return (x + y) {op1} {c}
    else:
        return x {op2} y""",
            f"Que renvoie \\texttt{{{nom}({a}, {b})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}} \\ Et \\texttt{{{nom}({c}, {c})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}({a}, {b})", f"{nom}({c}, {c})"],
        ),
        _t(
            f"""def {nom}(n):
    if n {cmp} {a}:
        return n {op1} n
    else:
        return n {op2} {c}""",
            f"Que renvoie \\texttt{{{nom}({a - 2})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}} \\ Et \\texttt{{{nom}({a + 3})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}({a - 2})", f"{nom}({a + 3})"],
        ),
        _t(
            f"""def {nom}(x, y):
    if x {op1} y {cmp} {a}:
        return x {op2} {b}
    else:
        return y {op3} {c}""",
            f"Que renvoie \\texttt{{{nom}({c}, {c})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}} \\ Et \\texttt{{{nom}({a}, {b})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}({c}, {c})", f"{nom}({a}, {b})"],
        ),
        _t(
            f"""def {nom}(n):
    if n {cmp} {a}:
        return n {op1} {c}
    else:
        return n {op2} {b}""",
            f"Que renvoie \\texttt{{{nom}({a - 3})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}} \\ Et \\texttt{{{nom}({a + 2})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}({a - 3})", f"{nom}({a + 2})"],
        ),
        _t(
            f"""def {nom}(mot, n):
    if n {cmp} len(mot):
        return mot[:n]
    else:
        return mot[n:]""",
            f"Que renvoie \\texttt{{{nom}('{s2}', {c})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}} \\ Et \\texttt{{{nom}('{s1}', {min(a, len(s1))})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}('{s2}', {c})", f"{nom}('{s1}', {min(a, len(s1))})"],
        ),
        _t(
            f"""def {nom}(a, b):
    if a {cmp} b:
        return a {op1} {c}
    else:
        return b {op2} {c}""",
            f"Que renvoie \\texttt{{{nom}({a}, {b})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}} \\ Et \\texttt{{{nom}({b}, {a})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}({a}, {b})", f"{nom}({b}, {a})"],
        ),
        _t(
            f"""def {nom}(n):
    if n % {c} {cmp2} 0:
        return n {op1} {b}
    else:
        return n {op2} {a}""",
            f"Que renvoie \\texttt{{{nom}({c * 2})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}} \\ Et \\texttt{{{nom}({c * 2 + 1})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}({c * 2})", f"{nom}({c * 2 + 1})"],
        ),
        _t(
            f"""def {nom}(x, y):
    if x {op1} {c} {cmp} y {op2} {c}:
        return x {op3} y
    else:
        return y {op1} x""",
            f"Que renvoie \\texttt{{{nom}({a}, {b})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}} \\ Et \\texttt{{{nom}({c}, {c})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}({a}, {b})", f"{nom}({c}, {c})"],
        ),
    ]

    return [{'content': f"\\begin{{lstlisting}}\n{t['code']}\n\\end{{lstlisting}}\n\n{t['question']}",
             'answer': t['answer']}
            for t in templates]


# ── Niveau 2 : boucle for ─────────────────────────────────────────────────────

def generate_niveau2():
    """Code avec une boucle for"""
    noms = ['mystere', 'calcul', 'secret', 'operation', 'test', 'enigme',
            'traiter', 'evaluer', 'appliquer', 'transformer']
    nom = random.choice(noms)

    n    = random.randint(4, 8)
    m    = random.randint(3, 6)
    c    = random.randint(2, 5)
    mult = random.randint(2, 4)
    op1  = random.choice(['+', '-', '*'])

    s2           = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(3, 5)))
    mot          = random.choice(['PYTHON', 'ALGO', 'BOUCLE', 'CODE', 'NSI'])
    petite_liste = [random.randint(1, 4) for _ in range(3)]
    liste_entiers = [random.randint(1, 10) for _ in range(random.randint(4, 5))]

    def _t(code, question, appels):
        return {'code': code, 'question': question,
                'answer': _compute_answer(code, appels)}

    templates = [
        _t(
            f"""def {nom}(n):
    resultat = 0
    for i in range(n):
        resultat += i * {mult}
    return resultat""",
            f"Que renvoie \\texttt{{{nom}({n})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}({n})"],
        ),
        _t(
            f"""def {nom}(mot):
    resultat = ""
    for lettre in mot:
        resultat = lettre + resultat
    return resultat""",
            f"Que renvoie \\texttt{{{nom}('{mot}')}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}('{mot}')"],
        ),
        _t(
            f"""def {nom}(n):
    resultat = []
    for i in range(n):
        resultat.append(i {op1} {c})
    return resultat""",
            f"Que renvoie \\texttt{{{nom}({m})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}({m})"],
        ),
        _t(
            f"""def {nom}(texte):
    resultat = ""
    for char in texte:
        resultat += char * {c}
    return resultat""",
            f"Que renvoie \\texttt{{{nom}('{s2}')}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}('{s2}')"],
        ),
        _t(
            f"""def {nom}(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** 2
    return total""",
            f"Que renvoie \\texttt{{{nom}({m})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}({m})"],
        ),
        _t(
            f"""def {nom}(liste):
    resultat = 1
    for nombre in liste:
        resultat *= nombre
    return resultat""",
            f"Que renvoie \\texttt{{{nom}({petite_liste})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}({petite_liste})"],
        ),
        _t(
            f"""def {nom}(n):
    resultat = 0
    for i in range(1, n + 1):
        resultat += i {op1} {c}
    return resultat""",
            f"Que renvoie \\texttt{{{nom}({m})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}({m})"],
        ),
        _t(
            f"""def {nom}(n):
    resultat = []
    for i in range(n):
        resultat.append({c} ** i)
    return resultat""",
            f"Que renvoie \\texttt{{{nom}({m})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}({m})"],
        ),
        _t(
            f"""def {nom}(liste):
    total = 0
    for x in liste:
        total += x
    return total""",
            f"Que renvoie \\texttt{{{nom}({liste_entiers})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}({liste_entiers})"],
        ),
        _t(
            f"""def {nom}(liste):
    resultat = []
    for x in liste:
        resultat.append(x * {mult})
    return resultat""",
            f"Que renvoie \\texttt{{{nom}({liste_entiers[:3]})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}({liste_entiers[:3]})"],
        ),
        _t(
            f"""def {nom}(mot):
    resultat = []
    for lettre in mot:
        resultat.append(lettre)
    return resultat""",
            f"Que renvoie \\texttt{{{nom}('{s2}')}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}('{s2}')"],
        ),
        _t(
            f"""def {nom}(n):
    resultat = 0
    for i in range(1, n + 1):
        resultat += i
    return resultat""",
            f"Que renvoie \\texttt{{{nom}({n})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}({n})"],
        ),
    ]

    return [{'content': f"\\begin{{lstlisting}}\n{t['code']}\n\\end{{lstlisting}}\n\n{t['question']}",
             'answer': t['answer']}
            for t in templates]


# ── Niveau 3 : for + if ───────────────────────────────────────────────────────

def generate_niveau3():
    """Code avec boucle for et if imbriqués"""
    noms = ['mystere', 'calcul', 'secret', 'operation', 'test', 'enigme',
            'traiter', 'evaluer', 'appliquer', 'transformer']
    nom = random.choice(noms)

    lst_mix  = [random.randint(-8, 8) for _ in range(random.randint(4, 6))]
    lst_int  = [random.randint(1, 15) for _ in range(random.randint(4, 6))]
    seuil    = random.randint(3, 8)
    mult     = random.randint(2, 4)
    c        = random.randint(2, 5)
    n        = random.randint(8, 15)

    prenoms = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
    random.shuffle(prenoms)
    dict_notes = {prenoms[i]: random.randint(5, 18) for i in range(4)}

    def _t(code, question, appels):
        return {'code': code, 'question': question,
                'answer': _compute_answer(code, appels)}

    templates = [
        _t(
            f"""def {nom}(liste):
    resultat = []
    for x in liste:
        if x > 0:
            resultat.append(x * {mult})
        else:
            resultat.append(x)
    return resultat""",
            f"Que renvoie \\texttt{{{nom}({lst_mix})}} ? \\fbox{{\\parbox{{9cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}({lst_mix})"],
        ),
        _t(
            f"""def {nom}(liste):
    resultat = []
    for x in liste:
        if x >= {seuil}:
            resultat.append(x)
    return resultat""",
            f"Que renvoie \\texttt{{{nom}({lst_int})}} ? \\fbox{{\\parbox{{9cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}({lst_int})"],
        ),
        _t(
            f"""def {nom}(liste):
    total = 0
    for x in liste:
        if x % 2 == 0:
            total += x
    return total""",
            f"Que renvoie \\texttt{{{nom}({lst_int})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}({lst_int})"],
        ),
        _t(
            f"""def {nom}(liste):
    compteur = 0
    for x in liste:
        if x > {seuil}:
            compteur += 1
    return compteur""",
            f"Que renvoie \\texttt{{{nom}({lst_int})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}({lst_int})"],
        ),
        _t(
            f"""def {nom}(liste):
    resultat = []
    for x in liste:
        if x % {c} == 0:
            resultat.append(x)
        else:
            resultat.append(0)
    return resultat""",
            f"Que renvoie \\texttt{{{nom}({lst_int})}} ? \\fbox{{\\parbox{{9cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}({lst_int})"],
        ),
        _t(
            f"""def {nom}(n):
    resultat = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            resultat.append(i)
    return resultat""",
            f"Que renvoie \\texttt{{{nom}({n})}} ? \\fbox{{\\parbox{{9cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}({n})"],
        ),
        _t(
            f"""def {nom}(n):
    total = 0
    for i in range(1, n + 1):
        if i % {c} == 0:
            total += i
    return total""",
            f"Que renvoie \\texttt{{{nom}({n})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}({n})"],
        ),
        _t(
            f"""def {nom}(n):
    resultat = []
    for i in range(n):
        if i * i < n:
            resultat.append(i)
    return resultat""",
            f"Que renvoie \\texttt{{{nom}({n})}} ? \\fbox{{\\parbox{{9cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}({n})"],
        ),
        _t(
            f"""def {nom}(dico):
    resultat = []
    for cle in dico:
        if dico[cle] >= 10:
            resultat.append(cle)
    return resultat""",
            f"Que renvoie \\texttt{{{nom}({dict_notes})}} ? \\fbox{{\\parbox{{9cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}({dict_notes})"],
        ),
        _t(
            f"""def {nom}(dico):
    total = 0
    for cle in dico:
        if dico[cle] > {seuil}:
            total += dico[cle]
    return total""",
            f"Que renvoie \\texttt{{{nom}({dict_notes})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}({dict_notes})"],
        ),
        _t(
            f"""def {nom}(liste):
    for x in liste:
        if x > {seuil}:
            return x
    return None""",
            f"Que renvoie \\texttt{{{nom}({lst_int})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}({lst_int})"],
        ),
        _t(
            f"""def {nom}(liste):
    resultat = []
    for x in liste:
        if x < 0:
            resultat.append(0)
        else:
            resultat.append(x)
    return resultat""",
            f"Que renvoie \\texttt{{{nom}({lst_mix})}} ? \\fbox{{\\parbox{{9cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}({lst_mix})"],
        ),
    ]

    return [{'content': f"\\begin{{lstlisting}}\n{t['code']}\n\\end{{lstlisting}}\n\n{t['question']}",
             'answer': t['answer']}
            for t in templates]


# ── Niveau 4 : double boucle for ─────────────────────────────────────────────

def generate_niveau4():
    """Code avec deux boucles for imbriquées"""
    noms = ['mystere', 'calcul', 'secret', 'operation', 'test', 'enigme',
            'traiter', 'evaluer', 'appliquer', 'transformer']
    nom = random.choice(noms)

    n    = random.randint(3, 4)
    c    = random.randint(2, 4)
    mat  = [[random.randint(1, 9) for _ in range(3)] for _ in range(3)]
    mat2 = [[random.randint(-5, 5) for _ in range(3)] for _ in range(3)]
    lst1 = [random.randint(1, 6) for _ in range(3)]
    lst2 = [random.randint(1, 6) for _ in range(3)]

    def _t(code, question, appels):
        return {'code': code, 'question': question,
                'answer': _compute_answer(code, appels)}

    templates = [
        _t(
            f"""def {nom}(n):
    resultat = 0
    for i in range(n):
        for j in range(i):
            resultat += 1
    return resultat""",
            f"Que renvoie \\texttt{{{nom}({n})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}({n})"],
        ),
        _t(
            f"""def {nom}(n):
    resultat = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            resultat.append(i * j)
    return resultat""",
            f"Que renvoie \\texttt{{{nom}({min(n, 3)})}} ? \\fbox{{\\parbox{{9cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}({min(n, 3)})"],
        ),
        _t(
            f"""def {nom}(matrice):
    total = 0
    for ligne in matrice:
        for x in ligne:
            total += x
    return total""",
            f"Que renvoie \\texttt{{{nom}({mat})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}({mat})"],
        ),
        _t(
            f"""def {nom}(matrice):
    resultat = []
    for ligne in matrice:
        for x in ligne:
            resultat.append(x)
    return resultat""",
            f"Que renvoie \\texttt{{{nom}({mat[:2]})}} ? \\fbox{{\\parbox{{9cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}({mat[:2]})"],
        ),
        _t(
            f"""def {nom}(n):
    resultat = []
    for i in range(n):
        ligne = []
        for j in range(i + 1):
            ligne.append(j)
        resultat.append(ligne)
    return resultat""",
            f"Que renvoie \\texttt{{{nom}({n})}} ? \\fbox{{\\parbox{{9cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}({n})"],
        ),
        _t(
            f"""def {nom}(n):
    resultat = []
    for i in range(n):
        ligne = []
        for j in range(n):
            ligne.append(i + j)
        resultat.append(ligne)
    return resultat""",
            f"Que renvoie \\texttt{{{nom}({min(n, 3)})}} ? \\fbox{{\\parbox{{9cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}({min(n, 3)})"],
        ),
        _t(
            f"""def {nom}(matrice):
    total = 0
    for ligne in matrice:
        for x in ligne:
            if x % 2 == 0:
                total += x
    return total""",
            f"Que renvoie \\texttt{{{nom}({mat})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}({mat})"],
        ),
        _t(
            f"""def {nom}(matrice):
    compteur = 0
    for ligne in matrice:
        for x in ligne:
            if x > {c}:
                compteur += 1
    return compteur""",
            f"Que renvoie \\texttt{{{nom}({mat})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}({mat})"],
        ),
        _t(
            f"""def {nom}(matrice):
    resultat = []
    for ligne in matrice:
        for x in ligne:
            if x > 0:
                resultat.append(x)
    return resultat""",
            f"Que renvoie \\texttt{{{nom}({mat2})}} ? \\fbox{{\\parbox{{9cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}({mat2})"],
        ),
        _t(
            f"""def {nom}(liste1, liste2):
    resultat = []
    for a in liste1:
        for b in liste2:
            resultat.append(a + b)
    return resultat""",
            f"Que renvoie \\texttt{{{nom}({lst1}, {lst2})}} ? \\fbox{{\\parbox{{9cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}({lst1}, {lst2})"],
        ),
        _t(
            f"""def {nom}(liste1, liste2):
    communs = []
    for a in liste1:
        for b in liste2:
            if a == b:
                communs.append(a)
    return communs""",
            f"Que renvoie \\texttt{{{nom}({lst1}, {lst2})}} ? \\fbox{{\\parbox{{9cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}({lst1}, {lst2})"],
        ),
        _t(
            f"""def {nom}(matrice):
    total = 0
    for i in range(len(matrice)):
        for j in range(len(matrice[i])):
            if i == j:
                total += matrice[i][j]
    return total""",
            f"Que renvoie \\texttt{{{nom}({mat})}} ? \\fbox{{\\parbox{{5cm}}{{\\rule{{0pt}}{{1cm}}}}}}",
            [f"{nom}({mat})"],
        ),
    ]

    return [{'content': f"\\begin{{lstlisting}}\n{t['code']}\n\\end{{lstlisting}}\n\n{t['question']}",
             'answer': t['answer']}
            for t in templates]


# ── Niveau 5 : structures imbriquées ─────────────────────────────────────────

def generate_niveau5():
    """Code avec plusieurs structures imbriquées"""
    lst = [random.randint(1, 20) for _ in range(random.randint(6, 10))]

    def _t(code, question, appels):
        return {'code': code, 'question': question,
                'answer': _compute_answer(code, appels)}

    templates = [
        _t(
            f"""def fonction(liste):
    resultats = []
    for i in range(len(liste)):
        sous_liste = []
        for j in range(i, len(liste)):
            if liste[j] > liste[i]:
                sous_liste.append(liste[j])
        if len(sous_liste) > 0:
            resultats.append(max(sous_liste))
    return resultats""",
            f"Que renvoie \\texttt{{fonction({lst})}} ?",
            [f"fonction({lst})"],
        ),
        _t(
            """def analyser(texte):
    mots = texte.split()
    resultats = {}
    for mot in mots:
        longueur = len(mot)
        if longueur not in resultats:
            resultats[longueur] = []
        resultats[longueur].append(mot)
    return resultats""",
            "Que renvoie \\texttt{analyser('le chat mange la souris')} ?",
            ["analyser('le chat mange la souris')"],
        ),
    ]

    return [{'content': f"Analysez attentivement le code suivant et répondez à la question :\n\n\\begin{{lstlisting}}\n{t['code']}\n\\end{{lstlisting}}\n\n{t['question']}",
             'answer': t['answer']}
            for t in templates]


# ── Niveau 6 : code complexe ─────────────────────────────────────────────────

def generate_niveau6():
    """Code complexe"""
    lst6 = [random.randint(1, 30) for _ in range(6)]

    def _t(code, question, appels):
        return {'code': code, 'question': question,
                'answer': _compute_answer(code, appels)}

    templates = [
        _t(
            """def mystere(liste):
    n = len(liste)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if liste[j] < liste[min_idx]:
                min_idx = j
        liste[i], liste[min_idx] = liste[min_idx], liste[i]
    return liste""",
            f"Que fait cette fonction ? Que renvoie \\texttt{{mystere({lst6})}} ?",
            [f"mystere({lst6})"],
        ),
        _t(
            """def fonction(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a""",
            "Quelle suite mathématique cette fonction calcule-t-elle ? Que renvoie \\texttt{fonction(7)} ?",
            ["fonction(7)"],
        ),
    ]

    return [{'content': f"Analysez le code suivant :\n\n\\begin{{lstlisting}}\n{t['code']}\n\\end{{lstlisting}}\n\n{t['question']}",
             'answer': t['answer']}
            for t in templates]
