# Exercice Coding Accelerator
 
# Pair et impair

# Importation des modules
import sys

# Set up des variables
argv_count = len(sys.argv) - 1 
argv_number_check = sys.argv[1].isnumeric()

# Fonctionnement du programme
def pair_ou_impair():
    if argv_count == 1 and argv_number_check == True:
        if int(sys.argv[1]) % 2 == 0:
            print("pair")
        else:
            print("impair")
    else:
        print("tu ne me la mettra pas à l'envers")

# Appeler le résultat
pair_ou_impair()