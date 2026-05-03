import argparse
import csv
import subprocess
import os

from generator import InterrogationGenerator

def assemblage_fichiers(c):
    print(f"Génération du fichier global pour la classe {c}")
    try:
        os.system(f'pdfunite output/*.pdf output_classe_{c}.pdf')

        os.system('mkdir -p output/indiv; mv output/*.pdf output/indiv/')
        return c+1
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors du pdfunite : {e}")
        raise

def main():
    parser = argparse.ArgumentParser(description='Générateur d\'interrogations NSI')
    parser.add_argument('--nom', default='Interrogation NSI',
                       help='Nom de l\'interrogation')
    parser.add_argument('--classe', default='NSI',
                       help='Classe')
    
    args = parser.parse_args()

    generator = InterrogationGenerator()

    with open("eleves.csv", newline="", encoding="utf-8") as fichier:
        lecteur = csv.DictReader(fichier, delimiter=';')
        c=1
        for ligne in lecteur:
            print(ligne)
            if ligne["eleve"] == "":
                c=assemblage_fichiers(c)

            else:
                path = f"output/{ligne["eleve"].replace(" ","_")}.pdf"
                print(path)
                generator.generate_interrogation(
                    axe=ligne["choix"],
                    niveau=int(ligne[ligne["choix"]])+1,
                    nom=args.nom,
                    classe=args.classe,
                    output_path=path,
                    eleve=ligne["eleve"]
                )
                print(f"Interrogation générée : {path}")
        assemblage_fichiers(c)

if __name__ == "__main__":
    main()