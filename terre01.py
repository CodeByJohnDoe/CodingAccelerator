# Exercice Coding Accelerator

# Créer une fonction affichant son nom de fichier

import os

def afficher_nom_fichier():
    result = os.path.basename(__file__)
    print(result)

afficher_nom_fichier()