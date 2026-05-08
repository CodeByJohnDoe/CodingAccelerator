# Exercice Coding Accelerator
# Affichage du contenu d'un fichier

import sys

def afficher_fichier(nom_fichier):
    try:
        with open(nom_fichier, 'r') as fichier:
            return fichier.read()
    except (FileNotFoundError, PermissionError, IOError):
        return "error"

# --- Test ---
if __name__ == "__main__":
    # Vérification des arguments
    if len(sys.argv) != 2:
        print("error")
        sys.exit()

    nom_fichier = sys.argv[1]

    contenu = afficher_fichier(nom_fichier)
    if contenu == "error":
        print("error")
        sys.exit()
    else:
        print(contenu, end='')
