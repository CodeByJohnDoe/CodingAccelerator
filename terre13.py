# Exercice Coding Accelerator
 
# Afficher la valeur du mileu entre 3 entiers

# Importation des modules
import sys



# Fonctionnement principal du programme
def middle_3():
    error = "error, merci d'entrer trois nombre différents sépraré chacun d'un espace. (11 40 34)"
    argv_count = len(sys.argv) - 1 

    # Sécurité : vérifier si l'argument existe avant d'y accéder
    if argv_count != 3:
        print(error)
        return

    input_1, input_2, input_3 = sys.argv[1], sys.argv[2], sys.argv[3]

    # Vérification de l'acquision de nombre différents
    if (input_1.isnumeric() and input_2.isnumeric() and input_3.isnumeric()) and (input_1 != input_2 and input_1 != input_3 and input_2 != input_3) :
        if (input_1 < input_2 and input_1 > input_3) or (input_1 > input_2 and input_1 < input_3) :
            print(input_1)
        elif (input_2 < input_1 and input_2 > input_3) or (input_2 > input_1 and input_2 < input_3) :
            print(input_2)
        else :
            print(input_3)
    else :
        print(error)

# Resultat
middle_3()