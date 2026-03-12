# Exercice Coding Accelerator
 
# Inverser une chaine de caractère sans reversz

# Importation des modules
import sys

# Set up des variables
argv_count = len(sys.argv) - 1 

# Fonctionnement du programme
def inverser_chaine_de_caractere():

    if argv_count == 1 :
        argv = "".join(sys.argv[1])
        result = []
        len_argv = len(sys.argv[1])
        for x in range(len_argv):
            result.append(argv[len_argv - x - 1]) # Le 1 permet de ne pas prendre en compte le caractère de fin de chaine pour partir de la fin de la chaine
        print(''.join(result))
    else:
        print("erreur.")

# Appeler le résultat
inverser_chaine_de_caractere()