# Exercice Coding Accelerator
 
# Afficher des valeurs comprises entre deux nombres min inclus et max exclus

# Importation des modules
import sys

# Fonctionnement principal du programme
def min_max() :
    error = "error"
    if len(sys.argv) != 3 :
        return error 
    argv1 = str(sys.argv[1])
    argv2 = sys.argv[2]
    

    if argv1.isdecimal() and argv2.isdecimal() :
        argv1 = int(argv1)
        argv2 = int(argv2)
        delta = 0
        min = 0

        # Paramattrage de la boucle
        if argv1 == argv2 : 
            return error
        if argv1 > argv2 : 
            min = argv2
            delta = argv1 - argv2
        else :
            min = argv1
            delta = argv2 - argv1

        result = [min]
        for i in range(delta) :
            result.append(min + i)
    return (" ".join(map(str , result))) # Découverte de la fonction Map très interessant pour éviter les patés de boucle

# Resultat
print(min_max())
