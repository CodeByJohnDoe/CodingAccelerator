import sys

def string_cut(string_to_cut, string_separator):
    # Vérification des entrées
    if not isinstance(string_to_cut, str) or not isinstance(string_separator, str):
        return "error"
    if not string_separator:  # Si séparateur est vide
        return "error"

    splited = []
    separator_len = len(string_separator)
    marker = 0
    i = 0

    while i <= len(string_to_cut) - separator_len:
        if string_to_cut[i:i+separator_len] == string_separator:
            if i > marker:  # Ajoute seulement s'il y a du contenu
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

    response = string_cut(sys.argv[1], sys.argv[2])
    if response == "error":
        sys.exit()
    else:
        for mot in response:
            print(mot)