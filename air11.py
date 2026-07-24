# Exercice Coding Accelerator
# Cortex

import sys

def afficher_pyramide(char, etages):
    # Vérification que le nombre d'étages est un entier positif
    try:
        etages = int(etages)
        if etages <= 0:
            return "error"
    except ValueError:
        return "error"

    # Construction de la pyramide
    pyramide = []
    for i in range(1, etages + 1):
        # Calcul des espaces avant les caractères
        espaces = "." + " " * (etages - i)   # Ajout du point afin de faciliter le test unitaire
        # Calcul des caractères pour chaque ligne (1, 3, 5, ... caractères)
        caracteres = char * (2 * i - 1)
        pyramide.append(espaces + caracteres)

    return "\n".join(pyramide)

# --- Test ---
if __name__ == "__main__":
    # Vérification des arguments d'entrée
    if len(sys.argv) != 3:
        print("error")
        sys.exit()

    char = sys.argv[1]
    etages = sys.argv[2]

    # Vérification que le caractère est bien un seul caractère
    if len(char) != 1:
        print("error")
        sys.exit()

    resultat = afficher_pyramide(char, etages)
    if resultat == "error":
        print("error")
        sys.exit()
    else:
        print(resultat)