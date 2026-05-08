# Exercice Coding Accelerator
# Insertion triée dans une liste d'entiers

import sys

def sorted_insert(sorted_array, new_element):
    # Vérification des entrées
    if not sorted_array:
        return [new_element] if new_element is not None else "error"

    try:
        new_element = int(new_element)
    except ValueError:
        return "error"

    # Vérification que la liste est triée
    for i in range(len(sorted_array) - 1):
        try:
            if int(sorted_array[i]) > int(sorted_array[i+1]):
                return "error"
        except ValueError:
            return "error"

    # Insertion de l'élément
    new_array = []
    inserted = False
    for num in sorted_array:
        try:
            current = int(num)
        except ValueError:
            return "error"

        if not inserted and new_element < current:
            new_array.append(str(new_element))
            inserted = True
        new_array.append(num)

    # Si l'élément est le plus grand
    if not inserted:
        new_array.append(str(new_element))

    return new_array

# --- Test ---
if __name__ == "__main__":
    # Vérification des arguments
    if len(sys.argv) < 3:
        print("error")
        sys.exit()

    # Séparation des éléments et du nouvel élément
    array = sys.argv[1:-1]
    new_element = sys.argv[-1]

    output = sorted_insert(array, new_element)
    if output == "error":
        print("error")
        sys.exit()
    else:
        print(" ".join(output))
