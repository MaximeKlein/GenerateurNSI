# Générateur d'Interrogations NSI

Outil Python de génération automatique d'interrogations individualisées pour les cours de NSI (Numérique et Sciences Informatiques). Chaque élève reçoit un PDF personnalisé adapté à son niveau dans chaque axe de compétence.

---

## Fonctionnement général

Le système lit un fichier `eleves.csv` contenant le nom de chaque élève, son niveau actuel dans chaque axe (0–N), et l'axe sur lequel il est interrogé. Il génère un PDF par élève puis les fusionne en un seul fichier via `pdfunite`.

```
python main.py --nom "Interrogation NSI" --classe "Terminale NSI"
```

Les PDFs individuels sont écrits dans `output/`, et le fichier fusionné dans `output.pdf`.

---

## Structure du projet

```
.
├── main.py               # Point d'entrée : lit eleves.csv, génère les PDFs
├── generator.py          # InterrogationGenerator : assemblage LaTeX + compilation pdflatex
├── eleves.csv            # Liste des élèves avec niveaux et axe du jour
├── output/               # PDFs individuels générés
├── temp/                 # Fichiers .tex et .aux temporaires (pdflatex)
└── exercises/
    ├── writing.py        # Écriture de code Python (niveaux 1–4)
    ├── reading.py        # Analyse de code Python (niveaux 1–4)
    ├── testing.py        # Débogage de code Python (niveaux 1–5)
    ├── logic.py          # Logique : aliens, sudoku, nonogramme (niveaux 1–5)
    ├── alien_grid.py     # Générateur de grilles d'aliens logiques
    ├── sudoku.py         # Générateur de sudokus 4×4 et 6×6
    └── nonogram.py       # Générateur de nonogrammes 5×5 et 6×6
```

---

## Format de `eleves.csv`

```csv
eleve,a,e,t,l,choix
DUPONT Alice,1,2,0,1,e
MARTIN Paul,0,0,0,0,a
,,,,,          ← ligne vide : déclenche pdfunite et arrêt
```

| Colonne | Description |
|---------|-------------|
| `eleve` | Nom complet de l'élève |
| `a` | Niveau actuel en **A**nalyse de code (0–N) |
| `e` | Niveau actuel en **É**criture de code (0–N) |
| `t` | Niveau actuel en **T**ests / débogage (0–N) |
| `l` | Niveau actuel en **L**ogique (0–N) |
| `choix` | Axe interrogé aujourd'hui (`a`, `e`, `t` ou `l`) |

Le niveau transmis au module est `valeur_csv + 1` (les niveaux internes commencent à 1).

---

## Les quatre axes

### Écriture de code (`e`) — `writing.py`

L'élève doit **écrire** une fonction Python à partir d'une description. La réponse se fait dans un cadre ligné.

| Niveau | Structure du code |
|--------|-------------------|
| 1 | Calcul direct / branchement simple |
| 2 | Boucle `for` sans `if` (liste, tuple, dict, string, `range`) |
| 3 | Boucle `for` avec `if` (filtrage, comptage) |
| 4 | Double boucle `for` (matrices, produits cartésiens) |

---

### Analyse de code (`a`) — `reading.py`

L'élève doit **lire et tracer** l'exécution d'une fonction Python pour trouver la valeur renvoyée.

| Niveau | Structure du code |
|--------|-------------------|
| 1 | Calcul direct / branchement simple |
| 2 | Boucle `for` sans `if` |
| 3 | Boucle `for` avec `if` (listes, strings, `range`, dicts) |
| 4 | Double boucle `for` (matrices, produits) |

Les noms de fonctions sont randomisés (`mystere`, `calcul`, `secret`, `enigme`…) pour éviter que les élèves reconnaissent l'exercice.

---

### Tests / Débogage (`t`) — `testing.py`

L'élève reçoit une fonction **contenant des erreurs** et doit les identifier, puis réécrire la version corrigée.

| Niveau | Structure | Nombre d'erreurs | Types d'erreurs |
|--------|-----------|-----------------|-----------------|
| 1 | `if/else` | 1 | Logique, cas limite, erreur courante |
| 2 | `for` | 1 | `range(liste)`, init incorrecte, `=` vs `+=`, mauvaise variable |
| 3 | `for` + `if` | 2 | Combinaisons des erreurs niveaux 1–2 |
| 4 | Double `for` | 2–3 | Opérations sur matrices, indices, conditions |
| 5 | Complexe | 3 | Tri, fusion, transformation de matrice |

Chaque exercice affiche : description de ce que doit faire la fonction → code bogué → exemple d'appel avec résultat incorrect → N cases d'identification → grande zone de réécriture.

---

### Logique (`l`) — `logic.py`

L'élève résout un **puzzle logique**. Trois types sont générés aléatoirement (50 % aliens, 25 % sudoku, 25 % nonogramme).

#### Grilles d'aliens (`alien_grid.py`)
Grille de symboles/aliens avec des règles de déduction logique (style Einstein/zebra puzzle).

#### Sudoku (`sudoku.py`)
- Niveaux 1–2 : grille **4×4** (blocs 2×2), 5 ou 7 cases retirées
- Niveaux 3–5 : grille **6×6** (blocs 2×3), 12 à 20 cases retirées
- Solution unique garantie par backtracking

#### Nonogramme (`nonogram.py`)
- Niveaux 1–2 : grille **5×5**
- Niveaux 3–5 : grille **6×6**
- Solution unique garantie par propagation de contraintes (résolution par lignes/colonnes)
- Jusqu'à 300 tentatives de génération aléatoire, puis repli sur un motif garanti

---

## Format du PDF généré

Chaque PDF contient :
- **En-tête** : nom de la classe, date, nom de l'élève, axe et niveau
- **N exercices** (3 pour écriture/logique, 5 pour analyse/tests)
- **Tableau de progression** en bas de page : cases à cocher pour le prochain test selon réussite ou échec

---

## Dépendances

### Python
```
Python 3.10+   (f-strings avec guillemets imbriqués)
```
Aucune bibliothèque tierce requise — uniquement la bibliothèque standard (`random`, `csv`, `subprocess`, `os`).

### LaTeX
```
pdflatex       (distribution TeX Live ou MiKTeX)
pdfunite       (poppler-utils, pour la fusion des PDFs)
```

Packages LaTeX utilisés : `inputenc`, `babel` (french), `lmodern`, `amsmath`, `tikz`, `listings`, `xcolor`, `geometry`, `fancyhdr`, `array`.

---

## Lancement

```bash
# Générer les interrogations pour tous les élèves du CSV
python main.py

# Avec options
python main.py --nom "Interro 3 - Fonctions" --classe "Terminale NSI G1"
```

Les PDFs individuels apparaissent dans `output/NOM_Prenom.pdf`.  
Le fichier fusionné (pour impression) est `output.pdf`.

---

## Ajouter des exercices

Chaque module expose une fonction :

```python
def generate_exercises(niveau: int, count: int = 5) -> list[dict]:
    # Retourne une liste de dicts {"content": "<LaTeX string>"}
```

Pour ajouter un template, il suffit d'ajouter une entrée dans la liste `templates` du niveau concerné — aucune autre modification n'est nécessaire.
