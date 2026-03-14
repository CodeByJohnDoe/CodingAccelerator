# Exercice Coding Accelerator
 
# Résultat d'une racine sans sqrt

# Importation des modules
import sys

# Fonctionnement principal du programme
def racine() :
    # Verification du nombre d'arguments
    argv_count = len(sys.argv) - 1 

    if argv_count == 1 and sys.argv[1].isnumeric() == True :

        argv_1 = int(sys.argv[1])
        result = 0 
        # Racine de 0
        if argv_1 == 0:
            result = 0  
        # Racine de 1
        elif argv_1 == 1:
            result = 1
        # Racine de 2 ou plus
        else:
            entier = 1
            # On cherche la valeur entier max
            while entier * entier <= argv_1:
                result = entier
                entier += 1
            
            # On cherche la valeur décimale (0.01 → 0.99)
            decimal = 0
            for i in range(1, 100):
                test = result + (i / 100)
                if test * test <= argv_1:
                    decimal = i / 100
                else:
                    # Si on dépasse, on s'arrête
                    break
            result = result + decimal
            print(result)       

    else:
        print("erreur, veuillez entrer un nombre entier positif.")

# Resultat
racine()