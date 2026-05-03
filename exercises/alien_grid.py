import random
import itertools
from typing import List, Tuple, Optional, Set
from dataclasses import dataclass
from copy import deepcopy


@dataclass
class Alien:
    """Représente un alien avec sa forme, son assertion et son statut"""
    forme: str
    assertion: str
    est_menteur: bool
    position: Tuple[int, int]

    def __str__(self):
        statut = "🔴" if self.est_menteur else "🟢"
        return f"{statut} {self.forme}: \"{self.assertion}\""


class GrilleAliens:
    def __init__(self, largeur: int, hauteur: int, nb_menteurs: int):
        """
        Initialise une grille d'aliens

        Args:
            largeur: Largeur de la grille
            hauteur: Hauteur de la grille
            nb_menteurs: Nombre d'aliens menteurs dans la grille
        """
        self.largeur = largeur
        self.hauteur = hauteur
        self.nb_menteurs = nb_menteurs
        self.formes = ["👽", "🛸", "🤖", "👾", "🦎"]
        self.grille: List[List[Optional[Alien]]] = [[None for _ in range(largeur)] for _ in range(hauteur)]

    def generer_grille(self, max_tentatives: int = 100) -> bool:
        """
        Génère la grille avec les aliens et leurs assertions
        Vérifie que la solution est unique

        Returns:
            True si une grille valide a été générée, False sinon
        """
        for tentative in range(max_tentatives):
            self._initialiser_aliens()
            self._generer_assertions()

            if self._verifier_unicite_solution():
                print(f"✅ Grille valide trouvée (tentative {tentative + 1})")
                return True
            else:
                print(f"⚠️  Tentative {tentative + 1}: Solution non unique, nouvelle génération...")

        print(f"❌ Échec après {max_tentatives} tentatives")
        return False

    def _initialiser_aliens(self):
        """Initialise les aliens dans la grille avec leurs formes et statuts"""
        positions = [(i, j) for i in range(self.hauteur) for j in range(self.largeur)]
        menteurs_indices = random.sample(range(len(positions)), self.nb_menteurs)

        for idx, (i, j) in enumerate(positions):
            forme = random.choice(self.formes)
            est_menteur = idx in menteurs_indices

            self.grille[i][j] = Alien(
                forme=forme,
                assertion="",
                est_menteur=est_menteur,
                position=(i, j)
            )

    def _generer_assertions(self):
        """Génère les assertions pour chaque alien"""
        for i in range(self.hauteur):
            for j in range(self.largeur):
                alien = self.grille[i][j]
                alien.assertion = self._generer_assertion_pour_alien(i, j)

    def _generer_assertion_pour_alien(self, i: int, j: int) -> str:
        """Génère une assertion cohérente pour un alien à la position (i, j)"""
        alien = self.grille[i][j]
        assertions_possibles = []

        # Type 1: Assertions sur les voisins
        voisins = [
            ("droite", i, j + 1, j < self.largeur - 1),
            ("gauche", i, j - 1, j > 0),
            ("haut", i - 1, j, i > 0),
            ("bas", i + 1, j, i < self.hauteur - 1)
        ]

        for direction, vi, vj, existe in voisins:
            if existe:
                voisin = self.grille[vi][vj]
                if alien.est_menteur:
                    # Il ment, donc dit l'inverse
                    if voisin.est_menteur:
                        assertions_possibles.append(f"Mon voisin de {direction} dit la vérité")
                    else:
                        assertions_possibles.append(f"Mon voisin de {direction} ment")
                else:
                    # Il dit la vérité
                    if voisin.est_menteur:
                        assertions_possibles.append(f"Mon voisin de {direction} ment")
                    else:
                        assertions_possibles.append(f"Mon voisin de {direction} dit la vérité")

        # Type 2: Assertions sur le nombre de menteurs par forme
        for forme in self.formes:
            nb_menteurs_forme = sum(
                1 for row in self.grille for a in row
                if a and a.forme == forme and a.est_menteur
            )

            # "Il n'y a aucun menteur dans les aliens de la forme X"
            if alien.est_menteur:
                if nb_menteurs_forme == 0:
                    assertions_possibles.append(f"Il y a au moins un menteur parmi les {forme}")
                else:
                    assertions_possibles.append(f"Il n'y a aucun menteur parmi les {forme}")
            else:
                if nb_menteurs_forme == 0:
                    assertions_possibles.append(f"Il n'y a aucun menteur parmi les {forme}")
                else:
                    assertions_possibles.append(f"Il y a au moins un menteur parmi les {forme}")

            # "Il y a N menteurs dans les aliens de la forme X"
            nb_total_forme = sum(1 for row in self.grille for a in row if a and a.forme == forme)
            if nb_total_forme > 0:  # Ne générer que si la forme existe
                if alien.est_menteur:
                    # Donner un nombre incorrect
                    nombres_faux = [n for n in range(nb_total_forme + 1) if n != nb_menteurs_forme]
                    if nombres_faux:
                        n_faux = random.choice(nombres_faux)
                        assertions_possibles.append(f"Il y a {n_faux} menteur(s) parmi les {forme}")
                else:
                    assertions_possibles.append(f"Il y a {nb_menteurs_forme} menteur(s) parmi les {forme}")

        # Type 3: Assertions sur le nombre d'aliens par ligne
        for ligne_idx in range(self.hauteur):
            nb_aliens_ligne = sum(1 for a in self.grille[ligne_idx] if a)

            if alien.est_menteur:
                nombres_faux = [n for n in range(self.largeur + 1) if n != nb_aliens_ligne]
                if nombres_faux:
                    n_faux = random.choice(nombres_faux)
                    assertions_possibles.append(f"Il y a {n_faux} alien(s) dans la ligne {ligne_idx + 1}")
            else:
                assertions_possibles.append(f"Il y a {nb_aliens_ligne} alien(s) dans la ligne {ligne_idx + 1}")

        # Type 4: Assertions sur le nombre de menteurs par ligne
        for ligne_idx in range(self.hauteur):
            nb_menteurs_ligne = sum(1 for a in self.grille[ligne_idx] if a and a.est_menteur)

            if alien.est_menteur:
                nombres_faux = [n for n in range(self.largeur + 1) if n != nb_menteurs_ligne]
                if nombres_faux:
                    n_faux = random.choice(nombres_faux)
                    assertions_possibles.append(f"Il y a {n_faux} menteur(s) dans la ligne {ligne_idx + 1}")
            else:
                assertions_possibles.append(f"Il y a {nb_menteurs_ligne} menteur(s) dans la ligne {ligne_idx + 1}")

        # Choisir une assertion aléatoire
        if assertions_possibles:
            return random.choice(assertions_possibles)
        else:
            return "Je suis un alien"

    def _verifier_unicite_solution(self) -> bool:
        """
        Vérifie que la solution est unique en testant toutes les configurations possibles

        Returns:
            True si la solution est unique, False sinon
        """
        total_aliens = self.hauteur * self.largeur
        solutions_valides = []

        # Tester toutes les combinaisons possibles de menteurs
        for combinaison_menteurs in itertools.combinations(range(total_aliens), self.nb_menteurs):
            if self._tester_configuration(set(combinaison_menteurs)):
                solutions_valides.append(combinaison_menteurs)

                # Si on trouve plus d'une solution, on peut s'arrêter
                if len(solutions_valides) > 1:
                    return False

        return len(solutions_valides) == 1

    def _tester_configuration(self, indices_menteurs: Set[int]) -> bool:
        """
        Teste si une configuration de menteurs est cohérente avec les assertions

        Args:
            indices_menteurs: Ensemble des indices des aliens qui seraient menteurs

        Returns:
            True si la configuration est cohérente, False sinon
        """
        # Créer une configuration temporaire
        config = {}
        idx = 0
        for i in range(self.hauteur):
            for j in range(self.largeur):
                config[(i, j)] = idx in indices_menteurs
                idx += 1

        # Vérifier chaque assertion
        for i in range(self.hauteur):
            for j in range(self.largeur):
                alien = self.grille[i][j]
                est_menteur_config = config[(i, j)]
                assertion = alien.assertion

                # Évaluer si l'assertion serait vraie dans cette configuration
                assertion_vraie = self._evaluer_assertion(i, j, assertion, config)

                # Si l'alien est menteur, son assertion doit être fausse
                # Si l'alien dit la vérité, son assertion doit être vraie
                if est_menteur_config and assertion_vraie:
                    return False  # Incohérent
                if not est_menteur_config and not assertion_vraie:
                    return False  # Incohérent

        return True

    def _evaluer_assertion(self, i: int, j: int, assertion: str, config: dict) -> bool:
        """
        Évalue si une assertion est vraie dans une configuration donnée

        Args:
            i, j: Position de l'alien
            assertion: L'assertion à évaluer
            config: Configuration des menteurs {(i,j): bool}

        Returns:
            True si l'assertion est vraie, False sinon
        """
        # Voisins
        if "voisin de droite" in assertion:
            if j < self.largeur - 1:
                voisin_ment = config[(i, j + 1)]
                if "ment" in assertion and "dit la vérité" not in assertion:
                    return voisin_ment
                else:
                    return not voisin_ment

        if "voisin de gauche" in assertion:
            if j > 0:
                voisin_ment = config[(i, j - 1)]
                if "ment" in assertion and "dit la vérité" not in assertion:
                    return voisin_ment
                else:
                    return not voisin_ment

        if "voisin du haut" in assertion:
            if i > 0:
                voisin_ment = config[(i - 1, j)]
                if "ment" in assertion and "dit la vérité" not in assertion:
                    return voisin_ment
                else:
                    return not voisin_ment

        if "voisin du bas" in assertion:
            if i < self.hauteur - 1:
                voisin_ment = config[(i + 1, j)]
                if "ment" in assertion and "dit la vérité" not in assertion:
                    return voisin_ment
                else:
                    return not voisin_ment

        # Assertions sur les formes
        for forme in self.formes:
            if f"parmi les {forme}" in assertion:
                nb_menteurs_forme = sum(
                    1 for ii in range(self.hauteur) for jj in range(self.largeur)
                    if self.grille[ii][jj].forme == forme and config[(ii, jj)]
                )

                if "Il n'y a aucun menteur" in assertion:
                    return nb_menteurs_forme == 0
                elif "Il y a au moins un menteur" in assertion:
                    return nb_menteurs_forme > 0
                elif "Il y a" in assertion and "menteur(s)" in assertion:
                    # Extraire le nombre
                    try:
                        parts = assertion.split()
                        idx = parts.index("a") + 1
                        n = int(parts[idx])
                        return nb_menteurs_forme == n
                    except:
                        pass

        # Assertions sur les lignes
        if "dans la ligne" in assertion:
            try:
                # Extraire le numéro de ligne
                parts = assertion.split("ligne")
                ligne_num = int(parts[1].strip()) - 1  # Convertir en index 0

                if "alien(s)" in assertion and "menteur" not in assertion:
                    # Nombre d'aliens dans la ligne
                    nb_aliens = self.largeur
                    parts = assertion.split()
                    idx = parts.index("a") + 1
                    n = int(parts[idx])
                    return nb_aliens == n

                elif "menteur(s)" in assertion:
                    # Nombre de menteurs dans la ligne
                    nb_menteurs_ligne = sum(
                        1 for jj in range(self.largeur)
                        if config[(ligne_num, jj)]
                    )
                    parts = assertion.split()
                    idx = parts.index("a") + 1
                    n = int(parts[idx])
                    return nb_menteurs_ligne == n
            except:
                pass

        return False

    def afficher(self):
        """Affiche la grille de manière lisible"""
        print(f"\n{'=' * 80}")
        print(f"GRILLE D'ALIENS ({self.hauteur}x{self.largeur}) - {self.nb_menteurs} menteur(s)")
        print(f"{'=' * 80}\n")

        for i in range(self.hauteur):
            print(f"Ligne {i + 1}:")
            for j in range(self.largeur):
                alien = self.grille[i][j]
                print(f"  [{i},{j}] {alien}")
            print()

    def afficher_solution(self):
        """Affiche uniquement les positions des menteurs"""
        print(f"\n{'=' * 40}")
        print("SOLUTION")
        print(f"{'=' * 40}\n")

        menteurs = []
        for i in range(self.hauteur):
            for j in range(self.largeur):
                alien = self.grille[i][j]
                if alien.est_menteur:
                    menteurs.append(f"[{i},{j}] {alien.forme}")

        print(f"Les {self.nb_menteurs} menteur(s) sont à :")
        for menteur in menteurs:
            print(f"  🔴 {menteur}")
        print()

    def exporter_latex(self, nom_fichier: str = "grille_aliens.tex"):
        """
        Exporte la grille au format LaTeX

        Args:
            nom_fichier: Nom du fichier LaTeX à générer
        """
        # Mapping des emojis vers des commandes LaTeX
        emoji_mapping = {
            "👽": r"\alien",
            "🛸": r"\saucer",
            "🤖": r"\robot",
            "👾": r"\invader",
            "🦎": r"\lizard"
        }

        latex_content = []
        latex_content.append(r"% Grille d'aliens - À intégrer dans votre document LaTeX")
        latex_content.append(r"% Nécessite les packages: tikz, array, xcolor")
        latex_content.append(r"")
        latex_content.append(r"\begin{center}")
        latex_content.append(r"\begin{tikzpicture}[scale=1.2]")
        latex_content.append(r"")
        latex_content.append(r"% Définition des styles")
        latex_content.append(r"\tikzset{")
        latex_content.append(
            r"    alien/.style={rectangle, draw=black, thick, minimum width=3cm, minimum height=2cm, align=center, font=\small},")
        latex_content.append(r"}")
        latex_content.append(r"")

        # Générer les cellules
        for i in range(self.hauteur):
            for j in range(self.largeur):
                alien = self.grille[i][j]
                x = j * 3.5
                y = -i * 2.5

                # Remplacer l'emoji par sa commande LaTeX (ou garder l'emoji)
                forme_latex = emoji_mapping.get(alien.forme, alien.forme)

                # Échapper les caractères spéciaux LaTeX dans l'assertion
                assertion_latex = alien.assertion.replace("_", r"\_")
                assertion_latex = assertion_latex.replace("#", r"\#")
                assertion_latex = assertion_latex.replace("&", r"\&")

                # Découper l'assertion en plusieurs lignes si nécessaire
                max_chars = 25
                mots = assertion_latex.split()
                lignes = []
                ligne_courante = []
                longueur_courante = 0

                for mot in mots:
                    if longueur_courante + len(mot) + 1 <= max_chars:
                        ligne_courante.append(mot)
                        longueur_courante += len(mot) + 1
                    else:
                        if ligne_courante:
                            lignes.append(" ".join(ligne_courante))
                        ligne_courante = [mot]
                        longueur_courante = len(mot)

                if ligne_courante:
                    lignes.append(" ".join(ligne_courante))

                assertion_multiline = " \\\\ ".join(lignes)

                latex_content.append(f"\\node[alien] at ({x},{y}) {{")
                latex_content.append(f"    \\textbf{{{forme_latex}}} \\\\")
                latex_content.append(f"    \\vspace{{0.2cm}} \\\\")
                latex_content.append(f"    \\textit{{{assertion_multiline}}}")
                latex_content.append(f"}};")
                latex_content.append(r"")

        latex_content.append(r"\end{tikzpicture}")
        latex_content.append(r"\end{center}")
        latex_content.append(r"")
        latex_content.append(r"% Solution (à commenter ou supprimer pour la version puzzle)")
        latex_content.append(r"% \vspace{1cm}")
        latex_content.append(r"% \textbf{Solution:}")
        latex_content.append(r"% \begin{itemize}")

        for i in range(self.hauteur):
            for j in range(self.largeur):
                alien = self.grille[i][j]
                if alien.est_menteur:
                    forme_latex = emoji_mapping.get(alien.forme, alien.forme)
                    latex_content.append(f"% \\item Position [{i + 1},{j + 1}]: {forme_latex} (MENTEUR)")

        latex_content.append(r"% \end{itemize}")

        # Écrire dans le fichier
        with open(nom_fichier, 'w', encoding='utf-8') as f:
            f.write("\n".join(latex_content))

        print(f"✅ Fichier LaTeX généré: {nom_fichier}")


