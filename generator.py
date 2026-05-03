import os
import subprocess
import random
from datetime import datetime
from exercises import writing, reading, testing, logic

class InterrogationGenerator:
    def __init__(self):
        self.exercises_modules = {
            'e': writing,
            'a': reading,
            't': testing,
            'l': logic
        }
        self.counts = {
            'e': 3,
            'a': 5,
            't': 5,
            'l': 3
        }
    
    def generate_interrogation(self, axe, niveau, nom, classe, output_path, eleve="..."):
        """Génère une interrogation complète"""
        # Générer 5 exercices
        module = self.exercises_modules[axe]
        exercises = module.generate_exercises(niveau, count=self.counts[axe])
        
        # Créer le contenu LaTeX
        latex_content = self.create_latex_content(
            nom=nom,
            classe=classe,
            axe=axe,
            niveau=niveau,
            exercises=exercises,
            eleve=eleve
        )
        
        # Compiler en PDF
        self.compile_to_pdf(latex_content, output_path)
        return exercises
    
    def create_latex_content(self, nom, classe, axe, niveau, exercises,eleve):
        """Crée le contenu LaTeX"""
        axe_names = {
            'e': 'Écriture de code Python',
            'a': 'Analyse de code Python',
            't': 'Tests de code Python',
            'l': 'Logique'
        }
        
        date = datetime.now().strftime("%d/%m/%Y")
        
        exercises_latex = "\n\n".join([
            f"\\section*{{Exercice {i+1}}}\n{ex['content']}"
            for i, ex in enumerate(exercises)
        ])
        
        template = r"""\documentclass[12pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[french]{babel}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{amsmath}
\usepackage{tikz}
\usepackage{listings}
\usepackage{xcolor}
\usepackage{geometry}
\usepackage{fancyhdr}
\usepackage{array} % pour tableaux plus propres

\newcommand{\cadreligne}{
  \fbox{%
    \parbox[c][5cm][t]{10cm}{%
      \vspace{0.45cm}
      \hspace{10cm}
      \hrule height 0.2pt
      \vspace{0.45cm}
      \hrule height 0.2pt
      \vspace{0.45cm}
      \hrule height 0.2pt
      \vspace{0.45cm}
      \hrule height 0.2pt
      \vspace{0.45cm}
      \hrule height 0.2pt
      \vspace{0.45cm}
      \hrule height 0.2pt
      \vspace{0.45cm}
      \hrule height 0.2pt
      \vspace{0.45cm}
      \hrule height 0.2pt
      \vspace{0.45cm}
      \hrule height 0.2pt
      \vspace{0.45cm}
      \hrule height 0.2pt
    }
  }
}

\geometry{margin=2cm}

% Configuration pour le code Python
\lstset{
    language=Python,
    basicstyle=\ttfamily\small,
    keywordstyle=\color{blue},
    commentstyle=\color{gray}\itshape,
    stringstyle=\color{red},
    numbers=left,
    numberstyle=\tiny\color{gray},
    stepnumber=1,
    numbersep=8pt,
    backgroundcolor=\color{gray!10},
    frame=single,
    breaklines=true,
    tabsize=4,
    showstringspaces=false
}

\pagestyle{fancy}
\fancyhf{}
\lhead{""" + classe + r"""}
\rhead{""" + date + r"""}
\cfoot{\thepage}

\begin{document}

\begin{center}
    {\Large \textbf{""" + nom + r"""}}\\[0.5cm]
    {\large """ + axe_names[axe] + r""" -- Niveau """ + str(niveau) + r"""}\\[0.3cm]
    Nom : """ + eleve + r"""
\end{center}

\vspace{1cm}

""" + exercises_latex + r"""


\vspace{0.5cm}
\hrule
\vspace{0.5cm}

\begin{tabular}{ >{\bfseries}l  c  c  c  c  |  >{\bfseries}l  c  c  c  c }
\multicolumn{5}{c}{\bfseries Prochain test en cas d'échec} & \multicolumn{5}{c}{\bfseries Prochain test en cas de réussite} \\
& Analyse & Écriture & Test & Logique & & Analyse & Écriture & Test & Logique \\
 & \fbox{\phantom{X}} & \fbox{\phantom{X}} & \fbox{\phantom{X}} & \fbox{\phantom{X}} &
 & \fbox{\phantom{X}} & \fbox{\phantom{X}} & \fbox{\phantom{X}} & \fbox{\phantom{X}} \\
\end{tabular}

\end{document}"""
        
        return template
    
    def generate_corrige(self, entries, nom, classe, output_path):
        """Génère le PDF de corrigé pour tous les élèves en analyse.

        entries : liste de dicts  {'eleve': str, 'niveau': int, 'exercises': list}
        """
        if not entries:
            return

        date = datetime.now().strftime("%d/%m/%Y")

        blocs = []
        for entry in entries:
            eleve   = entry['eleve']
            niveau  = entry['niveau']
            exos    = entry['exercises']
            items   = "\n".join(
                f"\\item {ex['answer']}"
                for ex in exos
            )
            blocs.append(
                f"\\subsection*{{\\normalfont {eleve} — Analyse N{niveau}}}\n"
                f"\\begin{{enumerate}}\n{items}\n\\end{{enumerate}}"
            )

        corps = "\n\n".join(blocs)

        latex = (
            r"\documentclass[11pt,a4paper]{article}" "\n"
            r"\usepackage[utf8]{inputenc}" "\n"
            r"\usepackage[french]{babel}" "\n"
            r"\usepackage[T1]{fontenc}" "\n"
            r"\usepackage{lmodern}" "\n"
            r"\usepackage{amsmath}" "\n"
            r"\usepackage{geometry}" "\n"
            r"\usepackage{fancyhdr}" "\n"
            r"\geometry{margin=2cm}" "\n"
            r"\pagestyle{fancy}\fancyhf{}" "\n"
            r"\lhead{" + classe + r"}"
            r"\rhead{" + date + r" — Corrigé analyse}"
            r"\cfoot{\thepage}" "\n"
            r"\begin{document}" "\n"
            r"\begin{center}{\Large\textbf{" + nom + r" — Corrigé}}\end{center}" "\n"
            r"\vspace{0.5cm}" "\n"
            + corps + "\n"
            r"\end{document}"
        )

        self.compile_to_pdf(latex, output_path)

    def compile_to_pdf(self, latex_content, output_path):
        """Compile le LaTeX en PDF"""
        # Créer les dossiers nécessaires
        os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
        os.makedirs('temp', exist_ok=True)
        
        # Écrire le fichier .tex temporaire
        tex_path = 'temp/interro.tex'
        with open(tex_path, 'w', encoding='utf-8') as f:
            f.write(latex_content)
        
        # Compiler avec pdflatex
        try:
            subprocess.run(
                ['pdflatex', '-output-directory=temp', '-interaction=nonstopmode', tex_path],
                check=True,
                capture_output=True
            )
            # Deuxième compilation pour les références
            subprocess.run(
                ['pdflatex', '-output-directory=temp', '-interaction=nonstopmode', tex_path],
                check=True,
                capture_output=True
            )
            
            # Déplacer le PDF généré
            os.rename('temp/interro.pdf', output_path)
            print(f"PDF généré avec succès : {output_path}")
            
        except subprocess.CalledProcessError as e:
            print(f"Erreur lors de la compilation LaTeX : {e}")
            raise