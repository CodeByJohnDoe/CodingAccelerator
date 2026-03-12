# Exercice Coding Accelerator

# Créer une fonction pour lire les arguments entrant dans le programme et les afficher

# Importation des modules
import sys

# Fonctionnement du programme
def afficher_arguments():

    for x in range(1, len(sys.argv)):
        print(sys.argv[x])

# Appeler le résultat
afficher_arguments()