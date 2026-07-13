# Exercice Coding Accelerator
# Insertion triée dans une liste d'entiers (version finale optimisée)

import sys

def sorted_insert(sorted_array, new_element):
    # Vérification des entrées
    if not sorted_array:
        try:
            return [str(int(new_element))]
        except ValueError:
            return "error"

    # Vérification que le nouvel élément est un entier
    try:
        new_element = int(new_element)
    except ValueError:
        return "error"

    # Vérification que la liste est triée et conversion en entiers
    try:
        int_array = [int(num) for num in sorted_array]
        if int_array != sorted(int_array):
            return "error"
    except ValueError:
        return "error"

    # Insertion de l'élément
    new_array = []
    inserted = False
    for i, num in enumerate(int_array):
        if not inserted and new_element <= num:  # <= pour gérer les doublons
            new_array.append(str(new_element))
            inserted = True
            # Ajout du reste de la liste directement
            new_array.extend(map(str, int_array[i:]))
            break
        new_array.append(str(num))

    # Si l'élément est le plus grand
    if not inserted:
        new_array.append(str(new_element))

    return new_array

# --- Test ---
if __name__ == "__main__":
    # Vérification des arguments
    if len(sys.argv) < 3:
        print("error")
        sys.exit(1)

    # Séparation des éléments et du nouvel élément
    array = sys.argv[1:-1]
    new_element = sys.argv[-1]

    output = sorted_insert(array, new_element)
    if output == "error":
        print("error")
        sys.exit(1)
    else:
        print(" ".join(output))