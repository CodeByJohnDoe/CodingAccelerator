# Exercice Coding Accelerator
 
# Résultat d'une puissance sans pow

# Importation des modules
import sys

# Fonctionnement du programme
def puissance() :
    # Verification du nombre d'arguments
    argv_count = len(sys.argv) - 1 

    if argv_count == 2 :
        argv_number_check_1 = sys.argv[1].isnumeric()
        argv_number_check_2 = sys.argv[2].isnumeric()

        # Verification qu'on a bien des nombres 
        if argv_number_check_1 == True and argv_number_check_2 == True : 
            argv_1 = int(sys.argv[1])
            argv_2 = int(sys.argv[2])
            answer = 0

            # Exposant 0
            if argv_2 == 0:
                answer = 1
            # Zéro
            elif argv_1 == 0:
                answer = 0

            # Calcul
            else :
                answer = argv_1
                while argv_2 != 1:
                    answer = answer * argv_1
                    argv_2 -= 1

            print(answer)       

                
        else:
            print("erreur.")

    else:
        print("erreur.")
# Appeler le résultat
puissance()