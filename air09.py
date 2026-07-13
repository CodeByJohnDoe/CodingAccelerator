# Exercice Coding Accelerator
# Affichage du contenu d'un fichier (version corrigée)

import sys
import os

def afficher_fichier(nom_fichier):
    # Vérification que le fichier existe et est accessible
    if not os.path.isfile(nom_fichier):
        return "error: fichier introuvable"

    # Vérification des permissions
    if not os.access(nom_fichier, os.R_OK):
        return "error: permission refusée"

    try:
        with open(nom_fichier, 'r', encoding='utf-8') as fichier:
            contenu = fichier.read()
            return contenu if contenu else ""  # Retourne "" si le fichier est vide
    except Exception as e:
        return f"error: {str(e)}"

# --- Test ---
if __name__ == "__main__":
    # Vérification des arguments
    if len(sys.argv) != 2:
        print("error: utilisation attendue: python air09.py <nom_fichier>")
        sys.exit(1)

    nom_fichier = sys.argv[1]
    contenu = afficher_fichier(nom_fichier)

    if contenu.startswith("error"):
        print(contenu)
        sys.exit(1)
    else:
        print(contenu, end='')