def main():
    """Fonction principale"""
    print("\n" + "=" * 60)
    print("🛸 GÉNÉRATEUR DE GRILLE D'ALIENS AVEC VALIDATION 🛸")
    print("=" * 60 + "\n")

    # Paramètres
    largeur = int(input("Largeur de la grille (ex: 4) : ") or "4")
    hauteur = int(input("Hauteur de la grille (ex: 3) : ") or "3")

    total_aliens = largeur * hauteur
    nb_menteurs = int(input(f"Nombre de menteurs (max {total_aliens}) : ") or "2")

    if nb_menteurs > total_aliens:
        print(f"⚠️  Trop de menteurs ! Maximum : {total_aliens}")
        nb_menteurs = total_aliens

    print("\n🔄 Génération en cours...\n")

    # Générer la grille avec vérification d'unicité
    grille = GrilleAliens(largeur, hauteur, nb_menteurs)

    if grille.generer_grille(max_tentatives=50):
        grille.afficher()

        # Demander si on veut voir la solution
        reponse = input("\nVoulez-vous voir la solution ? (o/n) : ").lower()
        if reponse == 'o':
            grille.afficher_solution()

        # Exporter en LaTeX
        reponse_latex = input("\nVoulez-vous exporter en LaTeX ? (o/n) : ").lower()
        if reponse_latex == 'o':
            nom_fichier = input("Nom du fichier (défaut: grille_aliens.tex) : ") or "grille_aliens.tex"
            grille.exporter_latex(nom_fichier)
    else:
        print("\n❌ Impossible de générer une grille avec solution unique.")
        print("💡 Essayez avec des paramètres différents.")


