# Exercice Coding Accelerator
 
# Vérifier si une chaine contient uniquement des chiffres

# Importation des modules
import sys

# Fonctionnement principal du programme
def all_num() :
    error = "false"
    if len(sys.argv) != 2 :
        return sys.exit()
    argv = sys.argv[1]

    # Scrutation pour avoir uniquement des chiffres
    for i in range (len(argv)) :
        if not (ord(argv[i]) >= 48 and ord(argv[i]) <= 57)  :
            return error

    return 'true'
# Resultat
print(all_num())
