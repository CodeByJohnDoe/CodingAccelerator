# Exercice Coding Accelerator
 
# Reste d'une division entre deux nombres 

# Importation des modules
import sys

# Set up des variables
argv_count = len(sys.argv) - 1 

# Fonctionnement du programme
def reste_de_la_division():

    # Verification du nombre d'arguments
    if argv_count == 2 :
        argv_number_check_1 = sys.argv[1].isnumeric()
        argv_number_check_2 = sys.argv[2].isnumeric()

        # Verification qu'on a bien des nombres 
        if argv_number_check_1 == True and argv_number_check_2 == True : 
            argv_1 = int(sys.argv[1])
            argv_2 = int(sys.argv[2])
            # Vérificartion que les nombres ne sont pas égaux à 0 et que le premier nombre est supérieur au second
            if argv_1 != 0 and argv_2 != 0 and argv_1 >= argv_2:
                print("résulat : " + str(argv_1 // argv_2))
                print("reste   : " + str(argv_1 % argv_2))
            else:
                print("erreur.")
        else:
            print("erreur.")

    else:
        print("erreur.")

# Appeler le résultat
reste_de_la_division()
