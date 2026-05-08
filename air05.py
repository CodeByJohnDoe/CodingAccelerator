# Exercice Coding Accelerator
# Filtrer un tableau de chaînes par sous-chaîne

import sys

def filter_strings_by_substring(strings, substring):
    # Vérification des entrées
    if not strings or substring is None:
        return "error"

    result = []
    for s in strings:
        if substring in s:
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
