# Exercice Coding Accelerator
# Afficher un rectangle dans le terminal

import sys

def dessiner_rectangle(largeur: int, hauteur: int) :
    ## Première ligne
        # Cas spécial : rectangle 1xN (ligne verticale)
        if largeur == 1:
            for h in range(hauteur):
                if h == 0 :
                    print("o")
                if h != hauteur - 1 :
                    print("|")
                else :
                    print("o")
            return

        # Cas spécial : rectangle Nx1 (ligne horizontale)
        if hauteur == 1:
            print("o" + "-" * (largeur - 1) + "o")
            return

        # Cas général : rectangle avec coins et côtés
        print("o" + "-" * (largeur - 1) + "o")

    ## Lignes du milieu
        for l in range(hauteur - 2):
            print("|" + " " * (largeur - 1) + "|")

    ## Ligne du bas
        print("o" + "-" * (largeur - 1) + "o")

def main():
    # Vérification des arguments d'entrée
    if len(sys.argv) != 3:
        print("error")
        sys.exit(1)

    # Récupération de la largeur et de la hauteur
    try:
        largeur = int(sys.argv[1])
        hauteur = int(sys.argv[2])
    except ValueError:
        print("error")
        sys.exit(1)

    # Validation des dimensions
    if largeur <= 0 or hauteur <= 0:
        print("error")
        sys.exit(1)

    # Dessin du rectangle
    dessiner_rectangle(largeur, hauteur)

# --- Test ---
if __name__ == "__main__":
    main()