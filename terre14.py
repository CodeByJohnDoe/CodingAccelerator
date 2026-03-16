# Exercice Coding Accelerator
 
# Savoir si une liste est trié ou non

# Importation des modules
import sys

# Fonctionnement principal du programme
def sort_byme():
    error = "error, merci d'entrer au moins trois nombres différents sépraré chacun d'un espace."
    argv_count = len(sys.argv) - 1 
    input = sys.argv[1:]
    check_numeric = all(x.isnumeric() for x in input)

    # On vérifie si tout est bon
    if argv_count >= 3 and check_numeric == True:
        
        # Convertir les valeurs en entiers
        input_int = [int(x) for x in input]

        # On compare tout les valeurs de gauche à droite
        result = []
        for i in range(1, argv_count):
            result.append(input_int[i] > input_int[i - 1])

        # On vérifie si on a tout en True (croissant) ou False (décroissant)
        if all(x == True for x in result) :
            print("La liste est triée dans l'ordre croissant.")
        elif all(x == False for x in result) :
            print("La liste est triée dans l'ordre décroissant.")   
        else :
            print("La liste n'est pas triée.")

    else :
        print(error)


# Resultat
sort_byme()