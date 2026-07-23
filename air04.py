# Exercice Coding Accelerator
# Supprimer les caractères identiques adjacents

import sys

def join_strings_with_separator(strings_list, separator):
    if not strings_list or len(strings_list) < 2: # Sécurité pour la fonction join nécessitant 2 arguments pour fonctionner
        return "error"

    return separator.join(strings_list) # La fonction join concat d'un coup la list

# -- Test --
if __name__ == "__main__":
    # Vérification des arguments
    if len(sys.argv) < 3:
        print("error")
        sys.exit()

    # Le dernier argument est le séparateur
    separator = sys.argv[-1]
    # Tous les arguments sauf le dernier sont les chaînes à joindre
    strings_to_join = sys.argv[1:-1]

    output = join_strings_with_separator(strings_to_join, separator)
    if output == "error":
        print("error")
        sys.exit()
    else:
        print(output)
    print(output)