import random

# Grille de base valide pour 4x4 (blocs 2x2)
_BASE_4x4 = [
    [1, 2, 3, 4],
    [3, 4, 1, 2],
    [2, 1, 4, 3],
    [4, 3, 2, 1],
]

# Grille de base valide pour 6x6 (blocs 2x3)
_BASE_6x6 = [
    [1, 2, 3, 4, 5, 6],
    [4, 5, 6, 1, 2, 3],
    [2, 3, 1, 5, 6, 4],
    [5, 6, 4, 2, 3, 1],
    [3, 1, 2, 6, 4, 5],
    [6, 4, 5, 3, 1, 2],
]


def generate_puzzle(niveau):
    """Génère un sudoku selon le niveau (1-2 → 4x4, 3-5 → 6x6)"""
    if niveau <= 2:
        sol = _melanger_4x4(_BASE_4x4)
        nb = {1: 5, 2: 7}.get(niveau, 6)
        puzzle = _retirer_cases(sol, 4, 2, 2, nb)
        return _latex_sudoku(puzzle, 4, 2, 2)
    else:
        sol = _melanger_6x6(_BASE_6x6)
        nb = {3: 12, 4: 16, 5: 20}.get(niveau, 14)
        puzzle = _retirer_cases(sol, 6, 2, 3, nb)
        return _latex_sudoku(puzzle, 6, 2, 3)


# ── Génération de grilles ────────────────────────────────────────────────────

def _melanger_4x4(base):
    g = [row[:] for row in base]
    # Permutation des lignes dans chaque bande (bandes de 2 lignes)
    for start in [0, 2]:
        if random.random() < 0.5:
            g[start], g[start + 1] = g[start + 1], g[start]
    # Permutation des bandes
    if random.random() < 0.5:
        g[0], g[1], g[2], g[3] = g[2], g[3], g[0], g[1]
    # Permutation des colonnes dans chaque pile (piles de 2 colonnes)
    for start in [0, 2]:
        if random.random() < 0.5:
            for row in g:
                row[start], row[start + 1] = row[start + 1], row[start]
    # Permutation des piles
    if random.random() < 0.5:
        for row in g:
            row[:] = row[2:4] + row[0:2]
    # Renumérotation des chiffres
    perm = list(range(1, 5))
    random.shuffle(perm)
    label = {i + 1: perm[i] for i in range(4)}
    return [[label[x] for x in row] for row in g]


def _melanger_6x6(base):
    g = [row[:] for row in base]
    # Permutation des lignes dans chaque bande (3 bandes de 2 lignes)
    for start in [0, 2, 4]:
        if random.random() < 0.5:
            g[start], g[start + 1] = g[start + 1], g[start]
    # Permutation des bandes
    order = [0, 1, 2]
    random.shuffle(order)
    g = [g[b * 2 + k] for b in order for k in range(2)]
    # Permutation des colonnes dans chaque pile (2 piles de 3 colonnes)
    for pile in range(2):
        perm = list(range(3))
        random.shuffle(perm)
        new_g = [row[:] for row in g]
        for new_j, old_j in enumerate(perm):
            for i in range(6):
                new_g[i][pile * 3 + new_j] = g[i][pile * 3 + old_j]
        g = new_g
    # Permutation des piles
    if random.random() < 0.5:
        for row in g:
            row[:] = row[3:6] + row[0:3]
    # Renumérotation des chiffres
    perm = list(range(1, 7))
    random.shuffle(perm)
    label = {i + 1: perm[i] for i in range(6)}
    return [[label[x] for x in row] for row in g]


# ── Solveur par backtracking ─────────────────────────────────────────────────

def _valide(g, ligne, col, val, taille, br, bc):
    if val in g[ligne]:
        return False
    if any(g[i][col] == val for i in range(taille)):
        return False
    bl = (ligne // br) * br
    bs = (col // bc) * bc
    for i in range(bl, bl + br):
        for j in range(bs, bs + bc):
            if g[i][j] == val:
                return False
    return True


def _compter_solutions(g, taille, br, bc, max_sol=2):
    for i in range(taille):
        for j in range(taille):
            if g[i][j] == 0:
                count = 0
                for val in range(1, taille + 1):
                    if _valide(g, i, j, val, taille, br, bc):
                        g[i][j] = val
                        count += _compter_solutions(g, taille, br, bc, max_sol)
                        g[i][j] = 0
                        if count >= max_sol:
                            return count
                return count
    return 1  # Aucune case vide = solution complète


def _retirer_cases(solution, taille, br, bc, nb_a_retirer):
    """Retire des cases en garantissant une solution unique."""
    puzzle = [row[:] for row in solution]
    positions = [(i, j) for i in range(taille) for j in range(taille)]
    random.shuffle(positions)
    retires = 0
    for (i, j) in positions:
        if retires >= nb_a_retirer:
            break
        val = puzzle[i][j]
        puzzle[i][j] = 0
        test = [row[:] for row in puzzle]
        if _compter_solutions(test, taille, br, bc) == 1:
            retires += 1
        else:
            puzzle[i][j] = val  # Restaurer si plus unique
    return puzzle


# ── Rendu LaTeX (TikZ) ───────────────────────────────────────────────────────

def _latex_sudoku(puzzle, taille, br, bc):
    """Rend le sudoku en LaTeX/TikZ."""
    scale = 0.9 if taille == 4 else 0.72
    chiffres = taille

    lignes = []
    lignes.append(f"\\textbf{{Sudoku {taille}×{taille}}}")
    lignes.append("")
    lignes.append(f"\\small Complétez la grille : chaque ligne, colonne et bloc doit contenir "
                  f"les chiffres de 1 à {chiffres} une seule fois.")
    lignes.append("")
    lignes.append("\\begin{center}")
    lignes.append(f"\\begin{{tikzpicture}}[scale={scale}]")

    # Lignes fines (grille intérieure)
    for k in range(1, taille):
        est_bloc_h = (k % br == 0)
        est_bloc_v = (k % bc == 0)
        if not est_bloc_h:
            lignes.append(f"\\draw[thin, gray!50] (0,{k}) -- ({taille},{k});")
        if not est_bloc_v:
            lignes.append(f"\\draw[thin, gray!50] ({k},0) -- ({k},{taille});")

    # Lignes épaisses (bordure et séparations de blocs)
    lignes.append(f"\\draw[line width=1.8pt] (0,0) rectangle ({taille},{taille});")
    for k in range(br, taille, br):
        lignes.append(f"\\draw[line width=1.8pt] (0,{k}) -- ({taille},{k});")
    for k in range(bc, taille, bc):
        lignes.append(f"\\draw[line width=1.8pt] ({k},0) -- ({k},{taille});")

    # Chiffres (puzzle[i][j], ligne i depuis le haut → y = taille-i-0.5)
    for i in range(taille):
        for j in range(taille):
            if puzzle[i][j] != 0:
                x = j + 0.5
                y = taille - i - 0.5
                lignes.append(f"\\node[font=\\large\\bfseries] at ({x},{y}) {{{puzzle[i][j]}}};")

    lignes.append("\\end{tikzpicture}")
    lignes.append("\\end{center}")

    return "\n".join(lignes)
