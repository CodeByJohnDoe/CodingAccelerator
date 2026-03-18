# Exercice Coding Accelerator
 
# Afficher les arguments reçus à l'envers

# Importation des modules
import sys

# Fonctionnement principal du programme
def arg_reverse() :
    if len(sys.argv) >= 1:
        input = sys.argv[1:]
        for char in input[::-1]:
            print(char)    
    else    :
        print("erreur, merci de d'entrer au moins un argument :)")

# Resultat
arg_reverse()
