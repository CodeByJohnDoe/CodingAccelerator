# Exercice Coding Accelerator
# Fusion de deux listes triées

import sys

def sorted_fusion(array1, array2):
    # Vérification des entrées
    if not array1 or not array2:
        return "error"

    # Vérification que les listes sont triées
    for i in range(len(array1) - 1):
        try:
            if int(array1[i]) > int(array1[i+1]):
                return "error"
        except ValueError:
            return "error"

    for i in range(len(array2) - 1):
        try:
            if int(array2[i]) > int(array2[i+1]):
                return "error"
        except ValueError:
            return "error"

    # Fusion des deux listes
    new_array = []
    i = j = 0

    while i < len(array1) and j < len(array2):
        try:
            num1 = int(array1[i])
            num2 = int(array2[j])
        except ValueError:
            return "error"

        if num1 < num2:
            new_array.append(str(num1))
            i += 1
        else:
            new_array.append(str(num2))
            j += 1

    # Ajout des éléments restants
    while i < len(array1):
        try:
            new_array.append(str(int(array1[i])))
            i += 1
        except ValueError:
            return "error"

    while j < len(array2):
        try:
            new_array.append(str(int(array2[j])))
            j += 1
        except ValueError:
            return "error"

    return new_array

# --- Test ---
if __name__ == "__main__":
    # Vérification des arguments
    if len(sys.argv) < 4 or "fusion" not in sys.argv:
        print("error")
        sys.exit()

    try:
        fusion_index = sys.argv.index("fusion")
        array1 = sys.argv[1:fusion_index]
        array2 = sys.argv[fusion_index+1:]
    except:
        print("error")
        sys.exit()

    output = sorted_fusion(array1, array2)
    if output == "error":
        print("error")
        sys.exit()
    else:
        print(" ".join(output))
