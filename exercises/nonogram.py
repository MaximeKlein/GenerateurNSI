import random


def generate_puzzle(niveau):
    """Génère un nonogramme selon le niveau (1-2 → 5x5, 3-5 → 6x6)."""
    taille = 5 if niveau <= 2 else 6
    densite = 0.45 + niveau * 0.03  # légèrement plus rempli aux niveaux supérieurs

    for _ in range(300):
        grille = [[1 if random.random() < densite else 0
                   for _ in range(taille)]
                  for _ in range(taille)]
        clues_lig = [_clue(grille[i]) for i in range(taille)]
        clues_col = [_clue([grille[i][j] for i in range(taille)]) for j in range(taille)]
        if _est_unique(clues_lig, clues_col, taille):
            return _latex_nonogram(grille, clues_lig, clues_col, taille)

    # Fallback : grille garantie unique (motif fixe + relabeling)
    return _latex_nonogram(*_grille_secours(taille), taille)


# ── Calcul des indices ────────────────────────────────────────────────────────

def _clue(ligne):
    """Retourne la liste des longueurs de blocs remplis."""
    clue, count = [], 0
    for cell in ligne:
        if cell == 1:
            count += 1
        elif count:
            clue.append(count)
            count = 0
    if count:
        clue.append(count)
    return clue  # [] pour une ligne vide


# ── Solveur de ligne (arrangements possibles) ────────────────────────────────

def _arrangements(longueur, blocs):
    """Génère tous les placements valides de `blocs` dans une ligne de `longueur` cases."""
    if not blocs:
        return [(0,) * longueur]
    results = []
    premier, reste = blocs[0], blocs[1:]
    # Espace minimum requis par les blocs restants (blocs + séparateurs)
    min_reste = sum(reste) + len(reste)
    for debut in range(longueur - premier - min_reste + 1):
        prefix = [0] * debut + [1] * premier
        if reste:
            prefix.append(0)  # séparateur obligatoire
            for suite in _arrangements(longueur - len(prefix), reste):
                results.append(tuple(prefix) + suite)
        else:
            suffix = [0] * (longueur - len(prefix))
            results.append(tuple(prefix) + tuple(suffix))
    return results


def _compatible(arrangement, etat):
    """Vérifie qu'un arrangement est cohérent avec l'état connu (-1 = inconnu)."""
    return all(e == -1 or e == a for e, a in zip(etat, arrangement))


# ── Vérification d'unicité par propagation de contraintes ────────────────────

def _est_unique(clues_lig, clues_col, taille):
    """Retourne True si la propagation de contraintes résout entièrement le nonogramme."""
    grille = [[-1] * taille for _ in range(taille)]
    changed = True
    while changed:
        changed = False
        # Propagation sur les lignes
        for i in range(taille):
            arrs = [a for a in _arrangements(taille, clues_lig[i])
                    if _compatible(a, grille[i])]
            if not arrs:
                return False
            for j in range(taille):
                vals = {a[j] for a in arrs}
                if len(vals) == 1:
                    v = vals.pop()
                    if grille[i][j] != v:
                        grille[i][j] = v
                        changed = True
        # Propagation sur les colonnes
        for j in range(taille):
            col = [grille[i][j] for i in range(taille)]
            arrs = [a for a in _arrangements(taille, clues_col[j])
                    if _compatible(a, col)]
            if not arrs:
                return False
            for i in range(taille):
                vals = {a[i] for a in arrs}
                if len(vals) == 1:
                    v = vals.pop()
                    if grille[i][j] != v:
                        grille[i][j] = v
                        changed = True
    return all(grille[i][j] != -1 for i in range(taille) for j in range(taille))


# ── Grille de secours (toujours unique) ──────────────────────────────────────

def _grille_secours(taille):
    """Retourne une grille simple dont on sait qu'elle est uniquement résoluble."""
    if taille == 5:
        g = [
            [1, 0, 1, 0, 1],
            [1, 1, 0, 1, 1],
            [0, 1, 1, 1, 0],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1],
        ]
    else:  # 6x6
        g = [
            [1, 1, 0, 0, 1, 1],
            [1, 0, 1, 1, 0, 1],
            [0, 1, 1, 1, 1, 0],
            [1, 1, 0, 0, 1, 1],
            [0, 0, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 1],
        ]
    lig = [_clue(g[i]) for i in range(taille)]
    col = [_clue([g[i][j] for i in range(taille)]) for j in range(taille)]
    return g, lig, col


# ── Rendu LaTeX (TikZ) ───────────────────────────────────────────────────────

def _latex_nonogram(grille, clues_lig, clues_col, taille):
    """Rend le nonogramme en LaTeX/TikZ."""
    # Taille de la zone des indices (en unités de cases)
    max_lig = max((len(c) for c in clues_lig), default=1)
    max_col = max((len(c) for c in clues_col), default=1)
    cw = max(max_lig, 2)   # largeur zone indices-lignes (gauche)
    ch = max(max_col, 2)   # hauteur zone indices-colonnes (haut)

    # Grille principale : x ∈ [cw, cw+taille], y ∈ [0, taille]
    # Indices colonnes : y ∈ [taille, taille+ch]
    # Indices lignes   : x ∈ [0, cw]

    scale = 0.65

    L = []
    L.append("\\textbf{Nonogramme}")
    L.append("")
    L.append("\\small Les nombres indiquent les longueurs des blocs de cases noires "
             "dans chaque ligne et colonne (dans l'ordre, séparés par au moins une case blanche).")
    L.append("")
    L.append("\\begin{center}")
    L.append(f"\\begin{{tikzpicture}}[scale={scale}]")

    # ── Grille principale ──
    # Lignes fines intérieures
    for k in range(1, taille):
        L.append(f"\\draw[thin,gray!50] ({cw},{k})--({cw+taille},{k});")
        L.append(f"\\draw[thin,gray!50] ({cw+k},0)--({cw+k},{taille});")
    # Bordure épaisse
    L.append(f"\\draw[line width=1.5pt] ({cw},0) rectangle ({cw+taille},{taille});")

    # ── Indices des lignes (à gauche, alignés à droite vers la grille) ──
    for i, clue in enumerate(clues_lig):
        y_centre = taille - i - 0.5
        nc = len(clue)
        for k, val in enumerate(reversed(clue)):
            # k=0 : dernier indice, adjacent à la grille (x = cw - 0.5)
            x = cw - k - 0.5
            L.append(f"\\node[font=\\small\\bfseries] at ({x},{y_centre}) {{{val}}};")
        if not clue:
            L.append(f"\\node[font=\\small] at ({cw - 0.5},{y_centre}) {{0}};")

    # ── Indices des colonnes (en haut, alignés en bas vers la grille) ──
    for j, clue in enumerate(clues_col):
        x_centre = cw + j + 0.5
        nc = len(clue)
        for k, val in enumerate(reversed(clue)):
            # k=0 : dernier indice, adjacent à la grille (y = taille + 0.5)
            y = taille + k + 0.5
            L.append(f"\\node[font=\\small\\bfseries] at ({x_centre},{y}) {{{val}}};")
        if not clue:
            L.append(f"\\node[font=\\small] at ({x_centre},{taille + 0.5}) {{0}};")

    # ── Séparation visuelle entre zone indices et grille ──
    L.append(f"\\draw[line width=1.2pt] ({cw},{taille})--({cw+taille},{taille});")  # haut grille
    L.append(f"\\draw[line width=1.2pt] ({cw},0)--({cw},{taille});")               # gauche grille

    L.append("\\end{tikzpicture}")
    L.append("\\end{center}")

    return "\n".join(L)
