# Exercice Coding Accelerator
# Quick Sort

import sys

def my_quick_sort(array):
    # Cas de base : si le tableau a 0 ou 1 élément, il est déjà trié
    if len(array) <= 1:
        return array

    # Conversion des éléments en entiers (pour gérer les erreurs)
    try:
        array = [int(x) for x in array]
    except ValueError:
        return "error"  # Si un élément n'est pas un nombre

    # Choix du pivot (milieu du tableau)
    pivot = array[len(array) // 2]

    # Partitionnement :
    # - left : éléments < pivot
    left = [x for x in array if x < pivot]
    # - middle : éléments == pivot
    middle = [x for x in array if x == pivot]
    # - right : éléments > pivot
    right = [x for x in array if x > pivot]

    # Appel récursif sur left et right, puis concaténation
    return my_quick_sort(left) + middle + my_quick_sort(right)

# --- Test ---
if __name__ == "__main__":
    # Vérification des arguments
    if len(sys.argv) < 2:
        print("error")
        sys.exit()

    # Récupération des arguments
    array = sys.argv[1:]

    # Tri du tableau
    sorted_array = my_quick_sort(array)

    if sorted_array == "error":
        print("error")
        sys.exit()
    else:
        print(" ".join(map(str, sorted_array)))