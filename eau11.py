# Exercice Coding Accelerator
 
# Afficher la valeur mini absolue entre deux elements d'un tableau

# Importation des modules
import sys
from math import sqrt

# Fonctionnement principal du programme
def low_min() :
    error = "error"
    if len(sys.argv) < 3 :
        return error , sys.exit() 
    argv = sys.argv[1:]
    tobecompare =[]    

    # Recherche des nombres et mise en valeur absolue
    for x in range (len(argv)) :
        if int(argv[x]) :
            tobecompare.append(sqrt(int(argv[x])*int(argv[x])))
        else :
            return error , sys.exit() 
        
    tobecompare = sorted(tobecompare)
    min = tobecompare[-1] - tobecompare[0]
    for i in range(len(tobecompare) - 1) :
        min_test = tobecompare[i + 1 ] - tobecompare[i]
        if  min_test < min :
            min = min_test
    return min
                
# Resultat
print(low_min())
