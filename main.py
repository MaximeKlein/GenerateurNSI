import argparse
import csv
import subprocess
import os

from generator import InterrogationGenerator

def assemblage_fichiers(c, generator, corrige_entries, nom, classe):
    print(f"Génération du fichier global pour la classe {c}")
    try:
        os.system(f'pdfunite output/*.pdf output_classe_{c}.pdf')
        os.system('mkdir -p output/indiv; mv output/*.pdf output/indiv/')
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors du pdfunite : {e}")
        raise

    if corrige_entries:
        corrige_path = f"output_corrige_{c}.pdf"
        generator.generate_corrige(corrige_entries, nom, classe, corrige_path)
        print(f"Corrigé analyse généré : {corrige_path}")

    return c + 1


def main():
    parser = argparse.ArgumentParser(description='Générateur d\'interrogations NSI')
    parser.add_argument('--nom', default='Interrogation NSI',
                       help='Nom de l\'interrogation')
    parser.add_argument('--classe', default='NSI',
                       help='Classe')

    args = parser.parse_args()

    generator = InterrogationGenerator()
    corrige_entries = []

    with open("eleves.csv", newline="", encoding="utf-8") as fichier:
        lecteur = csv.DictReader(fichier, delimiter=';')
        c = 1
        for ligne in lecteur:
            print(ligne)
            if ligne["eleve"] == "":
                c = assemblage_fichiers(c, generator, corrige_entries,
                                        args.nom, args.classe)
                corrige_entries = []
            else:
                axe    = ligne["choix"]
                niveau = int(ligne[axe]) + 1
                path   = f"output/{ligne['eleve'].replace(' ', '_')}.pdf"
                print(path)

                exercises = generator.generate_interrogation(
                    axe=axe,
                    niveau=niveau,
                    nom=args.nom,
                    classe=args.classe,
                    output_path=path,
                    eleve=ligne["eleve"]
                )
                print(f"Interrogation générée : {path}")

                if axe == 'a':
                    corrige_entries.append({
                        'eleve':     ligne["eleve"],
                        'niveau':    niveau,
                        'exercises': exercises,
                    })

        assemblage_fichiers(c, generator, corrige_entries, args.nom, args.classe)
        corrige_entries = []

if __name__ == "__main__":
    main()