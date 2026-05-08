import sys

def my_quick_sort(array):
    # Cas de base : tableau vide ou avec un seul élément
    if len(array) <= 1:
        return array

    # Conversion en entiers si possible
    try:
        array = [int(x) for x in array]
    except ValueError:
        return "error"

    # Choix du pivot (ici l'élément du milieu)
    pivot = array[len(array) // 2]

    # Partitionnement
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]

    # Appel récursif et concaténation
    return my_quick_sort(left) + middle + my_quick_sort(right)

if __name__ == "__main__":
    # Vérification des arguments
    if len(sys.argv) < 2:
        print("error")
        sys.exit()

    # Récupération des arguments (tous sauf le nom du script)
    array = sys.argv[1:]

    # Tri du tableau
    sorted_array = my_quick_sort(array)

    if sorted_array == "error":
        print("error")
        sys.exit()
    else:
        print(" ".join(map(str, sorted_array)))
