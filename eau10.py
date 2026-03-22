# Exercice Coding Accelerator
 
# Recherhce le dernier argment dans un tableau

# Importation des modules
import sys

# Fonctionnement principal du programme
def arg_search() :
    error = "-1"
    if len(sys.argv) < 3 :
        sys.exit()
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
print(arg_search())
