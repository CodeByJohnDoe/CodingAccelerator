# Exercice Coding Accelerator
 
# Résultat d'un nombre premier

# Importation des modules
import sys
from toolbox import modulo

# Fonctionnement principal du programme
def premier() :
    # Verification du nombre d'arguments
    argv_count = len(sys.argv) - 1 

    if argv_count == 1 and sys.argv[1].isnumeric() == True :

        argv_1 = int(sys.argv[1])
        oui = f'Oui, {argv_1} est un nombre premier.'
        non = f'Non, {argv_1} n\'est pas un nombre premier.'

        # Exculusion de 0 et 1 + 2 pour init boucle
        if argv_1 == 0 or argv_1 == 1 or argv_1 == 2:
            print(oui)

        # Nombre premier de 3 ou plus
        else:
            for i in range(2, argv_1 - 1):
                if modulo(argv_1, i )[1] == 0:
                    print(non)
                    break
            else:
                print(oui)

    else:
        print("erreur, veuillez entrer un nombre entier positif supérieur à 1.")

# Resultat
premier()