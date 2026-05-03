import argparse
import csv
import subprocess

from generator import InterrogationGenerator

def main():
    parser = argparse.ArgumentParser(description='Générateur d\'interrogations NSI')
    parser.add_argument('--nom', default='Interrogation NSI',
                       help='Nom de l\'interrogation')
    parser.add_argument('--classe', default='NSI',
                       help='Classe')
    
    args = parser.parse_args()

    generator = InterrogationGenerator()

    with open("eleves.csv", newline="", encoding="utf-8") as fichier:
        lecteur = csv.DictReader(fichier, delimiter=',')
        i=0
        for ligne in lecteur:
            if i==0:
                if ligne["eleve"] == "":
                    i+=1
                continue
            print(ligne)
            if ligne["eleve"] == "":
                try:
                    subprocess.run(
                        'pdfunite output/*.pdf output.pdf',
                        check=True,
                        capture_output=True
                    )
                    break
                except subprocess.CalledProcessError as e:
                    print(f"Erreur lors du pdfunite : {e}")
                    raise

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

if __name__ == "__main__":
    main()