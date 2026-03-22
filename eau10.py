# Exercice Coding Accelerator
 
# Recherhce le dernier argment dans un tableau

# Importation des modules
import sys

# Fonctionnement principal du programme
def arg_search() :
    error = "-1"
    if len(sys.argv) < 3 :
        sys.exit()
    list = sys.argv[1:-1]
    target = sys.argv[-1]
    if target in list :
        for i in range(len(list)) :
            if target == list[i] :
                return i
    else :
        return error

# Resultat
print(arg_search())
