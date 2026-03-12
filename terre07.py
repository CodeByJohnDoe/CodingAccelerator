# Exercice Coding Accelerator
 
# Nombre de caractères d'une chaine de caractère dans fontion de comptage toute faite

# Importation des modules
import sys


# Fonctionnement du programme
def nombre_de_caracteres_d_une_chaine_de_caractere():
    result = 0
    if len(sys.argv) == 2 :
        input = sys.argv[1]

        while input:
            input = input[1:]
            result += 1
        print(result)
    else :
        print('erreur.')
        
nombre_de_caracteres_d_une_chaine_de_caractere()