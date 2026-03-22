# Exercice Coding Accelerator
 
# Verifier si une chaine est dans une autre

# Importation des modules
import sys

# Fonctionnement principal du programme
def charinchar() :
    error = "error"
    if len(sys.argv) != 3 :
        return sys.exit() 

    if len(sys.argv[1]) < len(sys.argv[2]) :
        return error 
    
    check = False
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
    if arg2 in arg1 :
        check = True
    
    return check
                
# Resultat
print(charinchar())
