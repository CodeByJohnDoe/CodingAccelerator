# Exercice Coding Accelerator
# Trouver l'élément sans paire dans une liste

import sys

def find_odd_one_out(lst):
    # Vérification de la liste
    if not lst:
        return "error"

    count_dict = {}

    # Compter les occurrences de chaque élément
    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1

    # Trouver l'élément avec un nombre impair d'occurrences
    for item, count in count_dict.items():
        if count % 2 != 0:
            return item

    return "error"  # Si tous les éléments ont une paire

# --- Test ---
if __name__ == "__main__":
    # Vérification des arguments
    if len(sys.argv) < 2:
        print("error")
        sys.exit()

    # Récupération des arguments (tous sauf le nom du script)
    args = sys.argv[1:]

    result = find_odd_one_out(args)
    if result == "error":
        sys.exit()
    else:
        print(result)
