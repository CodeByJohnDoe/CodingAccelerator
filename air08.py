# Exercice Coding Accelerator
# Rotation gauche d'un tableau

import sys

def ma_rotation(array):
    # Vérification des entrées
    if not array or len(array) < 2:
        return array if array else "error"

    # Rotation vers la gauche
    return array[1:] + array[:1]

# --- Test ---
if __name__ == "__main__":
    # Vérification des arguments
    if len(sys.argv) < 2:
        print("error")
        sys.exit()

    # Récupération du tableau (tous les arguments sauf le nom du script)
    array = sys.argv[1:]

    output = ma_rotation(array)
    if output == "error":
        print("error")
        sys.exit()
    else:
        print(", ".join(output))
