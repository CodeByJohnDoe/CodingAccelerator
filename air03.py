# Exercice Coding Accelerator
# Trouver l'élément sans paire dans une liste

import sys

def l_intrus(lst):
    if not lst:
        return ["error"]

    count_dict = {}

    for item in lst:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1

    result = [item for item, count in count_dict.items() if count % 2 != 0]
    return result if result else ["error"]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("error")
        sys.exit()

    args = sys.argv[1:]
    result = l_intrus(args)

    if result == ["error"]:
        print("error")
    else:
        # Affichage des éléments séparés par des espaces, sans formatage de liste
        print(" ".join(result))