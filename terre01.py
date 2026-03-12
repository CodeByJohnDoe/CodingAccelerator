# Exercice Coding Accelerator

# Créer une fonction affichant son nom de fichier

# Importation des modules
import os

# Fonctionnement du programme
def afficher_nom_fichier():
    result = os.path.basename(__file__)
    print(result)

# Affichage du résultat
afficher_nom_fichier()