# Exercice Coding Accelerator
# Supprimer les caractères identiques adjacents

import sys

import sys

def suppr_doublons_adjacents(chaine):
    if not chaine:
        return ""
    resultat = [chaine[0]]
    for char in chaine[1:]:
        if char != resultat[-1]:
            resultat.append(char)
    return ''.join(resultat)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("error")
        sys.exit()

    chaine = sys.argv[1]
    print(suppr_doublons_adjacents(chaine))