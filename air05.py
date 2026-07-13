# Exercice Coding Accelerator
# Filtrer un tableau : garder les éléments qui NE contiennent PAS la sous-chaîne (insensible à la casse)

import sys

def filter_strings_by_substring(strings, substring):
    # Vérification des entrées
    if not strings or not substring:
        return "error"

    result = []
    for s in strings:
        # Recherche insensible à la majuscule (On aurait pu aussi utiliser une conversion et comparaison via le systeme ascii)
        if substring.lower() not in s.lower():
            result.append(s)

    return result if result else "error"

# --- Test ---
if __name__ == "__main__":
    # Vérification des arguments
    if len(sys.argv) < 3:
        print("error")
        sys.exit()

    # Séparation des chaînes et de la sous-chaîne
    strings = sys.argv[1:-1]
    substring = sys.argv[-1]

    output = filter_strings_by_substring(strings, substring)
    if output == "error":
        print("error")
        sys.exit()
    else:
        print(", ".join(output))