# Exercice Coding Accelerator
# Découper une chaîne avec un séparateur personnalisé

import sys

def string_cut(string_to_cut, string_separator):
    # Vérification des entrées
    if not string_to_cut or not string_separator:
        return "error"

    splited = []
    separator_len = len(string_separator)
    marker = 0
    i = 0

    while i <= len(string_to_cut) - separator_len:
        # Vérifie si on trouve le séparateur à la position i
        if string_to_cut[i:i+separator_len] == string_separator:
            # Ajoute le segment avant le séparateur
            if i > marker:
                splited.append(string_to_cut[marker:i])
            marker = i + separator_len
            i += separator_len  # Saute le séparateur
        else:
            i += 1

    # Ajoute le dernier segment
    if marker < len(string_to_cut):
        splited.append(string_to_cut[marker:])

    return splited

# --- Test ---
if __name__ == "__main__":
    # Vérification des arguments
    if len(sys.argv) != 3:
        print("error")
        sys.exit()

    reponse = string_cut(sys.argv[1], sys.argv[2])
    if reponse == "error":
        sys.exit()
    else:
        for mot in reponse:
            print(mot)
