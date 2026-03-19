# Exercice Coding Accelerator
 
# Afficher le prochain nombre premier

# Importation des modules
import sys

# Fonctionnement principal du programme
def show_next() :
    error = "-1"
    if len(sys.argv) != 2 :
        return error 
        
    arg = sys.argv[1]
    if not arg.isnumeric() : #  isnumercic prend uniquement des chiffres possitif entier
        return error

    arg = int(arg)
    if arg == 0 :
        print(1)
    if arg == 1 :
        print(2)

    check = [False]  
    while not all(check):
        check = [True]  
        for i in range(2, arg -1) :
            if arg % i == 0 :
                check = [False]  
                arg += 1
            else :
                exit
            
    return arg
                
# Resultat
print(show_next())
