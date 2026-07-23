# Exercice Coding Accelerator
# Concaténer une liste de chaînes avec un séparateur

import sys

def concatener(lst, separator):

    result = ""
    for i in range(len(lst)):
        if i > 0:
            result += separator
        result += lst[i]
    return result

# --- Programme principal ---
if __name__ == "__main__":
    # Vérification des arguments (minimum 2 mots + 1 séparateur)
    if len(sys.argv) < 3:
        print("error")
        sys.exit(1)

    # Le dernier argument est le séparateur
    separator = sys.argv[-1]

    # Tous les arguments entre le premier et le dernier sont les mots à concaténer
    words = sys.argv[1:-1]

    # Appel de la fonction et affichage du résultat
    result = concatener(words, separator)
    print(result)