if __name__ == "__main__":
    main()


def obtenir_formes_disponibles():
    """Retourne une liste de formes compatibles LaTeX"""
    formes = [
        {
            'code': r"""\begin{tikzpicture}[scale=0.3]
\draw[fill=black] (0,0) circle (0.5);
\end{tikzpicture}""",
            'nom': 'Cercle',
            'simple': r'\textbullet'
        },
        {
            'code': r"""\begin{tikzpicture}[scale=0.3]
\draw[fill=black] (0,0) rectangle (1,1);
\end{tikzpicture}""",
            'nom': 'Carré',
            'simple': r'\rule{0.5em}{0.5em}'
        },
        {
            'code': r"""\begin{tikzpicture}[scale=0.3]
\draw[fill=black] (0.5,0) -- (1,1) -- (0,1) -- cycle;
\end{tikzpicture}""",
            'nom': 'Triangle',
            'simple': r'$\blacktriangle$'
        },
        {
            'code': r"""\begin{tikzpicture}[scale=0.3]
\draw[fill=black] (0.5,0) -- (1,0.5) -- (0.5,1) -- (0,0.5) -- cycle;
\end{tikzpicture}""",
            'nom': 'Losange',
            'simple': r'$\blacklozenge$'
        },
        {
            'code': r"""\begin{tikzpicture}[scale=0.3]
\draw[fill=black] (0.5,0) -- (1,0.4) -- (0.8,1) -- (0.2,1) -- (0,0.4) -- cycle;
\end{tikzpicture}""",
            'nom': 'Étoile',
            'simple': r'$\star$'
        },
        {
            'code': r"""\begin{tikzpicture}[scale=0.3]
\draw[fill=white,draw=black] (0,0) circle (0.5);
\end{tikzpicture}""",
            'nom': 'Cercle vide',
            'simple': r'$\circ$'
        },
        {
            'code': r"""\begin{tikzpicture}[scale=0.3]
\draw[fill=white,draw=black] (0,0) rectangle (1,1);
\end{tikzpicture}""",
            'nom': 'Carré vide',
            'simple': r'$\square$'
        },
        {
            'code': r"""\begin{tikzpicture}[scale=0.3]
\draw[fill=white,draw=black] (0.5,0) -- (1,1) -- (0,1) -- cycle;
\end{tikzpicture}""",
            'nom': 'Triangle vide',
            'simple': r'$\triangle$'
        },
        {
            'code': r"""\begin{tikzpicture}[scale=0.3]
\draw[fill=black] (0.5,1) -- (1,0.6) -- (0.8,0) -- (0.2,0) -- (0,0.6) -- cycle;
\end{tikzpicture}""",
            'nom': 'Pentagone',
            'simple': r'$\pentagon$'
        },
        {
            'code': r"""\begin{tikzpicture}[scale=0.3]
\draw[fill=gray] (0,0) circle (0.5);
\end{tikzpicture}""",
            'nom': 'Cercle gris',
            'simple': r'$\bullet$'
        },
    ]

    # Version simplifiée sans TikZ (plus compatible)
    formes_simples = [
        {'code': r'\textbullet', 'nom': 'Rond plein'},
        {'code': r'\rule{0.8em}{0.8em}', 'nom': 'Carré plein'},
        {'code': r'$\blacktriangle$', 'nom': 'Triangle plein'},
        {'code': r'$\blacklozenge$', 'nom': 'Losange plein'},
        {'code': r'$\star$', 'nom': 'Étoile'},
        {'code': r'$\circ$', 'nom': 'Rond vide'},
        {'code': r'$\square$', 'nom': 'Carré vide'},
        {'code': r'$\triangle$', 'nom': 'Triangle vide'},
        {'code': r'$\bigtriangledown$', 'nom': 'Triangle inversé'},
        {'code': r'$\diamondsuit$', 'nom': 'Carreau'},
        {'code': r'$\heartsuit$', 'nom': 'Cœur'},
        {'code': r'$\clubsuit$', 'nom': 'Trèfle'},
        {'code': r'$\spadesuit$', 'nom': 'Pique'},
        {'code': r'$\bigstar$', 'nom': 'Grande étoile'},
        {'code': r'$\bullet$', 'nom': 'Puce'},
    ]

    return formes